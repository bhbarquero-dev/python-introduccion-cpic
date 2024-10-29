# cargar lista de enteros y detenerse cuando digita un cero. Imprimir al final

x = int(input("Introduce un número: "))
la_lista = []

while x != 0:
    la_lista.append(x)
    x = int(input("Introduce un número: "))
else:
    print(la_lista)