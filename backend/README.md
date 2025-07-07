## Diccionario de ejemplo

El backend incluye un archivo de ejemplo en `data/dictionary.csv` con palabras, idioma e IPA. Puedes ampliarlo descargando diccionarios abiertos (como Wiktionary) y agregando más filas.

Formato esperado:

```
word,language,ipa
hello,en,həˈloʊ
hola,es,ˈola
...etc
```

El backend carga este archivo automáticamente para buscar palabras por fonema o idioma.
# Backend - Pronunciación y Fonética

Este backend provee una API para comparar fonética de palabras extranjeras con el idioma madre del usuario, marcando fonemas idénticos, similares o distintos.

## Estructura del proyecto
- `app/` : Código fuente principal (FastAPI, lógica fonética)
- `tests/` : Pruebas automáticas
- `scripts/` : Scripts para ejecutar el backend y los tests en Windows
- `requirements.txt` : Dependencias
- `tasks.json` : Comandos rápidos para VS Code

## Comandos útiles

- Instalar dependencias:
  ```bash
  pip install -r requirements.txt
  ```
- Iniciar backend (UTF-8, recomendado en Windows):
  ```powershell
  cd scripts
  .\run_utf8_server.ps1
  ```
- Ejecutar tests (UTF-8):
  ```powershell
  cd scripts
  .\run_utf8_tests.ps1
  ```

## Endpoints principales (para Postman)

- POST `/phonetics/transcription`  
  Body: `{ "word": "hello", "language": "en" }`
- POST `/phonetics/analyze`
- POST `/phonetics/compare`
- GET  `/phonetics/examples`
- GET  `/languages`

## Uso rápido en VS Code

Puedes usar los comandos definidos en `tasks.json` desde la paleta de comandos (Ctrl+Shift+P → "Run Task") para iniciar el backend o correr los tests fácilmente.
