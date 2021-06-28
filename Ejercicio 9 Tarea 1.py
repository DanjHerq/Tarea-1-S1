class Ejercicio_9:
    def __init__(self):
        pass
    
    def OperadorAND (self):
        nota1, nota2=0,0
        nota1=float(input("Ingrese la nota del 1er examen: "))
        nota2=float(input("Ingrese la nota del 2do examen: "))
        if nota1>=80 and nota2>=80:
            print("Felicidades, has sido aceptado")
        else:
            print("Lamentablemente has sido rechazado")
    
    def OperadorOR (self):
        nota1, nota2=0,0
        nota1=float(input("Ingrese la nota del 1er examen: "))
        nota2=float(input("Ingrese la nota del 2do examen: "))
        if nota1>=90 or nota2>=90:
            print("Felicidades has sido aceptado")
        else:
            print("Lamentablemente has sido rechazado")
            
operador1=Ejercicio_9()
operador1.OperadorAND()
operador2=Ejercicio_9()
operador2.OperadorOR()