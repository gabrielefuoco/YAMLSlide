# presentation-generator Specification

## Purpose
TBD - created by archiving change implement-presentation-generator. Update Purpose after archive.
## Requirements
### Requirement: Generator Execution Logic

The `generator.py` script SHALL orchestrate the generation process.

#### Scenario: Script execution
Given `config.yaml` and `template.html` exist
When `generator.py` is executed
Then it SHALL load the YAML configuration
And it SHALL load the Jinja2 template
And it SHALL render the template with the configuration
And it SHALL save the result to `presentazione_finale.html`
And it SHALL print a success message

