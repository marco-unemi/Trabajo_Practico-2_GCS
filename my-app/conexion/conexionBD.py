# Importando Libreria mysql.connector para conectar Python con MySQL
import mysql.connector
import os
from decouple import config

def connectionBD():
    try:
        connection = mysql.connector.connect(
            host=config("DB_HOST"),
            user=config("DB_USER"),
            passwd=config("DB_PASSWORD"),
            database=config("DB_NAME"),
            charset='utf8mb4',
            collation='utf8mb4_unicode_ci',
            raise_on_warnings=True,
            port=config("DB_PORT")
        )
        if connection.is_connected():
            return connection

    except mysql.connector.Error as error:
        print(f"No se pudo conectar: {error}")
        return None
