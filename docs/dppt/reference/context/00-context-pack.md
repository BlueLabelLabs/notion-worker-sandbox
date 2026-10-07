# Context pack for the DPPT v6.3 reverse-engineering workflow

Subject: Google Sheet "BL###.## - [Title] - DPPT v6.3", spreadsheet id 1kwmFH-61_4K8E-rGVie395TAQsExGBZ8TV3_hZ2oiGE
(created 2026-10-07, 45.6 KB, locale en_US, timezone America/New_York). It is the blank TEMPLATE from which each
deal's DPPT is copied. DPPT = "Delivery Project Planning Tool" (BlueLabel's pricing / staffing / schedule tool for a deal).
Note: Config!J1 "DPPT Version" still reads 6.2 inside the v6.3 template.

## Files in ../dppt-dump/  (one per tab; `A1 | entered formula/value | formatted | note | validation | numfmt`)
Tasks.txt, Team.txt, Requirements (see tab notes below; cell data is in ../context/requirements_constants_templates.md),
Config.txt, Overview.txt, Allocations.txt, Output.txt, Sprint_Invoicing.txt, Monthly_Invoicing.txt,
Top-Level_Tasks.txt, Timeline_Data.txt.  Formatted values are the TEMPLATE's sample data (a 2-phase example:
"Discovery Team" 2 sprints + "Validation Team" 1 sprint, start 1/4/27, total $102,667).

## Tabs (index order), sheetId, visibility, grid
| # | Tab | sheetId | hidden | rows x cols | frozen |
|---|-----|---------|--------|-------------|--------|
| 0 | Tasks | 1156089416 | no | 22 x 77 (A..BY) | 6 rows |
| 1 | Team | 1247661352 | no | 31 x 13 | 1 row |
| 2 | Requirements | 1078800328 | YES | 18 x 16 | 10 rows, 2 cols |
| 3 | Config | 2036713466 | no | 9 x 11 | |
| 4 | Overview | 947124104 | YES | 27 x 11 | |
| 5 | Allocations | 232688409 | no | 500 x 2 | |
| 6 | Output | 1855008443 | no | 21 x 4 | 1 row |
| 7 | Sprint Invoicing | 495690930 | YES | 613 x 7 | 2 rows |
| 8 | Monthly Invoicing | 407217026 | YES | 565 x 4 | 1 row |
| 9 | Templates | 781778228 | no | 14 x 72 | 1 row |
| 10 | Timeline | 1712160992 | YES | sheetType OBJECT (a Sheets Timeline view, data from "Timeline Data") | |
| 11 | Constants | 1809442114 | YES | 24 x 2 | |
| 12 | Top-Level Tasks | 78862207 | YES | 1000 x 88 | 1 row, 4 cols |
| 13 | Timeline Data | 1835558126 | YES | 1000 x 26 | |

Tab colors: Tasks orange, Team blue, Requirements purple, Config green, Overview magenta.

## Protected ranges (all warning-only unless noted; editors = andon.keller, parvathy.harilal, parvathy, jordan, daniel.deserto, bobby @bluelabellabs.com)
- Tasks row 22 "Last Task Row Stays Empty & Hidden" (editor: andon only)
- Tasks B6:U6 "Role Titles"
- Team D:K "Team Formulas"
- Requirements B8 (editor: andon only, NOT warning-only = hard protection)
- Overview whole sheet "Don't Edit"; Allocations, Output, Sprint Invoicing, Monthly Invoicing whole sheet

## Conditional formats (summary)
- Tasks B6:AE6 (role headers): pink if the capability row (B8) = "Product", light blue if "Engineering".
- Tasks: zero values grey text in AF, AK:AL, AO:AP, AS (rows 6-22) and in the hidden AT:BY block.
- Tasks AQ14:AR22: grey background + bold accent text when the cell is NOT a formula (=NOT(ISFORMULA(AQ14))) -> flags a manually typed start/end date.
- Tasks A14:AS22: grey background when $AP>0 (row has a subtotal, i.e. an active phase row).
- Team rows: greyed out when Include (B) = FALSE; pink when Capability (H) = "Product"; blue when "Engineering".
- Requirements A11:P18: grey bold when $A (Group checkbox) is TRUE.
- Config F4:J4: white-on-white (hidden) when externalCommissionPercent <= 0.
- Templates: mirrors of the Tasks rules (zero grey, NOT(ISFORMULA(A2)), $C2>0).

## Named ranges in v6.3 (name -> range).  Prefix 'Templates'! = sheet-scoped names on the Templates tab (legacy).
Tasks (1156089416): startDate=AQ1, lastDate=AR1, checkboxOptionShowFees=AR3, checkboxOptionMonthly=AR4,
  optionShowWeeklyBillRate=AQ5, optionShowActivityHours=AQ5, tasksHiddenRows=rows 7-14, tasksRowResourceIncluded=row 9,
  tasksLastHiddenRow=row 14, tasksBottomRow=row 22, tasksRoleCells=B15:AE22, tasksRoleCellFormatSource=B15:B15,
  tasksResourceHoursColumns=B:AE, tasksDynamicVisibilityColumns=B:AS, tasksFormulaBlockColumns=AG:AR,
  tasksRangeWeeks=AG14:AG22, tasksWeekCountColumn=AG, tasksSprintSumColumn=AH, tasksCalculatedColumns=AK:AP,
  tasksWeeklyRateColumn=AK, tasksActivityHoursColumn=AL, tasksPhaseNumColumn=AM, tasksPhaseTitleColumn=AN,
  tasksSprintRateColumn=AO, tasksPriceColumn=AP, tasksStartDateColumn=AQ, tasksEndDateColumn=AR,
  tasksHiddenColumns=AT:BY, tasksResourcePriceColumns=AT:BW, tasksSprintCountTextColumns=BX, tasksTeamStringColumn=BY
Team (1247661352): teamIncludeRoleColumn=B, teamHiddenColumns=D:J
Requirements (1078800328): projectCode=E3, projectTitle=E3, zenDeskDealID=E3 (all three point at E3!), platformList=L3:L6,
  reqView=B8, reqGroupCheckboxColumn=A, reqEstimationWeeksColumns=C:D, reqWeekCountColumn=D, reqEstimationHoursColumns=E:H,
  reqSprintPlanningColumns=I:J, reqFormulaColumns=N:P, reqNextHeaderColumn=N, reqLastRowInGroupColumn=O,
  reqWeekCountFormulaColumn=P, reqHiddenRows=row 11, reqFormulaSource=N11:P11, reqFormulaDestination=N12:P18,
  reqHiddenColumns=N12:P18, reqBottomRow=row 18
Config (2036713466): DPPTVersionNumber=J1, margin=D3, totalPrice=G3, externalCommissionAmount=G4,
  externalCommissionPercent=D5, ISRName=I4, proposalDocTitle=C8, proposalDocId=C8:E8
Sprint Invoicing (495690930): InvoiceSchedule4Weeks=A:C, invoiceFrequency=E2, firstInstallmentDate=E3
Monthly Invoicing (407217026): InvoiceScheduleMonthly=B:D
Constants (1809442114): constantLastTaskRowNum=B1 (=22), constantLastReqRowNum=B2 (=18)
Templates sheet-scoped legacy names: tasksBottomRow=row14, tasksLastHiddenRow=row2 ... (mirror an older Tasks layout).

The named-range vocabulary (tasksDynamicVisibilityColumns, tasksLastHiddenRow, reqFormulaSource/Destination,
constantLastTaskRowNum, proposalDocId, reqView ...) is the footprint of a BOUND APPS SCRIPT that we cannot read through
the Sheets API. Infer its behaviours from the names, the protected rows, the Constants tab and the hidden template rows.

## Sibling files in the templates folder (Drive folder 18wdqv1ZnrM8DK2fagr0CBM262ZLYKQhu)
- BL###.## - [Title] - DPPT v6.3  (this one, created 2026-10-07)
- BL###.## - [Title] - DPPT v6.2  (1n29g-iNQ-qkUE0vbKXlAQ5uh1-jppBvSMrohyAkkAYY, created 2026-07-29, modified 2026-10-01). Same 14 tabs, same shape.
- BL###.## - [Title] - DPPT v7    (15uz_8M7HjjpWoJQUXtTPDJIErtq_YixHtbe46rWK700, created 2025-05-28, modified 2026-07-22).
  Despite the number it has the OLDER tab set: Tasks(26 rows), Team(12 cols), Requirements(12 rows, 4 frozen), Config(20 rows),
  Overview, Sprints(58x9), Sprint Allocations(566x4), Sprint Invoicing, Monthly Invoicing, Templates, Timeline, Constants,
  Top-Level Tasks, Timeline Data. Config in v7 has margin=D15, totalPrice=G15, ISRName=I16, proposalDocId=C20:E20,
  platformList=J9:J12 and a stale name phaseListForProposal. Treat v7 as an abandoned/parallel experiment branch.
- Folder "Archived Versions": DPPT v6.1 (1bLSl1if47ezYfA_d0-DcT9Cxlq97aF3-xx4GmZksZio), v5 (old), v4 (old), v3 (old), v2 (old),
  "Delivery Plan Pricing Tool v1" (2023-08-30). Folder "Next": "Example SOW" (Google Doc, 2025-05-24), "DPPT Experiment" (Slides, 2023).
- Also in the folder: "BlueLabel Doc Test" (Doc), "kantata role ids.csv" (2025-05-24).

## Live DPPTs found in Drive (all copies of the template, named "BL<deal#> - <Title> - DPPT v6.x")
BL187.17 - NTI Security Updates - DPPT v6.2; BL373.01.CR10 - Ergo Overwatch Team Increase Through 2026 - DPPT v6.2;
BL380.05 - NFM ACDV & Credit Reporting - DPPT v6.2; BL373.01.CR09 - Ergo Overwatch Team Increase - 2 Engineers - DPPT v6.1;
BL349.## - Mapline 2026 Additional Features- DPPT v6.2.  (see real_dppt_samples.md for two of them)

## Code that consumes the DPPT (repos checked out at /home/user)
- /home/user/notion-worker-dppt  (Notion Worker; parses the sheet; src/lib/parse.ts, sheets.ts, dates.ts, notionBlocks.ts,
  webhooks/buildDpptTables.ts, updateDpptDates.ts (writes Tasks!AQ15), onRevenueScheduleChanged.ts; parse.test.ts has
  transcribed v6.1/v6.2 grids). README.md and CLAUDE.md describe the contract.
- /home/user/notion-worker-forecast (reads Notion Deal Revenue Schedules, not the sheet; forked from dppt worker).
- notion-worker-kantata (NOT checked out): reads the Notion "DPPT Details" DB and realigns Kantata workspaces.
See notion_schemas.md for the Notion databases.
