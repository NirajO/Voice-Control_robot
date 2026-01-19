import speech_recognition as sr
import state

recognizer = sr.Recognizer()

LANG_CODE_MAP = {
    "english": "en-US",
    "nepali": "ne-NP"
}

def listen():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        print("Listening...")
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
        except sr.WaitTimeoutError:
            return None

    try:
        lang_code = LANG_CODE_MAP.get(state.selected_language, "en-US")
        text = recognizer.recognize_google(audio, language=lang_code)

        # SAFE PRINT (Windows compatible)
        if state.selected_language == "english":
            print("You said (english):", text)
        else:
            print("You said (nepali): [recognized]")

        return text.lower()

    except sr.UnknownValueError:
        print("Could not understand audio")
        return None
