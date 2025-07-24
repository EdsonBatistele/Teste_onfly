import os
import pandas as pd
from src.report import save_csv, build_graph


def test_save_csv(tmp_path):
    df = pd.DataFrame({"Coluna": [1, 2, 3]})
    file_path = tmp_path / "test.csv"
    save_csv(df, file_path)
    assert os.path.exists(file_path)


def test_build_graph(tmp_path):
    df = pd.DataFrame({"Tipo": ["Fogo", "Água"], "Quantidade": [10, 5]})
    file_path = tmp_path / "grafico.png"
    build_graph(df, file_path)
    assert os.path.exists(file_path)
