# StudentID: 011818662

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
    
print("\n" + "#" * 59)
print("# The Western Governors University Parcel Service (WGUPS) #")
print("#" * 59 + "\n")


package_hashtable = Hashtable()

import_package_data("C950-DSA2/Data/package_data.csv", package_hashtable)
print_all_packages(package_hashtable)
