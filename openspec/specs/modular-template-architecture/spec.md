# modular-template-architecture Specification

## Purpose
TBD - created by archiving change modularize-template-html. Update Purpose after archive.
## Requirements
### Requirement: Template Directory Structure

The template system SHALL organize files into logical subdirectories.

#### Scenario: Directory Layout
Given the YAMLSLIDE template system
When examining the `templates/` directory
Then it SHALL contain a `base.html` layout skeleton
And it SHALL contain a `partials/` directory for reusable fragments
And it SHALL contain a `slides/` directory for per-slide-type templates
And it SHALL contain a `macros/` directory for reusable Jinja2 macros

### Requirement: Template Inheritance

The presentation template SHALL use Jinja2 template inheritance.

#### Scenario: Base Layout Extension
Given a `base.html` file
When a presentation is rendered
Then the entry template SHALL extend `base.html`
And `base.html` SHALL define `{% block content %}` for slide content
And `base.html` SHALL include partials for head, styles, and scripts

### Requirement: Dynamic Slide Inclusion

The template system SHALL dynamically include per-slide-type templates.

#### Scenario: Slide Type Rendering
Given a slide with `type: "grid"` in the configuration
When the slide loop renders
Then the system SHALL include `slides/grid.html`
And the slide template SHALL receive the `slide` and `loop` context variables

#### Scenario: Unknown Slide Type Handling
Given a slide with an unrecognized `type` value
When the slide loop renders
Then the system SHALL gracefully skip the slide OR display a fallback message
And the system SHALL NOT raise an error

### Requirement: Reusable Component Macros

The template system SHALL provide macros for repeated UI patterns.

#### Scenario: Card Rendering Macro
Given a slide that displays cards (e.g., grid type)
When rendering card elements
Then the template SHALL use a `render_card` macro from `macros/components.html`
And the macro SHALL accept card data and stagger index as parameters

#### Scenario: Badge List Macro
Given footer badges or tech stack items
When rendering badge elements
Then the template SHALL use a `render_badge_list` macro
And the macro SHALL accept a list of badge strings

### Requirement: Tailwind CSS Integration

The template system SHALL use Tailwind CSS for styling via CDN.

#### Scenario: Tailwind CDN Loading
Given the presentation template
When the HTML head is rendered
Then it SHALL include the Tailwind CSS CDN script
And it SHALL configure Tailwind with theme colors from YAML

#### Scenario: Theme Color Mapping
Given a `theme` configuration in config.yaml
When Tailwind is configured
Then `theme.accent_primary` SHALL map to `colors.accent.primary`
And `theme.bg_primary` SHALL map to `colors.bg.primary`
And `theme.text_primary` SHALL map to `colors.text.primary`

#### Scenario: Custom Utility Classes
Given the Tailwind configuration
When custom utilities are defined
Then it SHALL define `.glass-card` for card styling
And it SHALL define `.text-gradient` for gradient text effects
And it SHALL define `.slide` and `.slide.active` for slide transitions

### Requirement: Typography Plugin Usage

The template system SHALL use Tailwind Typography for Markdown content.

#### Scenario: Markdown Content Styling
Given Markdown-rendered content in a slide
When the content is displayed
Then it SHALL be wrapped in an element with `prose` class
And Tailwind Typography SHALL style headings, lists, code, and blockquotes automatically

