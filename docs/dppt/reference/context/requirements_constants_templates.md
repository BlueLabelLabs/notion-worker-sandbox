# Requirements tab (hidden), Constants, Templates: cell data from the v6.3 template

## Requirements (sheetId 1078800328; hidden; frozen 10 rows / 2 cols; hidden cols N,O,P; hidden rows 11 and 18)
Row 2: C2="Interface" F2="Technology" I2="Notes"
Rows 3-6 (platform list, named range platformList=L3:L6): C3="Backend" F3="?" L3==IF(ISBLANK(C3)," ",CONCATENATE(C3," | ",F3,)) -> "Backend | ?";
  C4="Admin Web" F4="?" L4 -> "Admin Web | ?"; C5="Mobile" F5="?" L5 -> "Mobile | ?"; C6 blank -> L6 " "
Row 8: B8 = dropdown (CHIP style, strict) with options "1 | Enter Requirements", "2 | T-Shirt Size", "3 | Estimate Hours", "4 | Sprint Planning";
  current value "4 | Sprint Planning". C8="T-Shirt Size", E8="Estimation: Hours", I8="Sprint Planning" (section labels over the column groups).
  B8 is hard-protected (editor andon only) and is the named range reqView -> the "view mode" selector the script reads to show/hide column groups.
Row 10 (header): A="Group", B="Requirement", C="Complexity", D="Weeks", E:G = TRANSPOSE(platformList) -> "Backend | ?", "Admin Web | ?", "Mobile | ?", H=" ",
  I="Sprint #", J="Story Points", K="Notes 📝", L="Questions & Assumptions❓", M="Risks ⚠️", N="Next header delta", O="Last row in group", P="Sum Weeks"
Row 11 (hidden template row = reqFormulaSource N11:P11): A11 checkbox FALSE; C11 dropdown (strict, ARROW) "1 | Straightforward", "2 | Normal",
  "3 | Complicated", "4 | Never Done Before"; N11==IF($A11,MATCH(TRUE,$A12:A,0),""); O11==IF($A11,ROW()+N11-1,""); P11==IF($A11,SUM(INDIRECT("D"&ROW()+1&":"&"D"&IFNA(O11,))),"")
Row 12: A12=TRUE (a Group header row), B12="Group", D12==P12 (group weeks = sum of its children) -> 4.2; N12/O12 -> #N/A (no next group), P12=4.2
Row 13: A=FALSE, B="requirement / goal / outcome", C="1 | Straightforward", D=2 weeks, E=10, F=10, G=10 (hours per platform), N:P formulas
Row 14: A=FALSE, B="requirement / goal / outcome", C="1 | Straightforward", D=0.2
Row 15: A=FALSE, (blank requirement), D==P15 (formula, so this row is treated like a potential group header)
Row 16: C="2 | Normal", D=1 ; Row 17: C="2 | Normal", D=1 ; Row 18 (hidden bottom row = reqBottomRow): formulas only
Conditional format: whole row grey+bold when $A (Group) is TRUE.
Semantics: a requirements backlog grouped into Groups; each requirement gets a Complexity (1-4), an estimate in Weeks (D) and/or Hours per platform (E:G),
and later a Sprint # and Story Points. Group rows sum the weeks of their children via the hidden N:P helper formulas. The view dropdown (B8) names a
4-step estimation workflow: 1 Enter Requirements -> 2 T-Shirt Size (complexity) -> 3 Estimate Hours -> 4 Sprint Planning. Nothing on the Tasks tab references
the Requirements tab in v6.3 (no formula links), so in v6.3 it is a standalone, hidden estimating worksheet.

## Constants (hidden)
A1="LastTaskRowNum" B1=22 (named constantLastTaskRowNum); A2="LastReqRowNum" B2=18 (constantLastReqRowNum). Script bookkeeping of the bottom rows.

## Templates (visible, 14 rows x 72 cols; hidden cols AO..BT)
Row 1 = header mirror of Tasks row 6: A==Tasks!AQ6 ("Start"), B==Tasks!AR6 ("End"), C==Tasks!AG6 ("Weeks"), D==Tasks!AI6, E==Tasks!AJ6, F==Tasks!A6, G..AJ==Tasks!B6..AE6 (roles),
AK==Tasks!AK6 (Weekly Rate), AL==Tasks!AL6 (Weekly Hours), AM==Tasks!AP6 (Subtotal), AN==Tasks!AS6 (Delivery Notes), AO..BR = =G1..=AJ1 (role names again, hidden), BS="Sprint Text", BT="Team".
Rows 2-14: EMPTY in the v6.3 template except number formats (A:B dates m/d/yy, AK currency, AL #,##0.0, AM:AN currency). Conditional formats mirror Tasks.
The sheet-scoped names 'Templates'!tasks* describe an OLDER Tasks layout (start/end in A:B, roles in G:AJ). Templates appears to be a legacy
"row template" sheet for the script; in v6.3 the live template row is Tasks row 14 (hidden) instead.
