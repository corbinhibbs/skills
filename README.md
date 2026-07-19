# Corbin's Skills — personal Claude Code plugin marketplace

My personal Claude Code plugin marketplace. Add it once and [Matt Pocock's
engineering skills](https://github.com/mattpocock/skills) are available in every
repo, with auto-updates.

> **This is a fork of [mattpocock/skills](https://github.com/mattpocock/skills).**
> All skills are Matt's work (MIT). The fork adds a marketplace identity I own,
> plus a daily sync that swaps in his latest skills as he ships them — I
> subscribe, I don't maintain.

---

## What's in it

One plugin — `mattpocock-skills` — synced daily from upstream:

<!-- SKILLS-TABLE:START -->

_22 skills, as listed in [`.claude-plugin/plugin.json`](.claude-plugin/plugin.json) — this table regenerates automatically on every sync._

| Skill | Category | What it does |
|---|---|---|
| [`ask-matt`](./skills/engineering/ask-matt/SKILL.md) | engineering | Ask which skill or flow fits your situation. A router over the skills in this repo. |
| [`diagnosing-bugs`](./skills/engineering/diagnosing-bugs/SKILL.md) | engineering | Diagnosis loop for hard bugs and performance regressions. Use when the user says "diagnose"/"debug this", or reports something broken/throwing/failing/slow. |
| [`grill-with-docs`](./skills/engineering/grill-with-docs/SKILL.md) | engineering | A relentless interview to sharpen a plan or design, which also creates docs (ADR's and glossary) as we go. |
| [`triage`](./skills/engineering/triage/SKILL.md) | engineering | Move issues and external PRs through a state machine of triage roles — categorise, verify, grill if needed, and write agent-ready briefs. |
| [`improve-codebase-architecture`](./skills/engineering/improve-codebase-architecture/SKILL.md) | engineering | Scan a codebase for deepening opportunities, present them as a visual HTML report, then grill through whichever one you pick. |
| [`setup-matt-pocock-skills`](./skills/engineering/setup-matt-pocock-skills/SKILL.md) | engineering | Configure this repo for the engineering skills — set up its issue tracker, triage label vocabulary, and domain doc layout. Run once before first use of the other engineering skills. |
| [`tdd`](./skills/engineering/tdd/SKILL.md) | engineering | Test-driven development. Use when the user wants to build features or fix bugs test-first, mentions "red-green-refactor", or wants integration tests. |
| [`to-spec`](./skills/engineering/to-spec/SKILL.md) | engineering | Turn the current conversation into a spec and publish it to the project issue tracker — no interview, just synthesis of what you've already discussed. |
| [`to-tickets`](./skills/engineering/to-tickets/SKILL.md) | engineering | Break a plan, spec, or the current conversation into a set of tracer-bullet tickets, each declaring its blocking edges, published to the configured tracker — edges as text in one file per ticket locally, or native blocking links on a real tracker. |
| [`wayfinder`](./skills/engineering/wayfinder/SKILL.md) | engineering | Plan a huge chunk of work — more than one agent session can hold — as a shared map of decision tickets on your issue tracker, and resolve them one at a time until the way to the destination is clear. |
| [`implement`](./skills/engineering/implement/SKILL.md) | engineering | Implement a piece of work based on a spec or set of tickets. |
| [`prototype`](./skills/engineering/prototype/SKILL.md) | engineering | Build a throwaway prototype to answer a design question. Use when the user wants to sanity-check whether a state model or logic feels right, or explore what a UI should look like. |
| [`research`](./skills/engineering/research/SKILL.md) | engineering | Investigate a question against high-trust primary sources and capture the findings as a Markdown file in the repo. Use when the user wants a topic researched, docs or API facts gathered, or reading legwork delegated to a background agent. |
| [`domain-modeling`](./skills/engineering/domain-modeling/SKILL.md) | engineering | Build and sharpen a project's domain model. Use when the user wants to pin down domain terminology or a ubiquitous language, record an architectural decision, or when another skill needs to maintain the domain model. |
| [`codebase-design`](./skills/engineering/codebase-design/SKILL.md) | engineering | Shared vocabulary for designing deep modules. Use when the user wants to design or improve a module's interface, find deepening opportunities, decide where a seam goes, make code more testable or AI-navigable, or when another skill needs the deep-module vocabulary. |
| [`code-review`](./skills/engineering/code-review/SKILL.md) | engineering | Review the changes since a fixed point (commit, branch, tag, or merge-base) along two axes — Standards (does the code follow this repo's documented coding standards?) and Spec (does the code match what the originating issue/PRD asked for?). Runs both reviews in parallel sub-agents and reports them side by side. Use when the user wants to review a branch, a PR, work-in-progress changes, or asks to "review since X". |
| [`resolving-merge-conflicts`](./skills/engineering/resolving-merge-conflicts/SKILL.md) | engineering | Use when you need to resolve an in-progress git merge/rebase conflict. |
| [`grill-me`](./skills/productivity/grill-me/SKILL.md) | productivity | A relentless interview to sharpen a plan or design. |
| [`grilling`](./skills/productivity/grilling/SKILL.md) | productivity | Grill the user relentlessly about a plan, decision, or idea. Use when the user wants to stress-test their thinking, or uses any 'grill' trigger phrases. |
| [`handoff`](./skills/productivity/handoff/SKILL.md) | productivity | Compact the current conversation into a handoff document for another agent to pick up. |
| [`teach`](./skills/productivity/teach/SKILL.md) | productivity | Teach the user a new skill or concept, within this workspace. |
| [`writing-great-skills`](./skills/productivity/writing-great-skills/SKILL.md) | productivity | Reference for writing and editing skills well — the vocabulary and principles that make a skill predictable. |

<!-- SKILLS-TABLE:END -->

Some skills are **user-invoked** (you type them, e.g. `/grill-me`); others are
**model-invoked** (the agent reaches for them when the task fits). See
[Matt's reference guide](https://github.com/mattpocock/skills#reference) for the
full breakdown and the philosophy behind each skill.

---

## How this works

- **This repo is a Claude Code plugin marketplace.**
  [`.claude-plugin/marketplace.json`](.claude-plugin/marketplace.json) is the
  catalog (marketplace name: `corbin-skills`). The repo root is its one plugin,
  `mattpocock-skills`; [`.claude-plugin/plugin.json`](.claude-plugin/plugin.json)
  lists the active skills and carries the `version` field — a version bump is
  what triggers the update on every client with auto-update on.
- **A daily GitHub Action keeps the skills current.**
  [`.github/workflows/sync-upstream.yml`](.github/workflows/sync-upstream.yml)
  merges `mattpocock/skills@main` into this fork every day (and on demand).
  Skills, docs, and `plugin.json` all track upstream, so new and updated skills
  — and the version bumps that push them to clients — flow through
  automatically.
- **Two files never sync:** `README.md` (this file) and
  `.claude-plugin/marketplace.json` stay local, so the marketplace stays mine
  while the skills stay Matt's.
- **The skills table above regenerates on every sync** via
  [`scripts/update-readme-skills.py`](scripts/update-readme-skills.py).

---

## Install (once)

In Claude Code, from any repo:

```
/plugin marketplace add corbinhibbs/skills
/plugin install mattpocock-skills@corbin-skills
```

Then open `/plugin marketplace`, find **corbin-skills**, and enable
**auto-update** so new versions arrive on their own.

Finally, run `/setup-matt-pocock-skills` once per repo — it configures the
issue tracker, triage labels, and docs location the engineering skills expect.

### Optional: auto-install per repo

Commit this `.claude/settings.json` to any repo to auto-provision the
marketplace + plugin for anyone who opens it in Claude Code:

```json
{
  "extraKnownMarketplaces": {
    "corbin-skills": {
      "source": { "source": "github", "repo": "corbinhibbs/skills" }
    }
  },
  "enabledPlugins": ["mattpocock-skills@corbin-skills"]
}
```

---

## Keeping in sync with Matt

- **Automatic:** the sync workflow runs daily at 06:17 UTC.
- **Manual:** Actions → **Sync from mattpocock/skills** → *Run workflow* (or
  GitHub's **Sync fork** button).
- **Conflicts** resolve in upstream's favour — except the two local files above.
- **Don't edit skill files in this fork**; the next sync overwrites them. To
  hack on a skill, copy it into a project with
  [skills.sh](https://skills.sh/mattpocock/skills) instead — that's the
  editable install path Matt recommends.
- **Adding my own skills later:** give them their own plugin (e.g.
  `plugins/corbin-extras/` with its own `plugin.json` + `skills/`) and add a
  second entry to `marketplace.json`. Never add them to Matt's `plugin.json` —
  it's synced, and local edits to it will be lost.
- **If syncs stop:** GitHub disables scheduled workflows after ~60 days without
  repo activity — re-enable from the Actions tab. Matt's `release.yml`
  (changesets versioning) is intentionally disabled on this fork.

---

## Repo layout

```
skills/                                 (GitHub: corbinhibbs/skills — fork of mattpocock/skills)
├── .claude-plugin/
│   ├── marketplace.json                # the catalog (LOCAL — marketplace: corbin-skills)
│   └── plugin.json                     # plugin: mattpocock-skills (SYNCED — version = update trigger)
├── skills/
│   ├── engineering/…                   # the skills themselves (SYNCED)
│   └── productivity/…
├── scripts/
│   └── update-readme-skills.py         # regenerates the table above (LOCAL)
├── .github/workflows/
│   └── sync-upstream.yml               # the daily sync (LOCAL)
└── README.md                           # this file (LOCAL)
```

---

## Credit

Every skill here is [Matt Pocock](https://www.aihero.dev)'s work, MIT-licensed —
see [LICENSE](LICENSE). If you like the skills,
[join his newsletter](https://www.aihero.dev/s/skills-newsletter).
