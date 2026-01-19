🤖 Voice-Controlled Robot (Multilingual: English & Nepali)

A Python-based voice-controlled robot system that supports English and Nepali voice commands, designed to work on Windows (Mock GPIO) and Raspberry Pi (real GPIO).
The robot responds to spoken commands such as start, stop, move forward, turn left, etc., using speech recognition and GPIO motor control.

🚀 Features

🎤 Voice control using speech recognition

🌐 Multilingual support

English (en-US)

Nepali (ne-NP)

🔄 Dynamic language switching via voice

⚙️ Motor control using GPIO

🪟 Windows compatible (MockGPIO for testing)

🍓 Raspberry Pi ready (RPi.GPIO)

🧠 Clean, modular, professional architecture

🗂️ Project Structure
voice_control_robot/
│
├── __init__.py
├── main.py              # Entry point
├── voice.py             # Speech recognition (English & Nepali)
├── language.py          # Language selection & command mapping
├── robot_control.py     # GPIO motor control logic
├── gpio_wrapper.py      # GPIO abstraction (Windows / Raspberry Pi)
├── mock_gpio.py         # Mock GPIO for Windows testing
├── state.py             # Shared global state
└── requirements.txt

🛠️ Requirements
Python

Python 3.9+ (tested on Python 3.12)

Python Libraries

Install dependencies using:

pip install -r requirements.txt


requirements.txt:

SpeechRecognition
pyttsx3
langdetect
pyaudio


⚠️ Note: PyAudio may require extra setup on Windows.
If installation fails, install from a prebuilt wheel.

▶️ How to Run
On Windows (Mock GPIO)
python main.py

On Raspberry Pi
python main.py


(GPIO pins will control real motors on Raspberry Pi.)

🗣️ Voice Commands
Language Selection

Say one of the following when prompted:

“English”

“Nepali”

English Commands
Command	Action
start	Start robot
stop	Stop robot
move forward	Move forward
move backward / backwards	Move backward
move left	Turn left
move right	Turn right
power off	Exit program

Nepali Commands
Nepali	Meaning
सुरु	Start
रोक	Stop
अगाडि	Move forward
पछि	Move backward
बायाँ	Turn left
दायाँ	Turn right
बन्द	Power off

Speak clearly and pause briefly before each command.

🔊 Text-to-Speech Behavior (Important)

On Windows, the robot speaks in English only

Windows does not provide Nepali TTS voices

This is an OS limitation, not a code bug

Nepali speech recognition works correctly

On Linux / Raspberry Pi, Nepali TTS can be added later (eSpeak / Festival)

🧠 Design Notes

Uses Google Speech Recognition API

Recognition language switches dynamically (en-US, ne-NP)

GPIO logic is abstracted for portability

MockGPIO allows safe testing without hardware

Unicode printing is safely handled on Windows

🔮 Future Improvements

🔌 Offline speech recognition (Vosk)

🧏 Nepali text-to-speech on Linux

📷 Camera-based person following

🚧 Obstacle avoidance (ultrasonic sensor)

🗣️ Wake-word detection (“Hey Robot”)

👨‍💻 Author

Niraj Ojha
Computer Science
Voice-Controlled Robotics Project

📜 License

This project is for educational and academic use.
Feel free to modify and extend.