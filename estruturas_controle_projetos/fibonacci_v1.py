#!/usr/local/bin/python3


# 0, 1, 1, 2, 3, 5, 8, 13, 21...
def fibonacci():
    penultimo = 0
    ultimo = 1
    print(f'{penultimo},{ultimo}', end=',')
    while True:
        proximo = penultimo + ultimo
        print(proximo, end=',')
        penultimo = ultimo
        ultimo = proximo


if __name__ == '__main__':
    fibonacci()
