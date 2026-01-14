import yaml
import markdown
import csv
import os
from jinja2 import Environment, FileSystemLoader

# Funzione filtro che converte Markdown in HTML
def markdown_filter(text):
    if not text: return ""
    return markdown.markdown(text)

DEFAULT_BLUEPRINTS = {
    'hero': {
        'layout': 'flex flex-col items-center justify-center text-center h-full',
        'slots': [
            {'name': 'title', 'component': 'markdown', 'class': 'text-7xl font-bold bg-clip-text text-transparent bg-gradient-to-br from-accent-primary to-text-primary mb-8 animate-fade-up'},
            {'name': 'subtitle', 'component': 'markdown', 'class': 'text-xl text-text-secondary mb-10 animate-fade-up delay-100'}
        ]
    },
    'split': {
        'layout': 'grid grid-cols-2 gap-12 items-center h-full',
        'slots': [
            {'name': 'content', 'component': 'markdown', 'class': 'col-span-1 animate-fade-in'},
            {'name': 'image_url', 'component': 'image', 'class': 'col-span-1 rounded-2xl shadow-2xl animate-fade-in delay-200'}
        ]
    },
    'code': {
        'layout': 'h-full flex flex-col',
        'slots': [
             {'name': 'title', 'component': 'markdown', 'class': 'text-5xl font-bold text-text-primary mb-6'},
             {'name': 'code', 'component': 'code', 'class': 'flex-1 overflow-auto'}
        ]
    },
    'grid': {
        'layout': 'flex flex-col h-full',
        'slots': [
            {'name': 'title', 'component': 'markdown', 'class': 'text-5xl font-bold text-text-primary mb-4'},
            {'name': 'lead', 'component': 'markdown', 'class': 'text-lg text-text-secondary mb-8'},
            {'name': 'cards', 'component': 'card', 'class': 'col-span-1'}
        ]
    },
    'table': {
         'layout': 'flex flex-col h-full',
         'slots': [
             {'name': 'title', 'component': 'markdown', 'class': 'text-5xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-accent-primary to-text-primary mb-8'},
             {'name': 'table_data', 'component': 'table', 'class': 'flex-1 overflow-visible'}
         ]
    },
    'mermaid': {
        'layout': 'flex flex-col h-full',
        'slots': [
            {'name': 'title', 'component': 'markdown', 'class': 'text-5xl font-bold text-text-primary mb-8'},
            {'name': 'code', 'component': 'mermaid', 'class': 'flex-1'}
        ]
    },
    'chart': {
        'layout': 'flex flex-col h-full',
        'slots': [
            {'name': 'title', 'component': 'markdown', 'class': 'text-5xl font-bold text-text-primary mb-4'},
            {'name': 'lead', 'component': 'markdown', 'class': 'text-lg text-text-secondary mb-8'},
            {'name': 'chart_data', 'component': 'chart', 'class': 'flex-1'}
        ]
    },
    'process': {
        'layout': 'flex flex-col justify-center h-full',
        'slots': [
             {'name': 'title', 'component': 'markdown', 'class': 'text-5xl font-bold text-text-primary mb-12 text-center'},
             {'name': 'steps', 'component': 'process', 'class': 'w-full'},
             {'name': 'footer_badges', 'component': 'badges', 'class': 'w-full'}
        ]
    }
}

def generate_presentation(config_path=os.path.join('input', 'config.yaml'), template_path=os.path.join('templates', 'universal.html'), output_filename=os.path.join('output', 'presentazione_finale.html')):
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
                                slide['table_data'] = {
                                    'columns': rows[0],
                                    'rows': rows[1:]
                                }
                    else:
                        print(f"⚠️ Attenzione: File CSV '{csv_path}' non trovato per la slide '{slide.get('title')}'.")
                
                # Handle inline table data (columns/rows defined directly in YAML)
                elif slide.get('type') == 'table' and 'columns' in slide and 'rows' in slide:
                    slide['table_data'] = {
                        'columns': slide['columns'],
                        'rows': slide['rows']
                    }
                
                # Pre-processamento: Chart data
                if slide.get('type') == 'chart':
                    # Universal template expects a single object or arguments passed to atom
                    # But atom call in universal.html is: render_chart(content, type)
                    # We need content to carry data, labels, label.
                    # Wait, our render_chart signature is (data, type, labels, label)
                    # And universal.html calls it as: {{ atoms.render_chart(content, slide.chart_type) }}
                    # We need to update universal.html to pass all args, OR package them into 'content'.
                    # Let's package them.
                    slide['chart_data'] = slide.get('data', [])


    except FileNotFoundError:
        print(f"❌ Errore: File '{config_path}' non trovato.")
        return False
    except yaml.YAMLError as exc:
        print(f"❌ Errore nel parsing del YAML: {exc}")
        return False

    # 2. Carica il template HTML
    try:
        # Resolve blueprints
        blueprints = DEFAULT_BLUEPRINTS.copy()
        if 'blueprints' in config:
            blueprints.update(config['blueprints'])

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
            slides=config.get('slides', []),
            blueprints=blueprints
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
