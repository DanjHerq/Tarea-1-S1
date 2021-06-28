class Ejercicio_15:
    def __init__(self):
        pass
    
    def Repeticion (self):
        serie=0
        i=1
        band="T"
        num=int(input("Ingrese el número de términos de la serie: "))
        for x in range(num):
            if band=="T":
                serie=serie+(1/i)
                band=="F"
            else:
                serie=serie-(1/i)
                band="T"
            i=i+1
        print(serie)
repet=Ejercicio_15()
repet.Repeticion()
    
           
            