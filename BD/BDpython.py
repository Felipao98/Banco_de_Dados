import mysql.connector
from mysql.connector import Error
import pandas as pd

def create_server_connection(nome_host, nome_usuario, senha):
    connection = create_server_connection("nomehost", "root", pd)
    try:
        connection = mysql.connector.connect(
            host=nome_host,
            user=nome_usuario,
            passwd=senha
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection