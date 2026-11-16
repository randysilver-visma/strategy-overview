# Starling

A private, per-client tool that shows what a company's strategy documents say, what its work and data show, and what people understand the strategy to be, organised on Martin Eriksson's Decision Stack, with gaps, owners, open questions and a chat interface over the accumulated knowledge.

It does not make decisions. It supports better discussion and faster decisions.

## Status

Early. Each implementation is built bespoke for a client. Only the onboarding step is defined so far.

## Contents

| Path | Purpose |
| --- | --- |
| `onboarding/ONBOARDING_PROMPT.md` | Prompt the client's Claude runs: asks about ten technical points, derives the rest from the client's own material, then asks the client to confirm or challenge it |
| `onboarding/profile.template.yaml` | Blank, versioned profile: the technical answers plus a list of sourced claims |
| `design/dist/*.html` | Built mockup of the modern skin with placeholder data (open in a browser) |
| `design/src`, `design/skins`, `design/build.py` | Shared base, per-skin styles and the build script |
| `docs/SKINS.md` | How skins work and how to add one |
| `docs/DATA_MODEL.md` | The JSON shape the page renders; `design/data/sample.json` is the synthetic sample |
| `docs/DESIGN_NOTES.md` | Design decisions, assumptions and open items |

## Prerequisites per client

- A place to host the code (GitHub by default).
- A database the client can use (for example Google Sheets, Excel on SharePoint, Airtable, or a SQL database). Onboarding finds out what is available and what it can and cannot do.

## Using it

1. Create a private repo for the client and copy this package into it.
2. Run the onboarding prompt. It writes `client/onboarding/profile.yaml`, `client/onboarding/readiness-report.md` and a draft data file `client/data/draft.json` (shape in `docs/DATA_MODEL.md`).
3. Everything specific to the client stays under `client/`. The generic package's `.gitignore` excludes `client/` so nothing client-specific is committed by accident; in the client's own private repo, remove that line.

## Credits

- The Decision Stack is by [Martin Eriksson](https://www.mindtheproduct.com/the-product-decision-stack-martin-eriksson/).
- The outcome roadmap template is by [Itamar Gilad](https://itamargilad.com/outcome-roadmaps/).
- Packaged by [Out of Owls](https://outofowls.com).

## Rules

- The generic files must contain nothing that identifies a client.
- Unknown values stay `null`; assumptions are labelled and have an owner to check them.
