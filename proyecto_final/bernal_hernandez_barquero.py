# Usted debe escribir un programa que lea dos archivos tipo texto, 
# donde cada uno de ellos contiene números enteros, un número por cada línea. 
# Son de tamaño diferente.
# Usted debe generar un único archivo tipo text, un número por lines, ordenado desendente.

los_numeros = []

datos1 = open("datos1.txt")

for la_linea in datos1:
    los_numeros.append(int(la_linea))

datos1.close()

datos2 = open("datos2.txt")

for la_linea in datos2:
    los_numeros.append(int(la_linea))

datos2.close()

los_numeros.sort(reverse = True)

datos_finales = open("resultado.txt", "w")

for el_numero in los_numeros:
    datos_finales.write(f"{el_numero}\n")

datos_finales.close()