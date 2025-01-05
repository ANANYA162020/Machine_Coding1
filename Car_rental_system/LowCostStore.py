from Store import Store 
from Strategy.LowCostStrategy import LowCostStrategy

class LowCostStore(Store):
    def __init__(self, store_id, store_location, vehicle_inventory_management):
        obj1 = LowCostStrategy()
        super().__init__(store_id, store_location, vehicle_inventory_management, obj1)