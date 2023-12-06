from dataclasses import dataclass, field
from typing import List, Dict
import json

@dataclass
class ObjectDetectorConfig:
    model_path:str
    selected_classes: List[int]
    score_threshold:float
    class_map_file: str
    class_map: Dict[str, str] = field(init=False)

    def __post_init__(self):
        with open(self.class_map_file, 'r') as map_file:
            self.class_map = json.load(map_file)
