import logging
import os
from src.extraction import extract_data
from src.transformation import (
    transform_data,
    count_by_type,
    mean_by_type,
    top_experience,
)
from src.report import (
    save_csv,
    build_graph,
    pie_chart_category,
    plot_strong_pokemons_per_type,
)


def rodar_pipeline():
    """
    Executa a pipeline completa de extração, transformação, análise e geração de relatórios.

    Passos realizados:
    - Criação dos diretórios necessários para logs e dados.
    - Configuração do sistema de logs.
    - Extração dos dados dos Pokémons da API (com cache opcional).
    - Transformação dos dados, incluindo categorização dos Pokémons.
    - Cálculo da contagem por tipo, médias estatísticas e seleção dos top 5 por experiência.
    - Salvamento dos relatórios em arquivos CSV.
    - Geração e salvamento de gráficos: distribuição por tipo, pizza por categoria e concentração dos pokémons fortes.
    - Logs de cada etapa para acompanhamento e debug.

    Não possui parâmetros e não retorna valor, apenas gera arquivos e logs no sistema.

    """
    os.makedirs("logs", exist_ok=True)
    os.makedirs("data", exist_ok=True)

    logging.basicConfig(
        filename="logs/pipeline.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        filemode="w",
        encoding="utf-8",
    )

    logging.info("Pipeline iniciado.")

    df = extract_data()
    logging.info(f"Extração concluída: {len(df)} registros obtidos.")

    df = transform_data(df)
    logging.info("Transformação concluída: coluna 'Categoria' adicionada.")

    tipos_df = count_by_type(df)
    logging.info(f"Contagem por tipo obtida: {len(tipos_df)} tipos.")

    medias_df = mean_by_type(df)
    logging.info("Cálculo de médias por tipo concluído.")

    top5_df = top_experience(df)
    logging.info("Top 5 Pokémon com maior experiência selecionados.")

    save_csv(tipos_df, "data/relatorio_tipos.csv")
    save_csv(medias_df, "data/relatorio_medias.csv")
    save_csv(top5_df, "data/relatorio_top5.csv")
    logging.info("Relatórios CSV salvos na pasta 'data'.")

    build_graph(tipos_df, "data/grafico_tipos.png")
    logging.info("Gráfico de distribuição por tipo gerado.")

    pie_chart_category(df)
    logging.info("Gráfico de pizza por categoria gerado.")

    plot_strong_pokemons_per_type(df)
    logging.info("Gráfico de concentração dos pokemons fortes.")

    logging.info("Pipeline finalizado com sucesso.")


if __name__ == "__main__":
    rodar_pipeline()
