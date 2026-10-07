# Notion documentation that describes the DPPT and the processes around it (fetched 2026-10-07)

## 1. "Delivery Plan Pricing Tool (DPPT)" page  (Knowledge / Client Solutions Databases; last edited 2025-05-28; icon list-indent)
Callout: "Methodology & development tracking for our Delivery Plan Pricing Tool."
How to create a DPPT: 1. Navigate to the Google Drive folder where you want to use the tool. 2. Top Left: New > Google Sheets > From Template.
3. Select "BL### - [Project Title] - DPPT". 4. Rename the file according to <the file-naming convention page e5025c40db2a4dca92e4a409d574e3c1>.
How to get started with a DPPT: 1. Select the Team tab. 2. Select the roles that will be involved in the work. 3. Select the Tasks tab.
4. Each activity needs: # of two-week sprints; Phase or activity title; Weekly hours per role. 5. Use lines underneath activities to add details
such as deliverables and external dependencies.
Training: Sep 12, 2023 Delivery Weekly Zoom recording (initial introduction / group workshop).
Issues & Feature Requests: inline database "DPPT Issues" (collection://e033af84-cbc0-4996-a52e-abb685de9784) -> see dppt_issues.md
NOTE: the page predates v6.2/v6.3 (it names the old template title and the old "Sprints" wording; the "lines underneath activities" advice predates
the Delivery Notes column AS).

## 2. Process Library: "Deal Revenue Schedule → DPPT → Kantata Sync Workflow (Automated)"  (Status: Accurate; owner Alex, Client Solutions Coordinator; last edited 2026-07-30)
Purpose: one-way workflow for syncing deal schedule changes into DPPT and Kantata, via two Notion Workers (DPPT Worker & Kantata Worker).
Sync path: Revenue Schedule → Deal Start Date → DPPT Start Date → DPPT Details → Kantata.
Definitions: Revenue Schedule = billing / revenue timing. DPPT = delivery plan, pricing, roles, hours, sprint dates. Kantata = delivery execution,
task dates, estimates, rate card, allocations. "Do not force Revenue Schedule lines to match DPPT sprints. Revenue and delivery timing can differ."
Source-of-truth table: Deal start date = earliest Revenue Schedule date (automation uses earliest; review before syncing). Delivery sprint plan = DPPT
(sprints, dates, roles, hours, budget, rate card). Delivery execution = Kantata (rebuilt from DPPT). Billing/revenue timing = Revenue Schedule.
Buttons/Workers: "Update DPPT Start Date" (Deal start -> DPPT start); "Get DPPT details" (reads DPPT: Sprints tab, Sprint Allocations tab, Team tab
roles & bill rates, margin, date range, price, rate card, sprint dates, hours, budget -> writes back into Notion); "Update Outline"; "Rebuild Kantata
to match DPPT" (sprint tasks, task dates, predecessors, role assignments, estimated hours, sprint budgets; posts in #delivery-ops); "Build Rate Card"
(from the DPPT-derived rate card table; archives a matching old card); "Build Allocations" (from task estimate hours; clears existing allocations first).
Process steps 1-8 + QA checklist (review schedule, update schedule, click Update DPPT Start Date and confirm sprint dates recalculated and sprint count
still makes sense, Get DPPT details and review Margin / Date range / Price / Rate Card / Sprint table / Sprint budgets / Role hours per sprint, Update
Outline, Rebuild Kantata, Build rate card, Rebuild allocations).
Known edge cases: Revenue Schedule has more lines than the DPPT has sprints; revenue timing differs from delivery timing; deposits, retainers, milestone
billing, non-sprint billing events; DPPT role names do not map cleanly to Kantata roles; manually adjusted Kantata allocations/tasks; an existing rate card.
Test case: BLTEST2 | TEST Deal confirmed the one-way sync.

## 3. To Do "Notion + Kantata Workers" (done 2026-08-07) = build spec of the workers
Get DPPT Details: read the sheet from the Deal URL property; extract Sprints (Sprints tab), Sprint Allocations, Team roles & bill rates (headings Role,
Bill Rate, Hours, Who); write callout "Populated <date> from <sheet>" + Margin/Dates/Price, "Rate Card" table (Role | Rate), "Sprints" table
(Sprint | Team | Hours Per Sprint | Start Date | End Date | Duration "10d").
Create Sprints in Kantata from the DPPT: add roles to the workspace; create tasks chained by predecessor; title = sprint title; assign roles; task
estimated hours per role; total hours; budget; start/end dates; message #delivery-ops. Create rate card: search by Engagement Code; archive exact match
("ARCHIVED"); create new with roles & billable rates from the Rates table; effective date today; assign to workspace. Estimated hours -> task-level
allocations (clear all; create per assignment; soft allocations for unnamed roles; custom field Last Allocate Date). Idea: sync timesheets to Notion.

## 4. To Do template "Setup BL###.## | <Deal>" (Kantata Project Setup checklist; example BL365.03 UEI Maintenance, done 2026-08-27)
Review documentation: statement of work and the DPPT (in the engagement's Google folder), ZenDesk deal, Slack channel. Confirm: Target Start Date,
Target End Date, Deal title "BL###.## | Client Name Engagement Title", **DPPT price == SoW price**.
Create Project: create rate card; create Kantata project via the make.com scenario from the "Prepare for Delivery" notice in #delivery-ops (enter ZenDesk
Deal ID); project settings: rate card with the margin (preferably) or account, **Target margin: same as DPPT**, billing mode, tasks billable, primary group.
Roles & Rates: **Add roles from Delivery Plan Pricing Tool** (cross-reference DPPT roles with Kantata resources; Add Unnamed Resource for missing roles);
check cost & billing rates for each role match the SOW & DPPT; set Delivery Lead to Product Partner / Product Manager.
Tasks & Staffing: build out tasking to match the DPPT (title, resource estimated hours, start date, due date); update task estimates; create allocations
from estimated hours; submit resource requests (approvers: Product & Strategy = Danny, Engineering = Ralph, Other = Parvathy).
Once SoW is signed: populate custom fields, confirm start & due dates and budget, soft -> hard allocations, snapshot "Snapshot YYYY-MM-DD | SoW Signed"
as baseline; Start Project; Delivery Status Active; set Kantata End Date on the Deal.

## 5. Where the DPPT sits (synthesis of the above)
Sales/estimating (ZenDesk deal, Notion Deal) -> DPPT (price, team, sprint plan; the SOW quotes the DPPT price) -> SOW signed -> Notion Deal
(DPPT URL, Start Date, Revenue Schedules) -> DPPT Worker (parse -> DPPT Details page; writes Deal start into Tasks!AQ15) -> Kantata Worker
(tasks, rate card, allocations) -> delivery. Forecast worker reads Revenue Schedules (not the DPPT).
