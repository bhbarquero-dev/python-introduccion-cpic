# Encontrar valor mayor, menor y promedio de la lista

from generar_lista import generar_lista_random

lista = generar_lista_random()
print(f"La lista: {lista}")

valor_mayor = lista[0]
valor_menor = lista[0]
promedio = 0

for x in lista:
    if x > valor_mayor:
        valor_mayor = x
    if x < valor_menor:
        valor_menor = x
    promedio += x

promedio = promedio / len(lista)

print(f"#1 - El valor mayor es {valor_mayor}, el valor menor es {valor_menor} y el promedio es {promedio}")
#----------
valor_mayor = max(lista)
valor_menor = min(lista)
promedio = sum(lista) / len(lista)

print(f"#2 - El valor mayor es {valor_mayor}, el valor menor es {valor_menor} y el promedio es {promedio}")
