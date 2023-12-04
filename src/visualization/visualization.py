# import numpy as np
# from PIL import Image, ImageColor, ImageDraw, ImageFont, ImageOps
# import matplotlib.pyplot as plt
import cv2
from src.config_handler.ClassMapping import class_mapping
# from config.CLASS_MAPPING import CLASS_MAPPING

def display_frame(frame, detections):
    cv2.namedWindow("Detection", cv2.WINDOW_NORMAL)
    im_height = frame.shape[0]
    im_width = frame.shape[1] 
    cv2.resizeWindow("Detection", im_width, im_height)
    my_x_min = 0
    my_y_min = 0
    my_x_max = 1920
    my_y_max = 1080

    for box, cls, conf in zip(detections['detection_boxes'], detections['detection_classes'], detections['detection_scores']):
        ymin, xmin, ymax, xmax = map(int, box)

        cls = class_mapping.get(cls)
        
        # (xmin * im_width, xmax * im_width, ymin * im_height, ymax * im_height)

        label = f"Class: {cls}, Conf: {conf:.2f}"
        cv2.rectangle(frame, (xmin, ymin), (xmax, ymax), (0, 0, 255), 2)
        cv2.rectangle(frame, (my_x_min, my_y_min), (my_x_max, my_y_max), (0, 255, 0), 2)
        cv2.putText(frame, label, (xmin, ymin - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    cv2.imshow("Detection", frame)



# def display_image(image):
#     fig = plt.figure(figsize=(20, 15))
#     plt.grid(False)
#     plt.imshow(image)


# def draw_bounding_box_on_image(image,
#                                ymin,
#                                xmin,
#                                ymax,
#                                xmax,
#                                color,
#                                font,
#                                thickness=4,
#                                display_str_list=()):
#     """Adds a bounding box to an image."""
#     draw = ImageDraw.Draw(image)
#     im_width, im_height = image.size
#     (left, right, top, bottom) = (xmin * im_width, xmax * im_width,
#                                   ymin * im_height, ymax * im_height)
#     draw.line([(left, top), (left, bottom), (right, bottom), (right, top),
#                (left, top)],
#               width=thickness,
#               fill=color)

#     # If the total height of the display strings added to the top of the bounding
#     # box exceeds the top of the image, stack the strings below the bounding box
#     # instead of above.
#     display_str_heights = [font.getbbox(ds)[3] for ds in display_str_list]
#     # Each display_str has a top and bottom margin of 0.05x.
#     total_display_str_height = (1 + 2 * 0.05) * sum(display_str_heights)

#     if top > total_display_str_height:
#         text_bottom = top
#     else:
#         text_bottom = top + total_display_str_height
#     # Reverse list and print from bottom to top.
#     for display_str in display_str_list[::-1]:
#         bbox = font.getbbox(display_str)
#         text_width, text_height = bbox[2], bbox[3]
#         margin = np.ceil(0.05 * text_height)
#         draw.rectangle([(left, text_bottom - text_height - 2 * margin),
#                         (left + text_width, text_bottom)],
#                        fill=color)
#         draw.text((left + margin, text_bottom - text_height - margin),
#                   display_str,
#                   fill="black",
#                   font=font)
#         text_bottom -= text_height - 2 * margin


# def draw_boxes(image, detections, max_boxes=10, min_score=0.1):

#     boxes = detections["detection_boxes"]
#     class_names = detections["detection_classes"]
#     scores = detections["detection_scores"]

#     """Overlay labeled boxes on an image with formatted scores and label names."""
#     colors = list(ImageColor.colormap.values())

#     try:
#         font = ImageFont.truetype("/usr/share/fonts/truetype/liberation/LiberationSansNarrow-Regular.ttf",
#                                   25)
#     except IOError:
#         print("Font not found, using default font.")
#         font = ImageFont.load_default()

#     for i in range(min(boxes.shape[0], max_boxes)):
#         if scores[i] >= min_score:
#             ymin, xmin, ymax, xmax = tuple(boxes[i])
#             display_str = "{}: {}%".format(class_names[i].decode("ascii"),
#                                            int(100 * scores[i]))
#             color = colors[hash(class_names[i]) % len(colors)]
#             image_pil = Image.fromarray(np.uint8(image)).convert("RGB")
#             draw_bounding_box_on_image(
#                 image_pil,
#                 ymin,
#                 xmin,
#                 ymax,
#                 xmax,
#                 color,
#                 font,
#                 display_str_list=[display_str])
#             np.copyto(image, np.array(image_pil))
#     return image


# def display_frame(frame, detections):
#     cv2.namedWindow("Detection", cv2.WINDOW_NORMAL)
#     cv2.resizeWindow("Detection", frame.shape[1], frame.shape[0])
#     for box, cls, conf in zip(detections['detection_boxes'], detections['detection_classes'], detections['detection_confidences']):
#         ymin, xmin, ymax, xmax = box.astype(int)
#         label = f"Class: {cls}, Conf: {conf:.2f}"
#         cv2.rectangle(frame, (xmin, ymin), (xmax, ymax), (0, 255, 0), 2)
#         cv2.putText(frame, label, (xmin, ymin - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

#     cv2.imshow("Detection", frame)





# def visualize_input_stream(input_stream, object_detector):
#     while True:
#         frame = input_stream.read_frame()

#         if frame is not None:
#             # Perform object detection on the frame
#             detections = object_detector.detect_objects(frame)

#             # Display the frame with object detection results
#             display_frame(frame, detections)

#         key = cv2.waitKey(1) & 0xFF

#         # Check if the 'q' key or the 'Esc' key is pressed
#         if key == ord('q') or key == 27:
#             break

#     input_stream.release()
#     cv2.destroyAllWindows()