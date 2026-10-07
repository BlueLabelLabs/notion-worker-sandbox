#!/usr/bin/env python3
"""Convert saved Sheets API get_spreadsheet(includeGridData) JSON into compact per-tab cell dumps.

Usage: dump_grid.py <out_dir> <json files...>
For each sheet/data block: one line per non-empty cell: `A1 | formula-or-value | formatted | note | validation`.
Also writes hidden rows/cols and number formats seen.
"""
import json, sys, os, re

def col_letter(idx):
    s = ""
    idx += 1
    while idx > 0:
        idx, r = divmod(idx - 1, 26)
        s = chr(65 + r) + s
    return s

def cell_value(v):
    uev = v.get("userEnteredValue") or {}
    if "formulaValue" in uev: return uev["formulaValue"]
    if "stringValue" in uev: return json.dumps(uev["stringValue"])
    if "numberValue" in uev: return repr(uev["numberValue"])
    if "boolValue" in uev: return "TRUE" if uev["boolValue"] else "FALSE"
    if "errorValue" in uev: return "ERR:" + str(uev["errorValue"])
    return None

def dv_summary(dv):
    if not dv: return ""
    cond = dv.get("condition", {})
    t = cond.get("type")
    vals = [x.get("userEnteredValue") for x in cond.get("values", []) if isinstance(x, dict)]
    extra = []
    if dv.get("strict"): extra.append("strict")
    if dv.get("showCustomUi"): extra.append("ui=" + str(dv.get("customUiMode", "")))
    if dv.get("inputMessage"): extra.append("msg=" + json.dumps(dv["inputMessage"]))
    return f"DV[{t}:{vals}{' ' + ' '.join(extra) if extra else ''}]"

def main(out_dir, files):
    os.makedirs(out_dir, exist_ok=True)
    for f in files:
        try:
            doc = json.load(open(f))
        except Exception as e:
            print(f"skip {f}: {e}"); continue
        for sh in doc.get("sheets", []):
            title = sh.get("properties", {}).get("title", "untitled")
            for bi, block in enumerate(sh.get("data", []) or []):
                r0 = block.get("startRow", 0); c0 = block.get("startColumn", 0)
                rows = block.get("rowData", []) or []
                # compute block extent for file naming
                safe = re.sub(r"[^A-Za-z0-9_-]+", "_", title)
                suffix = "" if (r0 == 0 and c0 == 0) else f"_r{r0+1}c{col_letter(c0)}"
                path = os.path.join(out_dir, f"{safe}{suffix}.txt")
                lines = [f"# TAB: {title}  (block starts at row {r0+1}, col {col_letter(c0)})", ""]
                hidden_rows = [i + r0 + 1 for i, m in enumerate(block.get("rowMetadata", []) or []) if m.get("hiddenByUser")]
                hidden_cols = [col_letter(i + c0) for i, m in enumerate(block.get("columnMetadata", []) or []) if m.get("hiddenByUser")]
                lines.append(f"hidden rows: {hidden_rows}")
                lines.append(f"hidden cols: {hidden_cols}")
                lines.append("")
                lines.append("## Cells (A1 | entered formula/value | formatted | note | validation | numfmt)")
                numfmts = {}
                count = 0
                for ri, row in enumerate(rows):
                    for ci, v in enumerate(row.get("values", []) or []):
                        if not v: continue
                        a1 = f"{col_letter(ci + c0)}{ri + r0 + 1}"
                        val = cell_value(v)
                        fmt = v.get("formattedValue")
                        note = v.get("note")
                        dv = dv_summary(v.get("dataValidation"))
                        nf = (v.get("userEnteredFormat") or {}).get("numberFormat") or (v.get("effectiveFormat") or {}).get("numberFormat")
                        nfs = f"{nf.get('type')}:{nf.get('pattern','')}" if nf else ""
                        if nfs: numfmts[a1] = nfs
                        if val is None and fmt is None and not note and not dv:
                            continue
                        parts = [a1, val if val is not None else "", json.dumps(fmt) if fmt is not None else ""]
                        if note: parts.append("NOTE=" + json.dumps(note))
                        if dv: parts.append(dv)
                        if nfs and val is not None: parts.append("FMT=" + nfs)
                        lines.append(" | ".join(parts))
                        count += 1
                lines.append("")
                lines.append(f"## {count} non-empty cells")
                open(path, "w").write("\n".join(lines) + "\n")
                print(f"wrote {path} ({count} cells, {len(rows)} rows)")

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2:])
