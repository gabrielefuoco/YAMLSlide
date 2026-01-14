# Design: Native Jinja2 Architecture

## Philosophy
**"HTML in HTML, Python in Python"**

The architecture strictly separates:
- **Data (Python):** `generator.py` loads YAML/CSV, processes data, and passes a clean context to Jinja2.
- **Structure & Style (HTML/Tailwind):** Individual template files (`templates/slides/*.html`) responsible for their own layout and styling.
- **Components (Macros):** Reusable UI atoms (`templates/macros/atoms.html`) for consistency.

## Template Mapping
The entry point `index.html` iterates over slides and includes the specific template:

```jinja
{% for slide in slides %}
    {% include 'templates/slides/' ~ slide.type ~ '.html' ignore missing %}
{% endfor %}
```

### Slide Modules
Each slide type has a dedicated file in `templates/slides/`. This allows unique layouts (e.g., standard Hero vs Grid vs Split) without a rigid "slot" system.

| Slide Type | Template File | Description |
| :--- | :--- | :--- |
| `hero` | `hero.html` | Centered layout with gradient text. |
| `grid` | `grid.html` | Grid layout for cards. |
| `code` | `code.html` | Syntax highlighted code block. |
| `split` | `split.html` | Two-column layout (Text + Image/Content). |
| `chart` | `chart.html` | Full-width or containerized chart. |
| `table` | `table.html` | Styled data table. |
| `mermaid` | `mermaid.html` | Centered Mermaid diagram. |
| `process` | `process.html` | Horizontal step-based process flow. |

## Component Library
`templates/macros/atoms.html` serves as the single source of truth for UI components.
- `render_markdown`
- `render_code`
- `render_image`
- `render_stat`
- `render_card`
- `render_mermaid`
- `render_process`
- `render_chart`
- `render_table`
