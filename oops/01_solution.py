class Car:
    total_car = 0
    
    def __init__(self, brand, model):
        
        self.__brand = brand
        self.__model = model
        Car.total_car += 1
        
    def get_brand(self):
        return self.__brand + " !"
    
    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    def fuel_type(self):
        return "petrol or Diesel"
    
    @staticmethod
    def general_description():
        return "Cars are just a means of transport"
    
    @property
    def model(self):
        return self.__model


# --- inheritance---
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    def fuel_type(self):
        return "Electric Charge"
        
my_tesla = ElectricCar("Tesla", "Model S", "85KWH")
print(isinstance(my_tesla, Car))
print(isinstance(my_tesla, ElectricCar))
print(my_tesla.fuel_type())

safari = Car("Tata", "safari")
print(safari.model)


print(Car.general_description()) 

my_car = Car("tata", "defender")
print(my_car.general_description())

# my_car = Car("tata", "defender")
# print(my_car.brand)
# print(my_car.model)


# my_new_car = Car("tata", "safari")
# print(my_new_car.full_name())


class Battery:
    def info(self):
        return "this is battery"

class Engine:
    def Engine_info(self):
        return "this is Engine"


class ElectricCarTwo(Battery, Engine, Car):
    pass

first = ElectricCarTwo("tesla", "model s")
print(first.Engine_info())
print(first.info())

