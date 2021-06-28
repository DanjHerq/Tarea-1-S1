class Ejercicio_12:
    def __init__(self):
        pass
    
    def Bucle_condicional (self):
        Suma=0
        Producto=1
        Respuesta=input("¿Desea comenzar con el procedimiento (S/N)? ")
        while Respuesta!="S" and Respuesta!="N":
            num=int(input("Por favor, ingrese un número: "))
            Suma=Suma+num
            Producto=Producto*num
            Respuesta=input("¿Desea continuar (S/N)? ")
        print("El total de la suma es de: ",Suma)
        print("El total del producto es de: ",Producto)

control=Ejercicio_12()
control.Bucle_condicional()