#!/usr/bin/env python3
"""Build each skin into a standalone HTML page.

Usage:  python design/build.py                    -> design/dist/<skin>.html (full documents)
        python design/build.py --data FILE.json   -> same, with the client's data instead of design/data/sample.json
        python design/build.py --bare DIR         -> DIR/<skin>.html without doctype/head wrapper
                                                     (for hosts that add their own page skeleton)
Data shape: docs/DATA_MODEL.md. Flags can be combined.
"""
import base64, json, pathlib, sys
here = pathlib.Path(__file__).parent
base = (here / "src" / "base.html").read_text(encoding="utf-8")
data_path = here / "data" / "sample.json"
if "--data" in sys.argv:
    data_path = pathlib.Path(sys.argv[sys.argv.index("--data") + 1])
data = json.loads(data_path.read_text(encoding="utf-8"))
# "</" is escaped so a data value can never close the inline <script>
data_js = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
bare = None
if "--bare" in sys.argv:
    bare = pathlib.Path(sys.argv[sys.argv.index("--bare") + 1]); bare.mkdir(parents=True, exist_ok=True)
out = here / "dist"; out.mkdir(exist_ok=True)
for d in sorted((here / "skins").iterdir()):
    if not d.is_dir(): continue
    cfg = json.loads((d / "config.json").read_text(encoding="utf-8"))
    page = base
    page = page.replace("/*@TOKENS@*/", (d / "tokens.css").read_text(encoding="utf-8"))
    page = page.replace("/*@SKIN@*/", (d / "skin.css").read_text(encoding="utf-8"))
    page = page.replace("<!--@FONTS@-->", '<link rel="stylesheet" href="%s">' % (d / "fonts.txt").read_text(encoding="utf-8").strip())
    page = page.replace("/*@TITLE@*/", cfg["title_tag"])
    page = page.replace("/*@CONFIG@*/{}", json.dumps(cfg))
    page = page.replace("/*@DATA@*/{}", data_js)
    logo = ""
    if cfg.get("logo"):
        b64 = base64.b64encode((here / "assets" / "out-of-owls-logo.png").read_bytes()).decode()
        logo = '<div class="bty"><span>%s</span><img class="oo-logo" alt="Out of Owls" src="data:image/png;base64,%s"></div>' % (cfg.get("broughtBy", "Brought to you by"), b64)
    page = page.replace("<!--@LOGO@-->", logo)
    if bare:
        (bare / (d.name + ".html")).write_text(page, encoding="utf-8")
        print("built (bare)", d.name)
        continue
    wrapper = '<!doctype html>\n<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><style>[hidden]{display:none!important}body{margin:0}</style>\n'
    (out / (d.name + ".html")).write_text(wrapper + page + "\n</html>\n", encoding="utf-8")
    print("built", d.name)
