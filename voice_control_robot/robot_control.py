from gpio_wrapper import GPIO
import pyttsx3
import threading

engine = pyttsx3.init()

MOVE_DURATION = 2.0  # seconds

def speak(msg):
    engine.say(msg)
    engine.runAndWait()

def setup_gpio():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    for pin in (17, 18, 22, 23):
        GPIO.setup(pin, GPIO.OUT)

def stop_motors():
    for pin in (17, 18, 22, 23):
        GPIO.output(pin, GPIO.LOW)
    speak("Stopping")

def _auto_stop():
    stop_motors()

def _run_with_timer(action_fn):
    action_fn()
    timer = threading.Timer(MOVE_DURATION, _auto_stop)
    timer.start()

def move_forward():
    def action():
        GPIO.output(17, GPIO.HIGH)
        GPIO.output(18, GPIO.LOW)
        GPIO.output(22, GPIO.HIGH)
        GPIO.output(23, GPIO.LOW)
        speak("Moving forward")
    _run_with_timer(action)

def move_backward():
    def action():
        GPIO.output(17, GPIO.LOW)
        GPIO.output(18, GPIO.HIGH)
        GPIO.output(22, GPIO.LOW)
        GPIO.output(23, GPIO.HIGH)
        speak("Moving backward")
    _run_with_timer(action)

def turn_left():
    def action():
        GPIO.output(17, GPIO.LOW)
        GPIO.output(18, GPIO.HIGH)
        GPIO.output(22, GPIO.HIGH)
        GPIO.output(23, GPIO.LOW)
        speak("Turning left")
    _run_with_timer(action)

def turn_right():
    def action():
        GPIO.output(17, GPIO.HIGH)
        GPIO.output(18, GPIO.LOW)
        GPIO.output(22, GPIO.LOW)
        GPIO.output(23, GPIO.HIGH)
        speak("Turning right")
    _run_with_timer(action)

def cleanup():
    GPIO.cleanup()
