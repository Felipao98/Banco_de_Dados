import requests
import mysql.connector

# Faz a requisição à API e obtém os dados
response = requests.get('http://api.fipeapi.com.br/v1/fipe/fipe_codigo?{apikey}')
data = response.json()

# Conecta-se ao banco de dados MySQL
conexao = mysql.connector.connect(
    host='localhost',
    user='seu_usuario',
    password='sua_senha',
    database='seu_banco_de_dados'
)

# Insere os dados na tabela
cursor = conexao.cursor()
for item in data:
    sql = "INSERT INTO nome_da_tabela (campo1, campo2) VALUES (%s, %s)"
    values = (item['campo1'], item['campo2'])
    cursor.execute(sql, values)

# Confirma as alterações e fecha a conexão
conexao.commit()
cursor.close()
conexao.close()
