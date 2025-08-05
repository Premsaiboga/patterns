# Create a parent class name Vehicle and create 3 child classes to inherit the properties of parent class.
# Parent class
class Vehicle:
    def __init__(self, year, engine_type):
        self.year = year
        self.engine_type = engine_type

    def display_info(self):
        print(f"Year: {self.year}, Engine Type: {self.engine_type}")

# Child class 1
class Bike(Vehicle):
    def __init__(self, year, engine_type, cc):
        super().__init__(year, engine_type)
        self.cc = cc

    def display_bike_info(self):
        self.display_info()
        print(f"Bike CC: {self.cc}")

# Child class 2
class Car(Vehicle):
    def __init__(self, year, engine_type, pistons):
        super().__init__(year, engine_type)
        self.pistons = pistons

    def display_car_info(self):
        self.display_info()
        print(f"Car Pistons: {self.pistons}")

# Child class 3
class HeavyDutyVehicle(Vehicle):
    def __init__(self, year, engine_type, load_capacity):
        super().__init__(year, engine_type)
        self.load_capacity = load_capacity

    def display_heavy_vehicle_info(self):
        self.display_info()
        print(f"Load Capacity: {self.load_capacity} tons")

# Example usage
bike1 = Bike(2022, "Petrol", 150)
bike1.display_bike_info()

car1 = Car(2021, "Diesel", 4)
car1.display_car_info()

truck1 = HeavyDutyVehicle(2020, "Diesel", 15)
truck1.display_heavy_vehicle_info()

        

        