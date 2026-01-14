# Blueprint System

## ADDED Requirements

### Requirement: Layout Definition via Blueprint
The system SHALL allow defining slide layouts using a "Blueprint" structure in YAML.

#### Scenario: Blueprint Structure
Given a `config.yaml` file
When the user defines a `blueprints` section
Then the system should parse these definitions including `layout` string and `slots` list.

#### Scenario: Slot Mapping
Given a blueprint with defined slots
When a slide uses that blueprint
Then the slide's top-level keys should map to the blueprint's `slots` by name.

#### Scenario: Default Blueprints
Given no user-defined blueprints
When the application starts
Then a set of default blueprints (hero, split, grid, code) should be available.
