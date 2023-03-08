#used to call multiple methods sequentially. each call performs an action on the same object adn returns self

class Car:

    def turn_on(self):
        print("You start the engine")
        return self

    def drive(self):
        print("You drive the car")
        return self

    def brake(self):
        print("You step on the brake")

    def turn_off(self):
        print("You turn off the engine")

car = Car()

#without using method chaining, we would call two actions like this:
car.turn_on()
car.drive()

#with method chaining, we can do this:
car.turn_on().drive() #those "return self" lines are needed in order for this to work


