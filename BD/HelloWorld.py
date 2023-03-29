import sqlite3

# Conectar ao banco de dados
conn = sqlite3.connect('exemplo.db')

# Criar um cursor para executar consultas
cursor = conn.cursor()

cursor.execute('''CREATE TABLE usuarios
                  (id INTEGER PRIMARY KEY, nome TEXT, idade INTEGER)''')
cursor.execute("INSERT INTO usuarios VALUES (1, 'João', 25)")
cursor.execute("INSERT INTO usuarios VALUES (2, 'Maria', 30)")

# Executar uma consulta SQL para recuperar os dados
cursor.execute('SELECT * FROM tabela')

# Recuperar os resultados da consulta
resultados = cursor.fetchall()

# Imprimir os resultados
for resultado in resultados:
    print(resultado)

# Fechar a conexão com o banco de dados
conn.close()
