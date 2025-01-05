from VehicleInventoryManager import VehicleInventoryManager
class FWVehicleInventoryManager(VehicleInventoryManager):
    def __init__(self):
        total_vehicles = []
        available_vehicles = []
        booked_vehicles = []
        super().__init__(total_vehicles, available_vehicles, booked_vehicles)
