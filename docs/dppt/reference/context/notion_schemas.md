# Notion databases around the DPPT (schemas fetched 2026-10-07)

## Deals  collection://ee89a6dd-be27-4bc5-bc5f-86b6ef40be2b  (icon signature-document)
DPPT-relevant properties: Deal Title (title); DPPT URL (url); DPPT Details (relation -> DPPT Details DB); Start Date (date);
Contract End (date); Kantata End (date); Kantata Outline (relation -> Kantata Outlines 862e6732-...); Kantata ID (rollup);
Sprint Fee (number $, "The *current* sprint rate"); Original Sprint Fee (number $); Fixed Fee ($); Monthly Fee (type email! a bug); Value ($);
Margin (percent, "From ZenDesk"); Contract Format (select: "Sprints | Ongoing", "Sprints | Fixed Amount", "Hourly / Time & Materials",
"Change to Sprint Team", "Staff Augmentation", "Fixed Scope"); ZD | Stage (select: New Opportunity, Qualifying, Estimating, Negotiating, Closing, Won,
Lost, Unqualified, On Hold..., Nurturing); Stage Probability (formula); ZD | Delivery Status (select: Estimate Needed, Estimated, Prepare for Delivery,
Implement Change (CR), Active, Completed, Cancelled, On Hold, None); Forecast (checkbox: "Only check for Deals that represent future forecasting. NOT for real deals.");
Forecast Confidence (select 1/3/6/9 months); Forecast Weeks (formula); Slack Channel ID (text); Client Account (relation); Client Partner (rollup person);
Client Partner (Text) (text, system-populated); Delivery Notes (text: "Constraints, Key Dates, etc. Anything the Delivery Team needs to know");
Description; Google Folder URL; Create Folders (button); Create Kantata (button); Update DPPT Start Date (button: "This will attempt to update the DPPT to
match the deal's start date. Watch for messages in #sales-ops."); Test Webhook (button); 📆 Deal Revenue Schedule (relation); Revenue Schedule Status
(status: Not started / AI Refresh / Error / Ready for Review / Done); Revenue Schedule Last Updated (date); Revenue Schedule Computed End Date (rollup);
2026.Q1 ... 2028.Q4 (rollup sums of the schedule formulas); ZenDesk ID; ZD | Owner; ZD | Contact ID; Lost Reason / Unqualified Reason (multi-select); ID (auto-increment).

## Deal Revenue Schedules  collection://37bf6504-1608-4bf0-af10-c6e5123cc618  (icon chart-area)
Schedule Item (title) | Deal (relation, limit 1) | Billing Basis (select: Per Week, Per Sprint, Per Month, Fixed Dates) | Rate (number $, "Amount per unit
determined by Billing Basis") | Duration Type (select: Weeks, Sprints [2-week], Months, Fixed Dates, Ongoing) | Duration (number) | Start Date (date) |
Fixed End Date (date) | Forecast Weeks (number, only for Ongoing) | Delivery Phase (multi-select: Discover, Validate, Production, Deploy, Evolve) |
Notes (text) | Archived (checkbox "Check to remove from forecast").
Formulas: Weekly Revenue (Per Week=Rate; Per Sprint=Rate/2; Per Month=Rate*12/52; Fixed Dates=0); Computed End Date (Exclusive); Effective End Date;
Total Value / Schedule Item Total Value (Num) (Rate*Duration, else estimated from dates); Annualized Run Rate; 2025.Q1..2028.Q4 recognized revenue;
Deal Title, Client Account (Plain Text), Client Partner (Plain Text), Deal Stage, Deal Stage Percent (Filter), Segment Key (Deal+Start+Billing Basis), Segment Window.
This is the model a future "Deal Cost Schedules" database would mirror (same shape, but Rate = cost per unit from Team cost rates instead of price).

## DPPT Details  collection://7ea7034e-ad61-4ac5-b9c3-25797100c2e2  (icon t-square)
Title (title) | Deal (relation) | rollups: Kantata Outline, Stage, Links. Page CONTENT (written by notion-worker-dppt): info callout
("Populated <date> from <sheet title>", Margin/Dates/Price), "Rate Card" table (Role | Rate), "Delivery Segments" table
(Name | Roles | Hours | Start | End | Duration | Budget). Read by notion-worker-kantata to build Kantata workspaces (tasks, budgets, allocations).
