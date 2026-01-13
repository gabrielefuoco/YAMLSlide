# Tasks: Folder Restructure

Ordered list of work items to implement the new folder hierarchy.

- [x] Create directory structure (`src`, `templates`, `input`, `output`)
- [x] Move files to target directories:
    - [x] `generator.py`, `bundler.py`, `watcher.py` -> `src/`
    - [x] `template.html` -> `templates/`
    - [x] `config.yaml`, `dati_vendite.csv` -> `input/`
- [x] Update `src/generator.py` to use new paths for:
    - [x] Template loading
    - [x] Config and data reading
    - [x] HTML output writing
- [x] Update `src/bundler.py` relative imports/paths if necessary
- [x] Create `run.bat` in the project root
- [x] Verify execution by running `run.bat` and checking `output/`
