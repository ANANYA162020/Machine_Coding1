from abc import ABC, abstractmethod

class CarStrategy(ABC):
    @abstractmethod
    def price(self):
        pass
