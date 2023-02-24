#classes cann be contained inside of other classes. Child classes will inherit all variables and methods of its parent class. In this way, common code only needs to be typed once, and changes only need to made once
#list anything that all classes have in common within the parent class. List unique attributes within the child class

class Animal:

    alive = True

    def eat(self):
        print("This animal is eating")

    def sleep(self):
        print("This animal is sleeping")

class Rabbit(Animal): #rabbit is the child class while animal is the parent class. 
    
    def run(self):
        print("This rabbit is running")

class Fish(Animal):
    
    def swim(self):
        print("This fish is swimming")

class Hawk(Animal):
    
    def fly(self):
        print("This hawk is flying")

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

print(rabbit.alive)
fish.eat()
hawk.sleep()

rabbit.run()
fish.swim()
hawk.fly()



