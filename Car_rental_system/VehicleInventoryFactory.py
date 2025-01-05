from Vehicle import Vehicle
from FWVehicleInventoryManager import FWVehicleInventoryManager
class VehicleInventoryFactory:
    def get_vehicle_inventory_manager(self, vehicle_category):
        if vehicle_category == "TwoWheeler":
            pass

        if vehicle_category  == "FourWheeler":
            fwv = FWVehicleInventoryManager()
            return fwv

