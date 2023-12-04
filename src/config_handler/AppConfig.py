from dataclasses import dataclass
from dataclasses_json import dataclass_json
from src.config_handler.InputStreamConfig import InputStreamConfig
from src.config_handler.ObjectDetectorConfig import ObjectDetectorConfig

@dataclass_json
@dataclass(frozen=True)
class AppConfig:
    input_stream_config: InputStreamConfig
    object_detector_config:ObjectDetectorConfig

