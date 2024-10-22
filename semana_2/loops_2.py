# Leer 10 números enteros e indicar cual es el mayor y cual es el menor

elNumero = int(input("Digite un número: "))
numeroMayor = elNumero
numeroMenor = elNumero
cantidadDeNumeros = 1

while cantidadDeNumeros < 10:
    elNumero = int(input("Digite un número: "))

    if(elNumero > numeroMayor):
        numeroMayor = elNumero
    if(elNumero < numeroMenor): 
        numeroMenor = elNumero
    cantidadDeNumeros += 1
else:
    print(f"El número mayor es {numeroMayor} y el número menor es {numeroMenor}")
