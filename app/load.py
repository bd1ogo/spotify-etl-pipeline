import time
import pandas as pd
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
    engine = create_engine(
        f"postgresql://{DB_USER}:{DB_PASSWORD}"
        f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )

    max_tentativas = 5
    conectado = False 

    for tentativa in range(max_tentativas):
        try:
            with engine.connect():
                logger.info("Conexão com PostgreSQL estabelecida")
                conectado=True
                break
        except Exception:
            logger.warning(
                f"PostgreSQL indisponível."
                f"Tentativa {tentativa + 1}/{max_tentativas}"
            )
            time.sleep(5)
    if not conectado:
        raise ConnectionError(
            "Não foi possível conectar ao PostgreSQL."
        )
    
    try:
        query = f"""
        SELECT track_id
        FROM {TABLE_NAME}
        """
        try:
            df_existente = pd.read_sql(query, engine)
        except Exception:
            logger.warning(
                "Tabela vazia ou inexistente. "
                "Realizando carga inicial."
            )
            df_existente = pd.DataFrame(
                columns=["track_id"]
            )
        logger.info(f"{len(df_existente)} registro já existente no banco.")
        
        novos_registros = df[~df["track_id"].isin(df_existente["track_id"])]

        logger.info(f"{len(novos_registros)} registros novos identificados.")

        if not novos_registros.empty:
            novos_registros.to_sql(
                TABLE_NAME,
                engine,
                if_exists="append",
                index=False
            )
            logger.info(f"{len(novos_registros)} registros inseridos.")
        else:
            logger.info("Nenhum registro novo encontrado.")
        
        logger.info("Dados carregados sucesso!")

    except Exception as e:
        logger.error(f"Erro ao carregar dados: {e}")
        raise