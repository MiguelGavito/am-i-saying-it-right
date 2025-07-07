# Am I Saying It Right?

Este programa ayuda a visualizar y comparar los sonidos de palabras en distintos idiomas usando el alfabeto fonético internacional (IPA).

## ¿Cómo usar?

1. Instala las dependencias del backend:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```
2. Inicia el backend de forma portable (UTF-8):
   ```powershell
   cd backend/scripts
   .\run_utf8_server.ps1
   ```
3. Prueba los endpoints con Postman:
   - POST http://127.0.0.1:8000/phonetics/transcription
   - POST http://127.0.0.1:8000/phonetics/analyze
   - POST http://127.0.0.1:8000/phonetics/compare
   - GET  http://127.0.0.1:8000/phonetics/examples
   - GET  http://127.0.0.1:8000/languages

Consulta el README del backend para más detalles y ejemplos de uso.
