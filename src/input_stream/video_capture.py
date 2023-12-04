import os
import cv2
from src.input_stream import InputStream
import logging

logger = logging.getLogger(__name__)


class VideoCapture(InputStream):
    def __init__(self, video_path):
        self.video_path = video_path
        self.video_files = [os.path.join(self.video_path, f) for f in os.listdir(self.video_path) if f.lower().endswith(('.mp4', '.mkv'))]
        self.video_files.sort()
        self.cap = None

    def check_input_source_exists(self):
        if not self.video_files:
            logger.error(f"No video file found in {self.video_path}")
            raise FileNotFoundError(f"No video file found in {self.video_path}")

    def open(self):
        self.cap = cv2.VideoCapture(self.video_files[0])

    def read_frame(self):
        if self.cap is not None and self.cap.isOpened():
            ret, frame = self.cap.read()
            if ret:
                return frame
        return None

    def release(self):
        if self.cap is not None:
            self.cap.release()
            logger.info("Released video input stream")