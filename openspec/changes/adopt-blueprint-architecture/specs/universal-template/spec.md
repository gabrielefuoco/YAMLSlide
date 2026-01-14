# Universal Template

## ADDED Requirements

### Requirement: Universal Slide Rendering
The system SHALL use a single template to render all slides based on their assigned blueprint.

#### Scenario: Dynamic Rendering
Given a slide with a specific blueprint
When `universal.html` renders the slide
Then it should apply the blueprint's layout classes to the main container
And it should iterate over the defined slots.

#### Scenario: Graceful Failure
Given a slot defined in the blueprint but missing in the slide data
When the slide is rendered
Then the slot should be skipped without error.

## REMOVED Requirements

### Requirement: Legacy Templates
The system SHALL NOT use individual template files for specific slide types.

#### Scenario: Template Cleanup
Given the universal template is operational
When the system is cleaned up
Then files like `hero.html`, `split.html`, `grid.html` should be deleted.
