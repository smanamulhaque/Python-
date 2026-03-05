# ABC → Abstract Base Class
# @abstractmethod → method declare করা হয় কিন্তু body থাকে না
# Child class (Dog, Cat) → method implement করে

from abc import ABC, abstractmethod

# Abstract Class
class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass


# Child Class
class Dog(Animal):
    def sound(self):
        print("Dog barks")


# Child Class
class Cat(Animal):
    def sound(self):
        print("Cat meows")


d = Dog()
d.sound()

c = Cat()
c.sound()