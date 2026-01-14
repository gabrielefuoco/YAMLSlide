# Adopt Blueprint Architecture

## Goal
Transform the application into a **Tailwind-Native** and **Data-Driven** system where layout is defined entirely in YAML via a "Blueprint" (Models) and "Atoms" (Components) system.

## Strategy
1.  **Tailwind-Native:** Move all stylistic configuration (colors, fonts, animations) to dynamically injected Tailwind JS configuration.
2.  **Blueprint Architecture:** Eliminate rigid HTML templates in favor of layouts defined in YAML.
3.  **Universal Slide:** Single HTML rendering engine that assembles slides based on YAML configuration.
4.  **Role Separation:** Optimize for both Simple Users (content focus) and Power Users (layout creation).

## Phases
1.  **Tailwind Foundation:** Remove custom CSS, dynamic tailwind config injection.
2.  **Atomic Components:** Create reusable Jinja macros (atoms) for content rendering.
3.  **Blueprint System:** Define YAML structure for layouts and implement Python parser logic.
4.  **Universal Template:** Implement `universal.html` to interpret blueprints.
5.  **Migration:** Define default blueprints and remove legacy templates.
