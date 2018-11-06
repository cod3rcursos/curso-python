#!/usr/local/bin/python3
arquivo = open('pessoas.csv')
for registro in arquivo:
    print('Nome: {} Idade: {}'.format(*registro.split(',')))
arquivo.close()
