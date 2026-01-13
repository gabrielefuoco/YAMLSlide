# New Slide Types Specification

## ADDED Requirements

### Requirement: Advanced Slide Templates

The generator SHALL support advanced slide layouts.

#### Scenario: Code Slide
Given a slide with `type: "code"`
When generated
Then it SHALL include syntax highlighting

#### Scenario: Diagram Slide
Given a slide with `type: "mermaid"`
When generated
Then it SHALL render the Mermaid diagram
