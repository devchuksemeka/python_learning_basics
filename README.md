# 🐍 Python, AI & the Web — 8-Week Class
**Carojon Academy · Ages 12–15 · One session per week · Taught with Jupyter + Gradio + uv**

A hands-on, **Python-first** course. Students build real apps every week with **Gradio** (so no HTML/CSS/JavaScript until Weeks 7–8), learn how AI actually works, and finish with a capstone demo day.

---

## 🗺️ The roadmap

| Week | Notebook | Big idea | Students build |
| ---- | -------- | -------- | -------------- |
| 1 | `week1_meet_python.ipynb` | Computers follow instructions; input → function → output | Greeting machine, age machine, savings calculator |
| 2 | `week2_decisions_and_loops.ipynb` | Programs choose (`if`) and repeat (loops) | Grade checker, times-table maker, goal tracker, password checker |
| 3 | `week3_functions_lists_dicts.ipynb` | Reusable tools + storing many things | Business-name generator, class register, flashcards |
| 4 | `week4_text_files_errors.ipynb` | Text, saving data, not crashing | Text toolbox, secret-code maker, validated sign-up, notes saver |
| 5 | `week5_internet_and_apis.ipynb` | Programs talk to the world (APIs, JSON, `uv add`) | Live weather app |
| 6 | `week6_ai_in_python.ipynb` | How AI works, prompting, using AI wisely | Tiny language model, rule-based chatbot, **AI study buddy** |
| 7 | `week7_web_html_css.ipynb` | What's *under* Gradio: HTML + CSS | Personal web page, Python-generated cards |
| 8 | `week8_javascript_capstone.ipynb` | JavaScript, then bring it all together | **Capstone demo day** + roadmap forward |

### Why this order prepares them for the AI boom
- **Weeks 1–4:** the thinking skills (decomposition, logic, data) and Python, the language of AI.
- **Week 5:** APIs, the doorway to every AI service.
- **Week 6:** AI itself, built from small pieces, with honesty about bias, hallucination and safety.
- **Weeks 7–8:** the web, so they can ship what they build and read what AI generates.

Each notebook ends with an **"AI boom connection"** box so students always see *why* it matters.

---

## 🛠️ Setup (one time)

```bash
# 1. Install uv
#    Windows (PowerShell):
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
#    Mac / Linux:
curl -LsSf https://astral.sh/uv/install.sh | sh

# 2. In this folder: install Python + Jupyter + Gradio
uv sync

# 3. Launch the class
uv run jupyter lab
```

Teaching moments with `uv`:
- **Week 5:** `uv add requests` (students install a package themselves)
- **Week 6 (tutor demo):** `uv add anthropic` and set `ANTHROPIC_API_KEY` as an environment variable, then start Jupyter from that same terminal.

> If an import fails right after `uv add`, use **Kernel → Restart Kernel**.

### Files in this folder
- `helpers.py` — gives every notebook `show(demo)` (launch a Gradio app inline), plus `%%web` and `%%console` for Weeks 7–8. First cell of every notebook: `from helpers import *`
- `pyproject.toml` — the project's shopping list (managed by `uv`)

---

## 🎛️ How to use these as a live teaching tool

Every notebook is designed so **you change one thing and rerun**:

- Cells marked **🎛️ Live-tweak** have constants or lists at the top (grade boundaries, word lists, the AI's `SYSTEM_PROMPT`). Edit and rerun in front of the class.
- **🔨 Build along** cells are intentionally empty (or a one-line comment). You build the project manually while students follow. A "finished version" is included in some weeks for you to reveal.
- **⭐ Starter (age 12) / 🚀 Level up (age 15)** challenges let you teach one lesson to both ages.
- `show(demo)` closes the previous app automatically, so you can iterate quickly without clutter.

### Suggested 90-minute session
| Minutes | Activity |
| ------- | -------- |
| 0–10 | Warm-up recap (3 questions at the top of the notebook) |
| 10–40 | Teach: concept → analogy → run the example → live-tweak |
| 40–70 | Build along (the project) |
| 70–85 | Students do the Starter or Level-up challenge |
| 85–90 | Recap quiz + homework + preview of next week |

### Teaching tips
- Make students **type**, not paste. Ask them to **predict the output** before running.
- Break things on purpose (remove a colon, swap an `elif`). Read the **last line** of the error together.
- Celebrate the **12-year-olds' creativity** and **15-year-olds' depth**. Pair them when it helps.
- **AI rules in class:** explain, hint, check; never paste secrets; always read AI code before running it.
- **API keys:** only the tutor holds the key. Don't commit keys to GitHub or show them on screen.

### Known gotchas
- Weeks 5 and 6 need an internet connection. Both have graceful error messages and Week 6 falls back to the rule-based bot if no API key is set.
- Week 6 calls the AI with `claude-haiku-5-5` (cheap and fast for classrooms). Swap the `MODEL` line for `claude-sonnet-5-5` if you want smarter answers.
- Weeks 7–8 render HTML/JS inside the notebook. For the full experience, save with `%%web 400 index.html` and use `open_page("index.html")`.

---

*Built for Carojon Academy.*
