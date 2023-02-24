#class for the file "38 object oriented programming"

class Car: #classes are typically capitalized 

    wheels = 4      #this is a class variable and is applied to all objects created with this class. This can be modified whenn calling the class by passing in a different variable, for example Car.wheels = 2 

    def __init__(self,make,model,year,color): #this is a special method that will construct objects for us. We need to define the arguments we can receive when the object is called
        self.make = make        #this is an instance variable
        self.model = model      #this is an instance variable
        self.year = year        #this is an instance variable
        self.color = color      #this is an instance variable

    def drive(self):
        print("This "+self.model+" is driving")

    def stop(self):
        print("This "+self.model+" is stopped")


