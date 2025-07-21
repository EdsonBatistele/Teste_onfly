import matplotlib.pyplot as plt
import seaborn as sns
import seaborn as sns
import logging


def save_csv(df, path="data/relatorio.csv"):
    """
    Salva um DataFrame em um arquivo CSV no caminho especificado.

    Args:
        df (pandas.DataFrame): DataFrame a ser salvo.
        path (str, optional): Caminho do arquivo CSV de destino. Padrão é "data/relatorio.csv".

    Returns:
        None
    """
    logging.info("Salvando relatório CSV...")
    df.to_csv(path, index=False)


def build_graph(tipo_df, path="data/grafico_tipos.png"):
    """
    Gera e salva um gráfico de barras da distribuição de Pokémons por tipo.

    Args:
        tipo_df (pandas.DataFrame): DataFrame contendo as colunas 'Tipo' e 'Quantidade' para o gráfico.
        path (str, optional): Caminho onde o gráfico será salvo como imagem PNG. Padrão é "data/grafico_tipos.png".

    Returns:
        None
    """
    logging.info("Gerando gráfico de distribuição por tipo...")
    plt.figure(figsize=(14, 7))
    ax = sns.barplot(x="Tipo", y="Quantidade", data=tipo_df, palette="viridis")
    
    for p in ax.patches:
        height = p.get_height()
        ax.annotate(f'{height}', (p.get_x() + p.get_width() / 2., height),
                    ha='center', va='bottom', fontsize=10, color='black')
    
    plt.xticks(rotation=45, ha='right')
    plt.ylabel("Quantidade")
    plt.xlabel("Tipo")
    plt.title("Distribuição de Pokémons por Tipo", fontsize=16, weight='bold')
    plt.tight_layout()
    plt.savefig(path, dpi=300)
    plt.close()


def pie_chart_category(df, path="data/grafico_categoria.png"):
    """
    Gera e salva um gráfico de pizza mostrando a distribuição percentual de Pokémons por categoria.

    Args:
        df (pandas.DataFrame): DataFrame contendo a coluna 'Categoria' com as categorias dos Pokémons.
        path (str, optional): Caminho para salvar o gráfico em formato PNG. Padrão é "data/grafico_categoria.png".

    Returns:
        None
    """
    counts = df["Categoria"].value_counts()
    plt.figure(figsize=(8, 8))
    plt.pie(
        counts,
        labels=counts.index,
        autopct="%1.1f%%",
        startangle=140,
        colors=["#ff9999", "#66b3ff", "#99ff99"],
    )
    plt.title("Distribuição percentual de Pokémons por Categoria")
    plt.axis("equal")
    plt.tight_layout()
    plt.savefig(path)
    plt.close()
    print(f"Gráfico de pizza salvo em {path}")


def plot_strong_pokemons_per_type(df, path="data/grafico_fortes_por_tipo.png"):
    """
    Gera e salva um gráfico de barras mostrando a quantidade de Pokémons classificados como 'FORTE' por tipo.

    Args:
        df (pandas.DataFrame): DataFrame contendo as colunas 'Categoria' e 'Tipos' (lista de tipos).
        path (str, optional): Caminho para salvar o gráfico em formato PNG. Padrão é "data/grafico_fortes_por_tipo.png".

    Returns:
        None
    """
    df_exploded = df.explode("Tipos")
    fortes = df_exploded[df_exploded["Categoria"] == "FORTE"]
    contagem = fortes["Tipos"].value_counts().reset_index()
    contagem.columns = ["Tipo", "Quantidade"]
    plt.figure(figsize=(12, 6))
    sns.barplot(data=contagem, x="Tipo", y="Quantidade", palette="Reds_d")
    plt.title("Quantidade de Pokémons FORTES por Tipo")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(path)
    plt.close()
    print(f"Gráfico salvo em {path}")
