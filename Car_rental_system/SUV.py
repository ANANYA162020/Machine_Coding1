from FourWheeler import FourWheeler
from Strategy.SuvStrategy import SuvStrategy

class SUV(FourWheeler):
    def __init__(self, vehicle_no, vehicle_cat, vehicle_name):
        obj = SuvStrategy()  # Create the strategy object

        super().__init__(vehicle_no, vehicle_cat, vehicle_name, obj)  # Call the parent constructor
