from voice import listen
from language import select_language, normalize_command
import robot_control as robot
import sys

def main():
  robot.setup_gpio()
  select_language(listen)

  print("Robot ready")
  robot.speak("Say start to begin")

  running = False

  try:
    while True:
      command = listen()
      if not command:
        continue

      command = normalize_command(command)

      if command == "start":
        running = True
        robot.speak("Robot started")

      elif command == "stop":
        running = False
        robot.stop_motors()
        robot.speak("Robot stopped")

      elif command == "power off":
        robot.speak("Poweing off")
        robot.cleanup()
        sys.exit()

      elif running:
        if command == "move forward":
          robot.move_forward()
        elif command == "move backward":
          robot.move_backward()
        elif command == "move left":
          robot.turn_left()
        elif command == "move right":
          robot.turn_right()
        else:
          robot.speak("Command not recognized")

      else:
        robot.speak("Say start to run the robot")
    
  except KeyboardInterrupt:
    robot.cleanup()

if __name__ == "__main__":
  main()
