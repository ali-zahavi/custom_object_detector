from abc import ABC, abstractmethod


class InputStream(ABC):
    def __init__(self, source_type):
        self.source_type = source_type
        self.cap = None

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

