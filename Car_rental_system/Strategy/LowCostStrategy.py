from Strategy.StoreStrategy import StoreStrategy  # Importing the CarStrategy class

class LowCostStrategy(StoreStrategy):
    def price(self):
        return 2