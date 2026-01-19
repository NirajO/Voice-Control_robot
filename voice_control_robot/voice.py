import speech_recognition as sr

recognizer = sr.Recognizer()

def listen():
  with sr.Microphone() as source:
    recognizer.adjust_for_ambient_noise(source, duration=0.5)
    print("Listening...")
    try:
      audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
    except sr.WaitTimeoutError:
      return None
    
  try:
    text = recognizer.recognize_google(audio)
    print("You said:", text)
    return text.lower()
  except sr.UnknownValueError:
    return None
  except sr.RequestError as e:
    print("Speech API error:", e)
    return None