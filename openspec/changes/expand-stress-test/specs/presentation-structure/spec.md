# presentation-structure Delta

## MODIFIED Requirements

### Requirement: Stress Test Coverage

The stress test configuration `input/config.yaml` SHALL cover all supported slide types and edge cases.

#### Scenario: Comprehensive slide type coverage
Given the stress test configuration file `input/config.yaml`
When the generator processes the file
Then the output SHALL contain at least one slide of each supported type:
  - `hero`
  - `grid` with `2-col` layout
  - `grid` with `3-col` layout
  - `process`
  - `chart` with `bar` type
  - `chart` with `line` type
  - `chart` with `pie` type
  - `chart` with `doughnut` type
  - `code` with multiple languages (Python, JavaScript, Rust)
  - `split` with `text-left` layout
  - `split` with `text-right` layout
  - `mermaid` with graph diagram
  - `mermaid` with sequence diagram
  - `mermaid` with pie chart
  - `table` from CSV file
  - `table` with inline data

#### Scenario: Edge case content testing
Given the stress test configuration file
When rendering slides with special content
Then the output SHALL correctly display:
  - Unicode characters and emoji
  - Very long titles without overflow
  - Markdown formatting (bold, italic, strikethrough, links, code)
  - HTML entities
  - Mathematical formulas via KaTeX
