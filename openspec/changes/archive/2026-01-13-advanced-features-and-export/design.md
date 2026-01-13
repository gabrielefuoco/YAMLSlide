# Design: Advanced Features and Export

## Architecture

### Diagrams as Code (Mermaid)
-   **Config**: `type: mermaid`, `code: "graph TD; A-->B;"`.
-   **Frontend**: Include `mermaid.min.js`. Initialize with `mermaid.initialize({startOnLoad:true})`.
-   **Template**: Render code inside `<div class="mermaid">{{ slide.code }}</div>`.

### Math Support (KaTeX)
-   **Config**: Math syntax can be used in Markdown text: `$E=mc^2$` (inline) or `$$...$$` (block), using standard LaTeX delimiters.
-   **Frontend**: Include `katex.min.css` and `katex.min.js`.
-   **Integration**: Use `auto-render` extension for KaTeX to automatically parse body text, OR use a Jinja filter. Auto-render is easier for mixed markdown content.

### Data Tables (CSV)
-   **Config**: `type: table`, `file: "data/stats.csv"`, `title: "Statistics"`.
-   **Backend (`generator.py`)**:
    -   Use `pandas` (or built-in `csv` module) to read the file.
    -   Pass data to Jinja as `columns` (headers) and `rows` (list of lists/dicts).
-   **Template**: Render standard HTML `<table>`. Use `simple-datatables` (lightweight JS lib) for sorting/search.

### Portable Export (Bundler)
-   **Script**: `bundler.py`.
-   **Logic**:
    1.  Read `presentazione_finale.html`.
    2.  Find all `<link rel="stylesheet" href="...">`. Download content and replace with `<style>...</style>`.
    3.  Find all `<script src="...">`. Download content and replace with `<script>...</script>`.
    4.  (Optional) Find fonts/images. For now, prioritize CSS/JS libraries. Images from URLs will remain URLs (online requirement), images from local path converted to Base64 (offline).
    5.  Save as `presentazione_portable.html`.

## Dependencies
-   `pandas` (for CSV reading) - *Optional, `csv` module might suffice for simple display, but pandas is requested for "Data Tables". Let's stick to standard `csv` first to save deps, or `pandas` if sorting/analysis needed. User said "Tabella ordinabile", so JS frontend is better for sorting. `csv` module is enough to read.*
-   `beautifulsoup4` (for HTML parsing in bundler).
-   `requests` (for downloading CDNs).
