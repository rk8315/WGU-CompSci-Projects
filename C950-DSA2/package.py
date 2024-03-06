import csv
from truck import *
from hashtable import *

class Package:
    def __init__(self, ID, address, city, state, zip, deadline, weight, special, status):
        self.ID = ID
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        self.special = special
        self.status = status
        self.time_departed = None
        self.time_delivered = None

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.ID, self.address, self.city, self.state, self.zip, self.deadline, self.weight, self.special, self.status, self.time_delivered)

    # Checks the delivery status of a package compared to a time input
    # Complexity O(1)
    def delivery_status_update(self, check_time, check_truck):
        truck = check_truck
        if self.time_delivered < check_time and check_time > truck.time_departed:
            self.status = "Delivered"
        elif self.time_delivered > check_time and check_time > truck.time_departed:
            self.status = "En route"
        else:
            self.status = "At hub"
    
# Import data from CSV and turn each row into a Package Object 
# Complexity O(n)
def import_package_data(filename, package_hashtable):
    with open(filename) as package_data_csv:
        package_data = csv.reader(package_data_csv, delimiter=',')
        for package in package_data:
            pID = int(package[0])
            pAddress = package[1]
            pCity = package[2]
            pState = package[3]
            pZip = package[4]
            pDeadline = package[5]
            pWeight = package[6]
            pSpecial = package[7]
            pStatus = "WGUPS HUB"
            
            package = Package(pID, pAddress, pCity, pState, pZip, pDeadline, pWeight, pSpecial, pStatus)
            
            package_hashtable.hash_add(pID, package)

# Lookup package information based on user input package ID and time
# Complexity O(n)
def package_lookup(user_package_id, package_hashtable, check_time, check_truck):
    user_package = package_hashtable.hash_lookup(int(user_package_id))
    user_package.delivery_status_update(check_time, check_truck)
    print(f"Package {user_package_id} Details:")
    print(f"\tDelivery Address: {user_package.address} {user_package.city} {user_package.state} {user_package.zip}")
    print(f"\tDelivery Deadline: {user_package.deadline}")
    print(f"\tPackage Weight: {user_package.weight}")
    print(f"\tDelivery Status: {user_package.status}")
    if user_package.status == "Delivered":
        print(f"\tTime Delivered: {user_package.time_delivered}")

# Print all the packages that are in the hashtable
# Complexity O(n)
def print_all_packages_timeframe(end_time, truck_num, package_hashtable):
    for package in truck_num.packages:
        package = package_hashtable.hash_lookup(package)
        package.delivery_status_update(end_time, truck_num)
        if package.status == "Delivered":
            print(f"| Package {package.ID} | {package.status} | {package.time_delivered} |")
        else:
            print(f"| Package {package.ID} | {package.status} |")
