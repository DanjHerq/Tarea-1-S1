class Ejercicio_17:
    def __init__(self):
        pass
    
    def Vector(self):
        Nuevo=[]
        A=[]
        B=[]
        print(Nuevo)
        for j in range(0,5):
            num=int(input("Por favor, ingrese un número: "))
            Nuevo.append(num)
        for j in Nuevo:
            if j>=0:
                A.append(j)
            else:
                B.append(j)
        print("Los numeros positivos son: {}".format(A))
        print("Los numeros negativos son: {}".format(B))
arry=Ejercicio_17()
arry.Vector()