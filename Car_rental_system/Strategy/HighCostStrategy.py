from Strategy.StoreStrategy import StoreStrategy  # Importing the CarStrategy class

class HighCostStrategy(StoreStrategy):
    def price(self):
        return 4