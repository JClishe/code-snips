#Prevents a user from creating an object of that class, and compels a user to override abstract methods in a child class

#abstract class = a class which contains one or more abstract methods
#abstract method = a method that has a declaration but does not have an implementation

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod #this decorator is telling any child objects that they can't call this method. They could, however, implement their own methods of the same name
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):

    def go(self):
        print("You drive the car")

class Motorcycle(Vehicle):

    def go(self):
        print("You ride the motorcycle")

vehicle = Vehicle()
car = Car()
motorcycle = Motorcycle()

vehicle.go()
car.go()
motorcycle.go()

