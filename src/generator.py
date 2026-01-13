import yaml
import markdown
import csv
import os
from jinja2 import Environment, FileSystemLoader

# Funzione filtro che converte Markdown in HTML
def markdown_filter(text):
    if not text: return ""
    return markdown.markdown(text)

def generate_presentation(config_path=os.path.join('input', 'config.yaml'), template_path=os.path.join('templates', 'index.html'), output_filename=os.path.join('output', 'presentazione_finale.html')):
    """
    Legge la configurazione, processa i dati (CSV per tabelle) e renderizza il template HTML.
    """
    # 1. Carica la configurazione YAML
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            config = yaml.safe_load(f)
            
        # Pre-processamento: Carica dati CSV per le slide di tipo 'table'
        if 'slides' in config:
            for slide in config['slides']:
                if slide.get('type') == 'table' and 'file' in slide:
                    csv_path = slide['file']
                    if not os.path.exists(csv_path) and not os.path.isabs(csv_path):
                        # Try looking in the same directory as the config file
                        config_dir = os.path.dirname(config_path)
                        alt_path = os.path.join(config_dir, csv_path)
                        if os.path.exists(alt_path):
                            csv_path = alt_path

                    if os.path.exists(csv_path):
                        with open(csv_path, 'r', encoding='utf-8') as csvfile:
                            reader = csv.reader(csvfile)
                            rows = list(reader)
                            if rows:
                                slide['columns'] = rows[0]
                                slide['rows'] = rows[1:]
                    else:
                        print(f"⚠️ Attenzione: File CSV '{csv_path}' non trovato per la slide '{slide.get('title')}'.")

    except FileNotFoundError:
        print(f"❌ Errore: File '{config_path}' non trovato.")
        return False
    except yaml.YAMLError as exc:
        print(f"❌ Errore nel parsing del YAML: {exc}")
        return False

    # 2. Carica il template HTML
    try:
        # Fallback to legacy template if index.html is requested by default but missing
        if template_path.endswith('index.html') and not os.path.exists(template_path):
            legacy_path = os.path.join('templates', 'template.html')
            if os.path.exists(legacy_path):
                print(f"⚠️ '{template_path}' not found, falling back to legacy '{legacy_path}'")
                template_path = legacy_path

        env = Environment(loader=FileSystemLoader('.'))
        env.filters['markdown'] = markdown_filter 
        # Jinja2 uses forward slashes even on Windows
        template = env.get_template(template_path.replace(os.sep, '/'))
    except Exception as e:
        print(f"❌ Errore nel caricamento del template: {e}")
        return False

    # 3. Renderizza l'HTML iniettando i dati
    try:
        output_html = template.render(
            meta=config.get('meta', {}),
            theme=config.get('theme', {}),
            slides=config.get('slides', [])
        )
    except Exception as e:
        with open("traceback.log", "a") as tf:
            import traceback
            tf.write("\n--- Error during rendering ---\n")
            traceback.print_exc(file=tf)
        print(f"❌ Errore durante il rendering del template: {e}")
        return False

    # 4. Salva il file finale
    try:
        with open(output_filename, 'w', encoding='utf-8') as f:
            f.write(output_html)
        print(f"✅ Presentazione generata con successo: {output_filename}")
        return True
    except Exception as e:
        print(f"❌ Errore durante il salvataggio del file: {e}")
        return False

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Generatore di presentazioni YAML+Jinja2')
    parser.add_argument('config', nargs='?', default=os.path.join('input', 'config.yaml'), help='File di configurazione YAML')
    args = parser.parse_args()
    
    generate_presentation(args.config)
