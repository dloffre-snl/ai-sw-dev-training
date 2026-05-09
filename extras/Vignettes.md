
# In-Situ Development: How AI Tools Are Collapsing the Boundaries Between Using, Building, and Extending

## Background

I recently did 2 VR surges, using AI, against 2 different software products. The work fell along a spectrum of human-to-AI delegation:

- **Heavy human judgment**: Manually studying prior bugs, then writing targeted AI analyses to find similar candidates. The human supplies the insight about the bug pattern; the AI scales the search.
- **Interactive collaboration**: Using ClaudeCode alongside manual code auditing. Pick a place to look, read code the classical way, and when something feels appropriate for AI, ask the question and fold the answer back into manual analysis.
- **High delegation**: Pointing AI at a codebase and asking it to generate candidate vulnerability points end-to-end.

Manual-heavy approaches found the most bugs in these surges. That's fine — the tools are maturing fast and the current win rate isn't the point. What's interesting is what I observed about how the work *felt*.

_Note: in this document ClaudeCode could be replaced with OpenCode or Codex CLI or any of a number of similar tools._
## Observation: The Boundaries Have Dissolved

The traditional workflow for capability development has clear handoffs: a practitioner hits a limitation, files a request, a developer builds a fix, it ships, the practitioner tries again. These are distinct roles with distinct tools and distinct timelines.

With ClaudeCode, those handoffs have collapsed. I develop a new capability (a SKILL.md) *inside* ClaudeCode. I apply that capability *inside* ClaudeCode. When it doesn't quite work for my specific problem — say, I'm looking at Go binaries and the skill was built for C/C++ — I extend the capability *inside* ClaudeCode, in the same session, without switching contexts. The person who hits the limitation is the person who fixes it, using the same tool, in the same moment.

I'm calling this **in-situ development**: building and refining the tool in the context of using it, not in a separate environment or workflow. The improvement happens where the work happens.

This is more than "non-programmers can code now." The deeper shift is that **the act of doing the work and the act of improving your tooling for the work are the same act.**

## Mechanism: Same Interface, Immediate Feedback Loop

Why is this happening now? Two things:

1. **Unified interface.** The tool for researching, developing, extending, applying, and collaborating is the same tool: a natural language conversation with ClaudeCode. There's no context switch between "user mode" and "developer mode."

2. **Immediate feedback loop.** When I extend a skill mid-session, I can test the extension against my actual problem immediately. The loop from "this doesn't work" to "now it does" can be minutes, not days.

These two properties together mean that the roles of Developer, Extender, User, and Collaborator don't just blur — they become incoherent as distinct categories. You flow between them without noticing.

## Implication: Implicit Knowledge Is Going Uncaptured

When I work in this mode, I'm constantly generating something valuable: **applied judgment in messy real-world situations.** A codified skill says "here's how to find command injection." But the trace of me actually using that skill — adapting it, working around its limitations, combining it with manual analysis — contains implicit knowledge that the skill itself doesn't encode.

This is the difference between a recipe and watching a chef cook. The recipe is the skill. The chef's improvisations, substitutions, and taste-tests along the way are the trace. Both are valuable, but we're only capturing the recipe.

## Proposal: The Vignette

A skill is codified capability. A vignette is captured experience. Both are valuable — but right now we're only building infrastructure for skills.

I think the **vignette** should be a first-class artifact: an annotated episode of applied judgment in a specific situation. Vignettes live in a flat pool, tagged by intent, and retrieved by query — not organized into hierarchical folders. The groupings are emergent, not structural. You ask "what do I have for Go binaries?" and get one slice. You ask "what do I have for command injection?" and get a different slice. Same vignettes, different views.

A vignette has three components:

**Intent**: When and why would someone reach for this vignette? This is analogous to a skill's trigger description. It's what a retrieval system matches against. Tags enable cross-cutting queries — a vignette about Go binary command injection is findable from both the "Go binary" direction and the "command injection" direction.

**Trace** (raw, passive, cheap): ClaudeCode records everything that happens in a session. Every command, every question, every result. Storage is cheap; capture everything. Most of this is noise, but it's the ground truth.

**Annotations** (human-supplied meaning): Not every trace is meaningful. An automated system watches traces and does intent extraction and grouping — proposing candidate vignettes. The human provides sparse annotation: thumbs up/down, tags, brief intent ("I was trying to bridge the gap between the Go binary and the C-oriented skill"). The annotation burden should be light — enough signal to make retrieval work, not enough overhead to kill adoption.

Vignettes may also produce **artifacts** — tools, scripts, or skills built during the episode. The vignette is the story of how an artifact was born; the artifact is what was born.

A pool of vignettes is:
- **Personalized** — my approach to VR might differ from yours, and that's encoded in my vignettes.
- **Shareable** — I can point my ClaudeCode at a colleague's vignette directory and absorb their experience. No tutorial writing, no knowledge transfer meetings.
- **Evolving** — new vignettes accumulate naturally as I work. The pool grows with practice.
- **Generative** — patterns across vignettes can seed new skill development. "You kept doing X then Y then Z — should we make this a skill?"

The hard problem is **retrieval and relevance**: given 200 vignettes from a colleague, which ones matter for my current task? This is essentially a supervised learning problem on work traces — the system gets better at identifying meaningful vignettes as more human labels accumulate.

There's also a tension between personalization and shareability. My idiosyncratic approach might mislead you. Raw traces without some abstraction layer risk spreading bad habits as easily as good ones. Some curation or quality signal is needed before sharing.

## Open Questions

- What does a good annotation schema for vignettes look like? Minimal enough that practitioners actually use it, rich enough to support retrieval.
- How do you handle the personalization vs shareability tension? Is there an abstraction layer between "my raw vignettes" and "vignettes I share"?
- The in-situ development loop only works when the tool is good enough that mid-session extension succeeds. What happens at the failure boundaries?
- What's the adoption path? Is the retrieval layer a product feature, a community convention, or something individual practitioners rig up with scripts and embeddings? The answer shapes how quickly this can exist. 
- Are failure vignettes more valuable than success vignettes? You arguably learn more from "I spent two hours on this approach and it was a dead end" than from a clean success story. If so, how do you incentivize people to capture and share their failures? 
- What's the minimum viable vignette? The example shows intent + trace + annotations + artifacts. In practice, will people actually fill out all four? If they only do one, which one matters most? 
- At what scale does the flat pool break down? 20 vignettes is browsable. 2,000 is not. Does this eventually need hierarchy, or does good retrieval keep it flat indefinitely?

---

## Appendix: A Vignette in Practice

This is a concrete example of how in-situ development produces a vignette.

### The Setup

I'm doing VR against a software product. The target is a mixture of compiled binaries and source code. I have a ClaudeCode skill for finding command injection candidates — it was built for C/C++ compiled source code and works well in that context. My intent today: find command injection across this entire software product.

### What Happened

**Step 1: Apply the skill.** I point the command injection skill at the code and binaries on the system.  I discover that one of the binaries is a Go binary. The skill needs string references to identify where user input flows into command execution. The skill calls a string extraction tool — but that tool is built for C/C++ binaries and doesn't understand Go's string representation. It returns garbage.

**Step 2: Diagnose the gap.** The skill isn't broken — it's scoped wrong for my task. Go binaries store strings differently than C binaries. The skill's assumption (null-terminated strings, standard symbol tables) doesn't hold.

**Step 3: Build the bridge, in-situ.** Without leaving ClaudeCode, I ask it to write a Go-specific string extraction tool. We iterate on a Ghidra script — first pass misses some strings, second pass picks up too much noise, third pass gets it right. This takes maybe 20 minutes. I now have a working `go-strings-extractor` tool, at least for today's software product.

**Step 4: Resume the mission.** I plug the new tool into the existing skill's pipeline and re-run the analysis. The skill now has the string references it needs. It finds candidate command injection sites. One of them is real.

**Step 5: Reflect.** I found the bug. But I also produced something else: a reusable tool (`go-strings-extractor`) and, more importantly, the *story* of why it was needed and how it fit into the analysis. That story is the vignette.

### The Vignette on Disk

```
~/.vignettes/go-binary-cmd-inject/
  intent.md
  trace.log
  annotations.md
  artifacts/
    go-strings-extractor/
```

**intent.md** — when and why would someone reach for this vignette?

```markdown
---
tags: [command-injection, go, binary-analysis, string-extraction]
---

Reach for this vignette when doing command injection analysis against
a Go binary. The standard C/C++ string extraction approach won't work —
Go stores strings differently. This vignette covers building a
Go-specific string extractor and integrating it into the existing
command injection skill pipeline.
```

**trace.log** — the raw session transcript. Every command, every ClaudeCode interaction, every dead end. Captured passively, stored cheaply.

**annotations.md** — the human-supplied meaning layered on top of the trace.

```markdown
## What I was trying to do
Find command injection in a Go binary using the existing cmd-inject skill.

## What went wrong
The skill depends on string references. The default string extraction
tool assumes C-style binaries. Go binaries store strings as
length-prefixed slices in a different section layout — the tool
returned garbage.

## The key insight
The gap wasn't in the analysis logic — it was in the data extraction
layer. Once I had correct string references, the rest of the skill
worked as-is.

## What I built to bridge the gap
A Go-specific string extractor (see artifacts/go-strings-extractor).
It parses Go's pclntab and moduledata structures to recover string
literals.

## Outcome
Found a real command injection. The extractor is reusable for any
future Go binary analysis.

## What I'd do differently
I spent time trying to make the C string tool work before accepting
it couldn't. Next time, check the binary format first and build the
right extraction tool upfront.
```

**artifacts/** — the `go-strings-extractor` tool itself. This could become a standalone skill or a component in other skills.

### How This Gets Used Later

**By me, next month:** I'm doing VR against another Go binary. ClaudeCode checks my vignette pool, matches on `[go, binary-analysis]`, and surfaces this vignette. I don't have to rediscover that Go strings are different — the vignette reminds me, and the artifact is ready to use.

**By a colleague:** They point their ClaudeCode at my shared vignettes. They're hunting command injection in a Rust binary. The retrieval system surfaces this vignette — not because Rust and Go are the same, but because the *shape* of the problem matches: a skill that assumes C-style strings, applied to a language with a different string representation. The vignette's value isn't the Go-specific tool. It's the pattern: *check whether your data extraction layer matches your target's binary format before trusting the analysis.*

**By a future skill author:** Someone notices that five different people have vignettes about string extraction failing on non-C binaries. That pattern seeds a new, more general skill: one that detects the binary format first and dispatches to the right string extractor. The vignettes are generative — they surface patterns that codified skills should absorb.
