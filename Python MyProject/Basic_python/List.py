li = [1,2,3]
print(li)
print(li[0])
print(type(li))
li[1]=10
print(li)
lis = ["anamul","haque","Shown","jakaria"]
print(type(lis))
print(lis)

List = [True,False,True,True]
print(List)
print(type(List))

# Access list items
lis = ["anamul","haque","Shown","jakaria"]
print(type(lis))
print(lis[2])

#change list item
lis = ["anamul","haque","Shown","jakaria"]
print(lis)
lis[2]="Sheikh"
print(lis)

# append(item add last side )
lis.append(10)
print(lis)

# insert ( item add any place but any item can,t remove )
lis.insert(0,100)
lis.insert(2,"Aziz")
print(lis)

#Remove item list(Remove specific part)
lis.remove("haque")
print(lis)
# Remove Index
lis.pop(1)
print(lis)
# del use delete specific index
del lis[0]
print(lis)

# The clear() method empties the list
lis.clear()
print(lis)


