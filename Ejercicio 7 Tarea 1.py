class Ejercicio_7:
    def __init__(self):
        pass
    
    def Mayor (self):
        num1, num2, num3=0,0,0
        num1=int(input("Ingrese el 1er número: "))
        num2=int(input("Ingrese el 2do número: "))
        num3=int(input("Ingrese el 3er número: "))
        if num1>num2 and num1>num3:
            print("El número mayor es el primero: ",num1)
        elif num2>num3:
            print("El número mayor es el segundo: ",num2)
        else:
            print("El número mayor es el tercero: ",num3)

nummayor=Ejercicio_7()
nummayor.Mayor()