# Design: Blueprint and Atomic Architecture

## Context
The current system relies on rigid HTML templates per slide type. This limits flexibility and requires code changes for new layouts. We need a system where layouts can be defined in configuration (YAML).

## Architecture

### 1. Tailwind-Native Styling
Instead of CSS classes for specific components (e.g., `.slide`, `.glass-card`), we use `macro` expansions or define styles purely via Tailwind utility classes stored in the Blueprint configuration.
The `head.html` will dynamically generate `tailwind.config` injecting:
- **Colors**: From `theme.colors` in YAML.
- **Typography**: Mapping tags to theme colors using `@tailwindcss/typography`.
- **Animations**: Injected keyframes and animations directly into JS config.

### 2. Atomic Components (Atoms)
`macros/atoms.html` provides the visual primitives. It cares only about *rendering* content, not layout.
- `render_markdown(content)`
- `render_code(content, language)`
- `render_image(src)`
- `render_stat(value, label)`

### 3. Blueprint System
Layouts are defined as data structures.
**YAML Structure:**
```yaml
blueprints:
  split-code:
    layout: "grid grid-cols-2 gap-4"
    slots:
      - name: "left_col"
        component: "markdown"
        span: "col-span-1"
      - name: "right_col"
        component: "code"
        span: "col-span-1"
```

### 4. Universal Rendering
A single `universal.html` template iterates over the active blueprint's slots.
Process:
1. `generator.py` determines slide type.
2. Fetches corresponding `blueprint` definition.
3. Passes `blueprint` and `slide_data` to `universal.html`.
4. `universal.html` sets container classes from `blueprint.layout`.
5. Iterates `blueprint.slots`.
6. For each slot, looks up data in `slide_data[slot.name]` and calls the corresponding Atom macro.

## Data Flow
`config.yaml` -> `BlueprintParser` -> `Generator` -> `universal.html` -> `Final HTML`
