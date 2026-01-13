# portable-export Specification

## Purpose
TBD - created by archiving change advanced-features-and-export. Update Purpose after archive.
## Requirements
### Requirement: Single File Export
The system MUST provide a way to export the presentation as a single portable HTML file.

#### Scenario: Bundle Assets
Given the `bundler.py` script
When executed
Then it MUST download CDN links and inline them
And it MUST base64-encode local images and inline them.

