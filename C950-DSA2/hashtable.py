# CITATION: 
    # C950-Webinar-1-Let's Go Hashing 
    # W-1_ChainingHashTable_zyBooks_Key-Value.py
    # Ref: zyBooks: Figure 7.8.2: Hash table using chaining.
class Hashtable:
    # Constructor for hashtable, establish size of 10 cells
    def __init__(self, size=10):
        self.table = []
        for i in range(size):
            self.table.append([])

    # Adds new items to hashtable, checks for existing key to update
    # Complexity O(n)
    def hash_add(self, key, item):
        cell = hash(key) % len(self.table)
        cell_list = self.table[cell]

        for kv in cell_list:
            if kv[0] == key:
                kv[1] = item
                return True

        key_value = [key, item]
        cell_list.append(key_value)
        return True

    # Searches hashtable based on key, returns value if exists or return None
    # Complexity O(n)
    def hash_lookup(self, key):
        cell = hash(key) % len(self.table)
        cell_list = self.table[cell]

        for kv in cell_list:
            if kv[0] == key:
                return kv[1]
        return None

    # Deletes key/value from hashtable based on key hash
    # Complexity O(n)
    def hash_delete(self, key):
        cell = hash(key) % len(self.table)
        cell_list = self.table[cell]

        for kv in cell_list:
            if kv[0] == key:
                cell.remove([kv[0],kv[1]])
