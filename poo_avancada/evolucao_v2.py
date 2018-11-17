#!/usr/local/bin/python3


class Humano:
    # atributo de classe
    especie = 'Homo Sapiens'

    def __init__(self, nome):
        self.nome = nome

    def das_cavernas(self):
        self.especie = 'Homo Neanderthalensis'
        return self

    @staticmethod
    def especies():
        adjetivos = ('Habilis', 'Erectus', 'Neanderthalensis', 'Sapiens')
        return ('Australopiteco',) + tuple(f'Homo {adj}' for adj in adjetivos)

    @classmethod
    def is_evoluido(cls):
        return cls.especie == cls.especies()[-1]


class Neanderthal(Humano):
    especie = Humano.especies()[-2]


class HomoSapiens(Humano):
    especie = Humano.especies()[-1]


if __name__ == '__main__':
    jose = HomoSapiens('José')
    # HomoSapiens.das_cavernas(jose)

    grokn = Neanderthal('Grokn')
    print(
        f'Evolução (a partir da classe): {", ".join(HomoSapiens.especies())}')
    print(f'Evolução (a partir da instancia): {", ".join(jose.especies())}')
    print(f'Homo Sapiens evoluído? {HomoSapiens.is_evoluido()}')
    print(f'Neanderthal evoluído? {Neanderthal.is_evoluido()}')
    print(f'José evoluído? {jose.is_evoluido()}')
    print(f'Grokn evoluído? {grokn.is_evoluido()}')
