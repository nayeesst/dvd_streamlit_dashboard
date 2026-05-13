from sqlalchemy import create_engine
import pandas as pd

# GANTI SESUAI DATABASE KAMU
DB_USER = "postgres"
DB_PASSWORD = "nayara123"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "dvdrental"

engine = create_engine(
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

def run_query(query):
    return pd.read_sql(query, engine)