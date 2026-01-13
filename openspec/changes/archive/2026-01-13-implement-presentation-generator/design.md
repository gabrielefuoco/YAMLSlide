# Design: Presentation Generator configuration and flow

## Architecture
The system follows a typical static site generation pattern:
`Data (YAML) + Template (Jinja2) -> Generator (Python) -> Output (HTML)`

### Components

#### 1. Configuration (`config.yaml`)
- **Schema**:
    - `meta`: Metadata like page title.
    - `theme`: Color palette definitions.
    - `slides`: List of slide objects.
- **Slide Types**:
    - `hero`: Title slide with subtitles and badge.
    - `grid`: 2 or 3 column layout for text/lists.
    - `process`: Step-by-step process visualization.
    - `chart`: Chart.js visualization (bar, line, etc.).

#### 2. Template (`template.html`)
- **Styling**: Uses CSS variables mapped to the `theme` config.
- **Layout**: Single page application feel with absolute positioning and transition effects for slides.
- **Interactivity**: simple JS for keyboard navigation.
- **Dependencies**: Tailwind-like utility classes (simulated via custom CSS) and Chart.js CDN.

#### 3. Generator (`generator.py`)
- **Logic**:
    1. Read `config.yaml` using `pyyaml`.
    2. Load `template.html` using `jinja2.FileSystemLoader`.
    3. Render template with `config` data.
    4. Write output to `presentazione_finale.html`.

## Data Dictionary
| Key | Type | Description |
| :--- | :--- | :--- |
| `meta.title` | String | Browser tab title |
| `theme.accent_primary` | Hex Color | Main accent color |
| `slides[].type` | Enum | `hero`, `grid`, `process`, `chart` |
