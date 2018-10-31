# %%
# Operador de Membro
lista = [1, 2, 3, 'Ana', 'Carla']
2 in lista
'Ana' not in lista

# Operador de Identidade
x = 3
y = x
z = 3
x is y
y is z
x is not z

lista_a = [1, 2, 3]
lista_b = lista_a
lista_c = [1, 2, 3]

lista_a is lista_b
lista_b is lista_c
lista_a is not lista_c
