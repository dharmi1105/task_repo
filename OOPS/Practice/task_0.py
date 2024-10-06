
# Creating a vehicle class with instance attributes

class Vehicle:
    def __init__(self,name,mileage,max_speed):
        self.name = name
        self.mileage = mileage
        self.max_speed = max_speed

    def fuel_type():
        print('It is an Automatic')

# Creating a child class Bus that will inherit all of the variables and methods of the Vehicle class
class Bus(Vehicle):
    def __init__(self, name, mileage, max_speed):
        super().__init__(name, mileage, max_speed)

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"



#Create a class and override the method

class Car(Vehicle):
    def __init__(self, name, mileage, max_speed):
        super().__init__(name, mileage, max_speed)

    def fuel_type(self):
        # TODO: Add docstring
        """
        This method specifies that the vehicle uses a manual transmission
        """
        print('It is a manual')


    def num_tires():
        print(f"Tires are: {5}")


if __name__ == "__main__":

    School_bus = Bus('Volvo',40,100)
    print(School_bus.name,School_bus.mileage,School_bus.max_speed)

    car = Car('Ferrari',10,200) 
    print(car.name, car.mileage, car.max_speed)
    car.fuel_type()
    Car.num_tires()