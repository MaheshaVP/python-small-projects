#inheritance

class Animal:
    def __init__(self,name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Cat(Animal):
    def speek(self):
        print("meow")

class Dog(Animal):
    def speek(self):
        print("woof")

class Mouse(Animal):
    def speek(self):
        print("sqeek")

cat = Cat("scooby")
dog = Dog("Garfield")
mouse = Mouse("mickey")

print(cat.name)
print(cat.is_alive)
cat.speek()
cat.eat()
cat.sleep()

print("\n")

print(dog.name)
print(dog.is_alive)
dog.speek()
dog.eat()
dog.sleep()