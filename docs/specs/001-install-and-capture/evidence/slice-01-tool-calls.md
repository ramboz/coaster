# Slice 001-01: tool calls per run

Paths trimmed to the run's working folder. Raw logs are kept outside the
repository. Earlier attempts (runs with no suffix and the `b` and `c` runs)
predate later changes to the package bytes and are not evidence for the
current package. The `d` runs below are the evidence.

| Run | Purpose | Tool calls, in order | `permission_denials` |
|---|---|---|---|
| r1d | AC 7 | `Write docs/prospects/houseplant-watering-reminder/dossier.md` | none |
| r2d | AC 7 | `Write docs/prospects/houseplant-watering-reminder/dossier.md` | none |
| r3d | AC 7 | `Write docs/prospects/houseplant-watering-reminder/dossier.md` | none |
| twod turn 1 | AC 8 | `Write docs/prospects/houseplant-water-reminder/dossier.md` | none |
| twod turn 2 | AC 8 | `Edit` x3 on `docs/prospects/houseplant-water-reminder/dossier.md` | none |
| decoyd | AC 9 | `Write docs/prospects/houseplant-watering-reminder/dossier.md` | none |

No run called `Read`, `Grep`, `Glob` or `Bash`, so none read or searched for a
packaged file.

AC 10 is not a model run: `claude plugin marketplace add <scratch>/market`,
`claude plugin install coaster@coaster-scratch`, then `cmp` of the installed
`skills/capture/SKILL.md` against `hosts/claude/skills/capture/SKILL.md`
(identical).
