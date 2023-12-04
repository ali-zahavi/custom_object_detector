import tensorflow as tf
import tensorflow_hub as hub
import numpy as np

class ObjectDetector:
    def __init__(self, object_detector_config):
        self.detector = hub.load(object_detector_config.model_path)
        self.score_threshold = object_detector_config.score_threshold
        self.selected_classes = object_detector_config.selected_classes

    def _preprocess_image(self, image):  
        pass
    
    def detect_objects(self, image):
        # self._preprocess_image(image)
        image = np.asarray(image)
        input_tensor = tf.convert_to_tensor(image)
        input_tensor = input_tensor[tf.newaxis,...]

        boxes, scores, classes, num_detections = [tensor.numpy() for tensor in self.detector(input_tensor)]
        classes = classes.astype(np.int32)

        selected_indices = np.where((scores >= self.score_threshold) & (np.isin(classes, self.selected_classes)))

        return {
            'detection_boxes': boxes[selected_indices],
            'detection_classes': classes[selected_indices],
            'detection_scores': scores[selected_indices]
        }           