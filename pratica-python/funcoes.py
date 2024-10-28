def imprime():
    print("Esta é uma função")


imprime()


def imprime2(n):
    print(n)


imprime2("Este é o texto que passei por parametro")


def potencia(n):
    return n * n


print(potencia(3))


def intervalo(inic=1, fim=10):
    for inic in range(1, fim + 1):
        print(inic)


x = intervalo(1, 10)
y = intervalo()
