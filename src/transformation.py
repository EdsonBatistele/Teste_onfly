import pandas as pd
import logging


def category(xp):
    categorias = {"FRACO": xp < 50, "MÉDIO": 50 <= xp <= 100, "FORTE": xp > 100}
    return next((k for k, v in categorias.items() if v), "Xp não informado")

def transform_data(df):
    logging.info("Adicionando coluna Categoria")
    df["Categoria"] = df["Experiência Base"].apply(category)
    return df

def medias_por_tipo(df):
    tipos = df.explode("Tipos")
    return (
        tipos.groupby("Tipos")[["Ataque", "Defesa", "HP"]].mean().round(2).reset_index()
    )

def top_experiencia(df):
    return df.sort_values(by="Experiência Base", ascending=False).head(5)

def contar_por_tipo(df):
    df_explodido = df.explode("Tipos")
    contagem = df_explodido["Tipos"].value_counts().reset_index()
    contagem.columns = ["Tipo", "Quantidade"]
    return contagem
