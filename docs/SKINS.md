# Skins

The page is built from one shared base plus a small skin per look, so a client can pick a style (or have one made) without touching the logic.

```
design/
  src/base.html          shared page: the six views, sample data model, scripts and layout
  skins/<name>/
    tokens.css           colour and font tokens (light and dark, or one look)
    skin.css             overrides for type, wordmark, post-it notes and background
    config.json          page title, wordmark, tagline and flock style
    fonts.txt            Google Fonts stylesheet URL
  build.py               builds each skin into design/dist/<name>.html
```

Build: `python design/build.py`. For hosts that add their own page skeleton: `python design/build.py --bare <dir>`.

## The shared idea (all skins)

- **North Star:** the company vision.
- **Views:** Overview (the flock and six levels), Strategy (objectives → strategies → goals → opportunities → initiatives, with traceable links), Work (outcome roadmap by quarter, plus FTE by strategy or beneficiary), Decisions (the current pilot decision, its blocking gaps, the portfolio and a what-if per initiative), Open questions and Review.
- **Flock:** each bird is a team or person. Tightness is computed from the levels that have a measure (work, team goals, team strategies); team role, Org objectives and the North Star show as not assessed until they have one. It is an illustrative score, not a measured metric.
- **Flock behaviour:** each bird follows its seven nearest neighbours (as real starlings do), with soft separation and some wander. The flock's target path leans toward the star as alignment rises and away from it as alignment falls. At high alignment the flock occasionally splits in two and rejoins. Lower alignment is looser and more jumbled. The score is computed once at load; there is no live alignment control in the shipped page.
- **Levels:** six bars under the flock, from work to the North Star, each coloured by its gap severity and linking to its view.
- **Open questions:** shown as post-it notes, each with a suggested decision maker.

## Skins so far

| Skin | Look | Flock |
| --- | --- | --- |
| modern | Neutral canvas in Out of Owls brand colours, large type, tabbed views, post-it questions, gradient green-amber-red level bars, violet for unfunded work, star-dotted wordmark with a tagline, soft tonal-wash background, North Star top right. The header logo is off (`logo: false`). | Chevron birds, no trails |

Three further skins (starling, corporate, arcade) were tried and dropped. The playful `starling` skin (grid paper, navy and yellow, sticky notes) was removed in favour of a single look.

`config.json` options: `product` (the product name shown in the wordmark, title and "Ask" buttons; default Starling), `title_tag`, `wordmark` (star-dotted "i"), `tagline`, `logo` (true shows the logo from `design/assets` with the `broughtBy` text), `broughtBy`, `starLabel`, `birds` (`chevron` is the one drawn), `alpha`, `colorVar`.

## Adding a skin

1. Copy an existing folder under `design/skins/`.
2. Edit tokens, CSS and config. Define every colour as a token on `:root`; a dark variant redefines tokens only.
3. Run `python design/build.py` and open `design/dist/<name>.html`.

## Status colours

In the Modern skin the level bars use a continuous green to amber to red gradient driven by a gap-severity score (0 aligned, 1 severe). Red appears only where severity is high. The scores in the sample are invented; in a real build they must come from a defined measure, not a judgement call.

## Notes

- Designed for desktop. At phone width the page stacks and the wide boards scroll sideways inside their own box; it has been checked in a headless browser only.
- Fonts load from Google Fonts. Offline, the page falls back to system fonts.
