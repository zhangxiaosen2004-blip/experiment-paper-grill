# Task for Codex

Prepare this folder as a GitHub repository and push it to the user's GitHub account.

## Repository intent

Suggested repository name:

`experiment-paper-grill`

Suggested description:

`A reviewer-style agent skill for verifying scientific understanding of AI-assisted experiments, manuscript claims, and formulas.`

## Required checks before push

1. Read `README.md`.
2. Read `skills/experiment-paper-grill/SKILL.md`.
3. Confirm the repository contains no secrets, credentials, generated caches, or machine-specific paths.
4. Preserve the current directory structure.
5. Do not rewrite the scientific-review behavior unless explicitly asked.
6. Initialize git if necessary.
7. Add all repository files.
8. Create an initial commit.

Suggested commit message:

`Initial experiment-paper-grill skill`

## Push

Create or use a GitHub repository named `experiment-paper-grill`, then push the default branch.

If the user's GitHub tooling requires authentication or explicit approval for repository creation, ask only for that action.

## Optional cleanup

You may improve Markdown formatting, fix typos, or normalize line endings.

Do not weaken these core rules in `SKILL.md`:

- ask exactly one question per turn;
- inspect supplied evidence before asking retrievable factual questions;
- focus on scientific understanding rather than implementation trivia;
- interrogate black-box experiments at the level required by the manuscript;
- verify formula understanding;
- distinguish observation, analysis, interpretation, mechanism, generalization, and limitation;
- continue until shared understanding is reached.
