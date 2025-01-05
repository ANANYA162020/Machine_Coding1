# In Strategy/SuvStrategy.py
from Strategy.CarStrategy import CarStrategy  # Importing the CarStrategy class

class SuvStrategy(CarStrategy):
    def price(self):
        return 10
