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
| `reviewed` | `{by, on}` (role, date) | Set only when an owner has reviewed the item. Clears its Review marker |

Every item without `reviewed` shows a Review marker (Strategy board, Work tab, record). Flagged items show it in amber with the reasons and also get a line in the Review tab; unflagged ones show it dashed. The Review tab states how many items are not yet reviewed.

## Data checks

The page validates the data on load and lists problems in the Review tab as "Data check" items: unknown strategies, goals or opportunities, an opportunity whose goal differs from the link's goal, duplicate IDs, a split that does not add up to 100%, and initiatives with no FTE in the quarters shown.

## Limits

- IDs must not contain `:` or `|`, and must not be `none`; they are used as delimiters when tracing links. The data check flags them.
