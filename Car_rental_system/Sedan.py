from FourWheeler import FourWheeler
from Strategy.SedanStrategy import SedanStrategy

class Sedan(FourWheeler):
    def __init__(self, vehicle_no, vehicle_cat, vehicle_name):
        obj = SedanStrategy()  # Create the strategy object
        super().__init__(vehicle_no, vehicle_cat, vehicle_name, obj)  # Call the parent constructor