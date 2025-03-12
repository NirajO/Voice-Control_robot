
import pyttsx3
from voice_command_recognition import recognize_speech, execute_command, listening

# Initialize text-to-speech engine
engine = pyttsx3.init()

def give_feedback(message):
    engine.say(message)
    engine.runAndWait()

# Main loop
try:
    while listening:
        command = recognize_speech()
        if command:
            execute_command(command)
except KeyboardInterrupt:
    from speech_recognition import GPIO
    GPIO.cleanup()
