# expand-stress-test

## Summary
Espandere il file `input/config.yaml` con un comprehensive stress test che copra **tutti** i tipi di slide, layout, configurazioni edge case e palette di colori estreme per validare il motore di rendering YAMLSlide.

## Motivation
L'attuale stress test copre 9 slide, ma mancano:
- Grid layout `4-col`
- Tutti i tipi di chart (line, pie, doughnut, radar, polarArea)
- Split con layout `text-right`
- Tabelle inline (non da CSV)
- Diagrammi Mermaid avanzati (sequence, class, pie)
- Palette di colori contrastanti e casi limite
- Contenuti lunghi per testare overflow
- Caratteri speciali e edge case Unicode

## Proposed Changes

### [MODIFY] [config.yaml](file:///c:/Users/gabri/APP/Studio/YAMLSLIDE/input/config.yaml)

Aggiungere le seguenti nuove slide dopo quelle esistenti:

1. **Grid 4-col** - Test layout a 4 colonne con molte card
2. **Grid 2-col** - Test layout diverso da 3-col
3. **Chart Line** - Grafico a linee con più dataset
4. **Chart Pie** - Grafico a torta con palette vivaci
5. **Chart Doughnut** - Variante ciambella
6. **Chart Radar** - Grafico radar
7. **Split text-right** - Layout invertito
8. **Table Inline** - Tabella definita direttamente in YAML
9. **Mermaid Sequence** - Diagramma di sequenza
10. **Mermaid Pie** - Grafico torta Mermaid
11. **Code Multi-Language** - Più blocchi code differenti (JavaScript, Rust)
12. **Grid con Markdown Estremo** - Tutte le formattazioni possibili
13. **Hero con Titoli Lunghissimi** - Test overflow
14. **Process con Molti Step** - 5+ step per testare layout
15. **Slide con Palette Alternativa** - Override colori per slide

## Verification Plan

### Manual Verification
1. Eseguire `python run.py` per generare la presentazione
2. Aprire `output/presentazione_finale.html` nel browser
3. Navigare tutte le slide con le frecce
4. Verificare visivamente:
   - Layout corretto per ogni tipo di slide
   - Colori contrastanti e visibili
   - Nessun overflow o testo tagliato
   - Animazioni staggering funzionanti
   - Chart renderizzati correttamente
   - Diagrammi Mermaid visibili e centrati
   - Tabelle con stile dark theme

### Automated Check
- Verificare che il file HTML generato contenga tutte le slide attese
- Eseguire export portable: `python run.py --portable` e verificare `output/presentazione_portable.html`
