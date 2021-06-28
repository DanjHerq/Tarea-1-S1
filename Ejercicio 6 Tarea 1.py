class Ejercicio_6:
    def __init__(self):
        pass
    
    def Horasextras (self):
        horastrabajadas, pagoxhora=0,0
        horastrabajadas=int(input("Por favor, ingrese las horas que ha trabajo: "))
        pagoxhora=int(input("A continuación, ingrese el valor que se le paga por hora: "))
        if horastrabajadas>40:
            horasextras=horastrabajadas-40
            if horasextras>8:
                horastotales=horasextras-8
                pagoextra=pagoxhora*2*8+pagoxhora*3*horastotales
            else:
                pagoextra=pagoxhora*2*horasextras
            pagototal=pagoxhora*40+pagoextra
        else:
            pagototal=pagoxhora*horastrabajadas
        print("El pago total por sus horas trabajadas es de: ",pagototal)
pagoextra=Ejercicio_6()
pagoextra.Horasextras()

        