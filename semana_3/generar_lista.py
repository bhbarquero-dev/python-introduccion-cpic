import random

def generar_lista_random(la_cantidad = 60):
    return [random.randint(0, 100) for _ in range(la_cantidad)]