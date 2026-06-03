title: "Good Practices for Agentic AI"
author: Daniel Loffredo
theme: uncover
class:
  - invert
paginate: true
size: 16:9
transition: none
style: "section { font-size: 22px; } h1 { font-size: 36px; } h2 { font-size: 30px; }"
---

# 6 Agentic Engineering Lessons

Daniel Loffredo
dloffre@sandia.gov

---

# Intro

- TODO Agentic Engineering terse casual definition
- **METR**: 50%-reliability task length is doubling roughly every 7 months — and the doubling is *accelerating*
  - Mythos preview pushed past 16-hour task horizons in May 2026
  - There is a real capability gap between frontier and open-weight on long-horizon agentic work
- Frontier tools can write code as well as most humans
- Here are 6 lessons on Agentic Engineering
- This is about using Agents to build software (the built software may itself use agents)

// TODO include the updated image with mythos instead of this older one
![bg right:40% fit](../images/metr-time-horizons.png)

---

# 1. Use AI to get the idea out of your head

- AI is great at turning a *clear spec* into code
- AI is bad at *guessing* what you actually want
- Your job: articulate the idea well enough that the AI can run with it
- Use agents to *think*, not just to type — interrogate your own idea before any code gets written
- The bottleneck moved upstream. Writing the code isn't even the hard part anymore
- Practical move: an MVP design session *before* you write code

---

# 2. Your job is alignment

- Implementation used to be costly, so we built many alignment points around it
- Suddenly implementation got cheap, we dropped those touchpoints — and the alignment problem reappeared as painful review at the *wrong end* of the lifecycle
- Use an LLM-driven wiki / markdown docs as the alignment substrate — durable, reviewable, both humans and AI write and read it
- **CLAUDE.md** is part of this surface: the always-on context that anchors the agent to your standards

// TODO we need both of the images here, this is where it makes sense. or maybe side by side / top bottom on a slide in between 2 and 3
![bg right:45% fit](../images/appleton1.png)

---

// TODO this title is odd phrasing. Time spent planning is XXX .. is maybe better
# 3. Plan-time saved = 2× review-time saved

- Front-loading planning *pays back more than it costs*
- **Vibe coding is fine — *with* a plan.** Vibing is a legitimate execution mode; the trick is you nailed down the spec *before* you started vibing
- Pure vibe + no plan = expensive review and rework
- I use superpowers a lot and its really good at brainstorming, planning, spec'ing, and aligning.
- Many named styles in this space (Research/Plan/Implement, spec-driven, plan-mode, multi-agent). Pick one — the meta-point is just *plan first*
- You have to actually review the plan!
- Errors in plan compound to spec, errors in spec compound to implementation

// TODO remember this is being moved up to a different slide.  
![bg right:45% fit](../images/appleton2.png)

---

# 4. Leverage both kinds of computation

- There are now 2 different forms of computation available! 
  - They have very different pros and cons
  - **Statistical / probabilistic** (LLMs): flexible, costly, slow, adaptable, intelligent
  - **Classical / deterministic** (code): cheap, reproducible, testable, fast, rigid
- Your job: decide *carefully* which parts of your solution use which — and where the handoffs happen
- This is the architectural skill of the new era — not "use AI for everything" or "use AI for nothing"

---

# 5. Manage context like a resource


- The context window is the working memory
- Target using only the first 40-60% of your context window
- Each independent task should be in its own session
- Use CLAUDE.md and other docs to supplement this working memory
- Tactical tools: `/clear`, `/compact`, handoff documents, knowing when to start a new session
- Proper task scoping = a task that fits in **one good context window**
- Handoffs aren't just session-to-session — they're you-to-future-you, you-to-teammate. Write them down

---

# 6. Skills + CLAUDE.md = your custom stack

- A **skill** is a reusable instruction file the model loads when it matches a task — teach the workflow once, get consistent execution thereafter
- Start with **superpowers** (obra/superpowers) — general workflow, brainstorming, debugging skills out of the box
- Build your **own** skill stack — the workflows *you* run repeatedly, written down so the AI runs them the way you would
- Skills compose and build on top of each other
- The artifacts you accumulate — skills + CLAUDE.md + wiki — travel across projects and get better with use

---


# Questions?
