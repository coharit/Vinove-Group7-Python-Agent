import threading
from time import sleep
from activity_tracker import ActivityTracker
from screenshot import ScreenshotManager
from uploader import Uploader
from config_manager import ConfigManager
import psutil
import signal
import os

class DesktopAgent:
    def __init__(self):
        self.config_manager = ConfigManager()
        self.screenshot_manager = ScreenshotManager(self.config_manager)
        self.activity_tracker = ActivityTracker(self.config_manager)
        self.uploader = Uploader(self.config_manager)
        self.running = True

    def run(self):
        # Monitor activity and capture screenshots at intervals
        while self.running:
            self.check_for_config_updates()
            self.activity_tracker.track()
            self.screenshot_manager.capture_screenshot()
            self.uploader.upload_data()
            self.check_for_shutdown_conditions()
            sleep(self.config_manager.get_screenshot_interval())

    def check_for_shutdown_conditions(self):
        # Example: suspend activity if low battery
        battery = psutil.sensors_battery()
        if battery and battery.percent < 20 and battery.power_plugged is False:
            print("Low battery detected. Suspending activity tracking.")
            self.suspend_activity()

    def suspend_activity(self):
        # Suspend agent until the battery is charged
        while True:
            battery = psutil.sensors_battery()
            if battery and battery.power_plugged:
                print("Power restored. Resuming activity.")
                break
            sleep(60)

    def check_for_config_updates(self):
        # Periodically check for updates from the web app
        self.config_manager.update_config()

    def stop(self, signum, frame):
        print("Gracefully stopping the agent...")
        self.running = False

if __name__ == '__main__':
    agent = DesktopAgent()
    signal.signal(signal.SIGINT, agent.stop)  # Graceful shutdown on Ctrl+C
    signal.signal(signal.SIGTERM, agent.stop)  # Handle kill signals
    agent.run()
