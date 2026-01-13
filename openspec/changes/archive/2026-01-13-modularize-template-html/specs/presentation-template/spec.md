# presentation-template Specification Delta

## MODIFIED Requirements

### Requirement: Jinja2 Template Integration

The `templates/` directory SHALL contain a modular Jinja2 template system.

#### Scenario: Template Rendering
Given a set of slide data
When the template is rendered
Then it SHALL produce a single HTML file
And it SHALL use template inheritance from `base.html`
And it SHALL dynamically include per-slide-type templates
And it SHALL apply styles from the `theme` configuration

#### Scenario: Entry Point Template
Given the presentation generator
When loading the main template
Then it SHALL load `templates/index.html` (or `templates/template.html` for backward compatibility)
And the entry template SHALL extend `base.html`

