# Object Detection Project

## Overview

This repository prioritizes best practices in code design and structure, facilitating easy expansion and adaptability for future enhancements, rather than placing emphasis on machine learning optimization.

This project is designed to conduct object detection across multiple source types, such as image sequences, videos, and potentially webcams (implementation is complete but awaiting testing). Currently, the system recognizes user-selected classes from a pre-trained model.

## Features

- **Docker Integration:** The project is containerized using Docker, ensuring consistent and reproducible environments.
- **Configurability with JSON Files and Dataclasses:** Configuration parameters, such as model paths, score thresholds, and class mappings, are stored in a JSON files and managed using dataclasses and for easy customization.
- **Modularity:** The codebase is structured in a modular fashion, allowing easy expansion of functionalities and the addition of new source types for object detection.
- **DVC Integration (Work in Progress):** The project is integrated with DVC (Data Version Control) for efficient management of large datasets and model files.
- **ROS Integration (Work in Progress):** Integration with ROS (Robot Operating System) for robotics applications.
- **Transfer Learning-Based Custom Object Detection (Work in Progress):** Employing a pre-trained model for detecting custom objects.
- **Developing a Tailored Model for Custom Object Detection (Future work, maybe another repo in the future!)** Creating a specialized model designed for the detection of custom objects.

## Getting Started

1. Clone the repository.
2. Open the folder in VScode, and reopen the project in container.
3. If necessary, adjust the configuration in config.json (e.g., update the selected classes for detection).
3. Run "main.py" while selecting the source type:

   ```bash
   python3 main.py --source-type video
   python3 mian.py --source-type images