# Example: Manuscript Section Review

## User setup

Provide:

- the manuscript paragraph or section;
- the experiment or figure it refers to;
- relevant logs, outputs, notes, or code when available.

Example request:

> Grill me on the scientific content of this section. I want to make sure I understand every claim well enough to defend it in a group meeting or reviewer response.

## Expected behavior

The skill should identify the most important scientific claim first, then ask exactly one question.

It should prioritize questions such as:

- What does this paragraph actually claim?
- Which experimental evidence supports that claim?
- What assumptions connect the measurement to the interpretation?
- What stronger conclusion would the current evidence fail to support?

It should not begin by rewriting the paragraph.
