# Leer archivo y contar las palabras

el_archivo = open("archivos\\palabras.txt", "r")
#cantidad_de_palabras = 1

# for el_caracter in el_archivo.read():
#     if el_caracter == " ":
#         cantidad_de_palabras += 1

# print(f"#1: El archivo tiene {cantidad_de_palabras} palabras.")

palabras = el_archivo.read().split()
cantidad_de_palabras = len(palabras)

print(f"#2: El archivo tiene {cantidad_de_palabras} palabras.")


el_archivo.close()