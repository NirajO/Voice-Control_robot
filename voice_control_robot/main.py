from offline_voice import listen
from language import select_language, normalize_command, auto_detect_language
import robot_control as robot
import state
import sys
import time

CONFIRM_WORDS_YES = ["yes", "yeah", "confirm"]
CONFIRM_WORDS_NO = ["no", "cancel"]
CONFIRM_TIMEOUT = 5

WAKE_WORDS = [
    "hey robot",
    "robot"
]

def is_wake_word(command):
    return any(wake in command for wake in WAKE_WORDS)

def get_confirmation():
    robot.speak("Did you say that? Please say yes or no.")
    start = time.time()

    while time.time() - start < CONFIRM_TIMEOUT:
        reply = listen()
        if not reply:
            continue
        
        reply = reply.lower()

        if any(word in reply for word in CONFIRM_WORDS_YES):
            return True
        if any(word in reply for word in CONFIRM_WORDS_NO):
            return False
        
    robot.speak("No confirmation received. Command cancelled.")
    return False

def main():
    robot.setup_gpio()
    select_language(listen)

    robot.speak("Robot ready. Say hey robot to begin.")
    print("[Robot] Waiting for wake word...")

    language_locked = False
    awake = False

    try:
        while True:
            command = listen()
            if not awake:
               if "robot" not in command:
                  continue
            command = normalize_command(command)
            if not language_locked:
               detected = auto_detect_language(command)
               if detected:
                  state.selected_language = detected
                  language_locked = True
                  print(f"[Robot] Language detected: {detected}")
            
            if not command:
                continue

            # Wake word detection
            if not awake:
                if is_wake_word(command):
                    awake = True
                    robot.speak("Yes?")
                    print(" Wake word detected")
                continue

            if command == "start":
              robot.speak("Robot activated")

            elif command == "stop":
              robot.stop_motors()
              robot.speak("Robot stopped")

            elif command == "power off":
              if get_confirmation():
                robot.speak("Powering off")
                robot.cleanup()
                sys.exit()
              else:
                 robot.speak("Power off cancelled")

            elif "forward" in command:
              if get_confirmation():
                robot.move_forward()
              else:
                robot.speak("Command cancelled.")

            elif "backward" in command:
              if get_confirmation():
                robot.move_backward()
              else:
                robot.speak("Command cancelled.")

            elif "left" in command:
              if get_confirmation():
                robot.turn_left()
              else:
                robot.speak("Command cancelled.")

            elif "right" in command:
              if get_confirmation():
                robot.turn_right()
              else:
                robot.speak("Command cancelled.")

            else:
              robot.speak("Command not recognized")

            # Go back to sleep after each command
            awake = False
            print(" Waiting for wake word...")

    except KeyboardInterrupt:
        robot.cleanup()

if __name__ == "__main__":
    main()
