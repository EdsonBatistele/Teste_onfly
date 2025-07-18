import logging
from src.extraction import extract_date
from src.transformation import transform_data
from src.transformation import transform_data, contar_por_tipo


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(levelname)s - %(message)s")

    df = extract_date()
    print(df.head(5))
    df = transform_data(df)
    print(df.head())

    df_tipos = contar_por_tipo(df)
    print(df_tipos.head())
