import cv2
from src.config_handler.ClassMapping import class_mapping

def display_frame(frame, detections):
    cv2.namedWindow("Detection", cv2.WINDOW_NORMAL)
    im_height = frame.shape[0]
    im_width = frame.shape[1] 
    cv2.resizeWindow("Detection", im_width, im_height)
    print(f'len(class_mapping = {len(class_mapping)})')

    for box, cls, conf in zip(detections['detection_boxes'], detections['detection_classes'], detections['detection_scores']):
        ymin, xmin, ymax, xmax = map(int, box)

        cls = class_mapping.get(cls)
        label = f"Class: {cls}, Conf: {conf:.2f}"

        cv2.rectangle(frame, (xmin, ymin), (xmax, ymax), (0, 0, 255), 2)
        cv2.rectangle(frame, (0, im_height), (0, im_width), (0, 255, 0), 2)
        cv2.putText(frame, label, (xmin, ymin - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    cv2.imshow("Detection", frame)
