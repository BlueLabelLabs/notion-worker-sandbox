# notion-worker-sandbox

Working space for BlueLabel sales-ops tooling research that does not yet belong in a deployed worker.

## Contents

| Path | What it holds |
| --- | --- |
| `docs/dppt/DPPT-v6.3-requirements.md` | Reverse-engineered requirements for the DPPT (Delivery Project Planning Tool) Google Sheets template, v6.3. Start here. |
| `docs/dppt/reference/cell-dumps/` | Every non-empty cell of the v6.3 template, one tab per file: entered formula or value, formatted value, validation and number format. The evidence behind the requirements. |
| `docs/dppt/reference/context/` | Supporting notes gathered during the analysis: tab inventory and named ranges, the Notion process documentation, Notion database schemas, the DPPT Issues history, the Kantata role catalogue. |
| `tools/sheets-dump/dump_grid.py` | Converts a Sheets API `spreadsheets.get` response (with `includeGridData`) into the cell-dump format above. |
| `tools/sheets-dump/formula_patterns.py` | Summarizes a cell dump by repeating formula pattern, for large tabs. |

## Brand rule

Always write "BlueLabel". Never "Blue Label", "Blue Label Labs", or "BLL".

## Regenerating the cell dumps

1. Call `spreadsheets.get` on the template with `includeGridData=true` and a field mask that includes `sheets.data.rowData.values.userEnteredValue`, `formattedValue`, `note`, `dataValidation`, `userEnteredFormat.numberFormat`, `sheets.data.rowMetadata.hiddenByUser` and `sheets.data.columnMetadata.hiddenByUser`.
2. Save the JSON responses to disk.
3. Run:

```bash
python3 tools/sheets-dump/dump_grid.py docs/dppt/reference/cell-dumps <response.json> [...]
python3 tools/sheets-dump/formula_patterns.py docs/dppt/reference/cell-dumps/Sprint_Invoicing.txt 60
```
