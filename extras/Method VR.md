## Method VR

I've seen several different approaches to incorporating AI into our VR practice,
and all of them are great to see. There's a different style of AI/VR that I
want to explore and describe here because I haven't seen much or any of it
happening yet.

This concept is a work in progress and I hope we can iterate and discover
together, while updating this page with our positive and negative experiences.
Since it is a nebulous idea right now I don't have a good name for it so I'm
just calling it "Method VR", a meaningless but useful name like "Method
acting".

**Scope:** Everything here is about how to do VR better by leveraging AI. The
principles probably apply to hardware VR as well as software VR.

---

## What Method VR is _not_

In the cloud of AI/VR solutions I want to carve out the space with 2 heavy
dividing lines. The first is captured by "Is the AI in the thinking loop along
with you (the human)?"

### Out of the thinking loop

AI as a function call. You build or use an AI-powered tool, and its outputs
drop into your normal VR workflow. The interaction is transactional: you throw
target code at a model, you read the answer.

### In the thinking loop

AI as a thinking partner. You and the model co-construct hypotheses about the
target. You read the reasoning, not just the answers. Your mental model of the
target updates from watching the AI think, and the conversation itself becomes
the artifact. This is pair analysis.

### Are you vibing?

The next dividing line is "Are you vibing or not?", to steal the term out of
"vibe coding". Vibe coding doesn't have an agreed upon definition but the one
I like to use is:

* **Vibe coding**: Using AI to generate code and only inspecting the code's
  behavior, _never looking at the resulting code itself_

When you're vibing you only care about the result. You don't care about the
journey and you don't care about the artifact that produced the result.

There is an analogous mode of using AI to generate VR results. On some targets
I can have the AI lead me to a result and even generate an exploit. This is
great! And AI's ability to have impact in the vibe style will continue to grow
as LLMs get better.

My hypothesis is that the hardest targets (or messiest CONOPS) will require
human-AI collaboration. *Vibing* is not really collaboration, it is leveraging
a tool to get a useful result.

If you're not vibing your VR then what are you doing? You are doing the work in
a way that builds understanding of the target. That understanding is shareable:
with colleagues, with future you, with future AI sessions. The understanding is
what compounds, and that compounding is the point.

Reminder that these other modalities of AI/VR are just as important and useful
as Method VR. However, I think our secret sauce in the coming years may lie in
Method VR.

---

## An attempt to describe Method VR

Method VR is vulnerability research where a human and an AI co-construct the
understanding of a target through collaboration.

VR is understanding a target well enough to break it. Understanding compounds
across years; findings do not. The artifact of Method VR is therefore shareable
*understanding*, not just a finding. Skill building is a side effect of the
practice: each session is another brick in a pyramid of compounding
capabilities.

The model brings several capabilities to this collaboration:

* **Memory**: holds the whole target in working context without forgetting
* **Reach**: pattern recognition and recall across languages, frameworks, vuln
  classes, and obscure APIs
* **Tirelessness**: will enumerate the 200th call site with the same care as
  the first
* **Eagerness**: willing to follow explicit directions

The human brings judgment, target-specific context, stake in the outcome, and
accountability for the claim. Neither side replaces the other; both degrade the
practice if removed.

---

## Method VR best practices

### Project setup

Use an AGENTS.md to set the stage. Describe your goal, what the target is,
high level details.

Set up your project appropriately:
  - target/ - the source code or artifacts of the target of the analysis
  - work/ - a place for you and Claude Code to place scripts, helper tools,
    intermediate investigation artifacts
  - wiki/ - a place for you and Claude Code to put finished and in-progress
    nuggets of understanding

Create a git repo at the project root to track your changes. The wiki, work,
and target all go in this repo. Human collaborators should have their own
branches of the audit project repo.

Describe the project structure (target, work, wiki) in your AGENTS.md.

### Three parallel views

Start three parallel views: have your audit environment (e.g. VSCode),
Obsidian, and AI harness (e.g. Claude Code / OpenCode) all open at the project
root.

### Use the wiki religiously

You are the _consumer_ of the wiki, not the writer. When the AI performs an
investigation it will output a bunch of useful information to the screen. Your
job is to get it to output that information to a wiki page and then review the
wiki page in Obsidian. Ask for clarification, ask for evidence, adjust wrong
claims, etc.

The wiki should represent you and the AI's combined knowledge of the target.
You shouldn't just ingest the whole of the target source code and ask the AI
to make a bunch of wiki pages. You need to at least have read everything
that's in the wiki and have it match your mental model.

### Keep the AI informed and grounded

Make sure the AI knows and understands what you're trying to do at every
step. The AI needs to know what you need. You can use the wiki to short-circuit
this, e.g. "Go read @intermediate-findings; we are going to pursue the
viability of the 3rd one".

Every major claim the AI makes should be grounded in an artifact, preferably
a vscode:// source+line clickable link in the wiki.

### Fix the premise

When the model is wrong, articulate why it is wrong and try to fix it for
next time. You want a compounding effect of knowledge and process improvement.
Correct the premise, not just the conclusion.

### Scope sessions

Scope problems appropriately. If the task is broad understanding, don't also
ask the AI to go deep in a specific area. If the task is deep analysis, don't
ask the AI to go broad for global understanding. Start a fresh session, do
the broad understanding, output as a wiki page. Then start another fresh
session, tell it to read the wiki page, then do the deep analysis task.

Does the model have enough context so that reasoning will be meaningful, not
just plausible? Put yourself in the shoes of the model and ask: could I do
the task I've asked the model to do with the context I've been given?

### Shared capability

When you give yourself a capability, also give it to the AI. If you build a
tiny dynamic test harness to test something, show the AI how to use it (wiki
page and a work/ subdir!). If it's useful to you it will likely be useful to
the AI.

When the AI does something useful, like generate a script or test harness,
capture it. If it's useful to the AI it will likely be useful to you and
others.

### Capture for compounding

Remember that the goal is understanding, not specific findings. The AI
conversation is the key artifact of understanding. Use the wiki to capture
all of this.

When something important happens, there are usually 2 things to document in
the wiki:
  - the knowledge, finding, understanding itself.
  - the process used to reach the finding.

If you make it repeatable and generalizable, the process utilized can be just
as valuable as the understanding. If a specific workflow yields good results
then write it up as a SKILL.md. You start to build up your own set of
expertise in using AI the way that works for you on the targets you examine.
These skills become sharable to other projects, other people, other AI tools.

A SKILL.md doesn't have to be a concrete executable thing. It can be an idea
or a vignette or a workflow captured in generalized form.

This is how the pyramid of compounding capabilities gets built, one brick at
a time.

