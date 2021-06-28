class Ejercicio_14:
    def __init__(self):
        pass
    
    def Numeroprimo (self):
        i=1
        divisores=0
        num=int(input("Por favor, ingrese un número: "))
        while i<=num:
            if num%i==0:
                divisores+=1
            i+=1
        if divisores==2:
            print("El numero {} que ingreso si es primo ".format(num))
        else:
            print("El numero {} que ingreso no es primo ".format(num))
            
primo=Ejercicio_14()
primo.Numeroprimo()