import logging
import requests

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import root_mean_squared_error, mean_squared_error
import matplotlib.pyplot as plt
import joblib


def sube_o_baja(fechas, precio_producto, precio_dolar, precio_euro):

    logger = get_logger()
    # Crear el DataFrame
    data = pd.DataFrame([{
        'fecha': fechas,
        'precio_producto': precio_producto,
        'precio_dolar': precio_dolar,
        'precio_euro': precio_euro
    }])
    modelo = joblib.load('model.pkl')
    #logger.info(data)


    # Paso 3: Definir características y objetivo
    X = data[['precio_producto', 'precio_dolar', 'precio_euro']]
    y = data['precio_producto']
    y_pred = modelo.predict(X)
    logger.info(y_pred)
    return y_pred[0] - y.iloc[-1]

    #return np.sign(precio_predicho-precio_producto[-1]) or 1






class PostgresConnection:
    def __init__(self, database, host, user_name, password, JDBC_url, schema_name, port, driver):
        self.database = database
        self.host = host
        self.user_name = user_name
        self.password = password
        self.JDBC_url = JDBC_url
        self.schema_name = schema_name
        self.port = port
        self.driver = driver

    def get_host(self):
        return self.host
    
    def get_database(self):
        return self.database

    def get_user_name(self):
        return self.user_name

    def get_password(self):
        return self.password

    def get_JDBC_url(self):
        return self.JDBC_url

    def get_schema_name(self):
        return self.schema_name
    
    def get_port(self):
        return self.port
    
    def get_driver(self):
        return self.driver

def get_dwh_connection(CONF, env):
    database = CONF["dwh"][env]["database"]
    host = CONF["dwh"][env]["host"]
    user_name = CONF["dwh"][env]["user_name"]
    password = CONF["dwh"][env]["password"]
    JDBC_url = CONF["dwh"][env]["JDBC_url"]
    schema_name = CONF["dwh"][env]["schema_name"]
    port = CONF["dwh"][env]["port"]
    driver = CONF["dwh"][env]["driver"]
    
    return PostgresConnection(
        database=database,
        host=host,
        user_name=user_name,
        password=password,
        JDBC_url=JDBC_url,
        schema_name=schema_name,
        port=port,
        driver=driver
    )

def get_logger():
    log_filename = "applog.log"  # Specify the file path and name
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)  # Set the logging level to INFO

    # Create a file handler and set the log level
    file_handler = logging.FileHandler(log_filename)
    file_handler.setLevel(logging.INFO)

    # Define the logger formatter
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s - [%(filename)s]')
    file_handler.setFormatter(formatter)

    # Add the file handler to the logger
    logger.addHandler(file_handler)

    return logger


# Función para enviar mensaje a Telegram
def send_telegram_message(message):
    # Datos de tu bot de Telegram
    TELEGRAM_BOT_TOKEN = '7416223917:AAFajUGZ6p2xMf_wd-zsJZIQCuBTgvkhCJg'  # Reemplaza con el token de tu bot
    TELEGRAM_CHAT_ID = '938602625'  # Reemplaza con tu chat ID
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message
    }
    try:
        response = requests.post(url, json=payload)
        if response.status_code != 200:
            logging.error(f"Error al enviar mensaje a Telegram: {response.text}")
    except Exception as e:
        logging.error(f"Error de conexión con Telegram: {e}")