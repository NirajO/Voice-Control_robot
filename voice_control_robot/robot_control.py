from gpio_wrapper import GPIO
import pyttsx3

engine = pyttsx3.init()
robot_running = False

def speak(msg):
  engine.say(msg)
  engine.runAndWait()

def setup_gpio():
  GPIO.setwarnings(False)
  GPIO.setmode(GPIO.BCM)

  for pin in (17, 18, 22, 23):
    GPIO.setup(pin, GPIO.OUT)

def move_forward():
  GPIO.output(17, GPIO.HIGH)
  GPIO.output(18, GPIO.LOW)
  GPIO.output(22, GPIO.HIGH)
  GPIO.output(23, GPIO.LOW)
  speak("Moving forward")

def move_backward():
  GPIO.output(17, GPIO.LOW)
  GPIO.output(18, GPIO.HIGH)
  GPIO.output(22, GPIO.LOW)
  GPIO.output(23, GPIO.HIGH)
  speak("Moving backward")

def turn_left():
  GPIO.output(17, GPIO.LOW)
  GPIO.output(18, GPIO.HIGH)
  GPIO.output(22, GPIO.LOW)
  GPIO.output(23, GPIO.HIGH)
  speak("Turning left")

def turn_right():
  GPIO.output(17, GPIO.LOW)
  GPIO.output(18, GPIO.HIGH)
  GPIO.output(22, GPIO.LOW)
  GPIO.output(23, GPIO.HIGH)
  speak("Turning right")

def stop_motors():
  for pin in (17, 18, 22, 23):
    GPIO.output(pin, GPIO.LOW)
  speak("Stopping")

def cleanup():
  GPIO.cleanup()