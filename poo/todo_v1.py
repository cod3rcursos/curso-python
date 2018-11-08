#!/usr/local/bin/python3
from datetime import datetime


class Tarefa:
    def __init__(self, descricao):
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()

    def concluir(self):
        self.feito = True

    def __str__(self):
        return self.descricao + (' (Concluída)' if self.feito else '')


def main():
    casa = []
    casa.append(Tarefa('Passar roupa'))
    casa.append(Tarefa('Lavar prato'))

    # Desafio -> 'Lavar prato'
    [tarefa.concluir() for tarefa in casa if tarefa.descricao == 'Lavar prato']

    for tarefa in casa:
        print(f'- {tarefa}')


if __name__ == '__main__':
    main()
