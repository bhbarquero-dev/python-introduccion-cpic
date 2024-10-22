# Programa para verificar si un número es par o impar

# Solicitar al usuario que ingrese un número
numero = int(input("Introduce un número: "))

# Verificar si el número es par o impar
if numero % 2 == 0:
    print(f"El número {numero} es par.")
else:
    print(f"El número {numero} es impar.")