# Imprimir los primeros 20 números pares

cantidad_de_numeros_pares = 0
numero_a_evaluar = 0

while cantidad_de_numeros_pares < 20:
    if numero_a_evaluar % 2 == 0:
        print(numero_a_evaluar)
        cantidad_de_numeros_pares += 1
    numero_a_evaluar += 1
else:
    print("Listo")