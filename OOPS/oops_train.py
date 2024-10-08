class Vehicle:
    #class varaible
    vehicle_type = "Generic Vehicle"

    def __init__(self,name,mileage,max_speed):
        """

        Constructor to initialize instance objects

        :parameter name: The name of the vehicle
        :parameter mileage: The mileage of the vehicle
        :parameter max_speed: The Maximum speed of the vehicle
        """
        self.name = name
        self.mileage = mileage
        self.max_speed = max_speed

    def vehicle_info(self):
        """
        Instance method to display vehicle details.
        
        :return: A string representing the vehicle information
        """
        return(f"Vehicle name:{self.name}, Mileage:{self.mileage}, Max_speed:{self.max_speed}")
    
    @classmethod
    def general_info(cls):
        """
        Class method to display the general information about the vehicle.

        :return: A string representing the type of vehicle
        """
        return(f"This is a :{cls.vehicle_type}")
    
class Car(Vehicle):
    #class variables for the child class
    vehicle_type = "Car"
    num_tires = 4

    def __init__(self, name, mileage, max_speed,transmission_type):
        """
        Constructor to initialize the car class

        :parameter name: The name of the car
        :parameter mileage: The mileage of the car
        :parameter max_speed: The maximum speed of the car
        :parameter transmission_type: The transmission type of the car
        """
        super().__init__(name, mileage, max_speed)
        self.transmission_type = transmission_type

    #overriding the vehicle_info method
    def vehicle_info(self):
        """
        overriding to display the vehicle information including transmission type

        :return: A string representing the car information 

        """

        return(f"Vehicle name:{self.name}, Mileage:{self.mileage}, Max_speed:{self.max_speed},Transmission Type:{self.transmission_type}")
    
    #Method overloading - like behavior using default arguments
    def seating_capacity(self, capacity =4):
        """
        Method to display seating capacity. default is 4 passengers

        :param capacity: The seating capacity of the car
        :return: A string representing the seating capacity
        """

        return(f"Seating capacity of: {self.name} is {capacity} passengers")
    
    @classmethod
    def num_of_tires(cls):
        """
        Method to display No of tires.

        :return: representing the no of tires
        """

        return cls.num_tires
    
    @classmethod
    def general_info(cls):
        """
        overridden Class method to display specific information about the car class.

        :return: A string representing the type of vehicle(car).
        """
        return(f"This is a :{cls.vehicle_type}")
    

if __name__ == "__main__":

    #Instance of a vehicle
    vehicle = Vehicle('General Vehicle',40,150)
    print(vehicle.vehicle_info())
    print(vehicle.general_info())

    #Instance of a car
    car = Car('AUDI',15,250,'Manual')
    print(car.vehicle_info())
    print(car.seating_capacity()) #default argument
    print(car.seating_capacity(6)) #Method with overloading the argument

    #calling class-only functions for the car class
    print(Car.general_info())
    print(f"Tires are :{Car.num_of_tires()}")