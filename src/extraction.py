import requests
import pandas as pd
import logging
from concurrent.futures import ThreadPoolExecutor, as_completed

CACHE_FILE = "data/pokemon_cache.parquet"


def get_pokemons(limit=100, offset=0):
    """
    Obtém uma lista básica de Pokémons da PokeAPI com base no limite,
    começando a partir de um índice específico (offset).

    Args:
        limit (int): Número máximo de Pokémons a retornar (padrão: 100).
        offset (int): Número de Pokémons a pular antes de começar a retornar os resultados.

    Returns:
        list: Lista de dicionários contendo o nome e a URL de cada Pokémon.
    """
    url = f"https://pokeapi.co/api/v2/pokemon?limit={limit}&offset={offset}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()["results"]


def get_details_pokemon(url):
    """
    Obtém os detalhes completos de um Pokémon a partir da URL fornecida.

    Args:
        url (str): URL da API com os dados completos do Pokémon.

    Returns:
        dict: Dicionário contendo todas as informações detalhadas do Pokémon.
    """
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def extract_data(use_cache=True):
    """
    Extrai os dados detalhados dos Pokémons a partir da PokeAPI.

    Caso o cache esteja habilitado e disponível, os dados serão carregados de um arquivo local
    para evitar requisições desnecessárias.

    Args:
        use_cache (bool): Se True, tenta carregar os dados de um arquivo cache `.parquet`.
                          Caso não encontre o cache, faz o download completo da API.

    Returns:
        pd.DataFrame: DataFrame contendo informações detalhadas de cada Pokémon,
                      incluindo atributos como nome, tipos, estatísticas e peso.
    """
    if use_cache:
        try:
            df_cache = pd.read_parquet(CACHE_FILE)
            logging.info(
                f"Cache encontrado. Usando dados salvos ({len(df_cache)} pokémons)."
            )
            return df_cache
        except FileNotFoundError:
            logging.info("Cache não encontrado, fazendo download dos dados.")

    pokemons = get_pokemons()
    dados = []

    def process_pokemon(p):
        """
        Processa os dados detalhados de um Pokémon obtidos pela URL fornecida.

        Recebe um dicionário básico do Pokémon (com nome e URL), faz a requisição dos detalhes,
        extrai e organiza informações relevantes como estatísticas, tipos, habilidades e peso,
        retornando tudo estruturado num dicionário.

        Args:
            p (dict): Dicionário com as informações básicas do Pokémon, incluindo a URL para detalhes.

        Returns:
            dict or None: Dicionário com dados organizados do Pokémon, ou None em caso de erro.
        """
        try:
            detalhes = get_details_pokemon(p["url"])
            stats = {s["stat"]["name"]: s["base_stat"] for s in detalhes["stats"]}
            tipos = [t["type"]["name"].capitalize() for t in detalhes["types"]]
            habilidades = [
                a["ability"]["name"].capitalize() for a in detalhes["abilities"]
            ]
            peso = detalhes.get("weight", 0)

            return {
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
        except Exception as e:
            logging.error(f"Erro ao extrair dados do Pokémon {p['name']}: {e}")
            return None

    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(process_pokemon, p) for p in pokemons]
        for future in as_completed(futures):
            res = future.result()
            if res is not None:
                dados.append(res)

    df = pd.DataFrame(dados)

    if use_cache:
        df.to_parquet(CACHE_FILE, index=False)
        logging.info(f"Cache salvo em {CACHE_FILE}")

    logging.info("Extração concluída.")
    return df
