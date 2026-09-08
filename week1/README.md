# Week 1 — Prompt In, Response Out

A first command-line tool that sends a prompt to a language model and prints the reply, with the sampling parameters exposed so you can see how each one changes the output.

## What it does

Takes a prompt (and optional settings), sends it to the model, prints the response. The point of the exercise was to get a working API loop and then *observe* how temperature and max tokens change what comes back.

## Run

```bash
python chat.py "Explain attention in one paragraph."
```

<!-- TODO: replace with your actual filename and flags if different -->
<!-- e.g. python chat.py "your prompt" --temperature 0.2 --max-tokens 200 -->

## Setup

```bash
pip install <your-sdk>          # TODO: e.g. anthropic  or  google-genai
export API_KEY="your-key"       # TODO: use your actual env var name; never hardcode the key
```

The key is read from the environment, never written in code.

## What I learned

- **Temperature** reshapes the next-token distribution before sampling. Low temperature sharpens toward the single most likely token (focused, repeatable); high temperature flattens it so less likely tokens get chosen (varied). This is the softmax-over-logits step, with a knob on it.
- **Max tokens** is a hard ceiling, not a "be concise" instruction. Hit the cap and the reply stops mid-sentence. To get a shorter answer, ask for one in the prompt.

<!-- TODO: add a line or two of your own observations from actually running it -->
