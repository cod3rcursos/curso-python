produto = {'nome': 'Caneta Chic', 'preco': 14.99,
           'importada': True, 'estoque': 793}

for chave in produto:
    print(chave)

for valor in produto.values():
    print(valor)

for chave2, valor2 in produto.items():
    print(chave2, '=', valor2)

print(chave, valor, chave2, valor2)
