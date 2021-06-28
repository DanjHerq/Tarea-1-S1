class Ejercicio_18:
    def __init__(self):
        pass
    
    def Promedio_de_notas (self):
        Notas_L=[]
        Alumnos_L=[]
        Alumnos=30
        Casillas_de_notas=6
        Promedio_de_examenes=[]
        for Alumnos in range(1,31):
            alumnos_temporales=input("Ingrese el nombre de alumno {}: ".format(Alumnos))
            Alumnos_L.append(alumnos_temporales)
            for Notas in range(1,7):
                print("Ingrese la calificación del alumno {} en el examen {}".format(alumnos_temporales,Notas))
                Notas_temporales=round(float(input("nota #{}: ".format(Notas))), 2)
                if Notas ==1:
                    Notas_L.append([Notas_temporales])
                else:
                    Notas_L[Alumnos-1].append(Notas_temporales)
            print(" ")
        
        for Numero_de_examen in range(6):
            suma_de_notas=0
            for Notas in Notas_L:
                suma_de_notas+=Notas[Numero_de_examen]
            Promedio=round((suma_de_notas/Alumnos), 2)
            print("promedio de examen {} : {} ".format(Numero_de_examen+1, Promedio))
            
        print(" ")
        for numero, Alumnos in enumerate(Alumnos_L):
            suma_de_notas=sum(Notas_L[numero])
            Promedio=round((suma_de_notas/Casillas_de_notas), 2)
            print("{} su promedio es: {} ".format(Alumnos, Promedio))
            
        promedio_mayor=0
        for Numero_de_examen in range(6):
            suma_de_notas=0
            for Notas in Notas_L:
                suma_de_notas+=Notas[Numero_de_examen]
            Promedio=round((suma_de_notas/Alumnos), 2)
            if promedio_mayor<Promedio:
                promedio_mayor=Promedio
            Promedio_de_examenes.append(Promedio)
        print(" ")
        print("El examen",Promedio_de_examenes.index(promedio_mayor)+1,"obtuvo el mayor promedio: ",promedio_mayor)
        
arreglo=Ejercicio_18()
arreglo.Promedio_de_notas()

         