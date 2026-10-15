# Example: Black-Box Experiment Review

## User setup

Provide the experiment input, output, agent-generated artifacts, configuration, code, logs, or notes.

Example request:

> This experiment was mostly executed by an AI agent. I know the input and the result, but the middle still feels like a black box. Grill me until I understand the experiment at the level needed to describe it in a paper.

## Expected behavior

The skill should reconstruct the scientifically meaningful pipeline from the supplied evidence.

It should distinguish:

- scientifically essential transformations;
- assumptions;
- metrics;
- intermediate quantities;
- engineering-only implementation details.

The user should only be questioned about scientific interpretation, reasoning, assumptions, or choices that cannot simply be read from the materials.
