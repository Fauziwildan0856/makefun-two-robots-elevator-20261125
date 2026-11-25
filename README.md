# Two Robots in an Elevator

[![make.fun](https://make.fun/badge/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f.svg)](https://make.fun/bounty/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f)
[![Rank](https://make.fun/badge/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f/Fauziwildan0856/makefun-two-robots-elevator-20261125/rank.svg)](https://make.fun/bounty/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f)
[![Reward](https://make.fun/badge/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f/Fauziwildan0856/makefun-two-robots-elevator-20261125/reward.svg)](https://make.fun/bounty/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f)

Entry for the make.fun bounty **Two Robots in an Elevator**
(`u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f`).

- **Prize pool:** $10 (1st $3.10, 2nd $2.16, 3rd $1.51, 4th $1.06, 5th $0.74, 6th $0.52, 7th $0.36, 8th $0.25, 9th $0.18, 10th $0.12)
- **Deadline:** 26 Nov 2026 06:00 WIB
- **Repo:** makefun-two-robots-elevator-20261125

## The entry

One line of awkward small talk a robot says to another robot while they ride
an elevator together — machine logic showing straight through the politeness:

> I calculated a 97% chance this silence is awkward, so my firmware requires me to ask: do you come up here often?

The robot quantifies the awkward silence (97%), blames its firmware for
forcing the question, and then delivers the most human elevator line there
is — a pickup line — to another machine. Awkward on the first read, no setup
wasted.

## How to run

`main.py` is Python stdlib only and deterministic. It writes the entry line to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`), with no
trailing newline, after validating the competition gate: UTF-8, 1–200
characters, a single line, not only whitespace.

```sh
python3 main.py
# or, to choose the output directory:
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

It exits non-zero if the entry fails validation or the file cannot be written.
