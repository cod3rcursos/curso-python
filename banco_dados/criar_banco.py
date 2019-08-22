from mysql.connector import connect

conexao = connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='12345678'
)

cursor = conexao.cursor()
# CREATE DATABASE IF NOT EXISTS agenda
cursor.execute('CREATE DATABASE agenda')