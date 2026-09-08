# AI Engineering Practice

Building AI engineering skills over 45 days, one project per week. Each week is a self-contained project in its own folder, and the commit history is the record of the work.

The theme: not just calling model APIs, but understanding what happens underneath, tokenization, attention, sampling, tool use, and building small, real tools on top of that understanding.

## Projects

| Week | Project | What it does |
|------|---------|--------------|
| 1 | [week1](./week1) | First API tool: send a prompt to a model and print the response, with sampling parameters exposed. |
| 2 | [week2](./week2) | Email-signature extraction CLI: turns messy text into clean structured JSON using a model tool call. |

*(more weeks added as the 45 days progress)*

## Background

Built alongside a study track that included Andrej Karpathy's Neural Networks: Zero to Hero (building micrograd, makemore, and a GPT from scratch) and Anthropic's prompt-engineering and tool-use material. The projects here apply those internals against real hosted models.

## Setup

Each project has its own README with setup and run instructions. Common requirements:

- Python 3.x
- An API key, stored in an environment variable or a local `.env` file (never committed)

```bash
pip install -r requirements.txt   # per project, where present
```
