import json
import time

class ConfigManager:
    def __init__(self):
        self.config = self.load_config()

    def load_config(self):
        with open("config.json", "r") as f:
            return json.load(f)

    def update_config(self):
        # Poll the web server or config file for updates
        self.config = self.load_config()

    def get_screenshot_interval(self):
        return self.config.get("screenshot_interval", 300)

    def is_screenshot_enabled(self):
        return self.config.get("screenshot_enabled", True)

    def is_blur_enabled(self):
        return self.config.get("blur_screenshots", False)

    def get_s3_bucket_name(self):
        return self.config.get("s3_bucket_name", "your-bucket-name")
