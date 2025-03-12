class MockGPIO:
    BCM = 'BCM'
    OUT = 'OUT'
    HIGH = True
    LOW = False

    def __init__(self):
        self.pins = {}

    def setmode(self, mode):
        print(f"MockGPIO: setmode() called with mode: {mode}")

    def setup(self, pin, mode):
        self.pins[pin] = MockGPIO.LOW
        print(f"MockGPIO: Pin {pin} set up as {mode}")

    def output(self, pin, state):
        self.pins[pin] = state
        state_str = 'HIGH' if state else 'LOW'
        print(f"MockGPIO: Pin {pin} set to {state_str}")

    def cleanup(self):
        print("MockGPIO: GPIO cleanup called")
        self.pins.clear()
