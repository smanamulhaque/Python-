#Short list Acanding order
number = [4,2,1,8,6,9]
eng = ["f","r","a","p","b"]
number.sort()
eng.sort()
print(number)
print(eng)

#Reverse list
num = [1,2,3,4,5,6]
num.sort(reverse= True)
print(num)

# Copy list
A = [1,2,3,4,5,6]
A2 = A.copy()
print(A)
print(A2)

# join list
B = [1,2,3,4]
B1 = [5,6,7,8]
B2 = B+B1
print(B2)

# join list use extend
B.extend(B1)
print(B)

