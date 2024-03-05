import csv  

#region CSV Imports
with open("C950-DSA2/Data/address_data.csv") as address_data_csv:
    address_data = csv.reader(address_data_csv, delimiter=',')
    address_data = list(address_data)

with open("C950-DSA2/Data/distance_data.csv") as distance_data_csv:
    distance_data = csv.reader(distance_data_csv, delimiter=',')
    distance_data = list(distance_data)
#endregion CSV Imports

# Find and return distance between two addresses from the distance CSV
def distance_between_addresses(x, y):
    distance = distance_data[x][y]
    if distance == '':
        distance = distance_data[y][x]

    return float(distance)

# Get an address as int from a given address from address CSV
def get_address(address):
    for row in address_data:
        if address in row[2]:
            return int(row[0])
    





## Test is distance between "Redwood Park 3060 Lester St" and "International Peace Gardens 1060 Dalton Ave S"
## returns 3.0
# test_distance = distance_between_addresses(1, 13)
# print(test_distance)
## Test search for address number and return its index
# test_address = get_address("1060")
# print(test_address)