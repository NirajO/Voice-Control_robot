import sys

if sys.platform == 'win32':
    from mock_gpio import MockGPIO
    GPIO = MockGPIO()
    
else:
    import RPi.GPIO as GPIO
    

import speech_recognition as sr
import time
import pyttsx3
from langdetect import detect
from googletrans import Translator

# Initialize text-to-speech engine
engine = pyttsx3.init()
robot_running = False
selected_language = None #default to English
translator = Translator()

language_names = {"en" : "English", 
                "es" : "Spanish", 
                "de": "German", 
                "fr": "French",
                "ne": "Nepali"}

def give_feedback(message):
    engine.say(message)
    engine.runAndWait()

def set_language(lang_code):
    global selected_language
    selected_language = lang_code
    language_name = language_names.get(lang_code, "Unknown language")
    give_feedback(f"Language selected: {language_name}")

def select_language():
    global selected_language
    give_feedback("Please say a language to select.")
    lang_command = recognize_speech()

    print(f"Recognized language command: {lang_command}")  # Debug line

    if lang_command:
        lang_command = lang_command.strip().lower()  # Normalize input
        # Print available languages for debugging
        print(f"Available languages: {list(language_names.values())}")  # Debug line
        
        # Check if recognized command matches any of the language names (case insensitive)
        lang_code = None
        for language in language_names.values():
            if lang_command == language.lower():
                lang_code = {v: k for k, v in language_names.items()}.get(language)
                break
                
        if lang_code:
            set_language(lang_code)
        else:
            give_feedback("Sorry, language not recognized. Please try again.")
            select_language()
    else:
        give_feedback("No input detected. Please try again.")
        select_language()  

# Set up GPIO pins
GPIO.setWarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)

def move_forward():
    GPIO.output(17, GPIO.HIGH)
    GPIO.output(18, GPIO.LOW)
    GPIO.output(22, GPIO.HIGH)
    GPIO.output(23, GPIO.LOW)
    give_feedback("Moving forward")

def move_backward():
    GPIO.output(17, GPIO.LOW)
    GPIO.output(18, GPIO.HIGH)
    GPIO.output(22, GPIO.LOW)
    GPIO.output(23, GPIO.HIGH)
    give_feedback("Moving back")

def turn_left():
    GPIO.output(17, GPIO.LOW)
    GPIO.output(18, GPIO.HIGH)
    GPIO.output(22, GPIO.HIGH)
    GPIO.output(23, GPIO.LOW)
    give_feedback("Moving left")

def turn_right():
    GPIO.output(17, GPIO.HIGH)
    GPIO.output(18, GPIO.LOW)
    GPIO.output(22, GPIO.LOW)
    GPIO.output(23, GPIO.HIGH)
    give_feedback("Moving right")

def stop():
    global listening
    GPIO.output(17, GPIO.LOW)
    GPIO.output(18, GPIO.LOW)
    GPIO.output(22, GPIO.LOW)
    GPIO.output(23, GPIO.LOW)
    give_feedback("Stopping")
    listening = False

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        return None
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        return None
    
def detect_language(command):
    # Detect the language of the command
    lang_code = detect(command)
    return lang_code
    
def translate_command(command):
    if selected_language:  # Ensure a language has been selected
        translated = translator.translate(command, dest='en')
        return translated.text.lower()
    return command.lower() 
    

def execute_command(command):
    global robot_running, selected_language

    if command is None:
        print("No command Recognized")
        return
    
    command = command.strip().lower()

    #feedback_given = False

    if command == "change language":
        select_language()
        return
    
    if selected_language is None:
        give_feedback("Please select a language first")
        return
    
    detected_language = detect_language(command)
    print(f"Detected language: {detected_language}")
    
    print(f"Current robot state: {'running' if robot_running else 'stopped'}")

    translated_command = translate_command(command)
    print(f"Translated command: {translated_command}")

    if translated_command  == "start":
        if not robot_running:
            robot_running = True
            print("Robot has Started")
            give_feedback("Robot has started")
        else:
            print("Robot is already running")
            give_feedback("Robot is alreday running")

    elif translated_command  == "stop":
        if robot_running:
            robot_running = False
            print("Robot has Stopped")
            give_feedback("Robot has stopped. Please say 'start' to resume")
        else:
            print("Robot has alreday stop")
            give_feedback("Robot has alreday stopped. Please say 'start' to resume")

    elif translated_command  == "power off":
        print("Powering off the robot")
        give_feedback("powering off the robot.")
        GPIO.cleanup()
        sys.exit()
    

    elif robot_running:
        if translated_command  == "move forward":
            move_forward()

        elif translated_command == "move back":
            move_backward()

        elif translated_command  == "move left":
            turn_left()

        elif translated_command  == "move right":
            turn_right()

        else:
             print("Command not recognized")
             give_feedback("Command not recognized")

    else:
        give_feedback("Please say start to run the robot.")
            

listening = True

try:
    select_language()
    while listening:
        command = recognize_speech() 
        if command:
            execute_command(command)
except KeyboardInterrupt:
    GPIO.cleanup()


