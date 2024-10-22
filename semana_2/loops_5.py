resultado_de_la_suma = 0
contador = 1

while 1/contador > 0.00001:
    resultado_de_la_suma += 1/contador
    contador += 1
else:
    print(f"El resultado final de la suma es: {resultado_de_la_suma} con n = {contador}")