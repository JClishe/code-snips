#objects are a combination of attributes (what an object is or has) and methods (what an object can do)
#classes describe the attributes and methods that an object has
#if classes are large, may want to create them in a seperate file
#this file is using the car.py file

from car import Car

car_1 = Car("Chevy","Corvette",2021,"blue")
car_2 = Car("Ford","Mustang",2022,"red")

print(car_1.make)
print(car_1.model)
print(car_1.year)
print(car_1.color)

print(car_1.wheels)

car_1.drive()
car_1.stop()







