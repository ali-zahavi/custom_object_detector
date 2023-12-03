import cv2

def display_frame(frame):
    cv2.imshow("", frame)

def close_windows():
    cv2.destroyAllWindows()

def wait_key(delay=1):
    return cv2.waitKey(delay) & 0xFF

def visualize_input_stream(input_stream):
    # Read and display frames until the user presses 'q'
    while True:
        frame = input_stream.read_frame()

        if frame is not None:
            # Display the frame
            display_frame(frame)

        # Break the loop if 'q' key is pressed
        if wait_key(1) == ord('q'):
            break
    
    # Close all OpenCV windows
    close_windows()