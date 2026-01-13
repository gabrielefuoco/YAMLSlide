# Design: Enhancements for Presentation Generator

## Architecture

### Markdown Support
- **Library**: Use Python `markdown` library.
- **Integration**: Create a custom Jinja2 filter `| markdown` that converts text to HTML.
- **Styling**: Wrap output in `.markdown-body` div for CSS targeting (if needed).

### Live Reload
- **Script**: `watcher.py`
- **Mechanism**: Polling loop (every 1s) checking `os.path.getmtime('config.yaml')`.
- **Action**: Imports `generate_presentation` function from `generator.py` and runs it on change detection.

### New Slide Types
- **Code Slide**:
    - **Config**: `type: code`, `language: str`, `code: str`.
    - **Frontend**: Use `Highlight.js` via CDN (Atom One Dark theme).
- **Split Slide**:
    - **Config**: `type: split`, `layout: text-left|text-right`, `image_url: str`, `content: str`.
    - **Layout**: CSS Grid `grid-2` with `order` property to swap columns.

## Data Dictionary
| Key | Type | Description |
| :--- | :--- | :--- |
| `slide.code` | String | Raw code content |
| `slide.language` | String | Language identifier for Highlight.js |
| `slide.image_url` | String | Path or URL to image |
| `slide.layout` | Enum | `text-left`, `text-right` |
