# Script para iniciar el servidor FastAPI forzando UTF-8 en Windows
$env:PYTHONUTF8 = 1
uvicorn app.main:app --reload
