import csv

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
        self.time_delivered = None

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.ID, self.address, self.city, self.state, self.zip, self.deadline, self.weight, self.special, self.status, self.time_delivered)

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

def print_all_packages(package_hashtable):
    for i in range(1, 41):
        print(package_hashtable.hash_lookup(i)) 
