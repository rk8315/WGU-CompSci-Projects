# StudentID: 011818662
# StudentName: Robert Kearns

import datetime
from distance_calc import *
from hashtable import *
from package import *
from truck import *

# Algorithm function to deliver packages. Concept usues the nearest neighbor algorithm
# Compare the packages on the truck to find the package with the closest distance of 
# where the truck is currently. Adds mileage and time based on distance traveled to deliver
# the package.
# Complexity O(n^2)
def deliver_packages(truck):
    # Store packages on a given truck into a list 
    on_truck = []
    for pID in truck.packages:
        package = package_hashtable.hash_lookup(pID)
        on_truck.append(package)

    truck.packages.clear()

    # Check while there are packages on the truck, perform delivery by calculating distance/time and removing delivered packages
    while 0 < len(on_truck): 
        # set a initial value that all packages is less than
        next_delivery_distance = 8000
        next_delivery = None

        # find the package that has the least amount of distance from trucks current location
        for package in on_truck:
            if distance_between_addresses(get_address(truck.current_address), get_address(package.address)) < next_delivery_distance:
                next_delivery_distance = distance_between_addresses(get_address(truck.current_address), get_address(package.address))
                next_delivery = package
        truck.packages.append(next_delivery.ID)
        on_truck.remove(next_delivery)

        # Calculate distance and time traveled by the truck
        truck.miles_driven += next_delivery_distance
        truck.current_address = next_delivery.address
        truck.time += datetime.timedelta(hours=next_delivery_distance / 18)
        next_delivery.time_delivered = truck.time
        next_delivery.time_departed = truck.time_departed

# Instantiate a Hashtable object and populate it with Package objects from the package data CSV
package_hashtable = Hashtable()
import_package_data("C950-DSA2/Data/package_data.csv", package_hashtable)

# Instantiate three Truck objects and manually place packages into each based on special notes on packages and proximity
truck1 = Truck(16, 18, 0.0, [1, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40], "4001 South 700 East", datetime.timedelta(hours=8)) # 13pkg leaves at 8:00am
truck2 = Truck(16, 18, 0.0, [2, 3, 4, 5, 6, 7, 8, 10, 11, 18, 25, 28, 32, 33, 36, 38], "4001 South 700 East", datetime.timedelta(hours=9, minutes=5))   # 16pkg leaves at 9:05am
truck3 = Truck(16, 18, 0.0, [9, 12, 17, 21, 22, 23, 24, 26, 27, 35, 39], "4001 South 700 East", datetime.timedelta(hours=10, minutes=20)) # 11pkg, leaves at 10:20am

# Perform deliveries of each truck, calculate total distance of all trucks
deliver_packages(truck1)
deliver_packages(truck2)
deliver_packages(truck3)
total_miles_driven = truck1.miles_driven + truck2.miles_driven + truck3.miles_driven

# User interface
print("\n" + "#" * 59)
print("# The Western Governors University Parcel Service (WGUPS) #")
print("#" * 59 + "\n")

# Requirement E - display the total mileage of each truck and combined mileage
print("-" * 16 + "Total Mileage by All Trucks" + "-" * 16)
print(f"\tTruck1 Total Mileage: {truck1.miles_driven}")
print(f"\tTruck2 Total Mileage: {truck2.miles_driven}")
print(f"\tTruck3 Total Mileage: {truck3.miles_driven}")
print(f"\tAll Trucks Total Mileage: {total_miles_driven}")
print("-" * 59 + "\n")

# Ask user to search for individual packages or all
print("Select delivery status view:")
print("(1) Individual Package status (Package ID)")
print("(2) View all package/truck status in at a specific time")
user_view_input = input("\t")

if user_view_input == "1":
    print("Enter the Package ID to lookup: ")
    user_package_id = input("\t")

    print("Define a time to filter delivery status (HH:MM:SS)")
    user_time_input = input("\t")
    (hour, minute, second) = user_time_input.split(":")
    check_time = datetime.timedelta(hours=int(hour), minutes=int(minute),seconds=int(second))

    # Verify which truck a package is in to update the status if At hub, en route, or delivered
    if (user_package_id) in truck1.packages:
        check_truck = truck1
    elif int(user_package_id) in truck2.packages:
        check_truck = truck2
    elif int(user_package_id) in truck3.packages:
        check_truck = truck3

    # Lookup package from user input package ID
    package_lookup(user_package_id, package_hashtable, check_time, check_truck )   

elif user_view_input == "2":
    print("Define a time to filter delivery status (HH:MM:SS)")
    check_time = input("\t")
    (cHour, cMinute, cSecond) = check_time.split(":")
    check_time = datetime.timedelta(hours=int(cHour), minutes=int(cMinute),seconds=int(cSecond))

    # Calculate and print delivery status of each package based on user input time
    print(f"Delivery Status for {check_time}")
    print(f"Truck1")
    print_all_packages_timeframe(check_time,truck1,package_hashtable)
    print(f"\nTruck2")
    print_all_packages_timeframe(check_time, truck2, package_hashtable)
    print(f"\nTruck3")
    print_all_packages_timeframe(check_time, truck3, package_hashtable)

else:
    print("Invalid input, run program again")
