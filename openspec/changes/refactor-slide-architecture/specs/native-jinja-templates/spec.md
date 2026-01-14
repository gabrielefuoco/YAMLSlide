# Native Jinja2 Templates

## ADDED Requirements

### Requirement: Slide Template Dispatch
The rendering logic MUST dispatch to specific template files based on slide type.

#### Scenario: Rendering a specific slide type
Given the generator is processing a slide with type "hero"
When the template renders
Then it MUST include `templates/slides/hero.html`
And it MUST NOT use any Python-defined blueprint dictionary

### Requirement: Decentralized Styling
Visual styling MUST be defined within the HTML templates, not in Python configuration.

#### Scenario: Styling a slide
Given a clean template architecture
When a developer wants to change the title font size
Then they MUST modify `templates/slides/<type>.html`
And they MUST NOT need to modify `src/generator.py`

### Requirement: Macro Standardization
All UI components MUST be provided by a single `atoms.html` library.

#### Scenario: Using UI components
Given a slide template
When it renders a markdown block or an image
Then it MUST use macros from `templates/macros/atoms.html`
And it MUST NOT use `templates/macros/components.html`

## REMOVED Requirements

### Requirement: Blueprint System
The proprietary "Blueprint" system and "Universal" template MUST be removed.

- The system MUST NOT use `DEFAULT_BLUEPRINTS` in `generator.py`.
- The system MUST NOT use `templates/universal.html`.
