
# তিনটা class আছে (Bird, Dog, Cat)
# তিনটাতেই same method name → sound()
# কিন্তু output আলাদা
# এই same method name but different behavior = Polymorphism

class Bird:
    def sound(self):
        print("Bird makes sound")

class Dog:
    def sound(self):
        print("Dog barks")

class Cat:
    def sound(self):
        print("Cat meows")


b = Bird()
d = Dog()
c = Cat()

b.sound()
d.sound()
c.sound()
print("\n\n\nn")

# **************************************************************************
class vehicle:
     def __init__(self,model,brand,component ):
         self.model = model
         self.brand = brand
         self.component= component


class plane(vehicle):
    pass

class car (vehicle):
     pass

p1=plane ("b023","SM","All")
c1=car("s2323","er","www3")
print(p1.model)
print(p1.model,p1.brand,c1.brand)