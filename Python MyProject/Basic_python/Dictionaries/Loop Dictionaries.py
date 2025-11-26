thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

#Print all key names in the dictionary, one by one
for i in thisdict:
    print(i)

print("\n")
#Print all values in the dictionary, one by one:
for i in thisdict:
    print(thisdict[i])

print("\n")
#You can use the keys() method to return the keys of a dictionary:
for x in thisdict.values():
  print(x)

print("\n")
#Loop through both keys and values, by using the items() method
for x,y in thisdict.items():
    print(x,y)

print("\n")
#You can use the keys() method to return the keys of a dictionary
for x in thisdict.keys():
  print(x)


