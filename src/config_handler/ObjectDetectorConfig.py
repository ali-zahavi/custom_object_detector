from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import List

@dataclass_json
@dataclass(frozen=True)
class ObjectDetectorConfig:
    model_path:str
    selected_classes: List[int]
    score_threshold:float

