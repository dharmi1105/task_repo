# Task 2 inheriting a class and showing example of overriding and overloading
#Created a class
class Course:
    course = 'ML'                     #These are class variables
    college = 'Techno'
    def picking(self):
       self.value = 'Parent Class'

class Student(Course):                   #Inherited class
    course = 'Data'                      #Overriding the method by declaring a class variable in child class by declaring and calling the same method
    def __init__(self,name,roll_no,gender):
        self.name = name
        self.roll_no = roll_no
        self.gender = gender    
    def picking(self):
        print('{} picked the course {}'.format(self.name, self.course))
        super().picking()
        
std1 = Student('Amy',123,'Female')
std2 = Student('Rambo',156,'Male')

print(std1.name,'\n',std1.roll_no,'\n',std1.gender)
std1.picking()                                              

print(std2.name,'\n',std2.roll_no,'\n',std2.gender,)
std2.picking()