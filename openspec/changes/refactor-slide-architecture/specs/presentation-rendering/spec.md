# Presentation Rendering

## REMOVED Requirements

### Requirement: Layout Definition via Blueprint
The system SHALL NOT define layouts using Python dictionaries or YAML blueprints.

## ADDED Requirements

### Requirement: Template-Based Rendering
The system SHALL render slides using individual Jinja2 template files located in `templates/slides/`.

#### Scenario: Slide Type Dispatch
Given a slide definition with `type: hero`
When the presentation is generated
Then the system should render `templates/slides/hero.html` with the slide data injected into the template context.

### Requirement: CSS Separation of Concerns
The system SHALL define all visual styling (Tailwind classes) within HTML templates, not within Python code.

#### Scenario: Styling Modification
Given a requirement to change a font size
When the developer modifies the corresponding HTML template
Then the change should be reflected without modifying any Python files.
