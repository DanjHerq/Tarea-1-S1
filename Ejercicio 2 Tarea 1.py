class Ejercicio_2:
    def __init__(self):
        pass
    
    def Comisiones (self):
        sueldo, venta1, venta2, venta3, porcomi= 0,0,0,0,0.10
        sueldo=int(input("Por favor, ingrese su sueldo: "))
        venta1=int(input("A continuación ingrese su primera venta: "))
        venta2=int(input("Ahora ingrese su segunda venta: "))
        venta3=int(input("Finalmente ingrese su tercera venta: "))
        Ventatotal=venta1+venta2+venta3
        comision=Ventatotal*porcomi
        Sueldototal= sueldo+comision
        print("La comision que obtuvo este mes es de :",comision)
        print("El total de su sueldo más las comisiones es de: ",Sueldototal)
        
sueldo=Ejercicio_2()
sueldo.Comisiones()
        