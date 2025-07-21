import pandas as pd
import logging


def category(xp):
    """
    Classifica um Pokémon em uma categoria com base na experiência base (XP).

    Args:
        xp (int): Valor da experiência base do Pokémon.

    Returns:
        str: Categoria do Pokémon - "FRACO", "MÉDIO" ou "FORTE".
             Retorna "Xp não informado" se o valor não corresponder a nenhuma categoria.
    """
    categorias = {"FRACO": xp < 50, "MÉDIO": 50 <= xp <= 100, "FORTE": xp > 100}
    return next((k for k, v in categorias.items() if v), "Xp não informado")


def transform_data(df):
    """
    Adiciona a coluna 'Categoria' ao DataFrame aplicando a função 'category' na coluna 'Experiência Base'.

    Args:
        df (pandas.DataFrame): DataFrame contendo os dados dos Pokémons com a coluna 'Experiência Base'.

    Returns:
        pandas.DataFrame: DataFrame atualizado com a coluna 'Categoria' adicionada.
    """
    logging.info("Adicionando coluna Categoria")
    df["Categoria"] = df["Experiência Base"].apply(category)
    return df


def mean_by_type(df):
    """
    Calcula a média dos atributos 'Ataque', 'Defesa' e 'HP' para cada tipo de Pokémon.

    Args:
        df (pandas.DataFrame): DataFrame contendo os dados dos Pokémons com coluna 'Tipos' (lista de tipos).

    Returns:
        pandas.DataFrame: DataFrame com a média dos atributos por tipo, colunas: 'Tipos', 'Ataque', 'Defesa', 'HP'.
    """
    tipos = df.explode("Tipos")
    return (
        tipos.groupby("Tipos")[["Ataque", "Defesa", "HP"]].mean().round(2).reset_index()
    )


def top_experience(df):
    """
    Retorna os 5 Pokémons com maior experiência base.

    Args:
        df (pandas.DataFrame): DataFrame contendo os dados dos Pokémons com coluna 'Experiência Base'.

    Returns:
        pandas.DataFrame: DataFrame contendo os 5 Pokémons com maior experiência base.
    """
    return df.sort_values(by="Experiência Base", ascending=False).head(5)


def count_by_type(df):
    """
    Conta a quantidade de Pokémons por tipo.

    Args:
        df (pandas.DataFrame): DataFrame contendo os dados dos Pokémons com coluna 'Tipos' (lista de tipos).

    Returns:
        pandas.DataFrame: DataFrame com colunas 'Tipo' e 'Quantidade' representando a contagem por tipo.
    """
    df_explodido = df.explode("Tipos")
    contagem = df_explodido["Tipos"].value_counts().reset_index()
    contagem.columns = ["Tipo", "Quantidade"]
    return contagem
