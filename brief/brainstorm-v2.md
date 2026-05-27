# Brief: Good Practices for Agentic AI — v2

A short slide deck distilling the top lessons from the week-long course. Goal: someone walking out of a 20–30 minute talk should leave with the *mindset shifts* and a few concrete handles, not a tool tutorial.

Audience: people who have heard of Cursor / Claude Code but haven't internalized agentic workflows.

---

## The single thread

If there's one takeaway: **coding is the busy work; the value is everything around it.**

Everything else below is a corollary of this.

---

## Top lessons (working list)

### 1. Coding is the busy work
- The agent's ability to write code isn't the most important thing
- The bottleneck has moved: writing code used to be expensive, now it's cheap
- What's *not* cheap: deciding what to build, scoping it correctly, knowing when it's done
- Use agents to help you *think*, not just to *type*
- Course tie-in: Curriculum Day 2 — "How development has changed" + Appleton slides

### 2. The highest-value activity is getting the idea out of your head
- AI is great at turning a clear spec into code
- It is bad at *guessing* what you actually want
- So the human's job becomes: articulate the idea well enough that the AI can run with it
- This is hard! Use the AI as a thinking partner to interrogate your own idea before any code gets written
- Course tie-in: MVP planning sessions with ChatGPT (Day 1 / Day 2)

### 3. Plan, plan, plan
- Spend the time up front rather than spending it on review
- Two Appleton charts: build-time *shrinks*, plan-time *expands*
- "Plan, design, execute" — loose phrasing, not a rigid framework, just a reminder that things happen before `execute`
- Pre-implementation alignment got dropped because implementation got cheap; we are re-discovering why those touchpoints existed
- Course tie-in: Day 2 — Agentic engineering styles (Research/Plan/Implement, Spec-driven, etc.); Dex Horthy "No Vibes Allowed"

### 4. Vibe coding is fine — *with* a plan
- Vibing isn't shameful; it's a perfectly good *execution mode*
- The trick is: vibe in the implementation phase, *after* you've nailed down the plan / spec
- Pure vibe with no plan = expensive review cycle and rework
- Planned vibe = let the AI drive the keyboard, you steer at the spec level
- Course tie-in: Day 1 vibe coding exercise → Day 2 "Building Code to Last"

### 5. Context management is a real skill
- Context window: what it is, how to fill it deliberately, what happens when it's full
- `/clear`, `/compact`, handoff documents, knowing when to start a new session
- Proper task scoping = a task that fits in one good context window
- A 3-hour session bloated with tool output is worse than a fresh session with a tight prompt
- Course tie-in: Day 1 — Context engineering slide; Jupyter exercise 02

### 6. Alignment points, handoffs, checkpoints
- We used to have many alignment points pre-implementation because implementation was costly
- We dropped them when implementation got cheap
- But the alignment problem didn't go away — it shifted to *review*, which is the wrong end of the lifecycle
- Put the checkpoints back, but at the right phase: spec review > plan review > scaffold review > diff review
- Course tie-in: Day 2 — Appleton "Collaborative AI Engineering" talk; Day 3 — Method VR's grounding-in-source loop

### 7. CLAUDE.md (and AGENTS.md, .cursorrules)
- Encode your standards once, get them applied every session
- Examples: YAGNI, replace-don't-deprecate, fail fast, test behavior not implementation
- Reduces the "negotiate with the AI every time" tax
- Course tie-in: Day 2 — Best practices encoded in CLAUDE.md

### 8. Skills, and your own custom stack
- Superpowers skill set (obra/superpowers) as a starting point
- Skills compose — each one captures a workflow once
- Over time you curate your **own personal skill library**: the workflows *you* run repeatedly, written down so the AI executes them consistently
- This is durable, portable across projects, and gets better with use
- Course tie-in: Day 3 — Skill install + SKILL.md creation exercise

### 9. Pick the right model for the job
- Frontier vs open-weight: real capability gap, especially for long-horizon agentic tasks
- METR data: 50%-reliability task length is doubling fast (and accelerating)
- Don't burn frontier-model budget on autocomplete; don't run open-weight for hard multi-step reasoning
- Course tie-in: Day 1 — METR slides; Day 3 — model/harness comparison

---

## Possible slide order

A talk-length cut (~8 slides + intro/outro):

1. Title + framing ("rough overview of good practices for agentic AI")
2. **Coding is the busy work** — the thread that runs through everything
3. **The bottleneck is in your head** — extracting the idea
4. **Plan, plan, plan** — Appleton charts, plan-time expand / build-time shrink
5. **Vibe with a plan** — yes-and on vibe coding
6. **Context is something you manage** — sessions, scoping, /clear
7. **CLAUDE.md + skills = your custom stack** — encode it once, use it forever
8. **Pick the right model** — METR + frontier-vs-open
9. Closing: "what would you build if coding was free?"

---

## Open questions / decisions for me

- Audience-shape: VR-focused or general SWE? Affects which examples to lean on
- Length budget: 15 min lightning vs 30 min talk vs 60 min workshop preview
- Do I want a single live demo at the end, or pure-talk?
- Should the deck steal slides from the full Curriculum.md, or be standalone?
- Which 2 images "from that other talk" exactly — Appleton's plan-time-expand and build-time-shrink? Confirm before pulling
