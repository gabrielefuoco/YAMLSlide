import time
import os
import sys
from generator import generate_presentation

def generate():
    print("🔄 Rilevata modifica! Rigenerazione in corso...")
    success = generate_presentation()
    if success:
        print("✅ Fatto.")
    else:
        print("❌ Errore durante la generazione.")

print("👀 In ascolto su input/config.yaml... (Premi Ctrl+C per uscire)")
last_mtime = 0
config_file = os.path.join('input', 'config.yaml')

try:
    # Prima esecuzione immediata
    generate()
    last_mtime = os.path.getmtime(config_file)

    while True:
        try:
            time.sleep(1)
            if os.path.exists(config_file):
                mtime = os.path.getmtime(config_file)
                if mtime > last_mtime:
                    last_mtime = mtime
                    generate()
        except FileNotFoundError:
            pass # Il file potrebbe essere stato cancellato momentaneamente
except KeyboardInterrupt:
    print("\n👋 Uscita dal watcher.")
