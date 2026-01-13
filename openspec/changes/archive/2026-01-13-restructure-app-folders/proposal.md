# Proposal: Restructure Application Folders

Improve the organization of the project by separating input, output, scripts, and templates into dedicated directories.

## Problem
The current root directory is cluttered with a mix of source code, input configuration, data files, template files, and generated output files. This makes it difficult to manage the project as it grows and doesn't follow standard software organization patterns.

## Proposed Solution
Introduce a structured folder hierarchy:
- `src/`: Core Python logic (`generator.py`, `bundler.py`, `watcher.py`).
- `templates/`: HTML templates (`template.html`).
- `input/`: User-provided configuration and data (`config.yaml`, data files, images).
- `output/`: Generated files (`*.html`).
- `run_process.bat`: A root-level batch script to trigger the generation process.

## Impact
- **Maintenance**: Easier to find and manage specific types of files.
- **Portability**: Clear separation between the application engine and the user's data.
- **User Experience**: Simplified execution via a single entry point script.
