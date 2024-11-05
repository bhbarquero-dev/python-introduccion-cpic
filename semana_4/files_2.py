import random

el_archivo = open("archivos\\datos41.txt", "w")

for el_indice in range(100):
    if el_indice < 99:
        el_archivo.write(str(random.randint(1,50)) + "\n")
    else:
        el_archivo.write(str(random.randint(1,50)))

el_archivo.close()