from Store import Store 
from Strategy.HighCostStrategy import HighCostStrategy

class HighCostStore(Store):
    def __init__(self, store_id, store_location, vehicle_inventory_management):
        obj1 = HighCostStrategy()
        super().__init__(store_id, store_location, vehicle_inventory_management, obj1)