# Enhance Presentation Generator

## Why
The current presentation generator works but requires raw HTML for formatting (uncomfortable in YAML), lacks code highlighting (critical for technical slides), and requires manual re-running to see changes (inefficient workflow).

## What Changes
We will improve the developer experience and presentation quality by:
1.  **Markdown Support**: Enabling Markdown syntax in YAML content.
2.  **Live Reload**: Adding a watcher script to auto-generate HTML on changes.
3.  **New Slide Types**: Adding 'Code' (with syntax highlighting) and 'Split' (text + image) layouts.

## Trade-offs
- **Dependencies**: Adds `markdown` package dependency.
- **Complexity**: `watcher.py` adds a running process that needs to be managed (stopped with Ctrl+C).
