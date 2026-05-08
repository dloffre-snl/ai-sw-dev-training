---
title: "Software Development with AI: A VR/Software Understanding Focus"
author: Daniel Loffredo
theme: uncover
class:
  - invert
paginate: true
size: 16:9
transition: none
style: "section {     font-size: 20px;   }"
---
# Software Development with AI: A VR/Software Understanding Focus
Daniel Loffredo
dloffre@sandia.gov
May 2026

---

# TOC

- TODO: linkify these
- Day 1 - Frontier AI tools 101: vibe coding → AI-assisted SWE
- Day 2 - Engineering discipline: prompts, specs, code that lasts
- Day 3 - Method VR + skills you can take home
- Day 4 - Security/attacks; project work
- Day 5 - Catch-up + project time
- Week 2 - Project deep-dive
- Optional topics
- Other resources

---

# Day 1

![Waterfall-Agile-AI](images/Waterfall-Agile-AI.png)

  
---

## Intro

- **_You are guinea pigs_** - this is an _experience_ and I hope to get 51% of it right.
	- Does someone mind keeping a notes doc with things that happened live that should have been in the course materials? 
- **Course constraints: non-sensitive ONLY, no SRN, open internet.**  PROXY problems
- This class will have lots of free exploration time - that's the main value of the course in fact!
	- Usually at the end of the day, more as the week goes on
	- By the end of the first week I hope you are all doing independent study while learning and collaborating with me / each other
- Pie chart of value from this course
	- 5% the exercises, course materials, what I have prepared to say
	- 35% our discussions, the questions you ask, my knowledge and experience, the other participants' experiences
	- 60% the accounts, laptops, frontier access, time to learn and play away from distractions
- My goal is to spend the first couple days getting you going and then treat this like a workshop
- We will make time to chat about each person's project idea - let's collaborate, pair program, experiment together
- We will discuss roadblocks and successes as a group 

<!-- 

- presenter notes look like this
- second note

-->

---

## Orientation

- Why are we here? - _Why are you here?_
- What's the deal with AI? - _Why am I here?_
	- This is the most exciting time to be computer scientist
	- Software development is my axe; sharpening my axe
- TODO: how much of software is written by AI today?
- TODO: news articles or stats about the rise of AI use in software development
- TODO: anecdote about AI making a parsing library in 2 hours that would have taken a week by hand

<!--
- Screenshot of cursor showing what AI development looks like (prompt for a new feature, AI thinks for a while, walk through diff of changes to accept/modify)
- Maybe a diagram instead? Showing user -> prompt -> AI coding tool -> queries -> AI model (LLM)
- Want to draw a clear and visible distinction between the AI model and the AI coding tool
-->

---

## Opsec for this course

- For this course, we will be using the open internet (not SRN) and everything we do will be non-sensitive
- Don’t pull in any CUI/OUO during this course
- This workflow is not generally allowed at Sandia right now, so don’t go try to do it at your office 
- We will talk more in the course about exactly what is allowed on Sandia networks and how you can make use of AI coding at Sandia
- If you are unsure about something, feel free to ask!

---

## What is Vibe Coding

- What is vibe coding?
- You tell the AI what you want, it writes the code for you.
- The less you interact with the actual code, the more “vibey” it is.
- This is a spectrum.
- Our first exercise will be a vibe coding exercise with Cursor.
- Experience the joys and pains!

---

## Environment set up

- Get your laptop from the bag of holding
- Log into it, WiFi, Cursor account, etc.
- Providers/accounts for this course:
	- Cursor (multiple backend models)
	- Anthropic (Claude / Claude Code)
	- OpenAI (ChatGPT / Codex)

<!--
- when to prefer one provider / model / harness over another
-->

---

## First exercise: Vibe Coding in Cursor

- See [Exercise 1](cursor_exercises/1-VibeCoding.pptx)
- “Write a library for parsing network packet captures in Python. Include a script that can take in a PCAP argument, and will display info about all DNS packets parsed to the terminal.”
- TODO: Bonus content for those that finish early
	- Push the boundaries of what an LLM can do on its own
	- Implement ...

---

## Discussion

- What went well?
- What went poorly?
- Any interesting findings or tricks applied?
- TODO: find a spot for the computerphile metr video as well as the METR plot inline in the slides

---

## Break

---

## Terminology

- Model / LLM
- Harness
- Agent
- Tool call
- Skill
- Prompt / System prompt
- Context / Tokens 

<!--
- TODO: include definitions of each of these here in the speaker notes
-->

---

## Jupyter exercise 02 Tool Calls: What They Actually Are

---

## Discussion: Regaining control of the output

- What kinds of tasks can an LLM perform well?
	- Defining the task precisely, leaving no ambiguity
- What size of task can an LLM perform well?
	- Scoping down and being incremental
- What tricks have you tried to get better code out of the LLM?

---

## AI-Assisted Development Tips

- Co-design: using ChatGPT to design an MVP, engineer prompt
- Ask mode vs agent mode vs planning mode in Cursor
- ~~.cursorrules file~~ AGENTS.md
- Autocomplete mode: write in the codebase, see it finish for you
- Try writing a comment to describe what you are about to do
- Using git, don’t delete your project
- Stopping the AI when it is going down the wrong path
- Ask it a question about the project (”how does this work?”) and see how well it knows the codebase
	- You can also ask it for help about its own codebase: “where is the parsing for import tables?”
- Ask it for a new feature
	- See what it does
- Context window
	- What is it?
	- How do you put things in it?
	- What happens when it gets full?
- TODO: include one of the software engineering videos here

---

## Your project: introductions

- Each student: 1-2 minute intro of the project you brought
	- What is it?
	- Why does it matter to your work?
	- What's the riskiest unknown?
- We'll keep coming back to your project across the week

---

## MVP planning / co-design 

- TODO: Note to Daniel - I'm not sure how to capture a good example of this kind of conversation. Maybe a good candidate for something you could do LIVE ("we'll do it LIVE!") projecting from the instructor's laptop? Show a back-and-forth and maybe custom tailor it to something one of the students wants to work on
- Does someone want to volunteer what their class project is?
- Let's open up ChatGPT and do an MVP design session
	- Have it output an initial prompt for Cursor/Claude

---

## Second Exercise: Beyond Vibes - AI-Assisted Development

- See [Exercise 2](cursor_exercises/2-BeyondVibes.pptx)
- The project these slides are working on is: building an interactive call graph visualizer for x86 binaries

---

## End of day Vibe Check

- How many tokens have we used?
- How much `$$$` have we used?

---

# Day 2

![Day-2-image](images/Day2.png)

<!--
TODO: drop in a meme/AI image here that maps to Day 2 themes - prompt
engineering, building code to last, moving from vibes to disciplined SWE.
Suggestions: a "Drake" meme (vibe coding rejected / prompt engineering
embraced), the "Distracted Boyfriend" (dev / vibes / proper SWE), or any
"expectation vs reality of AI-generated code" image. Save as images/Day2.png.
-->

---

## Jupyter exercise 04 Prompt Engineering: Why It Works

---

## Proper software engineering with AI

- TODO: this list is maybe outdated / I don't know what to say to it. Instead, I should make this a list of my best practices (source: my CLAUDE.md / AGENTS.md - *don't* preemptively abstract, fail-fast errors, no speculative features, replace don't deprecate, etc.)
- TODO: include another software engineering video here
- Prompt Engineering Lessons
- Spec-driven engineering
- unit and system tests
- Let the AI debug itself
- GitHub SpecKit?
- Providing information from online (e.g. website for JVM spec)
- Refactoring slop
- Changing the model (Opus 4.6 vs Sonnet vs other stuff)
- Agents
	- Multi-agent swarm mode?
- Writing server/clients that interact with each other
- UI development with Canva, Figma, JS/HTML
- Dumb Idea: you are making code you have to maintain; good SWE practices, testing, etc.; maybe an exercise where you have to work as a class and delegate pieces (maybe 10 people)

---

## Third Exercise: Building Code to Last

- TODO: flesh out this exercise
- Let’s imagine you are no longer working on a one-day piece of code that we are going to throw away.
- Instead, let’s say you are collaborating on a project with other people, and you are making code that you will have to maintain
- Does someone want to volunteer their class project?
- What would you do to help make AI-developed coding manageable?
- Dumb Idea: you are making code you have to maintain; good SWE practices, testing, etc.; maybe an exercise where you have to work as a class and delegate pieces (maybe 10 people)
- For the third exercise, we will try this out as a class!
- Everyone pull this git repo: blah
- (What should the joint project be?)
- First we will discuss a plan to delegate different pieces/tasks

---

## Break

---

## Jupyter exercise 01 RAG Under the Covers

---

## Third Exercise: Building Code to Last (continuation)

---

## Your project: planning + MVP design

- Each of you, with an AI co-designer: sketch your MVP
	- What is the smallest version of the project that proves the idea?
	- What inputs / outputs?
	- What's explicitly out of scope for the MVP?
- Output: a starting prompt for Cursor / Claude you'll refine across the week
- We'll discuss volunteers' MVPs as a group

---

## End of day discussion

---

# Day 3

---

## Success and Failure Stories

- Success and failure stories
- What has worked well, and what has not

---

## Method VR - VR with AI in the thinking loop

- A different style of AI/VR: human + AI co-construct understanding of the target through collaboration
- VR is understanding a target well enough to break it. **Understanding compounds; findings do not.** The shareable artifact is the understanding itself
- Two dividing lines:
	- *Is the AI in the thinking loop with you?* - vs. AI as a function call you throw code at
	- *Are you vibing?* - only inspecting behavior, never the artifact - vs. doing the work to build understanding
- Hypothesis: the hardest targets / messiest CONOPS will require human-AI collaboration, not vibing
- Reference: [Method VR (local notes)](extras/Method%20VR.md)

---

## Method VR scaffolding demo

- Scaffold a new VR project from scratch, projected from the instructor laptop
- Project structure (single git repo at the project root):
	- `target/` - source code or artifacts under analysis
	- `work/` - scripts, helper tools, intermediate investigation artifacts
	- `wiki/` - finished and in-progress nuggets of understanding
- `AGENTS.md` / `CLAUDE.md` - describe goal, target, and project structure so the AI starts grounded
- Three parallel views: editor (VSCode) + Obsidian + AI harness (Claude Code / OpenCode)
- One full cycle: ask → AI investigates → write to wiki → human reviews / corrects / grounds claims in source

---

## Skill install + play time

- Install harness skills from [Daniel's VR starter kit](<extras/Daniel's VR starter kit.md>)
	- `superpowers` (general workflow + brainstorming skills) - github.com/obra/superpowers
	- ToB security skill: `audit-context-building` - github.com/trailofbits/skills
	- Optionally browse the rest: `c-review`, `differential-review`, `semgrep-rule-creator`, `variant-analysis`, etc.
- Free play: try them on a small sample target
- Discussion: which felt useful? where did they break down?

---

## SKILL creation exercise

- Now write your own `SKILL.md`
- Two flavors:
	- **Workflow capture** - you found something useful during play; write it up so the AI (and others) can reuse it
	- **Tool wrapper** - wrap a tool or script you want exposed to the AI
- Closes the loop with Method VR's "capture for compounding" - the goal is reusable practice, not one-off scripts
- Reference: [skill-creator (Anthropic)](https://github.com/anthropics/skills/tree/main/skills/skill-creator)

---

## Break

---

## Play time: beyond Cursor; MCP, Claude, Copilot

- Set up an MCP in Cursor
- Set up Claude or Opencode
- LLM On Command Line
- Claude
- Claude can refer to both an AI model and an AI tool
- Analysis-focused; using skills
- ToB skills, etc.
- OpenClaw

---

## Jupyter exercise 03 MCP: It's Just JSON-RPC

- Aside: Code Mode vs MCP - when raw code execution outperforms a structured tool protocol

---

## Your project: plan / begin implementation

- Take everything you've learned this week so far and apply it to your project
- Plan, scaffold, or begin implementation depending on where you are
- Use the rest of the day to make real progress; ask for help freely

---

## End of day wrap-up

---

# Day 4

---

## Opsec, security risks, mitigations

- TODO: flesh this slide out
- Show abox / shirty / claudecode setup
- Talk about what is allowed on SRN
- One thing is copy/paste into Sandia AI
- Two Concerns
  - CUI/OUO/sensitive data being sent to off-site models
  - Dev tools running malicious commands on your machine (like we just gave it permission to do)
- Figure out how to access Shirty in this environment (SRN laptop?)
- Talk about local models (roocode, continue.dev, cline)
- API access vs OAuth access (which auth model lets you use which tools at Sandia)

---

## Trevor slides

- TODO: figure out how to handle Trevor's slides
- [AI Threat Intel 2026](https://sandialabs-my.sharepoint.com/:p:/r/personal/dloffre_sandia_gov/Documents/AI%20Threat%20Intel%20-%20tlapay.pptx?d=w1b929a826d3b467faf6bb035233b843b&csf=1&web=1&e=bzGVJc) by Trevor LaPay

---

## Jupyter exercise 05 LLM Attacks & Security: What's Actually Happening

---

## Project ideas / datasets (if you don't have your own yet)

DataSets:

- OpenWRT; value add
- APK / 2048
- C#, Rust, Go
- SmarterMail
- dropbear

Tasks:
- setup frida
- find valueadd in OpenWRT
- FuzzHarness for X
- Control MineSweeper output

---

## Your project: build time

- Continue project work
- Drop in for help / pair programming as needed
- Surface roadblocks for the group - chances are someone else is hitting the same wall

---

# Day 5

---

## Catch-up + project time

- Free working time
- Catch up on anything we skipped or rushed through
- 1:1 office hours with instructor
- Cohort cross-pollination - see what others built, demo informally

---

# Week 2 - Project deep-dive

- Project-funded second week
- Full-time project work
- Continue to use the cohort + instructor as a resource

---

# Optional topics

<!--
Future overflow / deep-dive topics that don't fit into the day flow.
Items previously here have been folded in:
  - Code Mode vs MCP -> Day 3, MCP Jupyter aside
  - Superpowers brainstorming -> Day 3, Skill install + play
  - Daniel's CLAUDE.md / AGENTS.md best practices -> Day 2, Proper SWE slide (source material for the best-practices list)
  - API access vs OAuth access -> Day 4, Opsec slide
  - OpenClaw -> Day 3, Play time slide
-->

- (placeholder - drop deep-dive topics here as they come up)

---

# Other resources

---

## Videos

- Playlist: [Daniel's AI Videos](https://www.youtube.com/playlist?list=PLXdnjErEE4gStE5-PxLQDiveJtIfIekSP)
- [The AI Revolution Is Underhyped - Eric Schmidt, TED](https://www.youtube.com/watch?v=id4YRO7G0wE)
- [AI's Version of Moore's Law? - Computerphile](https://www.youtube.com/watch?v=evSFeqTZdqs) (see also [Measuring AI Ability to Complete Long Tasks - METR](https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/))
- [Autoresearch, Agent Loops and the Future of Work](https://www.youtube.com/watch?v=nt9j1k2IhUY) - *"closing the loop"*
- [Don't Build Agents, Build Skills Instead - Barry Zhang & Mahesh Murag, Anthropic](https://www.youtube.com/watch?v=CEvIs9y1uog)
- [Does AI Actually Boost Developer Productivity? (100k Devs Study) - Yegor Denisov-Blanch, Stanford](https://www.youtube.com/watch?v=tbDDYKRFjhk)
- [No Vibes Allowed: Solving Hard Problems in Complex Codebases - Dex Horthy, HumanLayer](https://www.youtube.com/watch?v=rmvDxxNubIg) - *"don't outsource the thinking"*
- [Rethinking how we Scaffold AI Agents - Rahul Sengottuvelu, Ramp](https://www.youtube.com/watch?v=-rsTkYgnNzM)
- [How We Build Effective Agents - Barry Zhang, Anthropic](https://www.youtube.com/watch?v=D7_ipDqhtwk)
- [Black-hat LLMs - Nicholas Carlini, [un]prompted 2026](https://www.youtube.com/watch?v=1sd26pWhfmg)
- [It Ain't Broke: Why Software Fundamentals Matter More Than Ever - Matt Pocock, AI Hero](https://www.youtube.com/watch?v=v4F1gFy-hqg)
- [Collaborative AI Engineering: One Dev, Two Dozen Agents, Zero Alignment - Maggie Appleton, GitHub](https://www.youtube.com/watch?v=ClWD8OEYgp8) - *build-time shrink / plan-time expand slides*

---

## Papers / articles

- [Latent Space: 2025 papers roundup](https://www.latent.space/p/2025-papers)
- [Simon Willison: prompt injection series](https://simonwillison.net/series/prompt-injection/)
- [Simon Willison: agentic engineering patterns](https://simonwillison.net/guides/agentic-engineering-patterns/)
- [Sketch: The Unreasonable Effectiveness of an LLM Agent Loop with Tool Use](https://sketch.dev/blog/agent-loop) (full agent loop in [agent_loop.py](https://sketch.dev/blog/agent_loop.py))

---

## Misc

- Stanford AI Dev course
	- [https://themodernsoftware.dev/](https://themodernsoftware.dev/)
	- [The Modern Software Developer (local notes)](extras/The%20Modern%20Software%20Developer.md)
- [Daniel's claude setup skill](https://github.com/DLthree/claude-setup/blob/main/dloffre-claude-setup/references/claude-md.md)
- [Method VR](extras/Method%20VR.md)
- [Daniel's VR starter kit](<extras/Daniel's VR starter kit.md>)
- [Misc discussion topics](extras/Misc%20discussion%20topics.md)

---

# Fin