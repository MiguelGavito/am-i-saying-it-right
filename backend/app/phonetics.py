from phonemizer import phonemize

LANG_MAP = {
    'en': 'en-us',
    'es': 'es',
    'fr': 'fr-fr',
    'de': 'de',
}

def word_to_ipa(word: str, language: str) -> str:
    """
    Transcribe a word to its IPA representation using phonemizer.
    """
    lang_code = LANG_MAP.get(language, language)
    ipa = phonemize(word, language=lang_code, backend='espeak', strip=True, punctuation_marks=None, njobs=1)
    return ipa
