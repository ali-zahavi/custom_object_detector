from dataclasses import dataclass
from dataclasses_json import dataclass_json

@dataclass_json
@dataclass(frozen=True)
class InputStreamConfig:
    images_path: str
    video_path: str