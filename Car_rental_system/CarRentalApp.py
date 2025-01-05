from collections import defaultdict
from VehicleInventoryFactory import VehicleInventoryFactory
from Vehicle import Vehicle 
from Store import Store
from HighCostStore import HighCostStore
from LowCostStore import LowCostStore
from Hatchback import Hatchback
from SUV import SUV
from Sedan import Sedan
from VehicleCategory import VehicleCategory
from VehicleType import VehicleType
from FWVehicleInventoryManager import FWVehicleInventoryManager
from User import User
from sortedcontainers import SortedList
from Booking import Booking
from datetime import datetime, date
import sys

class CarRentalApp:
    def __init__(self):
        self.CityVsStore = defaultdict(list)
        self.user_location = ""
        self.vehicles_dict = {}
        self.users = {}
        self.stores = {}
        self.vehicle_list = SortedList()
        self.booking_id = 0
        self.vim = []
        self.user_id = 0
        self.bookings = {}
        self.initialize()

    def initialize(self):
        self.create_four_wheeler()
        self.create_stores()

    def create_four_wheeler(self):
        vehicle_category = VehicleCategory.FourWheeler.value
        #first set 
        vif = VehicleInventoryFactory()
        vehicle_inventory_manager1 = vif.get_vehicle_inventory_manager(vehicle_category)
        vehicle_1 = SUV("12345", vehicle_category, VehicleType.SUV.value)
        self.vehicles_dict[vehicle_1.vehicle_number] = vehicle_1
        vehicle_2 = Sedan("54321", vehicle_category, VehicleType.SEDAN.value)
        self.vehicles_dict[vehicle_2.vehicle_number] = vehicle_2
        vehicle_3 = Hatchback("75545", vehicle_category, VehicleType.HATCHBACK.value)
        self.vehicles_dict[vehicle_3.vehicle_number] = vehicle_3
        vehicle_inventory_manager1.total_vehicles += [vehicle_1, vehicle_2, vehicle_3]
        vehicle_inventory_manager1.available_vehicles = vehicle_inventory_manager1.total_vehicles

        vehicle_inventory_manager2 = vif.get_vehicle_inventory_manager(vehicle_category)
        vehicle_4 = SUV("88888", vehicle_category, VehicleType.SUV.value)
        self.vehicles_dict[vehicle_4.vehicle_number] = vehicle_4
        vehicle_5 = Sedan("77700", vehicle_category, VehicleType.SEDAN.value)
        self.vehicles_dict[vehicle_5.vehicle_number] = vehicle_5
        vehicle_6 = Hatchback("33344", vehicle_category, VehicleType.HATCHBACK.value)
        self.vehicles_dict[vehicle_6.vehicle_number] = vehicle_6
        vehicle_inventory_manager2.total_vehicles += [vehicle_4, vehicle_5, vehicle_6]
        vehicle_inventory_manager2.available_vehicles = vehicle_inventory_manager2.total_vehicles

        vehicle_inventory_manager3 = vif.get_vehicle_inventory_manager(vehicle_category)
        vehicle_7 = SUV("10000", vehicle_category, VehicleType.SUV.value)
        self.vehicles_dict[vehicle_7.vehicle_number] = vehicle_7
        vehicle_8 = Sedan("20000", vehicle_category, VehicleType.SEDAN.value)
        self.vehicles_dict[vehicle_8.vehicle_number] = vehicle_8
        vehicle_inventory_manager3.total_vehicles += [vehicle_7, vehicle_8]
        vehicle_inventory_manager3.available_vehicles = vehicle_inventory_manager3.total_vehicles
        self.vim += [vehicle_inventory_manager1, vehicle_inventory_manager2, vehicle_inventory_manager3]

    def create_stores(self):
        store_counter = 0
        vehicle_inventory_management1 = self.vim[0]
        store_counter+=1
        low_cost_store = LowCostStore(store_counter, "DELHI", vehicle_inventory_management1)
        self.stores[store_counter] = low_cost_store
        self.CityVsStore["DELHI"].append(low_cost_store)
        vehicle_inventory_management2 = self.vim[1]
        store_counter+=1
        high_cost_store = HighCostStore(store_counter, "DELHI", vehicle_inventory_management2)
        self.stores[store_counter] = high_cost_store
        self.CityVsStore["DELHI"].append(high_cost_store)
        vehicle_inventory_management3 = self.vim[2]
        store_counter+=1
        low_cost_store = LowCostStore(store_counter, "DELHI", vehicle_inventory_management3)
        self.stores[store_counter] = low_cost_store
        self.CityVsStore["DELHI"].append(low_cost_store)


    def log_to_file(self, message):
        file_name = "output_car_rental.py"
        with open(file_name, "a") as f1:
            f1.write(f"{message}\n")

    def user_details(self, user_name, location):
        #ideally first user wi;l register, but im assuning user is coming for the first time so tagging teh location part along with savubg user details to db
        self.user_id+=1
        user = User(self.user_id, user_name, location)
        self.users[user.id] = user
        return "User created Successfully"

    def set_location(self, location):
        self.user_location = location
        return f"{location} set succesfully!"

    def search_vehicle(self, vehicle_name):
        #self.user_location = "DELHI"
        self.vehicle_list = SortedList()
        #get alL the stores with that location
        stores = self.CityVsStore[self.user_location]
        VehicleVsStore = {}
        store_distance = 0
        VehicleVsStore[vehicle_name] = []

        for store in stores:
            #for evrbry store by default dictance will be increased by 2
            store_distance += 2
            vehicles = store.vehicle_inventory_management.total_vehicles
            for v in vehicles:
                if v.vehicle_name == vehicle_name and v.available == True:
                    #print(v.vehicle_name, v.price, store.store_price)
                    v.price += store.store_price
                    #add data to list
                    self.vehicle_list.add((v.price, store_distance, store.store_id, v.vehicle_number))
                    #if we get one vehicle also present in that store, that means that store is applicable
                    VehicleVsStore[vehicle_name].append(store)
                    break

        print(self.vehicle_list)

        return f"list of stores with available car - {vehicle_name} : {self.vehicle_list}"

    def book_vehicle(self, user_id, vehicle_idx, pickup_from, drop, pickup_time, drop_time):
        user = self.users[user_id]
        vehicle_number = self.vehicle_list[vehicle_idx][3]
        vehicle = self.vehicles_dict[vehicle_number]
        store_id = self.vehicle_list[vehicle_idx][2]
        store = self.stores[store_id]
        self.booking_id+=1
        booking = Booking(self.booking_id, user, vehicle, pickup_from, drop, pickup_time, drop_time)
        store.vehicle_inventory_management.update_vehicle(vehicle)
        self.bookings[booking.booking_id] = booking

        return f"booking created with booking id : {self.booking_id}"

    

    def get_store_report(self, store_id):
        store = self.stores[store_id]
        result = {}
        store_available_vehicles = store.vehicle_inventory_management.available_vehicles
        store_booked_vehicles = store.vehicle_inventory_management.booked_vehicles
        result['available_vehicles'] = store_available_vehicles
        result['booked_vehicles'] = store_booked_vehicles

        return f"Station report is as follows - {result}"
        

def main():
    car_rental_app = CarRentalApp()
    #car_rental_app.search_vehicle("SEDAN")
    #sys.exit(0)
    car_rental_app.log_to_file(f"Session started at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    while True:
        user_command = input("\nEnter Command : ").strip().upper()
        command_parts = user_command.split()
        
        command = command_parts[0] if command_parts else ""
        print(f"Command received: {command}")

        if command == "ENTER_USER_DETAILS":
            user_name = str(command_parts[1])
            location = str(command_parts[2])
            message = car_rental_app.user_details(user_name, location)
            car_rental_app.log_to_file(message)

        if command == "ENTER_LOCATION":
            location = str(command_parts[1])
            message = car_rental_app.set_location(location)
            car_rental_app.log_to_file(message)

        if command == "SEARCH_VEHICLE":
            vehicle_name = str(command_parts[1])
            message = car_rental_app.search_vehicle(vehicle_name)
            car_rental_app.log_to_file(message)

        if command == "BOOK_VEHICLE":
            user_id = int(command_parts[1])
            selected_vehicle_idx = int(command_parts[2])
            pickup_from = str(command_parts[3])
            drop = str(command_parts[4])
            pickup_time = str(command_parts[5])
            drop_time = str(command_parts[6])
            message = car_rental_app.book_vehicle(user_id, selected_vehicle_idx, pickup_from, drop, pickup_time, drop_time)
            car_rental_app.log_to_file(message)

        if command == "STATION_REPORT":
            store_id = int(command_parts[1])
            message = car_rental_app.get_store_report(store_id)
            car_rental_app.log_to_file(message)
    

if __name__ == "__main__":
    main()