# methode

class  ParentInfo:

    def EshanFamily ( self,Name,age):
          print(f"My Name is {Name}, My age is {age}")

p1 = ParentInfo()
p1.EshanFamily("anamul", 19)

# ***********************************************************************

# parameterized Constructor
class Family:
    def __init__(self,name , number):
       print(f"My Name is {name}, My age is {number}")

p1 = Family("Anamul", 24)
