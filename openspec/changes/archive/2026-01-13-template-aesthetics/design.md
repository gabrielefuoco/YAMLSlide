# Design: Template Aesthetics Extension

## Architectural Reasoning

The extension of the template aesthetics focuses on CSS-driven enhancements that maintain compatibility with the existing Jinja2-based generator.

### Animation System
The animation system uses CSS `@keyframes` and a set of utility classes (`.stagger-*`). 
- **Integration**: We will modify `template.html` to include these classes.
- **Automation**: In loops (like cards in a grid), we will use `loop.index0 % 3 + 1` to automatically assign a stagger class, ensuring a rhythmic entry of elements.

### Enhanced Background
The current background is a dual radial gradient. We will enrich it with additional layers and a linear gradient base to match the "Clean Green" look of the reference file.
- **Variables**: We will continue using CSS variables (`--bg-primary`, `--accent-primary`, etc.) to allow theming while providing a more complex default structure.

### Utility Components
The `.highlight-box` will be added to the CSS. To make it accessible via Markdown (without custom YAML properties if possible), we can target specific blockquote styles or provide instructions for users to use a specific HTML div if needed, but a dedicated YAML property `highlight` in slides might be cleaner.
