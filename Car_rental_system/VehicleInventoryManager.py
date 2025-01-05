class VehicleInventoryManager:
    def __init__(self, total_vehicles, available_vehicles, booked_vehicles):
        self.total_vehicles = total_vehicles
        self.available_vehicles = available_vehicles
        self.booked_vehicles = booked_vehicles

    def update_vehicle(self, vehicle):
        self.available_vehicles.remove(vehicle)
        self.booked_vehicles.append(vehicle)


