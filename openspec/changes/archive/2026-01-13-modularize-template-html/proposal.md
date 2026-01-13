# Modularize Template HTML

## Summary
Refactor the monolithic `templates/template.html` (967 lines) into a modular Jinja2 architecture using inheritance, partials, macros, and per-slide-type includes. Additionally, adopt **Tailwind CSS via CDN** to eliminate custom CSS and establish a consistent design system driven by YAML theme configuration.

## Motivation
The current `template.html` contains:
- **~715 lines of CSS** embedded in `<style>` tags
- **Complex Jinja2 logic** for 8 slide types in a single if/elif chain
- **Multiple inline `<script>` blocks** for Chart.js, Mermaid, KaTeX, and navigation
- **Repeated component patterns** (cards, badges, process steps)

This makes adding new slide types error-prone, finding bugs difficult, and collaborative work prone to merge conflicts.

## Proposed Architecture

### New Folder Structure
```
templates/
├── base.html              # Layout skeleton with block definitions
├── index.html             # Entry point that extends base.html
├── partials/
│   ├── head.html          # Meta, fonts, Tailwind CDN + config
│   ├── tailwind-layers.html  # Custom @layer utilities and components
│   └── scripts.html       # Navigation JS, library init scripts
├── slides/
│   ├── hero.html          # {{ slide.type == 'hero' }} template
│   ├── grid.html          # {{ slide.type == 'grid' }} template
│   ├── process.html       # {{ slide.type == 'process' }} template
│   ├── chart.html         # {{ slide.type == 'chart' }} template
│   ├── code.html          # {{ slide.type == 'code' }} template
│   ├── split.html         # {{ slide.type == 'split' }} template
│   ├── mermaid.html       # {{ slide.type == 'mermaid' }} template
│   └── table.html         # {{ slide.type == 'table' }} template
└── macros/
    └── components.html    # Reusable macros with Tailwind classes
```

### Key Design Decisions

1. **Tailwind CSS via CDN**: Use `https://cdn.tailwindcss.com` script with inline `tailwind.config` that injects YAML theme values directly. This eliminates ~700 lines of custom CSS.

2. **Dynamic Theme Configuration**: Map `theme.accent_primary`, `theme.bg_primary`, etc. from YAML directly into Tailwind's `theme.extend.colors`.

3. **Custom Utility Layers**: Define reusable patterns (`.glass-card`, `.text-gradient`) in `@layer utilities` within a `<style type="text/tailwindcss">` block.

4. **Typography Plugin**: Use Tailwind's `prose` classes for Markdown-rendered content, eliminating manual `.markdown-body` styles.

5. **Template Inheritance**: `index.html` extends `base.html` which defines `{% block content %}`, `{% block styles %}`, and `{% block scripts %}`.

6. **Dynamic Slide Inclusion**: Replace the if/elif chain with `{% include 'slides/' ~ slide.type ~ '.html' ignore missing %}` inside the slide loop.

7. **Macro Usage**: Extract repeated patterns (e.g., card rendering, badge lists) into `macros/components.html` using Tailwind utility classes.

8. **Zero Python Changes**: The `generator.py` continues to render a single entry template; only the template path may optionally change from `template.html` to `index.html`.

## Tailwind Configuration Example

```html
<script src="https://cdn.tailwindcss.com"></script>
<script>
    tailwind.config = {
        theme: {
            extend: {
                colors: {
                    bg: {
                        primary: '{{ theme.bg_primary }}',
                        secondary: '#f8fafc',
                    },
                    accent: {
                        primary: '{{ theme.accent_primary }}',
                        secondary: '{{ theme.accent_secondary }}',
                        tertiary: '{{ theme.accent_tertiary }}',
                    },
                    text: {
                        primary: '{{ theme.text_primary }}',
                        secondary: '{{ theme.text_secondary }}',
                    }
                },
                fontFamily: {
                    sans: ['Inter', 'sans-serif'],
                    mono: ['JetBrains Mono', 'monospace'],
                }
            }
        }
    }
</script>
```

## Impact Assessment

| Area | Impact |
|------|--------|
| `templates/` | NEW folder structure, Tailwind adoption |
| CSS | ~700 lines REMOVED, replaced with utility classes |
| `generator.py` | Optional 1-line path change |
| Slide rendering | Identical visual output expected |
| Future slide types | Add a single file to `slides/` |
| Bundle size | Tailwind CDN ~100KB (cached by browser) |

## Risks & Mitigations

| Risk | Mitigation |
|------|------------|
| Internet required for CDN | Option A: Bundle `tailwindcss.js` locally. Option B: Pre-compile CSS with Tailwind CLI. |
| Jinja2 context in includes | Variables propagate automatically; test with all slide types. |
| Learning curve | Tailwind is well-documented; utility classes are intuitive. |

## Portable Export Considerations

The CDN approach requires internet. For offline "portable" exports:

1. **Simple**: Download `tailwindcss.js` and include it in the output folder alongside the HTML.
2. **Advanced**: Use Tailwind CLI standalone binary to generate a static `.css` file at build time, then inline it in the bundled HTML.

> [!IMPORTANT]
> The current `bundler.py` would need modification to handle either local Tailwind script or pre-compiled CSS for truly offline portable exports.

## Open Questions
1. ~~Should we rename the entry point from `template.html` to `index.html`?~~ → **Yes, use `index.html` for clarity.**
2. ~~Should CSS remain inline or use Tailwind?~~ → **Adopt Tailwind CSS via CDN.**
3. For portable offline export, which approach: local script bundle or Tailwind CLI pre-compilation?

## Status
- [ ] Pending user review and approval
