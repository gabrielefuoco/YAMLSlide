@echo off
echo 🚀 Avvio generazione presentazione...
python src/generator.py
if %ERRORLEVEL% NEQ 0 (
    echo ❌ Errore durante la generazione.
    pause
    exit /b %ERRORLEVEL%
)

echo 📦 Creazione versione portable (Single HTML)...
python src/bundler.py
if %ERRORLEVEL% NEQ 0 (
    echo ⚠️ Avviso: Errore durante il bundling, ma la versione base è ok.
)

echo ✅ Processo completato. I file si trovano in 'output/'.
pause
