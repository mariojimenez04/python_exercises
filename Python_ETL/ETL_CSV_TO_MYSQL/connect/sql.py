from sqlalchemy import create_engine
import os
# from get_env import get_env

user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
host = os.getenv('DB_HOST')
port = os.getenv('DB_PORT')
db = os.getenv('DB_DATABASE')
table = os.getenv('DB_TABLE')