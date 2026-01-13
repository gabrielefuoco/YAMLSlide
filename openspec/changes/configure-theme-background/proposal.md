# Proposal: Configure Theme Background

## Goal
Allow users to customize the presentation background directly from the YAML configuration file. Currently, the "abstract" background (radial gradients and linear gradient) is hardcoded in the `template.html` and only partially influenced by the theme accents.

## Proposed Changes
- Introduce a `background` section within the `theme` configuration in `config.yaml`.
- Allow toggling between different background types: `abstract`, `solid`, and `gradient`.
- Expose parameters for the radial gradient layers (colors, opacity, positions).
- Update `template.html` to dynamically generate the CSS for the background based on these settings.

## User Review Required
> [!IMPORTANT]
> This change introduces a new structure under `theme.background`. If not provided, it will fall back to the current "abstract" default behavior to maintain backward compatibility.
