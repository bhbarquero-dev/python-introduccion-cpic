cantidad_de_numeros = int(input("Ingrese la cantidad de números: "))
resultado_de_sumatoria = 0
i = 1

while i <= cantidad_de_numeros:
    valor_del_numero = int(input("Ingrese un número: "))
    resultado_de_sumatoria += (valor_del_numero  / valor_del_numero **2)
    i += 1
else:
    print(resultado_de_sumatoria)