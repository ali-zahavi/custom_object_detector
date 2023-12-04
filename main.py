import argparse
from src.input_stream import InputStream, ImageCapture, VideoCapture, WebcamCapture
from src.visualization import display_frame
from src.object_detection import ObjectDetector
import cv2
import numpy as np
from src.config_handler import AppConfig
import json


def parse_arguments():
    valid_source_types = ["images", "video", "webcam"]
    parser = argparse.ArgumentParser(description="Custom Object Detector Application")
    parser.add_argument("--source-type", choices=valid_source_types, help="Type of input source (images, video, webcam)")

    args = parser.parse_args()

    # Check if --source-type is provided and is one of the valid choices
    if not args.source_type:
        parser.error("You must provide --source-type (choose from: {})".format(', '.join(valid_source_types)))

    return args

def main():
    # Parse command-line arguments
    args = parse_arguments()
    with open('config.json', 'r') as f:
        app_config = json.load(f)
    app_config = AppConfig.from_dict(app_config)

    # Create an input stream based on user-provided source_type
    if args.source_type == "images":
        input_stream = ImageCapture(images_path=app_config.input_stream_config.images_path)
    elif args.source_type == "video":
        input_stream = VideoCapture(video_path=app_config.input_stream_config.video_path)
    elif args.source_type == "webcam":
        input_stream = WebcamCapture()
    else:
        raise ValueError(f"Invalid source type: {args.source_type}")    
    
    # create object detector
    object_detector = ObjectDetector(object_detector_config=app_config.object_detector_config)
    
    input_stream.check_input_source_exists()
    input_stream.open()

    # frame_no = 0
    # old_detection = np.array([None])
    # detection_no = 0
    while True:
        frame = input_stream.read_frame()

        if frame is not None:
            # Perform object detection on the frame
            detections = object_detector.detect_objects(frame)
            # if not np.all(detections['detection_boxes'] == old_detection):
            #     detection_no +=1
            #     print('############################')
            #     print(f'detection_no = {detection_no}')
            #     print(detections)
            #     print('############################')
            #     old_detection = detections
            # # Display the frame with object detection results
            # frame_no +=1
            # print(frame_no)
            display_frame(frame, detections)
            
            # image_with_boxes = draw_boxes(
            # frame, detections)

            # display_image(image_with_boxes)

        key = cv2.waitKey(1) & 0xFF

        # Check if the 'q' key or the 'Esc' key is pressed
        if key == ord('q') or key == 27:
            break
    
    input_stream.release()
    cv2.destroyAllWindows()
    
    # Visualize the input stream
    # visualize_input_stream(input_stream, object_detector)

    # Release the input stream
    input_stream.release()

if __name__ == "__main__":
    main()

