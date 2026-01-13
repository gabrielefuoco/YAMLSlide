# diagrams-as-code Specification

## Purpose
TBD - created by archiving change advanced-features-and-export. Update Purpose after archive.
## Requirements
### Requirement: Mermaid Diagrams
The system MUST render diagrams using the Mermaid.js library.

#### Scenario: Diagram Rendering
Given a slide with `type: "mermaid"`
Then it MUST include the `mermaid.js` library
And it MUST render the code block into a `<div class="mermaid">`.

