MAIOR_IDADE = 18


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        if not self.idade:
            return self.nome
        return f'{self.nome} ({self.idade} anos)'

    def is_adulto(self):
        return (self.idade or 0) > MAIOR_IDADE
