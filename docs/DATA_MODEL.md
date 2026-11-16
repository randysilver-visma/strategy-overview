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
| `initiatives` | `[{id, name, strat, goal, opp, fte, q, funded, ws, disc, benef, jira, com, comRisk, capSens}]` | `q` is FTE per quarter (same length as `quarters`); `strat`, `goal` and `opp` are IDs or `null`; `jira` is `{open, unsized, past}` or `null` |
| `pilot` | `[strategy ids]` | Strategies opened in the Decisions view. Empty hides the content with a prompt |
| `questions` | `[{id, cat, t, why, dm}]` | Open questions |
| `changes`, `claimDocs`, `modelChecks`, `otherDecisions` | lists | Review and Decisions content |

## Known limits (to be fixed)

- An initiative links to one strategy, goal and opportunity (many-to-many is planned).
- IDs must not contain `:` or `|`; they are used as delimiters when tracing links.
