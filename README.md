# Pokémon Data Analysis Pipeline

Projeto para extrair, transformar, analisar e gerar relatórios visuais sobre dados de Pokémons utilizando a [PokeAPI](https://pokeapi.co/).

---

## Descrição

Este projeto realiza uma pipeline completa que:

- Extrai dados detalhados de Pokémons via API (nome, tipos, status, habilidades, peso, experiência, etc).
- Aplica transformações e categorização (exemplo: categoriza Pokémons em "Fraco", "Médio" e "Forte" pela experiência base).
- Realiza análises estatísticas como média de status por tipo e top 5 Pokémons por experiência.
- Gera gráficos (barras, pizza) para visualização dos dados.
- Exporta relatórios consolidados em CSV e imagens PNG.

---

## Funcionalidades

- Extração paralelizada com cache para acelerar múltiplas execuções.
- Categorização automática dos Pokémons pela experiência.
- Visualização da distribuição por tipo e por categoria.
- Gráfico detalhado dos Pokémons mais fortes por tipo.
- Registro detalhado das etapas da pipeline via logs.

---

## Tecnologias

- Python 3.8+
- pandas
- requests
- matplotlib
- seaborn
- concurrent.futures (paralelismo)
- parquet (cache dos dados)
- logging

---

## Instalação

1. Clone este repositório:

```bash
git clone https://github.com/EdsonBatistele/Teste_onfly.git
cd Teste_onfly
```

2 .Crie e ative um ambiente virtual:

```bash
# Linux/macOS
python -m venv venv

# Windows
source venv/bin/activate
venv\Scripts\activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Execute o código:
```bash
python main.py
```
