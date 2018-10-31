#!/usr/local/bin/python3


# 0, 1, 1, 2, 3, 5, 8, 13, 21...
def fibonacci(limite):
    penultimo = 0
    ultimo = 1
    print(f'{penultimo},{ultimo}', end=',')
    while ultimo < limite:
        penultimo, ultimo = ultimo, penultimo + ultimo
        print(ultimo, end=',')


if __name__ == '__main__':
    fibonacci(20000)
