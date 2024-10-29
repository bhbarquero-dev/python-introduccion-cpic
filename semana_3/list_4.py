# definir si dos listas son iguales o no

import random

lista_1 = []
lista_2 = []
son_iguales = True

for un_numero in range(random.randint(5,100)):
    lista_1.append(random.randint(0,100000))
    lista_2.append(random.randint(0,100000))

print(f"Las listas son iguales: {lista_1 == lista_2}")