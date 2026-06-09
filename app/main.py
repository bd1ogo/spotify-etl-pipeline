from extract import extract_data
from transform import transform_data
from load import load_data
from logger import logger

def main():
    try:
        logger.info("Pipeline iniciado!")
        dados = extract_data()

        df = transform_data(dados)

        load_data(df)

        logger.info("Pipeline finalizado com sucesso!")
    except Exception as e:
        logger.error(
            f"Falha no pipeline: {e}"
        )

if __name__ == "__main__":
    main()