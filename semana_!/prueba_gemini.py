def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            print(f"{numero} no es primo")
            return False
    print(f"{numero} es primo")
    return True

# es par
def es_par(numero):
    if numero % 2 == 0:
        print(f"{numero} es par")
        return True
    else:
        print(f"{numero} no es par")
        return False


es_par(2)
es_primo(3)