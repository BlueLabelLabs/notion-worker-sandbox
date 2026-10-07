# DPPT: solution options

**Read me first.** This is the framing and options exploration for rebuilding the DPPT (Delivery Project Planning Tool), run with the BlueLabel architect skill (v0.1.0) as Phase 0 (ingest and frame) plus an options study. It answers three questions the architect asked: how to rebuild it in Google Sheets, what other stacks fit, and whether it belongs in Notion. It does not yet choose a platform. That choice is the first gateway decision and it is the architect's to make. Once made, the full design walk (shape, platform and realization, cross-cutting) produces the architecture spec and invariants.

Source of truth for what the tool does today: `DPPT-v6.3-requirements.md` in this folder (sections 6, 7 and 9 matter most here).

---

## 1. Design brief

### 1.1 What the DPPT is, structurally

Today one spreadsheet copy per deal carries three different concerns:

| Concern | What it is | Who uses it |
| --- | --- | --- |
| Authoring | Pick roles, type weekly hours per role per phase, set sprint or month counts, set a start date, tune the margin until the fee matches the SOW | Client Partners, Delivery leads |
| Engine | Cost-plus pricing, sequential date chain, sprint or month expansion, fractional sprints, commission math | Nobody directly; it is the formulas and the bound script |
| Outputs | Output and Allocations tables for the SOW, Rate Card and Delivery Segments for Notion and Kantata, Overview, invoice schedules | Coordinators, the Notion worker, the Kantata worker, clients (via the SOW) |

Because all three live in every copy, the engine is duplicated per deal (version drift), the authoring UI and the engine cannot be changed independently, and the outputs are consumed by scraping header text. Every option below is judged first on whether it separates the engine from the copies.

### 1.2 Drivers (assumptions to confirm)

| ID | Driver | Basis |
| --- | --- | --- |
| D1 | Tiny scale: 5 to 15 planners, tens of DPPTs a year, a handful of phases and up to 30 roles each. No latency or throughput concern. | Live Drive inventory; Team has 30 slots; Tasks has 7 phase rows |
| D2 | Users are fluent in Google Sheets and Notion. Engineering maintains TypeScript Notion Workers and Apps Script. Nobody operates infrastructure for internal tooling. | notion-worker-dppt, notion-worker-forecast; bound script |
| D3 | Confidential but not PII: cost rates, margins, commission. Clients must never see cost or margin; they do see price, fees, dates, roles, hours. Hidden columns are today's only control. | TEAM-16, GOV-09, DEF-16 |
| D4 | Integrations that must keep working: Notion Deals, Deal Revenue Schedules, DPPT Details (Rate Card, Delivery Segments) read by the Kantata worker, Slack, SOW tables. Deal Cost Schedules is planned. | Section 7; section 10.7 |
| D5 | Version drift is the structural pain: copies freeze formulas and rates; bugs ship to every copy; fixes never reach existing deals; the worker scrapes by header text. | DEF-03, PRICE-28, GOV-16 |
| D6 | The pricing model is preserved exactly; the 50 defects are designed out where possible. | Section 6; section 9 |
| D7 | Business-hours availability; a day of data loss is tolerable; small budget; ownership must survive one person leaving. | GOV-10, Q-35 |
| D8 | Deal metadata (code, title, client) lives in Notion; ZenDesk is the CRM. | PRICE-23, notion_schemas |

### 1.3 Constraints and context

- Google Workspace and Notion are both in daily use. The automation platform of record is Notion Workers (TypeScript). There is no GCP provider pack in the golden path; AWS and Azure packs exist.
- Notion made page content on worker-managed rows read-only to integrations on 2026-07-16; property writes still work. A worker with a `worker.sync` needs a managed database and changes the deploy profile.
- Live v6.1 and v6.2 copies will keep circulating for the life of their engagements. Any new tool coexists with them.
- The bound Apps Script cannot be read through the API. Its behaviour is inferred (section 5.9 of the requirements).

### 1.4 Active packs

- `universal-baseline`: always. For a no-code option most service invariants (TLS, health probes, three environments, IaC) do not apply because nothing is deployed; the ones that still apply are: any code lives in a repo with CI and review, secrets never in source, monitoring to Slack for anything that runs, auditability of changes, UTC and IANA zones where code handles dates.
- `workload/web-application` and `workload/server-side`: active only for an option that builds software.
- No compliance pack. No client pack (internal tool).

### 1.5 Architecture barrier check

Choosing the platform (Sheets, Notion, low-code, custom app) selects system-wide technology and introduces or removes system elements, so it is architecture. Everything inside a chosen platform (which formulas, which tab layout, which Notion property) is below the barrier and belongs to the build.

## 2. Decision ledger (seeded)

| Key | State | Notes |
| --- | --- | --- |
| `platform` (authoring surface and engine host) | ready | The gateway. Options A to E below. Everything else is blocked on it. |
| `app_stack` | blocked | Follows platform. TypeScript is the observed team stack (Notion Workers, Apps Script). |
| `primary_datastore` | blocked | Sheets cells, Notion databases, or PostgreSQL by option. |
| `rate_card_source` | ready | Central rate card with effective dates vs per-copy constants. Every option can decide this now; the default is central. |
| `engine_location` | ready | Engine as tested code in one deploy vs formulas per copy. Default: code, one deploy. |
| `integration_contract` | ready | Named ranges or a typed API instead of header scraping. Default: typed contract, versioned. |
| `auth` | blocked | Google Workspace identity in every option; RBAC for cost and margin visibility is the open part. |
| `observability`, `secrets`, `cicd` | blocked | Apply to whatever code exists; universal-baseline defaults (GitHub Actions, Slack alerts). |
| `sow_export` | ready | How Output and Allocations reach the SOW: paste, Google Docs generation, or a rendered Sheet view. |
| `deal_cost_schedules` | deferred | Recorded only, per the architect's request. Inputs exist in every option. |

<!-- OPTIONS -->
