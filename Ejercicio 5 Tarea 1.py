class Ejercicio_5:
    def __init__(self,limite=600):
        self.sueldo=limite
    
    def Aumento (self):
        sueldoinicial, porcentaje=0,0.1
        sueldoinicial=int(input("Por favor, ingrese su sueldo inicial: "))
        if sueldoinicial<self.sueldo:
            sueldototal=(sueldoinicial*porcentaje)+sueldoinicial
            print("Su sueldo total es de: ",sueldototal)
        else:
            sueldototal=sueldoinicial
            print("Su sueldo total es de: ",sueldototal)

sueldo=Ejercicio_5()
sueldo.Aumento()