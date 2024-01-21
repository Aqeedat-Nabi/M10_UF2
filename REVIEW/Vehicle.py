import json

class Vehicle:
    def __init__(self, brand, model, year, color, fuel_type, mileage):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.fuel_type = fuel_type
        self.mileage = mileage

    # Getters and Setters
    def get_make(self):
        return self.brand
    
    def set_make(self, brand):
        self.brand = brand

    def get_model(self):
        return self.model
    
    def set_model(self, model):
        self.model = model

    def get_year(self):
        return self.year
    
    def set_year(self, year):
        self.year = year

    def get_color(self):
        return self.color
    
    def set_color(self, color):
        self.color = color

    def get_fuel_type(self):
        return self.fuel_type
    
    def set_fuel_type(self, fuel_type):
        self.fuel_type = fuel_type

    def get_mileage(self):
        return self.mileage
    
    def set_mileage(self, mileage):
        self.mileage = mileage
        

    def display(self):
        print("Vehicle Information:")
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Color: {self.color}")
        print(f"Fuel Type: {self.fuel_type}")
        print(f"Mileage: {self.mileage} miles \n")

    def to_dict(self):
        return {
            "brand": self.brand,
            "model": self.model,
            "year": self.year,
            "color": self.color,
            "fuel_type": self.fuel_type,
            "mileage": self.mileage
        }

# OBJECT :
vehicle_obj = Vehicle("Toyota", "Camry", 2022, "Blue", "Gasoline", 5000)
vehicle_obj.display()
print()
print(f"Vehicle Information In JSON Format : \n {vehicle_obj.to_dict()}")
