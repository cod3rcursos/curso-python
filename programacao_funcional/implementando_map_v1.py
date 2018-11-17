#!/usr/local/bin/python3
# Implementação simplificada do map


def mapear(funcao, lista):
    for elemento in lista:
        yield funcao(elemento)


if __name__ == "__main__":
    resultado = mapear(lambda x: x ** 2, [2, 3, 4])
    print(list(resultado))
