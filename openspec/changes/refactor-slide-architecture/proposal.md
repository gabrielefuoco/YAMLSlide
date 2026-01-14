# Refactor Slide Architecture

## Goal
Completely replace the Python-based "Blueprint" system with a standard Jinja2 template inheritance model. This restores Separation of Concerns by ensuring all HTML structure and CSS styling resides exclusively in `.html` files, while Python code handles only data processing.

## Context
The previous "Blueprint" architecture defined layout and Tailwind CSS classes within `generator.py` dictionaries. This caused:
- **Coupling:** Visual changes required modifying Python code.
- **Rigidity:** "Universal" templates restricted custom layouts for specific slide types.
- **Maintainability Issues:** Frontend developers could not work effectively without touching backend logic.

## Strategy
1.  **Backend Cleanup:** Ensure `generator.py` is purely for data loading and context passing.
2.  **Explicit Templates:** Implement dedicated Jinja2 templates for every slide type in `templates/slides/` (e.g., `hero.html`, `grid.html`).
3.  **Direct Inclusion:** Update `index.html` to dynamically include specific slide templates based on type.
4.  **Macro Consolidation:** Standardize on `atoms.html` for reusable UI components and remove redundant files.

## Phases
1.  **Backend Verification:** Confirm `src/generator.py` is free of blueprint dictionary logic.
2.  **Template Migration:** Create individual HTML files for all supported slide types (`hero`, `grid`, `code`, `split`, `chart`, `table`, `mermaid`, `process`).
3.  **Cleanup:** Remove `templates/universal.html` and `templates/macros/components.html`.
