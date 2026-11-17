# Strategy Mirror readiness report: Agentic Experience (AX)

Interview held 2026-11-16 between the consultant and Claude. Profile: `client/onboarding/profile.yaml`. Nothing below has yet been confirmed by the people named, except where it says so.

## Verdict

**Not ready to build.** Hosting and the data-store setup are provisional, and the only source that shows what AX actually does (Jira) has no read permission yet. Five blockers are listed below. Most sit with the consultant's tech contact.

## Decided, and by whom

| Area | Decision | Decided by | Status |
|---|---|---|---|
| Scope | The AX team; Org vision and objectives as context | Consultant | Sponsor to confirm |
| Sponsor | Product Lead, AX | Consultant | Sponsor to confirm |
| Day-to-day contact | Consultant; AX-only questions go through the sponsor | Consultant | Sponsor to confirm |
| Access | Any e-conomic/Visma employee via SSO; may narrow to a named group | Consultant | Provisional |
| Hosting | On GitHub if possible | Consultant | Provisional; tech contact |
| Data store | Slite, tested 2026-11-16 | Consultant | Setup provisional |
| Setup | 1. Slite plus a backend that logs changes. 2. On GitHub: changes as pull requests, approved by merge. 3. Fallback: scheduled snapshot plus a "change through the Changes collection" rule | Consultant | Depends on hosting |
| Backup | Git history if on GitHub, otherwise Slite's own | Consultant | Not business-critical |
| Framework | OKRs, mapped onto the Strategy Mirror model; the mapping is largely unknown | Consultant | |
| Effort | FTE per quarter | Consultant | Until AX shows otherwise |
| Confidence | Hypothesis, partly validated, validated | Consultant | |
| Link changes | Initial batch signed off by the Product Lead; then the initiative owner proposes and the goal owner approves | Consultant, on Claude's recommendation | |
| Ownership | Strategies: Product Lead and Engineering Lead jointly (what/why vs how/capacity; escalate to governance). Goals: Product Lead, governance approves changes. Initiatives: named owner each. Org vision and objectives: CPO | Consultant | None confirmed by role-holders |
| Administrator | Consultant during the pilot | Consultant | |
| AI provider | Claude via the company's Claude account | Consultant | API key use to check |
| Names on the page | Shown, for now | Consultant | |
| Approval deadline | None in the pilot; show how long changes wait | Consultant | |
| Notices | Private Slack channel for AX | Consultant | To be created |

## Slite test results (2026-11-16)

Run by the consultant in a claude.ai chat, because approvals for the connector's write tools don't work from this session.
- Links between collections work, including many-to-many.
- Links read back as titles, not ids. Every row needs a short unique id in its title, and titles must not contain commas.
- There is no record of who changed a cell. Rows carry only a "last edited at" time. This is the main reason for preferring a setup that logs changes.
- Not tested: concurrent edits, field-level permissions, size limits.
- Six archived test docs need deleting in Slite. Two older "[TEST] Strategy Mirror spike" docs from 11 Nov are also in the consultant's personal channel.

## Blockers

| # | Blocker | Owner | Needed by |
|---|---|---|---|
| 1 | Code host and hosting: stay in the personal repo or move; GitHub Pages behind SSO (needs GitHub Enterprise Cloud, unverified); who keeps it running | Tech contact | Before the first build |
| 2 | Approvals before going live: security, privacy, architecture, AI use | Tech contact | Before opening the page beyond the consultant |
| 3 | Slite API key, and a Claude API key if the build calls Claude: who holds them, where they're stored | Tech contact or IT | Before the first build |
| 4 | Jira read permission: which projects and fields | Engineering Lead, AX | Before showing "done" evidence |
| 5 | List of the competing AX strategy documents, each with owner and permission | Consultant | Before the first build |

## Assumptions still open

- Sensitivity of S1 (Jira), S2 (Slite roadmap) and S3 (review decks) is "general".
- Everyone who would propose or approve a change has GitHub access.
- No level sits between the Org objectives and AX.
- GitHub Pages serves static files only, so writes need a backend or pull requests (unverified).
- The planning horizon, review cadence and governance team details are unknown.

## Coverage gaps

- No source is named yet for the Org vision or Org objectives.
- Strategy and goals have only "said" evidence. Jira covers the work level only, and its permission is pending.
- "Understood" evidence comes only from team slides in the review decks.

## First version will include

- AX only.
- The Slite roadmap (S2) and published strategy review decks and notes (S3), plus the competing strategy docs once listed.
- The prototype's views, with AX content in place of placeholders.
- Changes proposed as pull requests.
- Decision points created in the tool (a requirement, since AX doesn't record them well yet).

## First version will not include

- Jira "done" evidence (until permission is granted and Jira is examined)
- e-conomic/Visma branding
- Chat over the knowledge base
- Approval deadlines and escalation

## Feedback on the onboarding approach

The consultant noted that much of this interview (sources, schema, owners, roles) can and should be derived from documentation and proposed for confirmation. Only the tech setup really needs question-by-question answers. We'll revise the onboarding approach next.
