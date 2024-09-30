import time
from PIL import ImageGrab, ImageFilter

class ScreenshotManager:
    def __init__(self, config_manager):
        self.config_manager = config_manager

    def capture_screenshot(self):
        if not self.config_manager.is_screenshot_enabled():
            return
        
        screenshot = ImageGrab.grab()
        if self.config_manager.is_blur_enabled():
            screenshot = screenshot.filter(ImageFilter.GaussianBlur(15))
        
        filename = f"screenshot_{time.strftime('%Y%m%d_%H%M%S')}.png"
        screenshot.save(filename)
        print(f"Screenshot saved as {filename}")
