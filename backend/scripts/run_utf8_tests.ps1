# Script para correr los tests forzando UTF-8 en Windows
$env:PYTHONUTF8 = 1
$env:PYTHONPATH = "."
pytest
