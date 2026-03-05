a =30 # Global Variable
b =40

def Anamul():
    global a
    a=50
    x=100   # Local Scope ( Declar only under Function )
    print(x)
    print(a)

Anamul()
print(a)