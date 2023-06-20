#OS DADOS JA FORAM INSERIDOS
import requests
import mysql.connector
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class Fipe:
    URL = 'https://parallelum.com.br/fipe/api/v1/'

    tipo = ''

    defaultRequestOptions = {
        'timeout': 40,
    }

    def __init__(self, tipo):
        self.tipo = tipo

    def instance_request(self, uri):
        response = requests.get(uri, verify=True)
        if response.status_code == 200:
            return response.json()
        else:
            return False

    @staticmethod
    def request(uri):
        response = requests.get(uri, **Fipe.defaultRequestOptions)
        if response.status_code >= 200 and response.status_code < 300:
            return response.json()
        return False

    @staticmethod
    def getMarcas():
        uri = Fipe.URL + Fipe.tipo + '/marcas'
        return Fipe.request(uri)

    @staticmethod
    def getModelos(codMarca):
        uri = Fipe.URL + Fipe.tipo + '/marcas/' + str(codMarca) + '/modelos'
        return Fipe.request(uri)

    @staticmethod
    def getAnos(codMarca, codModelo):
        uri = Fipe.URL + Fipe.tipo + '/marcas/' + str(codMarca) + '/modelos/' + str(codModelo) + '/anos'
        return Fipe.request(uri)

    @staticmethod
    def getVeiculo(codMarca, codModelo, codAno):
        uri = Fipe.URL + Fipe.tipo + '/marcas/' + str(codMarca) + '/modelos/' + str(codModelo) + '/anos/' + codAno
        return Fipe.request(uri)

    @staticmethod
    def setRequestOptions(config):
        Fipe.defaultRequestOptions.update(config)


def criar_tabela():
    # Conecta ao banco de dados
    mydb = mysql.connector.connect(
        host='localhost',
        user='LuisFelipe',
        password='Silvafodao98',
        database='tabelafipe'
    )

    # Cria o cursor
    cursor = mydb.cursor()

    # Cria a tabela
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS veiculos (
            id INT AUTO_INCREMENT PRIMARY KEY,
            marca VARCHAR(255),
            modelo VARCHAR(255),
            ano VARCHAR(10),
            valor VARCHAR(255),
            combustivel VARCHAR(255),
            codigo_fipe VARCHAR(255),
            UNIQUE KEY (codigo_fipe)
        );
    ''')

    # Fecha a conexão com o banco de dados
    cursor.close()
    mydb.close()


def inserir_dados(marca, modelo, ano, valor, combustivel, codigo_fipe):
    # Conecta ao banco de dados
    mydb = mysql.connector.connect(
        host='localhost',
        user='LuisFelipe',
        password='Silvafodao98',
        database='tabelafipe'
    )

    # Cria o cursor
    cursor = mydb.cursor()

    query = "INSERT IGNORE INTO veiculos (marca, modelo, ano, valor, combustivel, codigo_fipe) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (marca, modelo, ano, valor, combustivel, codigo_fipe)
    cursor.execute(query, values)

    # Confirma a transação
    mydb.commit()

    # Fecha a conexão com o banco de dados
    cursor.close()
    mydb.close()


def mostrar_valores_fipe():
    tipos_permitidos = ['carros']
    tipo = 'carros'  # Defina o tipo desejado, como 'carros' ou 'motos'

    if tipo not in tipos_permitidos:
        print(f'O tipo {tipo} não é permitido.')
        return

    Fipe.tipo = tipo

    # Consulta as marcas disponíveis
    marcas = Fipe.getMarcas()
    if not marcas:
        print('Falha ao consultar as marcas.')
        return

    # Cria a tabela no banco de dados
    criar_tabela()

    # Variável para contar o número de registros inseridos
    count = 0

    # Consulta os modelos e anos para cada marca
    for marca in marcas:
        cod_marca = marca['codigo']
        modelos = Fipe.getModelos(cod_marca)
        if not modelos:
            print('Falha ao consultar os modelos.')
            continue

        for modelo in modelos['modelos']:
            cod_modelo = modelo['codigo']
            anos = Fipe.getAnos(cod_marca, cod_modelo)
            if not anos:
                print('Falha ao consultar os anos.')
                continue

            for ano in anos:
                cod_ano = ano['codigo']

                # Consulta as informações do veículo selecionado
                veiculo = Fipe.getVeiculo(cod_marca, cod_modelo, cod_ano)
                if not veiculo:
                    print('Falha ao consultar o veículo.')
                    continue

                # Insere os dados na tabela do MySQL
                inserir_dados(
                    veiculo['Marca'],
                    veiculo['Modelo'],
                    veiculo['AnoModelo'],
                    veiculo['Valor'],
                    veiculo['Combustivel'],
                    veiculo['CodigoFipe']
                )

                count += 1

                # Exibe a mensagem a cada 200 registros adicionados
                if count % 200 == 0:
                    print(f'Foram adicionados {count} registros.\n')

    # Exibe a mensagem de sucesso
    print(f'Total de {count} registros inseridos na tabela.')


mostrar_valores_fipe()
