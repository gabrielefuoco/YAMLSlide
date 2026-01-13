# Implement Presentation Generator

## Summary
Implement a static presentation generator using YAML for data, Jinja2 for templating, and Python for generation, as per standard industry practices for clean design and separation of concerns.

## Why
The user requires a professional, clean, and maintainable way to generate presentation slides. Using YAML for content allows for easy editing without touching HTML structure. Jinja2 provides a powerful templating engine to inject this content into a polished HTML design. This separates content from presentation logic.

## What Changes
The solution consists of three main components:
1.  **`config.yaml`**: A configuration file containing the presentation theme and slide content.
2.  **`template.html`**: An HTML/Jinja2 template that defines the structure and style of the presentation, including Chart.js integration.
3.  **`generator.py`**: A Python script that orchestrates the generation process by reading the config and rendering the template.

## Trade-offs
- **Dependencies**: Requires `pyyaml` and `jinja2` Python packages. Users must have these installed.
- **Browser Compatibility**: The generated HTML uses modern CSS and JS (Chart.js), which should work in all modern browsers but might have issues in very old ones.

## Alternates Considered
- **Pure HTML**: Harder to maintain and update content.
- **Markdown-based generators (e.g., Marp)**: While good, the user specifically requested a custom YAML+Jinja2 solution for maximum control over the "clean design" and specific features like Chart.js integration.
