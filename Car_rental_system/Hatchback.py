from FourWheeler import FourWheeler
from Strategy.HatchbackStrategy import HatchbackStrategy

class Hatchback(FourWheeler):
    def __init__(self, vehicle_no, vehicle_cat, vehicle_name):
        obj = HatchbackStrategy()  # Create the strategy object
        super().__init__(vehicle_no, vehicle_cat, vehicle_name, obj)  # Call the parent constructor