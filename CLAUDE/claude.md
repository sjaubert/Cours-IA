# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

This is a training materials repository for **"Maîtriser Claude et l'IA Agentique"**, a professional course authored by S. JAUBERT for Pôle Formation UIMM-CVDL. The audience is non-developer enterprise employees (trainers, administrative staff, industrial engineers).

## Structure

- `Formation_Maitriser_Claude/` — Main formation: plan de formation and livret pratique (Markdown + HTML exports)
- `cours-claude-code-workflow/` — Masterclass on Claude Code & Workflow (Markdown + HTML export)
- `morphic_programming_manual_v1.md` — Morphic programming reference manual
- `Structure_formation_claude.txt` — Raw notes for a 7-day learning ramp-up
- `Guide - Veille IA automatique…pdf` — PDF guide on automated AI monitoring with Claude Code
- `*.jpg` — Course visual assets (cheat sheet, workflow diagram)

## Conventions

- Course documents are authored in **Markdown** then exported to **HTML**. When editing course content, edit the `.md` source — the `.html` is a rendered copy.
- French is the language for all course content. Keep that language when editing existing documents.
- No build system, no tests, no dependencies to install.

## Behavioral Guidelines

These apply to all work in this repo:

**Think before coding.** State assumptions explicitly. If multiple interpretations exist, surface them — don't pick silently. If something is unclear, ask first.

**Simplicity first.** Minimum changes that solve the problem. No speculative additions, no abstractions for single-use edits.

**Surgical changes.** Touch only what the task requires. Match the existing style. Don't refactor adjacent content.

**Goal-driven execution.** For multi-step tasks, state a brief plan with verifiable outcomes before starting.
