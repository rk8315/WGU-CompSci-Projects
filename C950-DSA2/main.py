import math
import csv
from hashtable import *
from package import *

#TODO:
    # [x] Create hashmap
    # [] Import CSV and read/handle data within
    # [] Populate hashmap with data from CSV
    # [x] Create Look-up Function
    # [] Create GUI (CommandLine Interface)

#region Import CSV Data


with open("C950-DSA2/Data/address_data.csv") as address_data_csv:
    address_data = csv.reader(address_data_csv, delimiter=',')
    # for a in address_data:
    #     print(",".join(a))

with open("C950-DSA2/Data/distance_data.csv") as distance_data_csv:
    distance_data = csv.reader(distance_data_csv, delimiter=',')
    # for d in distance_data:
    #     print(",".join(d))

#endregion Import CSV Data

package_hashtable = Hashtable()

import_package_data("C950-DSA2/Data/package_data.csv", package_hashtable)
print_all_packages(package_hashtable)