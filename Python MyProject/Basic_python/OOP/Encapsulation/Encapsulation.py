class Student:

    def __init__(self, name, age):
        self.name = name
        self.__age = age   # private variable

    def show(self):
        print("Name:", self.name)
        print("Age:", self.__age)


s1 = Student("Anamul", 22)
s1.show()