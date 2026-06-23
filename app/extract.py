import json
import os
import spotipy

from logger import logger

from spotipy.oauth2 import SpotifyClientCredentials
from config import (
    SPOTIFY_CLIENT_ID,
    SPOTIFY_CLIENT_SECRET
)

from constants import (
    ARTISTS,
    SEARCH_LIMIT,
    BRONZE_PATH
)

def extract_data():
    logger.info("Iniciando extração do Spotify")

    try:
        sp = spotipy.Spotify(
            auth_manager=SpotifyClientCredentials(client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_CLIENT_SECRET)
        )

        resultado_final = {
            "tracks": {"items": []}
        }
        for artist in ARTISTS:
            logger.info(f"Buscando músicas de {artist}")

            resultado = sp.search(
                q=f"artist:{artist}",
                type="track",
                limit=SEARCH_LIMIT
            )

            contador = 0

            for track in resultado["tracks"]["items"]:
                artista_principal = track["artists"][0]["name"]

                if artista_principal.lower() == artist.lower():
                    resultado_final["tracks"]["items"].append(track)
                    contador += 1

        os.makedirs(os.path.dirname(BRONZE_PATH), exist_ok=True)

        with open(
            BRONZE_PATH,
            "w",
            encoding="utf-8"
        ) as arquivo:
            json.dump(resultado_final, arquivo, ensure_ascii=False, indent=4)
        
        logger.info("JSON salvo na camada Bronze")

        return resultado_final
    except Exception as e:

        logger.error(
            f"Erro ao consultar Spotify: {e}"
        )
        raise