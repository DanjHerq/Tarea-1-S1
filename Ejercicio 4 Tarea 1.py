class Ejercicio_4:
    def __init__(self):
        pass
    
    def Notafinal (self):
        nota=0
        nota=float(input("Por favor, ingrese su calificación: "))
        if nota>=7:
            print("Felicidades, has aprobado sigue así")
        else:
            print("Lamentablemente no has aprobado, sigue estudiando")
            
examen= Ejercicio_4()
examen.Notafinal()