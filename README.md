# Experiment Paper Grill

A research-review skill for interrogating the scientific understanding behind AI-assisted experiments and manuscript writing.

Its purpose is to simulate an internal lab review, advisor questioning, or reviewer-style discussion so that the author can verify they genuinely understand the scientific content they plan to claim in a paper.

## What this skill is for

This skill is designed for workflows where:

- experiments are partly executed by AI agents or automated tools;
- the user knows the experiment input and output but parts of the process feel like a black box;
- manuscript prose contains scientific claims that need to be understood and defended;
- formulas appear in the paper and the author must be able to explain their meaning;
- academic wording may differ from implementation details;
- the goal is to prepare for advisor questions, group review, peer review, and academic-integrity scrutiny.

The skill focuses on scientific understanding rather than implementation trivia.

It asks whether the author can explain:

- the research question;
- why the experiment addresses it;
- the scientific meaning of the method;
- assumptions and limitations;
- metrics and what they actually measure;
- what the result supports and what it does not support;
- formulas, variables, and their role in the argument;
- how to defend the paper under follow-up questioning.

## Core behavior

The skill follows a strict one-question-at-a-time review loop.

For each question it:

1. inspects supplied materials first when the answer can be retrieved from them;
2. asks the user about scientific judgment, interpretation, assumptions, and reasoning;
3. gives a concise recommended answer direction;
4. waits for the user's answer;
5. drills deeper only when understanding is partial, superficial, incorrect, or unresolved;
6. continues until the relevant scientific branch is understood.

The skill deliberately avoids asking the user to memorize every experimental number or every implementation detail.

## Repository structure

```text
experiment-paper-grill/
├── README.md
├── CODEX_TASK.md
├── .gitignore
├── skills/
│   └── experiment-paper-grill/
│       └── SKILL.md
└── examples/
    ├── manuscript-review.md
    ├── black-box-experiment.md
    └── formula-review.md
```

## Main skill

The complete skill definition is here:

```text
skills/experiment-paper-grill/SKILL.md
```

Use that directory as the installable skill unit in any environment that supports `SKILL.md`-style agent skills.

## Suggested invocation scenarios

### Manuscript review

Provide a manuscript section together with the relevant experiment notes, figures, code, logs, or outputs.

Then invoke the skill with an instruction such as:

> Grill me on the scientific content of this section. Focus on whether I can correctly explain and defend the claims in the paper.

### Black-box experiment

Provide the agent-generated experiment artifacts and say:

> I understand the experiment input and output, but parts of the procedure are still a black box to me. Grill me until I can scientifically explain the procedure at the level required by the paper.

### Formula review

Provide the formula and surrounding manuscript text and say:

> Grill me on this formula until I can explain every symbol, assumption, scientific role, and connection to the experiment.

## Review philosophy

This skill does not treat AI assistance itself as an academic-integrity violation.

The review standard is whether the author can responsibly stand behind the scientific content they choose to publish.

Implementation and manuscript wording may legitimately differ in abstraction level. The skill only raises code-to-prose discrepancies when they materially affect the scientific validity, reproducibility, interpretation, assumptions, or conclusions of the paper.

## Conceptual lineage

This skill was inspired by the interaction pattern of the `grill-me` / `grilling` family of agent skills, especially the ideas of:

- relentless questioning;
- one question at a time;
- inspecting available facts before asking the user;
- resolving a decision tree dependency-by-dependency;
- delaying implementation until shared understanding is reached.

The current skill specializes that interaction pattern for experiment understanding, scientific manuscript defense, formula comprehension, reviewer simulation, and academic-integrity risk control.

Relevant upstream examples:

- https://github.com/mattpocock/skills
- https://github.com/Wifabric/AISC

## Status

This is an initial working version intended for personal research workflows. The behavior can be refined further as real manuscript-review sessions expose useful additional checks.

## License

Released under the [MIT License](LICENSE).
