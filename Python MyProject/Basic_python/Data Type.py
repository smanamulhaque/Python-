# int type data
# float are same
from enum import nonmember

Anam = 420
print(Anam)
print(type(Anam))
# complex are  have must be j
Anam1 = 420j
print(type(Anam1))

# String type you know
yourName = 'Anamul'
myName = "Haque"

print(yourName+' '+myName)

# Bool type data
Bool =True
Bool1 = False
print(Bool)
print(Bool1)

x=8
y=10
print(x>y)

# Binary type data Byte--------
# Byte can,t changeable
# image related work for we can use byte
x_list = {1,2,3,4,5,6,255}
b = bytes(x_list)
print(type(b))

# Binary type data Bytearray--------
# Bytearray are changeable
Y_list = {1,2,3,4,5,6,255}
b1 = bytearray(Y_list)
b1[1] = 100
print(b1[1])
print(type(b1))


# None Type data
# None = NUll value
x = None
print(type(x))

#Squer brackets []
#Parentheses ()
#Curly brackets {}

#list type data
# list is changeable
li = ['Anamul','Haque','Shown','Jakaria']
print(li)
li[1]='Aziz'
print(li)
print(type(li))

#Triple Type data
#Triple can,t changeable
tr = ('apple','banana','cherry')
print(tr)

#Range Type data
ran =range(6)
print(ran)
for i in ran:
 print(i)









