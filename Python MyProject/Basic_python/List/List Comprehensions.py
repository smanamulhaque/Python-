'''
# Use for loop
num = [1,2,3,4,5]
for i in num:
    print(i* 2)
'''

# use Comprehensions
num = [1,2,3,4,5]
double= [i * 2 for i in num]
double1= [i + 2 for i in num]
double2= [i / 2 for i in num]
print(double)
print(double1)
print(double2)

# print([i * 2 for i in num])
