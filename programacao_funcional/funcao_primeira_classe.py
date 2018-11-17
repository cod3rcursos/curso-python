#!/usr/local/bin/python3
def dobro(x):
    return x * 2


def quadrado(x):
    return x ** 2


if __name__ == '__main__':
    d = dobro
    print(d(5))

    q = quadrado
    print(q(5))

    # Retornar alternadamente o dobro ou quadrado nos números de 1 a 10
    funcs = [dobro, quadrado] * 5
    for func, numero in zip(funcs, range(1, 11)):
        print(f'O {func.__name__} de {numero} é {func(numero)}')
