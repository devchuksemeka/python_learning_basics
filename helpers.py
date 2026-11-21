"""
Carojon Academy - class helpers
First cell of every notebook:   from helpers import *

What you get
------------
show(demo)           Launch a Gradio app right under the cell (closes the previous one for you)
%%web                Weeks 7-8: run HTML / CSS / JavaScript and SEE the page under the cell
%%web 400            ...same, but 400px tall
%%web 400 index.html ...same, and also SAVE it as my_site/index.html
%%console            Week 8: run JavaScript and see console.log() output
open_page("index.html")   Open a saved page from my_site/ in your real browser
"""
import html as _html
import webbrowser
from pathlib import Path

from IPython.core.magic import register_cell_magic
from IPython.display import HTML, display

SITE_DIR = Path("my_site")
_running = []


def show(demo, height=520):
    """Launch a Gradio app inline. Closes the app from the previous call first."""
    for old in _running:
        try:
            old.close()
        except Exception:
            pass
    _running.clear()
    demo.launch(inline=True, height=height, quiet=True)
    _running.append(demo)


def _frame(page: str, height: int) -> HTML:
    srcdoc = _html.escape(page, quote=True)
    return HTML(
        f'<iframe srcdoc="{srcdoc}" '
        f'style="width:100%;height:{height}px;border:2px solid #cfd8dc;'
        f'border-radius:10px;background:white"></iframe>'
    )


@register_cell_magic
def web(line, cell):
    """Render HTML/CSS/JS from a cell. Optional: a height (number) and a filename."""
    height, filename = 300, None
    for token in line.split():
        if token.isdigit():
            height = int(token)
        else:
            filename = token
    if filename:
        SITE_DIR.mkdir(exist_ok=True)
        (SITE_DIR / filename).write_text(cell, encoding="utf-8")
        print(f"Saved -> {SITE_DIR / filename}   (open in your browser: open_page('{filename}'))")
    display(_frame(cell, height))


@register_cell_magic
def console(line, cell):
    """Run JavaScript and show console.log output underneath."""
    page = f"""<pre id="console" style="font-family:monospace;background:#111;color:#7CFC00;
padding:12px;border-radius:8px;min-height:40px;white-space:pre-wrap;margin:0"></pre>
<script>
const _out = document.getElementById('console');
console.log = (...args) => {{
  _out.textContent += args.map(a => typeof a === 'object' ? JSON.stringify(a) : String(a)).join(' ') + '\\n';
}};
window.onerror = (msg, src, line) => {{
  _out.textContent += 'ERROR: ' + msg + ' (line ' + line + ')\\n';
}};
</script>
<script>
{cell}
</script>"""
    height = int(line) if line.strip().isdigit() else 220
    display(_frame(page, height))


def open_page(filename="index.html"):
    """Open a saved page from my_site/ in your real browser."""
    path = (SITE_DIR / filename).resolve()
    if not path.exists():
        print(f"I can't find {path}. Did you run a %%web cell with that filename?")
        return
    webbrowser.open(path.as_uri())


print("Ready! show(), %%web and %%console are available in this notebook.")
