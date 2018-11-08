#!/usr/local/bin/python3
from datetime import datetime


class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def __iter__(self):
        return self.tarefas.__iter__()

    def add(self, descricao):
        self.tarefas.append(Tarefa(descricao))

    def pendentes(self):
        return [tarefa for tarefa in self.tarefas if not tarefa.feito]

    def procurar(self, descricao):
        # Possível IndexError
        return [tarefa for tarefa in self.tarefas
                if tarefa.descricao == descricao][0]

    def __str__(self):
        return f'{self.nome} ({len(self.pendentes())} tarefa(s) pendente(s))'


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
    casa = Projeto('Tarefas de Casa')
    casa.add('Passar roupa')
    casa.add('Lavar prato')
    print(casa)

    casa.procurar('Lavar prato').concluir()
    for tarefa in casa:
        print(f'- {tarefa}')
    print(casa)

    mercado = Projeto('Compras no mercado')
    mercado.add('Frutas secas')
    mercado.add('Carne')
    mercado.add('Tomate')
    print(mercado)

    comprar_carne = mercado.procurar('Carne')
    comprar_carne.concluir()
    for tarefa in mercado:
        print(f'- {tarefa}')
    print(mercado)


if __name__ == '__main__':
    main()
