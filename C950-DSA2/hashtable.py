class Hashtable:
    # Constructor for hashtable, establish size of 10 cells
    def __init__(self, size=10):
        self.table = []
        for i in range(size):
            self.table.append([])

    # Adds new items to hashtable, checks for existing key to update
    def hash_add(self, key, item):
        cell = hash(key) % len(self.table)
        cell_list = self.table[cell]

        for key in cell_list:
            if key[0] == key:
                key[1] = item
            return True

        key_value = [key, item]
        cell_list.append(key_value)
        return True

    # Searches hashtable based on key, returns value if exists or return None
    def hash_lookup(self, key):
        cell = hash(key) % len(self.table)
        cell_list = self.table[cell]

        for key_value in cell_list:
            if key_value[0] == key:
                return key_value[1]
        return None

    # Deletes key/value from hashtable based on key hash
    def hash_delete(self, key):
        cell = hash(key) % len(self.table)
        cell_list = self.table[cell]

        for key in cell_list:
            if key[0] == key:
                cell.remove([key[0],key[1]])
