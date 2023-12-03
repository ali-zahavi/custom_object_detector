import os
import cv2
from src.input_stream import InputStream
from config.PATH import INPUT_STREAM_IMAGES_PATH
import logging

logger = logging.getLogger(__name__)

class ImageCapture(InputStream):
    def __init__(self):
        super().__init__("images")
        self.image_directory = INPUT_STREAM_IMAGES_PATH
        self.image_files = [os.path.join(self.image_directory, f) for f in os.listdir(self.image_directory) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
        self.image_files.sort()

    def check_input_source_exists(self):
        if not self.image_files:
            logger.error(f"No images found in {self.image_directory}")
            raise FileNotFoundError(f"No images found in {self.image_directory}")

    def open(self):
        pass
        
        
    def read_frame(self):
        if self.image_files:
            image_path = self.image_files.pop(0)
            frame = cv2.imread(image_path)
            return frame
        return None

    def release(self):
        pass