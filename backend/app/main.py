from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import List, Optional
from app.phonetics import word_to_ipa
from app.dictionary_utils import find_words_by_ipa

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
    # 1. Transcribir la palabra a IPA
    ipa = word_to_ipa(request.word, request.target_language)

    # 2. Listas de fonemas por idioma (simplificadas, pueden ampliarse)
    PHONEMES = {
        "en": set(["p", "b", "t", "d", "k", "g", "f", "v", "θ", "ð", "s", "z", "ʃ", "ʒ", "h", "m", "n", "ŋ", "l", "r", "j", "w", "i", "ɪ", "e", "æ", "ɑ", "ʌ", "ɔ", "ɒ", "ʊ", "u", "ə", "ɜ", "aɪ", "aʊ", "ɔɪ", "eɪ", "oʊ"]),
        "es": set(["p", "b", "t", "d", "k", "g", "f", "θ", "s", "x", "ʝ", "m", "n", "ɲ", "l", "ʎ", "r", "ɾ", "i", "e", "a", "o", "u"]),
        "fr": set(["p", "b", "t", "d", "k", "g", "f", "v", "s", "z", "ʃ", "ʒ", "m", "n", "ɲ", "l", "ʁ", "j", "ɥ", "w", "i", "e", "ɛ", "a", "ɑ", "o", "ɔ", "u", "y", "ø", "œ", "ə"]),
        "de": set(["p", "b", "t", "d", "k", "g", "f", "v", "s", "z", "ʃ", "ç", "x", "h", "m", "n", "ŋ", "l", "r", "j", "i", "ɪ", "e", "ɛ", "a", "aː", "o", "u", "ʊ", "y", "ø", "œ", "ə"])
    }

    # 3. Extraer fonemas de la palabra en IPA (simplificado: cada símbolo individual)
    phonemes_in_word = [c for c in ipa if c.isalpha() or c in ["ˈ", "ˌ", "ː"]]

    # 4. Obtener fonemas de cada idioma
    target_phonemes = PHONEMES.get(request.target_language, set())
    mother_phonemes = PHONEMES.get(request.mother_language, set())

    # 5. Comparar fonemas
    shared = list(target_phonemes & mother_phonemes)
    unique_to_target = list(target_phonemes - mother_phonemes)
    unique_to_mother = list(mother_phonemes - target_phonemes)

    # 6. Buscar fonemas "similares" (simplificado: mapeo manual)
    SIMILAR = [
        ("x", "h"), ("ʝ", "j"), ("θ", "θ"), ("ɲ", "ŋ"), ("ʎ", "l"), ("r", "ʁ"), ("ɾ", "r"), ("b", "v"), ("ʃ", "ʃ"), ("ʒ", "ʒ")
    ]
    similar_phonemes = []
    for t in unique_to_target:
        for m in unique_to_mother:
            if (t, m) in SIMILAR or (m, t) in SIMILAR:
                similar_phonemes.append({"target": t, "mother": m, "similarity": "high"})

    return {
        "word": request.word,
        "ipa": ipa,
        "target_language": request.target_language,
        "mother_language": request.mother_language,
        "phonemes_in_word": phonemes_in_word,
        "phonemes_target_language": list(target_phonemes),
        "phonemes_mother_language": list(mother_phonemes),
        "shared_phonemes": shared,
        "unique_to_target": unique_to_target,
        "unique_to_mother": unique_to_mother,
        "similar_phonemes": similar_phonemes
    }


# Endpoint: Mapa de colores de fonemas para colorear IPA
from fastapi import Body

class ColorMapRequest(BaseModel):
    word: str
    target_language: str
    mother_language: str

@app.post("/phonetics/color-map")
def phonetic_color_map(request: ColorMapRequest):
    ipa = word_to_ipa(request.word, request.target_language)

    PHONEMES = {
        "en": set(["p", "b", "t", "d", "k", "g", "f", "v", "θ", "ð", "s", "z", "ʃ", "ʒ", "h", "m", "n", "ŋ", "l", "r", "j", "w", "i", "ɪ", "e", "æ", "ɑ", "ʌ", "ɔ", "ɒ", "ʊ", "u", "ə", "ɜ", "aɪ", "aʊ", "ɔɪ", "eɪ", "oʊ"]),
        "es": set(["p", "b", "t", "d", "k", "g", "f", "θ", "s", "x", "ʝ", "m", "n", "ɲ", "l", "ʎ", "r", "ɾ", "i", "e", "a", "o", "u"]),
        "fr": set(["p", "b", "t", "d", "k", "g", "f", "v", "s", "z", "ʃ", "ʒ", "m", "n", "ɲ", "l", "ʁ", "j", "ɥ", "w", "i", "e", "ɛ", "a", "ɑ", "o", "ɔ", "u", "y", "ø", "œ", "ə"]),
        "de": set(["p", "b", "t", "d", "k", "g", "f", "v", "s", "z", "ʃ", "ç", "x", "h", "m", "n", "ŋ", "l", "r", "j", "i", "ɪ", "e", "ɛ", "a", "aː", "o", "u", "ʊ", "y", "ø", "œ", "ə"])
    }
    SIMILAR = [
        ("x", "h"), ("ʝ", "j"), ("θ", "θ"), ("ɲ", "ŋ"), ("ʎ", "l"), ("r", "ʁ"), ("ɾ", "r"), ("b", "v"), ("ʃ", "ʃ"), ("ʒ", "ʒ")
    ]

    target_phonemes = PHONEMES.get(request.target_language, set())
    mother_phonemes = PHONEMES.get(request.mother_language, set())

    # Extraer fonemas de la palabra en IPA (simplificado: cada símbolo individual)
    phonemes_in_word = [c for c in ipa if c.isalpha() or c in ["ˈ", "ˌ", "ː"]]

    color_map = []
    for symbol in phonemes_in_word:
        if symbol in target_phonemes and symbol in mother_phonemes:
            category = "igual"  # verde
        elif any((symbol, m) in SIMILAR or (m, symbol) in SIMILAR for m in mother_phonemes):
            category = "similar"  # amarillo
        elif symbol in target_phonemes:
            category = "distinto"  # rojo
        else:
            category = "otro"  # gris o sin color
        color_map.append({"symbol": symbol, "category": category})

    return {
        "ipa": ipa,
        "color_map": color_map
    }

# Endpoint: Ejemplos de fonemas
@app.get("/phonetics/examples")
def get_phonetic_examples(phonemas: Optional[List[str]] = Query(None), language: str = Query(...)):
    if not phonemas:
        return {"error": "Debes proporcionar al menos un fonema."}
    examples = []
    for phon in phonemas:
        words = find_words_by_ipa(phon, language)
        examples.extend(words)
    return {
        "language": language,
        "phonemas": phonemas,
        "examples": list(set(examples))
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