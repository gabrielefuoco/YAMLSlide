# Background Configuration Design

## Overview
The goal is to move the background styling logic from hardcoded CSS in `template.html` to the YAML configuration. This allows for branding and aesthetic flexibility without editing the template.

## YAML Schema
```yaml
theme:
  background:
    type: "abstract" # Options: "abstract", "solid", "gradient"
    base_color: "#ffffff" # Optional, defaults to bg_primary
    opacity: 1.0 # Overall opacity of the background effect
    radial_layers:
      - at: "15% 25%"
        color: "accent_secondary" # Can be a hex string or a theme variable name
        opacity: 0.12
        size: "55%"
      - at: "85% 75%"
        color: "accent_tertiary"
        opacity: 0.12
        size: "55%"
    linear_gradient:
      angle: "135deg"
      stops:
        - color: "#ffffff"
          pos: "0%"
        - color: "#f7fdf9"
          pos: "50%"
        - color: "#ecfdf5"
          pos: "100%"
```

## Implementation Strategy
1. **Default Logic**: If `theme.background` is missing, use the current hardcoded values as defaults in the Jinja2 template.
2. **Variable Resolution**: In `generator.py` or within the template, resolve theme variable names (like `accent_primary`) to their hex values if used in background settings.
3. **CSS Generation**: Use Jinja2 loops to generate the `background-image` property for the `.background-fx` class.

## Trade-offs
- **Complexity**: Adding more YAML options increases the learning curve for users. We will provide sensible defaults and documentation.
- **Performance**: Dynamic CSS generation has negligible overhead compared to the overall rendering.
