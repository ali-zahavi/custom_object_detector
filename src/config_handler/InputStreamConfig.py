from dataclasses import dataclass

@dataclass(frozen=True)
class InputStreamConfig:
    images_path: str
    video_path: str