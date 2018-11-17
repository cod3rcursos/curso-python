#!/usr/local/bin/python3
# Implementação simplificada do map


def mapear(funcao, lista):
    return (funcao(elemento) for elemento in lista)


if __name__ == "__main__":
    resultado = mapear(lambda x: x ** 2, [2, 3, 4])
    print(tuple(resultado))
