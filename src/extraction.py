import requests
import pandas as pd
import logging


def get_pokemons(limit=100, offset=0):
    url = f"https://pokeapi.co/api/v2/pokemon?limit=100&offset=0"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()["results"]


def get_details_pokemon(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def extract_date():
    logging.info("Iniciando extração dos dados")
    pokemons = get_pokemons()
    dados = []

    for p in pokemons:
        try:
            detalhes = get_details_pokemon(p["url"])
            stats = {s["stat"]["name"]: s["base_stat"] for s in detalhes["stats"]}
            tipos = [t["type"]["name"].capitalize() for t in detalhes["types"]]
            habilidades = [
                a["ability"]["name"].capitalize() for a in detalhes["abilities"]
            ]
            peso = detalhes.get("weight", 0)

            dados.append(
                {
                    "ID": detalhes["id"],
                    "Nome": detalhes["name"].capitalize(),
                    "Experiência Base": detalhes.get("base_experience", 0),
                    "Tipos": tipos,
                    "Habilidades": habilidades,
                    "HP": stats.get("hp", 0),
                    "Ataque": stats.get("attack", 0),
                    "Ataque Especial": stats.get("special-attack", 0),
                    "Defesa": stats.get("defense", 0),
                    "Defesa Especial": stats.get("special-defense", 0),
                    "Velocidade": stats.get("speed", 0),
                    "Peso": peso,
                }
            )

        except Exception as e:
            logging.error(f"Erro ao extrair dados do Pokémon {p['name']}: {e}")

    df = pd.DataFrame(dados)
    logging.info("Extração concluída.")
    return df
