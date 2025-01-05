from sortedcontainers import SortedList


ms = SortedList()
ms.add((10, 3, "s1"))
ms.add((10, 1, "s2"))
ms.add((15, 8, "s3"))
print(ms)


from enum import Enum

class VehicleCategory(Enum):
    TwoWheeler = "TwoWheeler"
    FourWheeler = "FourWheeler"

print(VehicleCategory.TwoWheeler.value)

from enum import Enum

class VehicleType(Enum):
    SUV = "SUV"
    SEDAN = "Sedan"
    HATCHBACK = "Hatchback"
    BIKE = "Bike"
    TRUCK = "Truck"
print(VehicleType.SUV.value)