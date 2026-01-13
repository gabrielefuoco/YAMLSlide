# Config YAML Specification

## ADDED Requirements

### Requirement: Configuration file structure

The `config.yaml` file SHALL define the presentation structure.

#### Scenario: Configuration file structure
Given a presentation generator
When reading `config.yaml`
Then it SHALL contain a `meta` section with a `title`
And it SHALL contain a `theme` section with color definitions
And it SHALL contain a `slides` list with slide objects

### Requirement: Slide types support

The generator SHALL support multiple slide types.

#### Scenario: Slide types
Given the `slides` list
When parsing a slide
Then it SHALL support `type: "hero"`
And it SHALL support `type: "grid"`
And it SHALL support `type: "process"`
And it SHALL support `type: "chart"`
