from generar_lista import generar_lista_random

la_lista = generar_lista_random()
#print(f"La lista: {la_lista}")

# Imprimir todos los valores pares
los_pares = []

for el_numero in la_lista:
    if el_numero % 2 == 0:
        los_pares.append(el_numero)

print(f"Lista de números pares: {los_pares}")
