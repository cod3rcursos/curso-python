from bd import nova_conexao
from mysql.connector import ProgrammingError

criar_tabela_grupo = """
    CREATE TABLE IF NOT EXISTS grupos (
        id INT AUTO_INCREMENT PRIMARY KEY,
        descricao VARCHAR(30)
    )
"""

alterar_tabela_contato_1 = """
    ALTER TABLE contatos ADD grupo_id INT
"""

alterar_tabela_contato_2 = """
    ALTER TABLE contatos ADD FOREIGN KEY (grupo_id)
    REFERENCES grupos(id)
"""

try:
    with nova_conexao() as conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute(criar_tabela_grupo)
            cursor.execute(alterar_tabela_contato_1)
            cursor.execute(alterar_tabela_contato_2)
        except ProgrammingError as e:
            print(f'Erro: {e.msg}')
except ProgrammingError as e:
    print(f'Erro CONEXÃO: {e.msg}')