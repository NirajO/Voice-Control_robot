import pyttsx3
import state

engine = pyttsx3.init()

LANGUAGES = {
    "english": ["english"],
    "nepali": ["nepali", "nepalese"]
}

COMMAND_MAP = {
    "english": {
        "start": "start",
        "stop": "stop",
        "move forward": "move forward",
        "move backward": "move backward",
        "move left": "move left",
        "move right": "move right",
        "power off": "power off",
    },
    "nepali": {
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
    if state.selected_language == "nepali":
        return  # silent mode for Nepali
    engine.say(msg)
    engine.runAndWait()


def select_language(listen_fn):
    speak("Please say a language")

    while True:
        cmd = listen_fn()
        if not cmd:
            speak("Please try again")
            continue

        cmd = cmd.lower()
        print("Language heard:", cmd)

        for lang, keywords in LANGUAGES.items():
            if any(word in cmd for word in keywords):
                state.selected_language = lang
                speak(f"Language set to {lang}")
                print("Language set to:", lang)
                return

        speak("Language not recognized")

def normalize_command(command):
    command = command.lower()

    for spoken, mapped in COMMAND_MAP.get(state.selected_language, {}).items():
        if spoken in command:
            return mapped

    return command
