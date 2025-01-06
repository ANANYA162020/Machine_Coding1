from abc import ABC, abstractmethod
class User(ABC):
    def __init__(self, id, name):
        self.id = id
        self.name = name

    
