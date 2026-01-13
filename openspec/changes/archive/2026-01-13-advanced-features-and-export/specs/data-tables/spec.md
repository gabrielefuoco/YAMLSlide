# Data Tables Specification

## ADDED Requirements

### Requirement: CSV Table Loading
The presentation generator MUST load data from CSV files.

#### Scenario: Table Data Injection
Given a slide with `type: "table"`
Then it MUST contain a `file` field
And it MUST render the data into the template.

