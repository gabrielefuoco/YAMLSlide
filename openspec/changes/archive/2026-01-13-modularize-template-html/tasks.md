# Tasks: Modularize Template HTML + Tailwind CSS

## Phase 1: Create Infrastructure
- [x] Create `templates/partials/` directory
- [x] Create `templates/slides/` directory
- [x] Create `templates/macros/` directory
- [x] Create `templates/base.html` with Tailwind-ready block definitions

## Phase 2: Setup Tailwind CSS
- [x] Create `partials/head.html` with Tailwind CDN script
- [x] Configure `tailwind.config` with theme colors from Jinja2 variables
- [x] Create `partials/tailwind-layers.html` with custom `@layer utilities`
- [x] Define `.glass-card`, `.text-gradient`, `.slide`, `.stagger-*` utilities
- [x] Define `.process-step`, `.tech-badge`, `.id-badge` components
- [x] Add `.background-fx` styles with Jinja2 gradient logic

## Phase 3: Create Macros
- [x] Create `macros/components.html`
- [x] Implement `render_card(card, index)` macro with Tailwind classes
- [x] Implement `render_badge_list(badges)` macro
- [x] Implement `render_process_step(step, index)` macro

## Phase 4: Extract Slide Templates
- [x] Create `slides/hero.html` with Tailwind utility classes
- [x] Create `slides/grid.html` using `render_card` macro
- [x] Create `slides/process.html` using `render_process_step` macro
- [x] Create `slides/chart.html` with Chart.js canvas
- [x] Create `slides/code.html` with highlight.js code block
- [x] Create `slides/split.html` with image + text layout
- [x] Create `slides/mermaid.html` with mermaid diagram container
- [x] Create `slides/table.html` with simple-datatables integration

## Phase 5: Scripts Partial
- [x] Create `partials/scripts.html`
- [x] Move navigation script (arrow keys, slide transitions)
- [x] Move KaTeX `renderMathInElement` initialization

## Phase 6: Create Entry Point
- [x] Create `templates/index.html` that extends `base.html`
- [x] Implement slide loop: `{% include 'slides/' ~ slide.type ~ '.html' ignore missing %}`
- [x] Add fallback handling for unknown slide types

## Phase 7: Update Generator (Optional)
- [x] Update `generator.py` to use `index.html` as default template path
- [x] Add backward compatibility check for old `template.html`

## Phase 8: Verification
- [x] Generate presentation with new modular template system
- [x] Visual comparison: screenshot old vs new output
- [x] Test hero slide rendering
- [x] Test grid slide with cards
- [x] Test process slide with steps
- [x] Test chart slide with Chart.js
- [x] Test code slide with syntax highlighting
- [x] Test split slide with image
- [x] Test mermaid slide with diagram
- [x] Test table slide with datatables
- [x] Test edge cases: empty slides, missing optional fields
- [x] Verify KaTeX math rendering works
- [x] Verify Mermaid diagrams render correctly

## Phase 9: Portable Export (If Required)
- [x] Decide approach: local Tailwind script OR pre-compiled CSS
- [x] If local script: download `tailwindcss.js` to assets folder
- [x] If pre-compiled: integrate Tailwind CLI into bundler.py
- [x] Update `bundler.py` to handle Tailwind in portable export
- [x] Test portable HTML works offline

## Phase 10: Cleanup & Documentation
- [x] Backup original `template.html` to `template.html.legacy`
- [x] Delete or archive old monolithic template
- [x] Update README with new template architecture
- [ ] Archive this OpenSpec change

## Dependencies
- Phase 2 depends on Phase 1
- Phase 3 depends on Phase 2 (needs Tailwind layers defined)
- Phase 4 depends on Phase 3 (slides use macros)
- Phase 6 depends on Phase 4 & 5
- Phase 8 depends on Phase 6
- Phase 9 can run in parallel after Phase 8
