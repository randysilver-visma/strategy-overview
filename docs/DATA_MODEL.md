# Data model

The page renders whatever is in `window.STARLING_DATA`. `design/build.py` inlines it from a JSON file:

```
python design/build.py                          # uses design/data/sample.json (synthetic)
python design/build.py --data client/data.json  # a client's own data
```

`design/src/base.html` holds no client data. Everything a client would change is in the JSON.

## Top-level keys (`schema: "starling-data/1"`)

| Key | Shape | Notes |
| --- | --- | --- |
| `meta` | `{org, team, teamFull, snapshot, sources, claims, sample?, built?}` | `sample: true` shows the synthetic-data footer note |
| `text` | `{source, tracker, review, pilot, decision, brief, discretionRule, workstream}` | The client's own words: data store name, issue tracker, review name, decision pilot, decision ID, decision document, discretion rule, workstream label. All optional, with neutral defaults |
| `quarters` | `[{label, year}]` | Any number of quarters; the roadmap and FTE tables follow it |
| `horizon` | `{label, from, to}` | Quarter indices averaged for the "planning year" FTE figures; `label` is shown in the page |
| `vision` | string | The North Star |
| `objectives` | `[{id, name}]` | Org objectives |
| `strategies` | `[{id, name, status, stated, objs, success, outputOnly?, proxies?, goals, opps}]` | `status`: `on`, `risk` or `na`; `stated` is the strategy's stated FTE; `objs` are objective IDs |
| `strategies[].goals` | `[{id, name, measured, measures: [{m, by, kind}]}]` | `kind`: `outcome` or `output`; `by` is the target year or `null` |
| `strategies[].opps` | `[{id, name, goal}]` | Proposed opportunities; `goal` is a goal ID or `null` |
| `initiatives` | `[{id, name, links, split?, fte, q, funded, ws, disc, benef, jira, com, comRisk, capSens}]` | `links` is `[{strat, goal, opp}]` (an initiative can serve several strategies; an empty list means unlinked). `strat`, `goal` and `opp` on their own still work as a single link. `split` is `{strategyId: share}`; without it the FTE is split equally across the strategies. `q` is FTE per quarter (same length as `quarters`); `jira` is `{open, unsized, past}` or `null` |
| `pilot` | `[strategy ids]` | Strategies opened in the Decisions view. Empty hides the content with a prompt |
| `questions` | `[{id, cat, t, why, dm}]` | Open questions |
| `changes`, `claimDocs`, `modelChecks`, `otherDecisions` | lists | Review and Decisions content |

## Best guesses and review flags

Starling is a mirror: it shows its best guess from the sources and does not wait for approval. Any strategy, goal, opportunity or initiative may carry:

| Field | Shape | Meaning |
| --- | --- | --- |
| `conf` | `high`, `medium` or `low` | How well the sources support the value. `low` flags the item |
| `flags` | list of `conflict`, `low_confidence`, `single_source`, `stale`, `no_owner`, `unclear` | Why an owner should look at it |
| `alternatives` | `[{value, source}]` | Other values found in other sources, shown beside the best guess |
| `owner` | text (also allowed on Org objectives) | Who owns the item. Strategies should have one. A challenge on an item with no owner notifies the owner of its parent (initiative → opportunity → goal → strategy) |
| `reviewed` | `{by, on, value?}` (role, date, preferred value) | Set only when an owner has reviewed the item. Clears its Review marker |
| `challenges` | `[{by, on, note}]` | Set when a reader challenges the item. The item also gets the `challenged` flag and stays in the review list |

Every item without `reviewed` shows a Review marker (Strategy board, Work tab, record). Flagged items show it in amber with the reasons and also get a line in the Review tab; unflagged ones show it dashed. The Review tab states how many items are not yet reviewed.

## Reviewing and the database

On the Review tab every row opens the item (or the related tab). In an item's record an owner can **Mark reviewed**, **Challenge** (with a note) or **Prefer** one of the other values found; each needs the person's role. In the sample page these actions change the page only. A live build reads reviews from, and writes them to, the client's database. The page calls `window.STARLING_HOOKS.onReview(event)` for every action, with `{rid, kind, id, action: "reviewed" | "challenge", by, on, note, value}`; the event also carries `notify` (the owner to tell, found by walking up from the item) and `notifyVia` (the parent it came from). The storage adapter implements that hook and puts `reviewed` / `challenges` back into the data on the next load.

## Ask Starling (chat overlay)

A side panel, opened from the header or the floating button. In the sample it answers from the page data (review and flags, conflicting sources, unlinked work, goals with no initiative, unfunded work, FTE coverage, owners, decisions, open questions), cites the records it used and says how much is unreviewed. A live build sends the question to a model hosted inside the client's network. Optional `chat` block: `{intro, chips: [..], answers: [{k: [keywords], a: text, cites: [record ids], act: [[label, "#view"]]}]}`; its answers are tried before the built-in ones.

### Responding to a challenge

The owner (or whoever the live build allows) can **Accept** a challenge, which flags the item "Challenge accepted, edit pending" until it is edited and reviewed, or **Reject** it with a reason. Each challenge in `challenges` then carries `status` (`accepted` or `rejected`) and `response: {by, on, reason}`. The hook receives `challenge_accepted` and `challenge_rejected` events. A challenge unanswered for more than `meta.challengeDays` (default 7, an assumption to confirm per client) is **overdue**. It is listed first in the Review tab with a "Challenges overdue" filter, and it escalates to the next distinct owner up the chain (item, then parent goal or strategy, then the strategy's Org objective, which may carry an `owner`). If nobody is above, it says so. There is one escalation only: a challenge that is still unanswered stays overdue at the top of the list and does not escalate again (decided). The page shows this; the live adapter sends the escalation.

## Model checks

The page computes these from the links and shows them in the Review tab. Each is something that should not occur: work not linked to any strategy, work linked to a strategy but to no goal or opportunity, goals with no initiative, goals with no outcome measure, opportunities not under a goal, strategies with no goals or no Org objective, and Org objectives that no strategy serves. A check clears itself when the data changes. `modelChecks` in the data file is optional and only for extra checks the import found: `[{title, detail}]`.

## From onboarding claims to a data file

```
python design/claims_to_data.py client/onboarding/profile.yaml --out client/data/draft.json
python design/build.py --data client/data/draft.json
```

`design/claims_to_data.py` reads the profile's `claims` (YAML needs PyYAML, or give JSON) and writes the data file. A worked example is `design/examples/profile.example.yaml`.

- Every claim that is not `rejected` becomes an item. `confidence`, `flags`, `alternatives` and `sources` (shown in the record as "Found in", with the quote) are carried over. Rejected claims are dropped and listed in the report.
- An item is `reviewed` only when `status` is `reviewed_ok` or `edited` and `reviewed_by_role` is set.
- `model.objectives`, `model.strategies`, `model.goals`, `model.opportunities` and `work.initiatives` carry the model. `value` may be one object or a list of them. Strategies, goals, opportunities and initiatives may carry `owner`; `roles.owner` with `{id, owner}` sets it afterwards.
- `cadence.horizon` supplies `quarters` and `horizon`; without it the periods are labelled Period 1..n and the script warns. `sources.inventory` becomes the source documents (with a count of claims citing each and how many conflict), and `open_items` become the Open questions.
- Initiative `links` use `strategy`, `goal` and `opportunity`; `fte_by_quarter`, `funded`, `workstream`, `discretionary`, `beneficiary` and `tracker` map to the page's fields. A `split` may be percentages or fractions.
- Fields the page does not use (terminology, principles, division level and similar) are left in the profile and listed in the report. The page runs its own data checks on load, so broken links show in the Review tab.

## Data checks

The page validates the data on load and lists problems in the Review tab as "Data check" items: unknown strategies, goals or opportunities, an opportunity whose goal differs from the link's goal, duplicate IDs, a split that does not add up to 100%, and initiatives with no FTE in the quarters shown.

## Limits

- IDs must not contain `:` or `|`, and must not be `none`; they are used as delimiters when tracing links. The data check flags them.
