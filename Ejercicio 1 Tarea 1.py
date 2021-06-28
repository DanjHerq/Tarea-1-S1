class Ejercicio_1:
    def __init__(self):
        pass
    
    def Compra (self):
        descuento=0.15
        compra=0
        producto=int(input("Por favor, ingrese su cuenta: "))
        porcentaje=producto*descuento
        total=producto-porcentaje
        print("El total a pagar con el descuento es de: ", total)
        
pago=Ejercicio_1()
pago.Compra()