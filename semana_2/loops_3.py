# leer n números y calcular la media aritmética
cantidad_de_numeros = int(input("Ingrese la cantidad de números: "))

if cantidad_de_numeros == 0:
    print("La cantidad de números no puede ser 0")
    exit()

suma_de_los_numeros = 0
cantidad_de_numeros_ingresados = 0

while cantidad_de_numeros_ingresados < cantidad_de_numeros:
    numero = float(input("Ingrese un número: "))
    suma_de_los_numeros += numero
    cantidad_de_numeros_ingresados += 1

media_aritmetica = suma_de_los_numeros / cantidad_de_numeros
print(f"La media aritmética es: {media_aritmetica}")
print(f"Operación matemática: suma({suma_de_los_numeros}) / cantidad({cantidad_de_numeros}) = media_aritmetica({media_aritmetica})")