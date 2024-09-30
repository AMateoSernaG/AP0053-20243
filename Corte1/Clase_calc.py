class Ini:
    def __init__(self, val):
        self.val = val

    def getval(self):
        print("Calculadora por Mateo Serna")
        return self.val * self.val


class Add_Sub:
    def __init__(self):
        self.a = 0
        self.b = 0
        self.r = 0

    # Método para ingresar operandos
    def ingresar_operandos(self):
        self.a = float(input("Ingrese el primer operando: "))
        self.b = float(input("Ingrese el segundo operando: "))

    # Operaciones matemáticas
    def sumar(self):
        self.r = self.a + self.b

    def restar(self):
        self.r = self.a - self.b

    def multiplicar(self):
        self.r = self.a * self.b

    def dividir(self):
        if self.b != 0:
            self.r = self.a / self.b
        else:
            print("Error: No se puede dividir entre 0.")
            return

    # Método para imprimir el resultado
    def imprimir_resultado(self):
        print("Resultado = ", self.r)

    # Método que ejecuta el flujo completo de la calculadora
    def ejecutar(self):
        while True:
            print("\nSeleccione una operación:")
            print("1. Sumar")
            print("2. Restar")
            print("3. Multiplicar")
            print("4. Dividir")
            print("5. Salir")
            
            opcion = input("Opción: ")

            if opcion == '5':
                break

            self.ingresar_operandos()

            if opcion == '1':
                self.sumar()
            elif opcion == '2':
                self.restar()
            elif opcion == '3':
                self.multiplicar()
            elif opcion == '4':
                self.dividir()
            else:
                print("Opción no válida")

            self.imprimir_resultado()
