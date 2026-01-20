from vosk import Model, KaldiRecognizer
import sounddevice as sd
import json
import state
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODELS = {
  "english": os.path.join(BASE_DIR, "models", "vosk-model-small-en-us-0.15"),
  "chinese": os.path.join(BASE_DIR, "models", "vosk-model-small-cn-0.22"),
  "hindi": os.path.join(BASE_DIR, "models", "vosk-model-small-hi-0.22"),
  "spanish": os.path.join(BASE_DIR, "models", "vosk-model-small-es-0.42"),
  "arabic": os.path.join(BASE_DIR, "models", "vosk-model-small-ar-tn-0.1-linto"),
}


current_model = None
current_lang = None

def get_model():
  model_path = MODELS.get(state.selected_language)

  if not model_path or not os.path.exists(model_path):
    raise FileNotFoundError(f"Vosk model not found at: {model_path}")
  
  global current_model, current_lang

  if current_lang != state.selected_language:
    print("Loading Vosk model from:", model_path)
    current_model = Model(model_path)
    current_lang = state.selected_language
  
  return current_model

def listen():
  model = get_model()
  rec = KaldiRecognizer(model, 16000)

  with sd.RawInputStream(
    samplerate=16000,
    blocksize=8000,
    dtype="int16",
    channels=1
  ) as stream:
    print("Listening (offline)...")

    while True:
      data, _ = stream.read(8000)
      if rec.AcceptWaveform(bytes(data)):
        result = json.loads(rec.Result())
        text = result.get("text", "").strip().lower()
        if len(text) < 3:
          continue
        
        if text in ("uh", "um", "a", "i", "it", "is", "the"):
          continue

        print("Heard: [offline speech recognized]")
        return text