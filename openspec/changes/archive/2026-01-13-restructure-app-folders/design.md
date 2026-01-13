# Design: Folder Restructuring

## Architecture Overview
The application will transition from a flat structure to a categorized hierarchy. This requires updating internal path references in scripts to ensure they can find their dependencies and write outputs to the correct location.

## Folder Mapping
| Original Location | New Location | Description |
|-------------------|--------------|-------------|
| `generator.py`    | `src/generator.py` | Main generation logic |
| `bundler.py`      | `src/bundler.py`   | HTML bundling logic |
| `template.html`   | `templates/template.html` | Base HTML template |
| `config.yaml`     | `input/config.yaml` | Main configuration |
| `dati_vendite.csv`| `input/dati_vendite.csv` | Example data file |
| `*.html` (output) | `output/*.html` | Generated presentations |

## External Interface
A `run.bat` file will be created in the root to provide a convenient way for the user to start the process without navigating into the `src/` directory.

### run.bat content (draft)
```batch
@echo off
python src/generator.py
pause
```

## Internal Path Handling
Scripts will be updated to use relative paths anchored to the root or based on their own location. 
Example:
```python
# In src/generator.py
TEMPLATE_PATH = os.path.join(os.path.dirname(__file__), "..", "templates", "template.html")
INPUT_PATH = os.path.join(os.path.dirname(__file__), "..", "input", "config.yaml")
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "output")
```
Alternatively, we can expect the script to be run from the root directory.
