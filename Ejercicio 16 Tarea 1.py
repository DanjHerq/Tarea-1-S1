class Ejercicio_16:
    def __init__(self):
        pass
    
    def Factorial (self):
        number=int(input("Por favor, indique la cantidad de números que ingresará: "))
        for i in range(number):
            numero=int(input("Ingrese un número: "))
            f=1
            for num in range(numero,0,-1):
                f=f*num
            
            print("El factorial del numero {} es de: {}".format(numero,f))

buanidado=Ejercicio_16()
buanidado.Factorial()