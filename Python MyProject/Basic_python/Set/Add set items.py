# ADD Set items use
Myset1 = { "Anamul","Haque","Sheikh"}
Myset1.add("MD")
print(Myset1)

# The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.)
Myset2 = {1,2,3}

Myset1.update(Myset2)
print(Myset1)     