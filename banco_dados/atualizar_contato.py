from mysql.connector.errors import ProgrammingError
from bd import nova_conexao

sql = 'UPDATE contatos SET nome = %s WHERE id = %s'
args = ('Lucas Yuri', 44)

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(sql, args)
        conexao.commit()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        print(f'{cursor.rowcount} registro(s) alterado(s).')