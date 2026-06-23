import os
import pandas as pd
from constants import SILVER_PATH
from logger import logger

def transform_data(dados):
    logger.info("Transformação iniciada")

    try:
        tracks = dados["tracks"]["items"]
        lista_tracks = []

        for track in tracks:
            lista_tracks.append({
                "track_id":track["id"],
                "track_name":track["name"],
                "artist_name":track["artists"][0]["name"],
                "album_name":track["album"]["name"],
                "release_date":track["album"]["release_date"],
                "duration_ms":track["duration_ms"]
            })

        df = pd.DataFrame(lista_tracks)

        df = df.drop_duplicates(subset=["track_id"])

        df["release_date"] = pd.to_datetime(
            df["release_date"],
            errors="coerce"
        )

        df["duration_minutes"] = (
            df["duration_ms"] / 1000 / 60
        ).round(2)

        os.makedirs(
            os.path.dirname(SILVER_PATH),
            exist_ok=True
        )

        df.to_csv(
            SILVER_PATH,
            index=False
        )
        logger.info("CSV salvo na camada Silver")

        logger.info(f'Total de registros transformados: {len(df)}')
        return df
    except Exception as e:
        
        logger.error(
            f"Erro na transformação: {e}"
        )

        raise