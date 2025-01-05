class Vehicle:
    def __init__(self, vehicle_number, vehicle_cat, vehicle_name, obj):
        self.vehicle_number = vehicle_number
        self.vehicle_cat = vehicle_cat
        self.vehicle_name = vehicle_name
        self.available = True
        self.obj = obj
        self.price = self.get_price()

    def get_price(self):
        self.price = self.obj.price()
        return self.price

    