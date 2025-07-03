from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import List, Optional
from app.phonetics import word_to_ipa

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "API de pronunciación activa"}

# Modelos de entrada para POST
class TranscriptionRequest(BaseModel):
    word: str
    language: str

class AnalyzeRequest(BaseModel):
    word: str
    target_language: str
    mother_language: str

class CompareRequest(BaseModel):
    word1: str
    language1: str
    word2: str
    language2: str

# Endpoint: Transcripción fonética
@app.post("/phonetics/transcription")
def transcribe_to_phonetics_IPA(request: TranscriptionRequest):
    ipa = word_to_ipa(request.word, request.language)
    return {
        "word": request.word,
        "language": request.language,
        "ipa_transcription": ipa
    }

# Endpoint: Análisis fonético
@app.post("/phonetics/analyze")
def analyze_phonetics(request: AnalyzeRequest):
    return {
        "word": request.word,
        "target_language": request.target_language,
        "mother_language": request.mother_language,
        "phonetic_analysis": "Phonetic analysis result here"
    }

# Endpoint: Comparar dos palabras
@app.post("/phonetics/compare")
def compare_phonetics(request: CompareRequest):
    return {
        "word1": request.word1,
        "language1": request.language1,
        "word2": request.word2,
        "language2": request.language2,
        "comparison": "Comparison result here"
    }

# Endpoint: Ejemplos de fonemas
@app.get("/phonetics/examples")
def get_phonetic_examples(phonemas: Optional[List[str]] = Query(None), language: str = Query(...)):
    return {
        "language": language,
        "phonemas": phonemas,
        "examples": ["Example 1", "Example 2", "Example 3"]
    }

# Endpoint: Idiomas soportados
@app.get("/languages")
def get_languages():
    return {
        "languages": [
            {"code": "en", "name": "English"},
            {"code": "es", "name": "Español"},
            {"code": "fr", "name": "Français"},
            {"code": "de", "name": "Deutsch"}
        ]
    }