#creating a class, constructor and functions
#create a class
class Vehicle:
    def __init__(self,name,type,color):          #constructor and instance variables
        self.name = name
        self.type = type
        self.color = color
    
    def max_speed(speed):                             #function
        print('The max speed is: ',speed)

v = Vehicle('BMW','Automatic','Red')              
print(v.name,v.color,v.type)
Vehicle.max_speed(180)
