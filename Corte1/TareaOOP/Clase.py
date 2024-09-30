class Square:
    def __init__(self,val):
        self.val=val
    def getval(self):
        return self.val*self.val
    
class Add_Sub:
    a=0
    b=0
    r=0

    def add(self, a, b):
        self.r = a + b
    def sub(self, a, b):
        self.r = a - b
    def imprimirResultado(self):
        print("Resultado = ",self.r)