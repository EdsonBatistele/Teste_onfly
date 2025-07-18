import logging
from src.extraction import extract_date

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(levelname)s - %(message)s")

    df = extract_date()
    print(df.head(10))
