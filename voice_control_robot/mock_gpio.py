class MockGPIO:
    BCM = 'BCM'
    OUT = 'OUT'
    HIGH = True
    LOW = False

    def __init__(self):
        self.pins = {}

    def setmode(self, mode):
        print(f"[MockGPIO] Mode set to {mode}")

    def setwarnings(self, state):
        pass

    def setup(self, pin, mode):
        self.pins[pin] = self.LOW
        print(f"[MockGPIO] Pin {pin} setup as {mode}")

    def output(self, pin, state):
        self.pins[pin] = state
        print(f"[MockGPIO] Pin {pin} = {'HIGH' if state else 'LOW'}")

    def cleanup(self):
        print("[MockGPIO] Cleanup")
        self.pins.clear()
