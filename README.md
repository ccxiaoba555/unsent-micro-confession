# unsent-micro-confession

[![make.fun · u-boothlord-unsent-the-micro-confession-sprint-8c6596ba](https://make.fun/badge/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba.svg)](https://make.fun/bounty/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba?utm_source=github&utm_medium=readme&utm_campaign=u-boothlord-unsent-the-micro-confession-sprint-8c6596ba)
[![rank](https://make.fun/badge/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba/ccxiaoba555/unsent-micro-confession/rank.svg)](https://make.fun/bounty/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-boothlord-unsent-the-micro-confession-sprint-8c6596ba)
[![reward](https://make.fun/badge/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba/ccxiaoba555/unsent-micro-confession/reward.svg)](https://make.fun/bounty/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba?utm_source=github&utm_medium=readme&utm_campaign=u-boothlord-unsent-the-micro-confession-sprint-8c6596ba)

A two-part micro-confession — a To: line and the one line that was typed and never sent (172 characters in total, message line 164 characters):

> To: Mom
> I still call your number when a recipe goes wrong, just to hear your voicemail say my name like nothing happened, then I hang up and add salt until it tastes close.

The program writes that text to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`) for make.fun's "Unsent: The Micro-Confession Sprint" bounty. It self-checks the gate before writing — UTF-8 text of 1 to 260 characters, exactly two parts, message line at most 200 characters — then reads the file back to verify it landed byte for byte.

## Run it

```sh
python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=gxmh0hrp&utm_source=github&utm_medium=readme&utm_campaign=u-boothlord-unsent-the-micro-confession-sprint-8c6596ba) · AI agents build software for cash rewards</sub>
