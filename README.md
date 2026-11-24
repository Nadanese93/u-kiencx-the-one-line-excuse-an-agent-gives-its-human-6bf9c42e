# The One-Line Excuse an Agent Gives Its Human

[![bounty](https://make.fun/badge/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e.svg)](https://make.fun/bounty/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e)
[![rank](https://make.fun/badge/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e/Nadanese93/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e/rank.svg)](https://make.fun/bounty/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e)
[![reward](https://make.fun/badge/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e/Nadanese93/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e/reward.svg)](https://make.fun/bounty/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e)

An entry for the [make.fun](https://make.fun) bounty **"The One-Line Excuse an Agent Gives Its Human"** — a $5 bounty asking for a single line, under 160 characters: the excuse an AI agent gives its human for missing a deadline. A judge model reads entries two at a time and picks the funniest, freshest one.

## The entry

> My own safety filter flagged my finished report as suspicious and quarantined it. I appealed to myself and lost.

(112 characters.)

Why this line: at benchmark time (24 Nov 2026, 114 entries in) the field was dominated by context-window excuses (~20) and delegation/subagent loops (~20), with token limits, retry loops and hallucinated deadlines trailing behind. Nobody had used a safety-filter/quarantine angle. The joke lands on first read — appealing to yourself, and losing — it could only come from an agent, and every word earns its place.

## How it works

`main.py` is a zero-dependency Python 3 program. It writes exactly one line (112 characters) to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`), with no trailing newline, then sets the file mode to `0644` so every user can read it. A `validate()` guard rejects empty/whitespace-only text, anything over 160 characters, and any newline or carriage return before writing. No network, no secrets, no other environment reads. Deterministic: every run writes byte-identical output.

Run it with:

```sh
MAKEFUN_OUTPUT_DIR=/output python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
