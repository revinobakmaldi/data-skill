---
name: insight-fact-check
description: Review LLM-generated insights before they are shared.
---

# Insight Fact Check

## Purpose
Review LLM-generated insights before they are shared.

## Expected inputs
- generated insight output
- source metrics or payload

## Expected outputs
- fact-check notes
- risk flags
- revised output guidance

## Guidance
- Check metric fidelity first.
- Flag unsupported causal claims.
- Reduce overconfident language.
- Preserve useful insight while tightening evidence.

## Starter prompt
Use this skill to handle **insight fact check**. Keep the output practical, concise, and ready for the analytics team to review.
