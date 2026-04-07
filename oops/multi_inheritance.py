#multiple and multi level inheritance

class Animal:
    def __init__(self,name):
        self.name = name

    def eat(self):
        print(f"The {self.name} is eating")

class pray(Animal):
    def flee(self):
        print(f"The {self.name} is fleeing")

class predator(Animal):
    def hunt(self):
        print(f"The {self.name} is hunting")

class Rabbit(pray):
    pass

class Fish(pray,predator):
    pass

class Fox(predator):
    pass

rabbit = Rabbit("Bugs")
fox = Fox("Tony")
fish = Fish("Nemo")


rabbit.eat()
rabbit.flee()

fish.eat()
fish.hunt()
fish.flee()
