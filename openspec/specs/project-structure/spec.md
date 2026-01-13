# project-structure Specification

## Purpose
TBD - created by archiving change restructure-app-folders. Update Purpose after archive.
## Requirements
### Requirement: Standardized Folder Hierarchy
The application files MUST be organized into logical subdirectories to separate concerns.

#### Scenario: Organized scripts
- **GIVEN** the project folder
- **THEN** all Python logic remains in `src/`

#### Scenario: Organized templates
- **GIVEN** the project folder
- **THEN** HTML templates are placed in `templates/`

#### Scenario: Organized input
- **GIVEN** the project folder
- **THEN** configuration and data files are placed in `input/`

#### Scenario: Organized output
- **GIVEN** the project folder
- **THEN** generated files are produced in `output/`

### Requirement: Root Execution Entry Point
A batch script MUST be provided in the root directory for easy process initiation.

#### Scenario: Automated processing
- **GIVEN** the user wants to generate the presentation
- **WHEN** the user executes the batch file in the root
- **THEN** the generator script is triggered with correct relative paths

