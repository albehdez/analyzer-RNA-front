# from fastapi import FastAPI
# import sqlalchemy
# import toml
# from sqlalchemy import create_engine, text
# import pandas as pd
# import toml
# from utils import get_dwh_connection, get_logger, sube_o_baja
# from datetime import datetime
# 


# logger = get_logger()
# logger.info('Start load the data')
# CONF = toml.load("config.toml")
# env = CONF["env"]
# conn = get_dwh_connection(CONF, env)
# username = conn.get_user_name()
# password = conn.get_password()
# host = conn.get_host()
# port = conn.get_port()
# database = conn.get_database()
# schema = conn.get_schema_name()
# #table_name = 'monarc_comments_leo'
# table_name = 'average'
# engine = create_engine(f'postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}')
# app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["http://localhost:5173"],  # Dominios permitidos (cambia según tu entorno)
#     allow_credentials=True,  # Permitir cookies
#     allow_methods=["*"],  # Métodos permitidos (GET, POST, etc.)
#     allow_headers=["*"],  # Encabezados permitidos
# )


# @app.get("/words")
# def read_words():
#     query = f"SELECT word, AVG(precio_lb_avg) FROM {schema}.{table_name} GROUP BY word"
#     logger.info(query)
#     batch = pd.read_sql(query, engine)
#     #with engine.connect() as connection:
#     #    result = connection.execute(text(f"SELECT word as producto, AVG(price) as precio_promedio FROM {schema}.{table_name} GROUP BY word"))
#     #    print(result)
#     logger.info(batch)
#     products = batch.to_dict(orient='records')
#     logger.info(products)
#     for product in products:
#         print(product)
#         logger.info(product)
#         #product['trend'] = sube_o_baja(datetime.now(),product['avg'], 328, 340)
        
#     html_content = "<h1>Productos y Precios Promedio</h1>"
#     #for product in products:
#     #    html_content += f"<p>Producto: {product['producto']}, Precio Promedio: {product['precio_promedio']}</p>"
#     return products


from fastapi import FastAPI
import sqlalchemy
import toml
from sqlalchemy import create_engine, text
import pandas as pd
import toml
from utils import get_dwh_connection, get_logger, sube_o_baja
from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware

logger = get_logger()
logger.info('Start load the data')
CONF = toml.load("config.toml")
env = CONF["env"]
conn = get_dwh_connection(CONF, env)
username = conn.get_user_name()
password = conn.get_password()
host = conn.get_host()
port = conn.get_port()
database = conn.get_database()
schema = conn.get_schema_name()
#table_name = 'monarc_comments_leo'
table_name = 'average'
engine = create_engine(f'postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}')
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Dominios permitidos (cambia según tu entorno)
    allow_credentials=True,  # Permitir cookies
    allow_methods=["*"],  # Métodos permitidos (GET, POST, etc.)
    allow_headers=["*"],  # Encabezados permitidos
)

@app.get("/words")
def read_words():
    query = f"SELECT word, AVG(precio_lb_avg)::INTEGER FROM {schema}.{table_name} GROUP BY word"
    batch = pd.read_sql(query, engine)
    #with engine.connect() as connection:
    #    result = connection.execute(text(f"SELECT word as producto, AVG(price) as precio_promedio FROM {schema}.{table_name} GROUP BY word"))
    #    print(result)
    products = batch.to_dict(orient='records')
    for product in products:
        product['trend'] = sube_o_baja(datetime.now(),product['avg'], 328, 340)
        
    print(products)
    logger.info("Aqui llegamos")
    logger.info(products)
    html_content = "<h1>Productos y Precios Promedio</h1>"
    #for product in products:
    #    html_content += f"<p>Producto: {product['producto']}, Precio Promedio: {product['precio_promedio']}</p>"
    return products

