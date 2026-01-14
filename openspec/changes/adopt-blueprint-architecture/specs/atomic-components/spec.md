# Atomic Components

## ADDED Requirements

### Requirement: Atomic Rendering Macros
The system SHALL provide Jinja macros for rendering common content types (atoms) without layout logic.

#### Scenario: Markdown Atom
Given a content block with rich text
When `render_markdown(content)` is called
Then it should render a div with `prose` classes
And the content should be correctly formatted as HTML.

#### Scenario: Code Atom
Given a code block with language specification
When `render_code(content, language)` is called
Then it should render a pre/code block
And syntax highlighting should be applied.

#### Scenario: Image Atom
Given an image path
When `render_image(src, alt)` is called
Then it should render an `img` tag
And it should support object-fit classes via optional arguments.

#### Scenario: Stat Atom
Given a numeric value and label
When `render_stat(value, label)` is called
Then it should render a distinct visual element displaying the value prominently.
