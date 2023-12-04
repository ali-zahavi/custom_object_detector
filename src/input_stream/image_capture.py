import os
import cv2
from src.input_stream import InputStream
import logging

logger = logging.getLogger(__name__)

class ImageCapture(InputStream):
    def __init__(self, images_path):
        self.images_path = images_path
        self.image_files = [os.path.join(self.images_path, f) for f in os.listdir(self.images_path) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
        self.image_files.sort()

    def check_input_source_exists(self):
        if not self.image_files:
            logger.error(f"No images found in {self.images_path}")
            raise FileNotFoundError(f"No images found in {self.images_path}")

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