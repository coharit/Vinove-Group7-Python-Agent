import pynput
from datetime import datetime

class ActivityTracker:
    def __init__(self, config_manager):
        self.mouse_listener = pynput.mouse.Listener(on_move=self.on_move)
        self.keyboard_listener = pynput.keyboard.Listener(on_press=self.on_press)
        self.config_manager = config_manager
        self.activity_log = []

    def on_move(self, x, y):
        if self.is_genuine_activity(x, y):
            self.log_activity("Mouse moved")

    def on_press(self, key):
        self.log_activity(f"Key pressed: {key}")

    def is_genuine_activity(self, x, y):
        # Implement logic to differentiate genuine from scripted activity
        # For example: Check mouse speed and randomness of movement
        return True

    def log_activity(self, activity):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.activity_log.append(f"[{timestamp}] {activity}")
        print(f"Activity logged: {activity}")

    def track(self):
        # Start tracking mouse and keyboard activity
        with self.mouse_listener, self.keyboard_listener:
            self.mouse_listener.join()
            self.keyboard_listener.join()

    def get_activity_logs(self):
        return "\n".join(self.activity_log)
