from abc import ABC, abstractmethod

class Figure(ABC):
    @abstractmethod
    def area(self):
        pass

    @classmethod
    @abstractmethod
    def name(cls):
        pass
