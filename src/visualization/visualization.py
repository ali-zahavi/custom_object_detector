import cv2
import colorsys
import random

class Visualization:
    def __init__(self,class_map) -> None:
        random.seed(100)
        self.class_map = class_map
        self.color_map = {_key: self.generate_distinct_rgb_color() for _key in self.class_map}
    

    @staticmethod
    def generate_distinct_rgb_color():
        saturation = 1
        lightness = 0.5
        hue = random.random()

        rgb_color = colorsys.hls_to_rgb(hue, lightness, saturation)
        rgb_color = tuple(int(val * 255) for val in rgb_color)

        return rgb_color
    
    
    def display_bboxes (self, frame, detections):
            cv2.namedWindow("Detection", cv2.WINDOW_NORMAL)
            im_height = frame.shape[0]
            im_width = frame.shape[1] 
            cv2.resizeWindow("Detection", im_width, im_height)

            for box, cls, conf in zip(detections['detection_boxes'], detections['detection_classes'], detections['detection_scores']):
                ymin, xmin, ymax, xmax = map(int, box)

                color = self.color_map.get(str(cls))
                
                label = f"{self.class_map.get(str(cls))}, {int(conf*100)}%"

                cv2.rectangle(frame, (xmin, ymin), (xmax, ymax), color, 2)
                
                cv2.putText(frame, label, (xmin, ymin - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

            cv2.imshow("Detection", frame)
