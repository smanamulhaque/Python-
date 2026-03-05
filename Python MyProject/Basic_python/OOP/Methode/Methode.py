class className:
    def InstanceMethode(self):
        print("Hello Instance Methode")

    @classmethod
    def classMethode(cls):
        print("Hello Class Methode")

    @staticmethod
    def StaticMethode():
        print("Hello StaticMethode")

v1 = className()
v1.InstanceMethode()
v1.classMethode()
className.classMethode()
v1.StaticMethode()
className.classMethode()