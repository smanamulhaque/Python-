thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
# #Use pop Key
thisdict.pop("model")
print(thisdict)

#The popitem() method removes the last inserted item The popitem() method removes the last inserted item
thisdict.popitem()
print(thisdict)

#The del keyword removes the item with the specified key name
del thisdict["model"]
print(thisdict)

# The clear() method empties the dictionary
thisdict.clear()
print(thisdict)