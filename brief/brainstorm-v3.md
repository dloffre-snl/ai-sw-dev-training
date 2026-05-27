# Brief: Good Practices for Agentic AI — v3

A short slide deck distilling the top lessons from the week-long course. Goal: someone walking out of a 20–30 minute talk should leave with the *mindset shifts* and a few concrete handles, not a tool tutorial.

Audience: people who have heard of Cursor / Claude Code but haven't internalized agentic workflows.

---

## The single thread

Coding is the busy work. What's *not* cheap anymore: deciding what to build, scoping it correctly, and knowing when it's done. The five lessons below are all corollaries of that shift.

---

## Framing: why now?

Before the five lessons, set the stakes:

- **METR**: 50%-reliability task length is doubling roughly every 7 months — and the doubling has *accelerated* in the latest measurements (Mythos preview pushed past 16-hour task horizons in May 2026)
- **Frontier vs open-weight**: real capability gap, especially on long-horizon agentic work. Don't burn frontier-model budget on autocomplete; don't run open-weight for hard multi-step reasoning
- This is the most exciting time to be a software developer; this conversation matters *now* because the tools are getting good fast
- Course tie-in: Day 1 METR slides; Computerphile + Eric Schmidt videos

---

## 1. The highest-value activity is getting the idea out of your head

- AI is great at turning a *clear spec* into code. It is bad at *guessing* what you actually want
- The human's job becomes articulating the idea well enough that the AI can run with it
- Use agents to *think*, not just to type — interrogate your own idea with the AI before any code gets written
- What's *not* cheap anymore: deciding what to build, scoping it correctly, knowing when it's done
- The agent's ability to write code isn't even the most important thing — the bottleneck moved upstream
- Practical move: an MVP design session with ChatGPT *before* you ever open Cursor/Claude
- Course tie-in: Day 1 MVP planning session; Day 2 live MVP planning demo

---

## 2. Your job is alignment

- We used to have many alignment points pre-implementation, because implementation was so costly
- When implementation got cheap, we dropped those touchpoints — and the alignment problem reappeared as painful review at the *wrong end* of the lifecycle
- Appleton's two charts: build-time *shrinks*, plan-time *expands* — but most teams haven't reinvested the saved time into plan-time yet
- Use an **LLM-driven wiki / markdown docs** as the alignment substrate — durable, reviewable, the AI and humans both write/read it
- Alignment phases worth keeping: spec → plan → scaffold → diff. Check each one before moving on
- This is the role-shift: you are no longer a typist, you are an aligner
- Course tie-in: Day 2 — "How development has changed" + Appleton "Collaborative AI Engineering"; Day 3 — Method VR's wiki-as-shared-understanding loop

---

## 3. Time spent planning is twice time saved reviewing

- The quantitative punchline behind #2: front-loading is not just nicer, it pays back more than it costs
- Same two Appleton charts cited again here — they support both #2 (lifecycle) and #3 (time math)
- **Vibe coding is fine — *with* a plan.** Vibing is a legitimate *execution mode*; the trick is that you've nailed down the spec *before* you start vibing
- Pure vibe with no plan = expensive review cycle and rework
- Planned vibe = let the AI drive the keyboard, you steer at the spec level
- "Plan, design, execute" — loose phrasing, not a rigid framework, just a reminder that things happen before `execute`
- Many named styles in this space (Research/Plan/Implement, spec-driven, plan-mode, multi-agent swarm) — pick one, the meta-point is just *plan first*
- Course tie-in: Day 2 — Agentic engineering styles; Dex Horthy "No Vibes Allowed"; Day 1 vibe coding exercise → Day 2 "Building Code to Last"

---

## 4. You have to manage context via sessions, handoffs, etc.

- Context window: what it is, how to fill it deliberately, what happens when it gets full
- Tactical tools: `/clear`, `/compact`, handoff documents, knowing when to start a new session
- Proper task scoping = a task that fits in **one good context window**
- A 3-hour session bloated with tool output is worse than a fresh session with a tight prompt
- Handoffs aren't just session-to-session — they're also you-to-future-you, or you-to-teammate. Write them down
- This is the tactical skill that makes #1–#3 actually work in practice — without it, your great plan and alignment artifacts get drowned in noise
- Course tie-in: Day 1 — Context engineering slide; Jupyter exercise 02 (tool calls); terminology slide

---

## 5. Skills are portable, composable knowledge and expertise

- A skill is a reusable instruction file the model loads when it matches a task — teach the workflow once, get consistent execution thereafter
- **Use superpowers** (obra/superpowers) as a starting point — general workflow + brainstorming + debugging skills out of the box
- **Build your own custom skill stack** — the workflows *you* run repeatedly, written down so the AI executes them the way you would
- Skills compose — a brainstorming skill calls into a writing-plans skill calls into an executing-plans skill, etc.
- **CLAUDE.md (global + project-specific)** is the same "encode it once" idea at a different scope — it's the always-on context, not the per-task workflow
  - Examples of what to encode: YAGNI, replace-don't-deprecate, fail fast with context, test behavior not implementation, mock boundaries not logic, finish the job
  - Reduces the "renegotiate with the AI every session" tax
- The artifacts you accumulate — skills + CLAUDE.md + wiki — travel with you across projects and get better with use
- Course tie-in: Day 2 — Best practices encoded in CLAUDE.md; Day 3 — Skill install + SKILL.md creation exercise

---

## Possible slide order

A talk-length cut (~7 slides + intro/outro):

1. Title + framing ("rough overview of good practices for agentic AI")
2. **Why now** — METR + frontier-vs-open
3. **Get the idea out of your head** — value frame
4. **Your job is alignment** — role definition + Appleton lifecycle chart
5. **Plan-time twice review-time saved** — the math + "vibe with a plan" + Appleton plan/build chart
6. **Manage context like a resource** — sessions, scoping, handoffs
7. **Skills + CLAUDE.md = your custom stack** — encode it once
8. Closing: *"what would you build if coding was free?"*

---

## Open questions / decisions for me

- Audience-shape: VR-focused or general SWE? Affects which examples to lean on
- Length budget: 15 min lightning vs 30 min talk vs 60 min workshop preview
- Do I want a single live demo at the end, or pure-talk?
- Should the deck steal slides from the full Curriculum.md, or be standalone?
- Confirm exactly which two Appleton images get used (and on which slide — #4, #5, or both)
- Decide whether CLAUDE.md lives only under #5 or gets a callback under #2 (alignment)
