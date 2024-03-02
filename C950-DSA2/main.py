# StudentID: 011818662
# StudentName: Robert Kearns

import datetime

from distance_calc import *
from hashtable import *
from package import *
from truck import *

#TODO:
    # [x] Create hashmap
    # [x] Import CSV and read/handle data within
    # [x] Populate hashmap with data from CSV
    # [x] Create Look-up Function
    # [] calculate distances, times
    # [] Create algorithm
    # [] Create GUI (CommandLine Interface)

package_hashtable = Hashtable()

import_package_data("C950-DSA2/Data/package_data.csv", package_hashtable)

truck1 = Truck(16, 18, 0.0, [1, 13, 14, 15, 16, 20, 29, 30, 31, 34, 37, 40], "4001 South 700 East", datetime.timedelta(hours=8)) # 15pkg leaves at 8:00am
truck2 = Truck(16, 18, 0.0, [2, 4, 5, 6, 7, 8, 9, 10, 11, 25, 28, 32, 33], "HUB", datetime.timedelta(hours=9, minutes=20))   # 13pkg leaves at 9:05am
truck3 = Truck(16, 18, 0.0, [3, 12, 17, 18, 19, 21, 22, 23, 24, 26, 27, 35, 36, 38, 39], "HUB", datetime.timedelta(hours=10, minutes=20)) # 12pkg, leaves at 10:20am

print("\n" + "#" * 59)
print("# The Western Governors University Parcel Service (WGUPS) #")
print("#" * 59 + "\n")

#print_all_packages(package_hashtable)


def deliver_packages(truck):
    on_truck = []
    for pID in truck.packages:
        package = package_hashtable.hash_lookup(pID)
        on_truck.append(package)
    
    truck.packages.clear()
    # check while there are packages on the truck
    while 0 < len(on_truck): 
        next_delivery_distance = 8000
        next_delivery = None
        for package in on_truck:
            if distance_between_addresses(get_address(truck.current_address), get_address(package.address)) < next_delivery_distance:
                next_delivery_distance = distance_between_addresses(get_address(truck.current_address), get_address(package.address))
                next_delivery = package
        truck.packages.append(next_delivery.ID)
        on_truck.remove(next_delivery)
        truck.miles_driven += next_delivery_distance
        truck.current_address = next_delivery.address
        truck.time += datetime.timedelta(hours=next_delivery / 18)


deliver_packages(truck1)
