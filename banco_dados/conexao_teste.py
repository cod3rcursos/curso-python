from bd import nova_conexao

with nova_conexao() as conexao:
    if conexao.is_connected():
        print('Conectado!')

print('Fim :)')