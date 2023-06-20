import mysql.connector
from datetime import datetime
import re
from decimal import Decimal

# Estabelece a conexão com o banco de dados
mydb = mysql.connector.connect(
    host="localhost",
    user="LuisFelipe",
    password="Silvafodao98",
    database="tabelafipe"
)

# Verifica se a conexão foi bem-sucedida
if mydb.is_connected():
    print("Conexão estabelecida com sucesso!\n")
else:
    print("Falha ao conectar-se ao banco de dados.\n")
    exit()

# Função para exibir o menu
def exibir_menu():
    print("MENU:")
    print("1) Consultar todos os registros")
    print("2) Consultar registros da tabela")
    print("3) Inserir registros na tabela")
    print("4) Remover registros da tabela")
    print("5) Desvalorização de um veículo")
    print("6) Sair")

# Função para consultar todos os registros na tabela
def consultar_todos_registros(cursor):
    cursor.execute("SHOW TABLES FROM tabelafipe")
    resultados = cursor.fetchall()
    for resultado in resultados:
        resultado_nome = resultado[0]
        print("Tabela:", resultado_nome)
        if resultado_nome == "veiculos":
            # Selecionar todos os registros da tabela "veiculos" ordenados pela coluna "marca"
            cursor.execute("SELECT * FROM veiculos ORDER BY marca")
            rows = cursor.fetchall()

            for row in rows:
                print(row)
        
        print("\n")

# Função para consultar registros por nomedef consultarTabela(cursor):
def consultarTabela(cursor):
    marca = input("Digite algo para consultar (marca): ")
    modelo = input("Digite algo para consultar (modelo): ")

    if not marca and not modelo:
        print("Pelo menos um campo deve ser preenchido.")
        return

    query = "SELECT * FROM veiculos WHERE "

    if marca and modelo:
        query += "marca = %s AND modelo = %s"
        params = (marca, modelo)
    elif marca:
        query += "marca = %s"
        params = (marca,)
    else:  # modelo
        query += "modelo = %s"
        params = (modelo,)

    cursor.execute(query, params)
    resultados = cursor.fetchall()

    if not resultados:
        print("Nenhum resultado encontrado.\n")
        return

    for resultado in resultados:
        print(resultado)

    # Obter a data atual
    data_atual = datetime.now().date()
    print("Data da consulta:\n", data_atual)
        
def Inserir_Tabela(cursor):
    marca = input("Digite a marca do veículo: ")
    modelo = input("Digite o modelo do veículo: ")
    ano = input("Digite o ano do veículo: ")
    valor = input("Digite o valor do veículo: ")
    combustivel = input("Digite o tipo de combustivel do veiculo: ")
    codigo_fipe = input("Digite o codigoFipe do veículo: ")
    
    cursor.execute("INSERT INTO veiculos (marca, modelo, ano, valor, combustivel, codigo_fipe) VALUES (%s, %s, %s, %s, %s, %s)", (marca, modelo, ano, valor, combustivel, codigo_fipe))
    
    mydb.commit()
    
    print("Registro inserido com sucesso!\n")
    
def remover_Tabela(cursor):
    marca = input("Digite a marca: ")
    modelo = input("Digite o modelo: ")
    
    cursor.execute("DELETE FROM veiculos WHERE marca = %s OR modelo = %s", (marca, modelo))

    mydb.commit()
    
    print("Removido com sucesso!\n")


def formatar_valor(valor):
    valor = valor.replace(".", "")  # Remover separadores
    valor = valor.replace(",", ".")  # Substituir a vírgula por ponto decimal
    return valor

def consultar_desvalorizacao(cursor):
    marca = input("Digite a marca do veículo: ")
    modelo = input("Digite o modelo do veículo: ")

    # Consulta os valores do veículo no banco de dados
    cursor.execute("SELECT valor FROM veiculos WHERE marca = %s AND modelo = %s", (marca, modelo,))
    resultados = cursor.fetchall()

    if not resultados:
        print("Veículo não encontrado.")
        return

    anos_de_uso = int(input("Digite a quantidade de anos de uso: "))
    taxa_de_depreciacao = Decimal(input("Digite a taxa de depreciação anual (em decimal): "))

    for resultado in resultados:
        valor_str = resultado[0]
        valor_str = formatar_valor(valor_str)
        numeros = re.findall(r'\d+', valor_str)  # Encontrar apenas os dígitos

        if numeros:
            valor_inicial = Decimal('.'.join(numeros))  # Converter para Decimal com ponto decimal
            valor_final = valor_inicial

            for _ in range(anos_de_uso):
                valor_final -= valor_final * taxa_de_depreciacao

            valor_inicial_formatado = f"R$ {valor_inicial:,.2f}"  # Formatar o valor inicial como moeda
            valor_final_formatado = f"R$ {valor_final:,.2f}"  # Formatar o valor final como moeda

            print(f"O veículo {marca} {modelo} tem o valor inicial de {valor_inicial_formatado}")
            print(f"O veículo {marca} {modelo} tem o valor atual de {valor_final_formatado}\n")
        else:
            print(f"Não foi possível obter o valor do veículo {marca} {modelo}.\n")

          
cursor = mydb.cursor()

# Loop principal do menu
while True:
    exibir_menu()
    opcao = input("Digite sua opção: ")

    if opcao == "1":
        consultar_todos_registros(cursor)
    elif opcao == "2":
        consultarTabela(cursor)
    elif opcao == "3":
        Inserir_Tabela(cursor)
    elif opcao == "4":
        remover_Tabela(cursor)
    elif opcao == "5":
        consultar_desvalorizacao(cursor)
    elif opcao == "6":
        print("Saindo....\n")
        break
    else:
        print("Opção inválida. Digite novamente.")
            
# Encerra o cursor e a conexão com o banco de dados
cursor.close()
mydb.close()
