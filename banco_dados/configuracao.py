from mysql.connector import connect

conexao = connect(
    passwd='12345678',
    port=3306,
    user='root',
    host='localhost',
)

print(conexao)