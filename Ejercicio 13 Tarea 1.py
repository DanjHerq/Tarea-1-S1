class Ejercicio_13:
    def __init__(self):
        pass
    
    def Buclecenti (self):
        Suma=0
        Producto=1
        num=int(input("Por favor, ingrese un número: "))
        while num!=-1:
            Suma=Suma+num
            Producto=Producto*num
            num=int(input("ingrese otro numero: "))
        print("El total de la suma es de: ",Suma)
        print("El total del producto es de: ",Producto)

centinela=Ejercicio_13()
centinela.Buclecenti()