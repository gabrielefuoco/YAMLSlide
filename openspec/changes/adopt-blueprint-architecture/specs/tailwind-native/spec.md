# Tailwind Native Configuration

## ADDED Requirements

### Requirement: Dynamic Configuration Injection
The system SHALL inject Tailwind configuration dynamically via `head.html` based on YAML settings.

#### Scenario: Color Injection
Given a slide deck with custom colors defined in `config.yaml`
When the presentation is generated
Then `head.html` should contain a `tailwind.config` script
And the script should inject `theme.extend.colors` from the YAML configuration.

#### Scenario: Typography Plugin Configuration
Given the application uses the `@tailwindcss/typography` plugin
When the configuration is generated
Then the `prose` classes should be customized to map `h1`, `h2`, `p`, `a` to the configured theme colors.

#### Scenario: Animation Injection
Given the config defines custom animations
When the `tailwind.config` is generated
Then `theme.extend.keyframes` and `theme.extend.animation` should be populated.

## REMOVED Requirements

### Requirement: Custom CSS Layers
The system SHALL NOT rely on static CSS files for component styling.

#### Scenario: Remove Tailwind Layers
Given the new dynamic configuration
When the application is built
Then `tailwind-layers.html` should be removed
And all styling should rely on utility classes or configured components.
