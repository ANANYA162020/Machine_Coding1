class Store:
    def __init__(self, store_id, store_location, vehicle_inventory_management, obj):
        self.store_id = store_id
        self.store_location = store_location
        self.vehicle_inventory_management = vehicle_inventory_management
        self.obj = obj
        self.store_price = self.get_store_wise_price()

    def get_store_wise_price(self):
        self.store_price = self.obj.price()
        return self.store_price

    