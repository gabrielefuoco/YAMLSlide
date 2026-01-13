# Advanced Features and Export

## Why
Users need to present complex technical and academic data (diagrams, math, huge tables) without creating external assets manually. Additionally, sharing presentations is currently difficult as it requires online access for CDNs or sending multiple files.

## What Changes
We will introduce:
1.  **Diagrams as Code**: Support for Mermaid.js for flowcharts, sequence diagrams, etc.
2.  **Math Support**: Support for KaTeX for rendering LaTeX math formulas.
3.  **Data Tables**: Ability to load CSV files and render them as sortable HTML tables.
4.  **Single File Export**: A "bundling" feature to inline all generic assets (CSS, JS, Fonts) into a single standalone HTML file.

## Trade-offs
-   **File Size**: The "Single File" export will be significantly larger (embedding fonts and libraries).
-   **Build Time**: Bundling requires downloading external resources, which increases build time.
-   **Complexity**: `generator.py` needs to handle CSV parsing and potentially downloading assets (or we use a separate `bundler.py`).
