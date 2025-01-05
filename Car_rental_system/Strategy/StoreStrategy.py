from abc import ABC, abstractmethod

class StoreStrategy(ABC):
    @abstractmethod
    def price(self):
        pass