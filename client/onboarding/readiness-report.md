# Strategy Mirror readiness report: Agentic Experience (AX)

Updated 2026-11-17 for onboarding 0.2.0 ("ask, derive, confirm or challenge"). The 0.1.0 report from the 16 November interview is in `archive/readiness-report-0.1.0.md`. Profile: `client/onboarding/profile.yaml`.

## Verdict

**Not ready to build.** The Ask phase is mostly done. Hosting and the data-store setup are provisional, the read grant is partial, and the Import phase has not started, so no claims have been derived from AX's own documents yet.

## Where onboarding stands

| Phase | State |
|---|---|
| 1. Ask (technical and permissions) | Mostly done. Hosting, approvals, keys and data location wait on the tech contact (questions doc for 17 Nov). |
| 2. Import (from granted sources) | Not started. Can begin now with the AX roadmap in Slite and the published review decks. |
| 3. Review queue (flagged items only) | Not started. |

## What changed with 0.2.0

- **One read grant replaces per-document permission.** AX has a partial grant: the Slite roadmap and published review material. Still needed: the competing strategy documents (or the spaces that hold them) and Jira.
- **Best guesses are shown, not held back.** Everything you told me in the interview about the model, work and roles is now one of 18 **claims** with origin "stated". The page will show them as best guesses with a Review marker until the named owner reviews them.
- **Flags route items to the right reviewer.** Of the 18 claims: 1 conflict (the competing strategy documents), 5 single-source, 1 with no owner, 7 unclear. None has been reviewed by its owner yet.

## Decided, and by whom

Unchanged from the 0.1.0 report: scope (AX), sponsor (Product Lead, AX), Slite as the store with a change log, GitHub hosting (provisional), Claude via the company account, names shown on the page, notices to a private AX Slack channel, consultant as administrator for the pilot. All were decided by the consultant, and none has yet been confirmed by the sponsor.

## Blockers

| # | Blocker | Owner | Needed by |
|---|---|---|---|
| 1 | Code host and hosting: GitHub Pages behind SSO; who keeps it running | Tech contact | Before the first build |
| 2 | Approvals before going live | Tech contact | Before opening the page beyond the consultant |
| 3 | Slite and Claude API keys: holder and storage | Tech contact or IT | Before the first build |
| 4 | Read grant for the competing strategy documents and further Slite pages | Consultant | Before import |
| 5 | Jira read permission | Engineering Lead, AX | Before showing "done" evidence |

## Coverage gaps

- No source for the Org vision or Org objectives yet.
- Strategy has only "said" evidence.
- No "done" evidence until Jira is granted.
- "Understood" evidence comes only from team slides in the review decks.

## Next step

Run the Import phase on the granted sources:
1. Read the AX roadmap and the published review decks and turn what they say into claims, each with a source and a short quote.
2. Flag conflicts, low confidence, single-source, stale and ownerless items.
3. Build a draft page with `design/claims_to_data.py`.

Then review only the flagged items with you.

## First version will include

- AX only.
- Best guesses from the Slite roadmap, the published review decks and the strategy documents once granted, each flagged where unsure.
- Challenges and changes proposed as pull requests.
- Decision points created in the tool.

## First version will not include

- Jira "done" evidence (until permission)
- e-conomic/Visma branding
- A live model behind the chat (the page's chat answers from page data only)
- Approval deadlines beyond the page's built-in 7-day "overdue" marker
