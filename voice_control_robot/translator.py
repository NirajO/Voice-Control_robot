from googletrans import Translator

_translator = Translator()

def translate_to_english(text, source_lang):
  if source_lang == "english":
    return text
  
  try:
    translated = _translator.translate(text, src=source_lang, dest="en")
    return translated.text.lower()
  except Exception:
    return text.lower()