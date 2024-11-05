# Leer un archivo y cree un archivo que contenga
# solo las líneas que tenga x cantidad de caracteres
# x = se pide al usuario

cantidad_de_caracteres = int(input("Digite la cantidad de caracteres:"))
el_archivo = open("archivos\\lineas.txt", "r", encoding="utf-8")
el_archivo_nuevo = open("archivos\\lineasNuevas.txt", "w")

for la_linea in el_archivo:
    linea_sin_salto = la_linea.rstrip("\n")
    if len(linea_sin_salto) == cantidad_de_caracteres:
        el_archivo_nuevo.write(la_linea)

el_archivo_nuevo.close()
el_archivo.close()