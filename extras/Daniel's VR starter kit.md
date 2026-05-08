
## Claude code

I have a skill that I use for setting up my claude environment the way I like: [https://github.com/DLthree/claude-setup/tree/main](https://github.com/DLthree/claude-setup/tree/main "https://github.com/DLthree/claude-setup/tree/main")

- This is heavily based on Trail of Bits’s recommended config: [https://github.com/trailofbits/claude-code-config](https://github.com/trailofbits/claude-code-config "https://github.com/trailofbits/claude-code-config")
- There’s a lot of forward engineering stuff in there that you don’t need.

---

These are tools I would install and tell Claude about:

|                |      |                                                                     |
| -------------- | ---- | ------------------------------------------------------------------- |
| `rg` (ripgrep) | grep | `rg "pattern"` - 10x faster regex search                            |
| `fd`           | find | `fd "*.py"` - fast file finder                                      |
| `ast-grep`     | -    | `ast-grep --pattern '$FUNC($$$)' --lang py` - AST-based code search |

---

General skills:
 

- skill-creator from [https://github.com/anthropics/skills/tree/main/skills/skill-creator](https://github.com/anthropics/skills/tree/main/skills/skill-creator "https://github.com/anthropics/skills/tree/main/skills/skill-creator")
- superpowers from [https://github.com/obra/superpowers](https://github.com/obra/superpowers "https://github.com/obra/superpowers")
    

---
 

Trail of bits has the best security relevant skill repo: [https://github.com/trailofbits/skills](https://github.com/trailofbits/skills "https://github.com/trailofbits/skills")

  
These are the skills I would include:

  
|   |   |
|---|---|
|[audit-context-building](https://github.com/trailofbits/skills/blob/main/plugins/audit-context-building "https://github.com/trailofbits/skills/blob/main/plugins/audit-context-building")|Build deep architectural context through ultra-granular code analysis|

|   |   |
|---|---|
|[c-review](https://github.com/trailofbits/skills/blob/main/plugins/c-review "https://github.com/trailofbits/skills/blob/main/plugins/c-review")|Comprehensive C/C++ security review with clustered parallel workers and SARIF output|
|[differential-review](https://github.com/trailofbits/skills/blob/main/plugins/differential-review "https://github.com/trailofbits/skills/blob/main/plugins/differential-review")|Security-focused differential review of code changes with git history analysis|

|   |   |
|---|---|
|[insecure-defaults](https://github.com/trailofbits/skills/blob/main/plugins/insecure-defaults "https://github.com/trailofbits/skills/blob/main/plugins/insecure-defaults")|Detect insecure default configurations, hardcoded credentials, and fail-open security patterns|
|[semgrep-rule-creator](https://github.com/trailofbits/skills/blob/main/plugins/semgrep-rule-creator "https://github.com/trailofbits/skills/blob/main/plugins/semgrep-rule-creator")|Create and refine Semgrep rules for custom vulnerability detection|
|[semgrep-rule-variant-creator](https://github.com/trailofbits/skills/blob/main/plugins/semgrep-rule-variant-creator "https://github.com/trailofbits/skills/blob/main/plugins/semgrep-rule-variant-creator")|Port existing Semgrep rules to new target languages with test-driven validation|
|[sharp-edges](https://github.com/trailofbits/skills/blob/main/plugins/sharp-edges "https://github.com/trailofbits/skills/blob/main/plugins/sharp-edges")|Identify error-prone APIs, dangerous configurations, and footgun designs|
|[static-analysis](https://github.com/trailofbits/skills/blob/main/plugins/static-analysis "https://github.com/trailofbits/skills/blob/main/plugins/static-analysis")|Static analysis toolkit with CodeQL, Semgrep, and SARIF parsing|

|   |   |
|---|---|
|[testing-handbook-skills](https://github.com/trailofbits/skills/blob/main/plugins/testing-handbook-skills "https://github.com/trailofbits/skills/blob/main/plugins/testing-handbook-skills")|Skills from the [Testing Handbook](https://appsec.guide/ "https://appsec.guide/"): fuzzers, static analysis, sanitizers, coverage|
|[trailmark](https://github.com/trailofbits/skills/blob/main/plugins/trailmark "https://github.com/trailofbits/skills/blob/main/plugins/trailmark")|Code graph analysis, Mermaid diagrams, mutation testing triage, and protocol verification|
|[variant-analysis](https://github.com/trailofbits/skills/blob/main/plugins/variant-analysis "https://github.com/trailofbits/skills/blob/main/plugins/variant-analysis")|Find similar vulnerabilities across codebases using pattern-based analysis|

---

Ask me about mini-toolkit which is a portable version of the above setup. 

## Method VR

* [[Method VR]]