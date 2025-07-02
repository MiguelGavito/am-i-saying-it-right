# Backend - Pronunciación y Fonética

Este backend provee una API para comparar fonética de palabras extranjeras con el idioma madre del usuario, marcando fonemas idénticos, similares o distintos.

## Estructura inicial
- `app/main.py`: FastAPI app principal
- `requirements.txt`: dependencias
- `tests/`: carpeta para tests

## Comandos útiles

- Instalar dependencias:
  ```bash
  pip install -r requirements.txt
  ```
- Ejecutar servidor de desarrollo:
  ```bash
  uvicorn app.main:app --reload
  ```
- Ejecutar tests:
  ```bash
  pytest
  ```
