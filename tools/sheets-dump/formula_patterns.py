import re, sys, collections
# Summarize a dump: first N data lines verbatim, then unique formula patterns (row numbers -> #) with counts and first/last cell.
path = sys.argv[1]; head_n = int(sys.argv[2]) if len(sys.argv) > 2 else 60
lines = open(path).read().splitlines()
print("\n".join(lines[:head_n]))
print("\n## Formula patterns (row digits normalized to #): count | first cell | last cell | pattern")
pat = collections.OrderedDict()
for ln in lines:
    m = re.match(r"^([A-Z]+)(\d+) \| (=.*?) \| ", ln)
    if not m: continue
    col, row, f = m.groups()
    norm = re.sub(r"(?<![A-Za-z!'])([A-Z]{1,3}\$?)(\d+)", lambda mm: mm.group(1) + "#", f)
    norm = re.sub(r"(?<=\$)(\d+)", "#", norm)
    key = (col, norm)
    if key not in pat: pat[key] = [0, f"{col}{row}", f"{col}{row}", f]
    pat[key][0] += 1; pat[key][2] = f"{col}{row}"
for (col, norm), (cnt, first, last, example) in pat.items():
    print(f"{cnt:4d} | {first:>6} | {last:>6} | {example if cnt == 1 else norm}")
