import cv2
from src.input_stream import InputStream
import logging

logger = logging.getLogger(__name__)

class WebcamCapture(InputStream):
    def __init__(self):
        super().__init__("webcam")
        self.cap = None

    def check_input_source_exists(self):
        # Check if a webcam is available
        available_cameras = [f"Camera {i}" for i in range(10) if cv2.VideoCapture(i).isOpened()]
        if available_cameras:
            logger.info(f"Available webcams: {', '.join(available_cameras)}")
        else:
            logger.error("No webcam available.")
            raise RuntimeError("No webcam available.")

    def open(self):
        self.cap = cv2.VideoCapture(0)

    def read_frame(self):
        if self.cap is not None and self.cap.isOpened():
            ret, frame = self.cap.read()
            if ret:
                return frame
        return None

    def release(self):
        if self.cap is not None:
            self.cap.release()
            logger.info("Released webcam input stream")