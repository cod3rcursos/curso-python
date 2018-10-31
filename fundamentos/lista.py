# %%
lista = []
type(lista)
dir(lista)
# help(list)
len(lista)
lista.append(1)
lista.append(5)
lista
len(lista)

nova_lista = [1, 5, 'Ana', 'Bia']
nova_lista
nova_lista.remove(5)
nova_lista
nova_lista.reverse()
nova_lista

# %%
lista = [1, 5, 'Rebeca', 'Guilherme', 3.1415]
lista.index('Guilherme')
# lista.index(42)
lista[2]
1 in lista
'Rebeca' in lista
'Pedro' not in lista
lista[0]
lista[4]
# lista[5]
lista[-1]
lista[-5]

# %%
lista = ['Ana', 'Lia', 'Rui', 'Paulo', 'Dani']
lista[1:3]
lista[1:-1]
lista[1:]
lista[:-1]
lista[:]
lista[::2]
lista[::-1]
del lista[2]
lista
del lista[1:]
lista
