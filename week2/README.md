# Week 2 — Email-Signature Extraction CLI

A command-line tool that takes a messy block of text (like an email signature) and returns clean, structured JSON, name, email, company, and more, by having the model call a single tool.

## What it does

Feed it unstructured text; it returns a structured record:

```
Input:   "Best regards, Sarah Chen | Senior PM | Brightwave Analytics | sarah.chen@brightwave.io"
Output:  {"name": "Sarah Chen", "email": "sarah.chen@brightwave.io",
          "company": "Brightwave Analytics", "title": "Senior PM", "phone": null}
```

## Run

```bash
python structuring_mess.py
```

<!-- TODO: replace with your actual run command / how you pass input (arg? stdin? file?) -->

## The interesting part: tool-calling as structured output

The reliable way to get structured data out of a model isn't to ask it to *write* JSON as text (which it can format wrong). Instead, this tool defines a single function whose **parameters are the schema** (`name`, `email`, `company`, ...). The model "calling" that function *is* the structured output, guaranteed to match the fields with the right types.

The flow: send the messy text plus the tool definition, the model responds with a tool-use request whose arguments are the extracted fields, and those arguments are the result.

## Handling messiness

Real signatures are messy: missing fields, noise, legal disclaimers, multiple emails, weird formatting. The tool is designed to return `null` for absent fields rather than hallucinate them. `test_signatures.py` holds a set of deliberately messy test cases, each stressing a different failure mode (missing company, forwarded-header noise, two email addresses, international formats, and so on).

## Files

- `structuring_mess.py` — the CLI tool
- `test_signatures.py` — messy test signatures with a few expected outputs to grade against

## Setup

```bash
pip install <your-sdk>          # TODO: e.g. anthropic
export API_KEY="your-key"       # TODO: your actual env var; never hardcode the key
```

## What I learned

- Defining a tool whose parameters mirror the desired schema is a more reliable path to structured output than parsing free-text JSON.
- A plausible-looking answer isn't proof the extraction was complete, testing against varied messy inputs surfaces the fields the model quietly drops.
