class baba :
    car = "BMW"
    tk = "100cr"
    Home = "10 floor"

class son1(baba):
    webcam = "ssss"
    Pc = "1cr"
    House = "1 floor"

class son2(son1) :
    airbuds = "Apple"
    laptop = "Apple"
    iphon = "17"

class son3(son2):
    BrokenHome = ""
    Brokrnphon = ""

k = son3()
print(k.car)
print(k.Pc)
