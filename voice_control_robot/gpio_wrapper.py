import sys

if sys.platform == "win32":
  from mock_gpio import MockGPIO
  GPIO = MockGPIO()

else:
  import Rpi.GPIO as GPIO

__all__ = ["GPIO"]