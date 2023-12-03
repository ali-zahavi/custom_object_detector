import argparse
from src.input_stream import ImageCapture, VideoCapture, WebcamCapture
from src.visualization import visualize_input_stream


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

    # Create an input stream based on user-provided source_type
    #input_stream = InputStream(source_type=args.source_type)
    if args.source_type == "images":
        input_stream = ImageCapture()
    elif args.source_type == "video":
        input_stream = VideoCapture()
    elif args.source_type == "webcam":
        input_stream = WebcamCapture()
    else:
        raise ValueError(f"Invalid source type: {args.source_type}")    
    
    # check_input_source_exists
    input_stream.check_input_source_exists()
    
    # Open the input stream
    input_stream.open()

    # Visualize the input stream
    visualize_input_stream(input_stream)

    # Release the input stream
    input_stream.release()

if __name__ == "__main__":
    main()
