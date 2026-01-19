import pyttsx3
from langdetect import detect

engine = pyttsx3.init()

LANGUAGES = {
    "english": "en",
    "spanish": "es",
    "german": "de",
    "french": "fr",
    "nepali": "ne"
}

selected_language = None

COMMAND_MAP = {
    "en": {
        "start": "start",
        "stop": "stop",
        "move forward": "move forward",
        "move backward": "move backward",
        "move left": "move left",
        "move right": "move right",
        "power off": "power off",
    },
    "ne": {
        "सुरु": "start",
        "रोक": "stop",
        "अगाडि": "move forward",
        "पछि": "move backward",
        "बायाँ": "move left",
        "दायाँ": "move right",
        "बन्द": "power off",
    }
}

def speak(msg):
    engine.say(msg)
    engine.runAndWait()

def select_language(listen_fn):
    global selected_language
    speak("Please say a language")

    while selected_language is None:
        cmd = listen_fn()
        if not cmd:
            speak("Try again")
            continue

        for name, code in LANGUAGES.items():
            if name in cmd:
                selected_language = code
                speak(f"Language set to {name}")
                return

        speak("Language not recognized")

def normalize_command(command):
    if not selected_language:
        return command

    command = command.lower()

    for spoken, mapped in COMMAND_MAP.get(selected_language, {}).items():
        if spoken in command:
            return mapped

    return command
