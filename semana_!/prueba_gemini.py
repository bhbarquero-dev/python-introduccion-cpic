def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            print(f"{numero} no es primo")
            return False
    print(f"{numero} es primo")
    return True


es_primo(3)