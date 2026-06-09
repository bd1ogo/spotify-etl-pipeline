from sqlalchemy import create_engine
from constants import TABLE_NAME

from config import (
    DB_USER,
    DB_PASSWORD,
    DB_HOST,
    DB_PORT,
    DB_NAME
)

from logger import logger

def load_data(df):
    logger.info("Iniciando carga no PostgreSQL")

    try:
        engine = create_engine(
            f"postgresql://{DB_USER}:{DB_PASSWORD}"
            f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
        )

        df.to_sql(
            TABLE_NAME,
            engine,
            if_exists="append",
            index=False
        )
        logger.info("Dados carregados com sucesso!")
        return True
    except Exception as e: 
        
        logger.error(
            f"Erro ao carregar dados: {e}"
        )
