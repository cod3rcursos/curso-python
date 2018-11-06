def soma(a, b):
    def soma_c(c):
        return a + b + c
    return soma_c


print(soma(2, 3)(5))
