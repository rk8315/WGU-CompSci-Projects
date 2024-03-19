import csv  
import os

#region CSV Imports
current_dir = os.getcwd()
address_data_csv = 'address_data.csv'
distance_data_csv = 'distance_data.csv'
address_file_path = os.path.join(current_dir, address_data_csv)
distance_file_path = os.path.join(current_dir, distance_data_csv)

# Open the CSV files in read mode
with open(address_file_path, 'r') as address_file:
    # Create a CSV reader object
    address_data = csv.reader(address_file)
    address_data = list(address_data)

with open(distance_file_path, 'r') as distance_file:
    # Create a CSV reader object
    distance_data = csv.reader(distance_file)
    distance_data = list(distance_data)
#endregion CSV Imports

# Find and return distance between two addresses from the distance CSV
# Complexity O(1)
def distance_between_addresses(x, y):
    distance = distance_data[x][y]
    if distance == '':
        distance = distance_data[y][x]

    return float(distance)

# Get an address as int from a given address from address CSV
# Complexity O(n)
def get_address(address):
    for row in address_data:
        if address in row[2]:
            return int(row[0])
    