import epitran
import eng_to_ipa as ipa_eng

LANG_MAP = {
    'en': 'eng-Latn',
    'es': 'spa-Latn',
    'fr': 'fra-Latn',
    'de': 'deu-Latn',
}

def word_to_ipa(word: str, language: str) -> str:
    if language == 'en':
        ipa = ipa_eng.convert(word)
        if not ipa.strip():
            return "[No IPA disponible para este idioma/palabra]"
        return ipa
    epi_code = LANG_MAP.get(language, 'eng-Latn')
    epi = epitran.Epitran(epi_code)
    try:
        ipa = epi.transliterate(word)
        if not ipa.strip():
            return "[No IPA disponible para este idioma/palabra]"
        return ipa
    except Exception as e:
        return f"[Error de transcripción: {str(e)}]"
