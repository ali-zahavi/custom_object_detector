from abc import ABC, abstractmethod


class InputStream(ABC):
    def __init__(self, source_type, input_stream_config):
        self.source_type = source_type
        self.input_stream_config = input_stream_config

    @abstractmethod
    def check_input_source_exists(self):
        raise NotImplementedError

    @abstractmethod
    def open(self):
        raise NotImplementedError

    @abstractmethod
    def read_frame(self):
        raise NotImplementedError

    @abstractmethod
    def release(self):
        raise NotImplementedError

