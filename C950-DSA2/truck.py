class Truck:
    def __init__(self, capacity, avg_speed, miles_driven, packages, current_address, time_departed):
        self.capacity = capacity
        self.avg_speed = avg_speed
        self.miles_driven = miles_driven
        self.packages = packages
        self.current_address = current_address
        self.time_departed = time_departed
        self.time = time_departed


    def __str__(self):
        return "%s, %s, %s, %s, %s, %s" % (self.capacity, self.avg_speed, self.miles_driven, self.packages, self.current_address, self.time)
    
