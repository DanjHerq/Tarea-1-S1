class Ejercicio_8:
    def __init__ (self):
        pass
    
    def Funcion (self):
        num, valor=0,0
        num=int(input("Por favor, ingrese un número entero del 1 al 3: "))
        valor=int(input("A continuación ingrese otro valor "))
        if num==1:
            respuesta=100*valor
            print(respuesta)
        if num==2:
            respuesta=100^valor
            print(respuesta)
        if num==3:
            respuesta=100/valor
            print(respuesta)
        if num>3 and num<0:
            print(0)

multiple=Ejercicio_8()
multiple.Funcion()