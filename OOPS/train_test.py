import pytest
import os
os.chdir('/Users/dpatibandla/Documents/training_files/')

from oops_train import Vehicle, Car

def test_vehicle_intialization():
    vehicle = Vehicle('Generic Vehicle',40,150)
    assert vehicle.name == 'Generic Vehicle'
    assert vehicle.mileage == 40
    assert vehicle.max_speed == 150

def test_vehicle_info():
    vehicle = Vehicle('Generic Vehicle', 40 , 150)
    assert vehicle.vehicle_info() == "Vehicle name:Generic Vehicle, Mileage:40, Max_speed:150" 

def test_general_info():
    assert Vehicle.general_info() == "This is a:Generic Vehicle"

def test_car_intialization():
    car = Car('Audi',15,250,'Manual')
    assert car.name == 'Audi'
    assert car.mileage == 15
    assert car.max_speed == 250
    assert car.transmission_type == 'Manual'

def test_car_vehicle_info():
    car = Car('Audi',15,250,'Manual')
    assert car.vehicle_info() == "Vehicle name:Audi,Mileage:15,Max_speed:250,Transmission Type:Manual" 

def test_car_seating_capacity_default():
    car = Car('Audi',15,250,'Manual')
    assert car.seating_capacity() == "Seating Capacity of:Audi is 4 passengers"

def test_car_seating_capacity_argument():
    car = Car('Audi',15,250,'Manual')
    assert car.seating_capacity() == "Seating Capacity of:Audi is 4 passengers"

def test_car_num_of_tires():
    assert Car.num_of_tires() == 4

def test_car_general_info():
    assert Car.general_info() == "This is a:Car"