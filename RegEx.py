import re


#Find all lower case characters alphabetically between "a" and "m":
text = "The rain in spain"
# pattern = "[a-z]"
# a = re.findall(pattern,text)
a = re.findall("[a-m]",text)
print(a)



#check if string start with hello
text1 = "hello planet"
x = re.findall("^hello",text1)
if x:
    print("yes the string start with hello")
else:
    print("No mach")

