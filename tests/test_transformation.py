import pandas as pd
from src.transformation import (
    category,
    transform_data,
    count_by_type,
    mean_by_type,
    top_experience,
)


def test_category():
    assert category(30) == "FRACO"
    assert category(70) == "MÉDIO"
    assert category(120) == "FORTE"


def test_transform_data():
    df = pd.DataFrame({"Experiência Base": [30, 70, 120]})
    df = transform_data(df)
    assert "Categoria" in df.columns
    assert df["Categoria"].tolist() == ["FRACO", "MÉDIO", "FORTE"]


def test_count_by_type():
    df = pd.DataFrame({"Tipos": [["Fogo", "Voador"], ["Água"], ["Fogo"]]})
    df["Categoria"] = "FORTE"
    result = count_by_type(df)
    assert "Tipo" in result.columns
    assert "Quantidade" in result.columns
    assert result[result["Tipo"] == "Fogo"]["Quantidade"].iloc[0] == 2


def mean_by_type(df):
    tipos = df.explode("Tipos")
    resultado = (
        tipos.groupby("Tipos")[["Ataque", "Defesa", "HP"]].mean().round(2).reset_index()
    )
    resultado.rename(columns={"Tipos": "Tipo"}, inplace=True)
    return resultado


def test_top_experience():
    df = pd.DataFrame({"Experiência Base": [10, 200, 50, 300, 150, 400]})
    top = top_experience(df)
    assert len(top) == 5
    assert top["Experiência Base"].iloc[0] == 400
