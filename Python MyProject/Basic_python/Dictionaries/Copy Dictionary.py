thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
print("\n")
#Make a copy of a dictionary with the copy() method:
mydic = thisdict.copy()
print(mydic)

print("\n")
#nother way to make a copy is to use the built-in function dict()
mydic1=dict(thisdict)
print(mydic1)