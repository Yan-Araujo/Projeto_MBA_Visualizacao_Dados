# Importação das bibliotecas necessárias
import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.set_page_config(page_title="Dashboard - Breast Cancer Dataset")

csv_file = "dados.csv"

if os.path.exists(csv_file):
  df = pd.read_csv(csv_file)

  chart_colors = ['#4682B4', '#FF6347']

  st.markdown("""
  #### 1.⁠ ⁠Introdução do Problema:
  - O governo enfrenta um grande desafio no diagnóstico de tumores malignos e benignos: identificar quais tumores realmente necessitam de cirurgia. A meta é otimizar o tratamento dos pacientes, garantindo que as intervenções cirúrgicas ocorram apenas quando absolutamente necessárias. Isso visa melhorar a qualidade de vida dos pacientes e economizar recursos médicos.

  #### 2.⁠ ⁠Histórico
  - Cenário atual: Todos os anos, milhares de pacientes são diagnosticados com tumores. Porém, nem todos os tumores precisam de cirurgia. Decisões sem uma análise detalhada podem levar a cirurgias desnecessárias, causando desgaste ao paciente, aumento de custos e sobrecarga no sistema de saúde.
  Desafio: Como determinar, com precisão, quais tumores benignos podem ser tratados de forma conservadora e quais malignos realmente precisam de cirurgia? A resposta está na análise das características dos tumores.
  """)

  st.markdown("### Dashboard dos Dados de Câncer de Mama")

  st.markdown("""
  #### 3.⁠ ⁠Apresentação dos Dados
  Fontes de Dados: Os dados analisados foram retirados da base disponível no https://www.kaggle.com e incluem variáveis como tamanho do tumor, concavidade, perímetro e simetria, que ajudam a indicar a gravidade do tumor.
  Segmentação: Utilizamos dois valores-chave para segmentar os tumores:

  - Maligno (valor 1): Tumores que geralmente exigem cirurgia.

  - Benigno (valor 0): Tumores que podem ser tratados com métodos menos invasivos.
  """)

  st.markdown("")

  # Exibir os dados carregados
  st.markdown("#### Dados de Câncer de Mama Carregados")
  st.dataframe(df.head())

  # Filtros de seleção
  st.sidebar.header("Filtros")
  selected_diagnosis = st.sidebar.multiselect(
    "Selecione o Tipo de Tumor", 
    options=df['diagnosis'].unique(), 
    default=df['diagnosis'].unique())
  
  selected_radius_mean = st.sidebar.slider(
    "Selecione o Raio Médio", 
    df['radius_mean'].min(), 
    df['radius_mean'].max(), 
    (df['radius_mean'].min(), df['radius_mean'].max()))
  
  selected_perimeter_mean = st.sidebar.slider(
    "Selecione o Perímetro Médio", 
    df['perimeter_mean'].min(), 
    df['perimeter_mean'].max(), 
    (df['perimeter_mean'].min(), df['perimeter_mean'].max()))
  
  selected_area_mean = st.sidebar.slider(
    "Selecione a Área Média", 
    df['area_mean'].min(), 
    df['area_mean'].max(), 
    (df['area_mean'].min(), df['area_mean'].max()))
  
  selected_concavity_mean = st.sidebar.slider(
    "Selecione a Concavidade Média", 
    df['concavity_mean'].min(), 
    df['concavity_mean'].max(), 
    (df['concavity_mean'].min(), df['concavity_mean'].max()))
  
  selected_concave_points_mean = st.sidebar.slider(
    "Selecione o Ponto Côncavo Médio", 
    df['concave points_mean'].min(), 
    df['concave points_mean'].max(), 
    (df['concave points_mean'].min(), df['concave points_mean'].max()))
  
  selected_symmetry_mean = st.sidebar.slider(
    "Selecione a Simetria Média", 
    df['symmetry_mean'].min(), 
    df['symmetry_mean'].max(), 
    (df['symmetry_mean'].min(), df['symmetry_mean'].max()))

  # Filtragem dos dados com base na seleção do usuário
  filtered_df = df[(df['diagnosis'].isin(selected_diagnosis)) & 
                    (df['radius_mean'] >= selected_radius_mean[0]) & 
                    (df['radius_mean'] <= selected_radius_mean[1]) & 
                    (df['perimeter_mean'] >= selected_perimeter_mean[0]) & 
                    (df['perimeter_mean'] <= selected_perimeter_mean[1]) & 
                    (df['area_mean'] >= selected_area_mean[0]) & 
                    (df['area_mean'] <= selected_area_mean[1]) & 
                    (df['concavity_mean'] >= selected_concavity_mean[0]) & 
                    (df['concavity_mean'] <= selected_concavity_mean[1]) & 
                    (df['concave points_mean'] >= selected_concave_points_mean[0]) & 
                    (df['concave points_mean'] <= selected_concave_points_mean[1]) & 
                    (df['symmetry_mean'] >= selected_symmetry_mean[0]) & 
                    (df['symmetry_mean'] <= selected_symmetry_mean[1])]

  # Exibindo os dados filtrados
  st.markdown("#### Dados Filtrados")
  st.dataframe(filtered_df)
  
  st.markdown("""
  #### 4.⁠ ⁠Contexto dos Dados
  Com análises avançadas, identificamos padrões no comportamento dos tumores com base em suas características. Aqui destacamos duas frentes principais da análise:

  Histograma de Diagnóstico x Área Média do Tumor:
  Um histograma foi gerado para correlacionar a frequência de tumores malignos e benignos com a área média (area_mean). A análise mostra que tumores malignos tendem a ter áreas médias maiores, enquanto a maioria dos tumores benignos está associada a áreas menores. Esse padrão pode auxiliar os médicos a priorizarem tumores que merecem maior atenção cirúrgica.

  Gráficos de Dispersão:
  Para melhor visualizar as correlações entre a área média do tumor e outras características, gráficos de dispersão foram gerados:

  - Área Média x Raio Médio (radius_mean): Tumores malignos, em geral, apresentam tanto uma área quanto um raio médio maiores.

  - Área Média x Perímetro Médio (perimeter_mean): Existe uma forte correlação entre o perímetro e a área, reforçando que tumores com maior perímetro também tendem a ser malignos.

  - Área Média x Concavidade Média (concavity_mean): Tumores com concavidades acentuadas também apresentam maior área, um indicativo de malignidade.

  - Área Média x Simetria Média (symmetry_mean): Tumores mais assimétricos tendem a ter uma área maior, o que pode ser outro indicativo de malignidade.

  Esses gráficos de dispersão revelaram padrões consistentes que ajudam na classificação dos tumores e na tomada de decisões sobre intervenções cirúrgicas.
  """)

  st.markdown('#### Divisão dos tumores dos dados filtrados')
  fig_amount = px.pie(
      filtered_df, 
      values='id', 
      names='diagnosis', 
      title="Quantidade de Tumores por Tipo de Diagnóstico",
      color='diagnosis')
  st.plotly_chart(fig_amount, use_container_width=True)

  st.markdown('#### Quantidade de Tumores')

  total_tumors = filtered_df.shape[0]
  total_benign_tumors = filtered_df['diagnosis'].value_counts().get('B', 0)
  total_maligning_tumors = filtered_df['diagnosis'].value_counts().get('M', 0)

  kpi0, kpi1, kpi2 = st.columns(3)
  kpi0.metric(label="Quantidade Total de Tumores", value=f"{total_tumors}")
  kpi1.metric(label="Quantidade de Tumores Benignos", value=f"{total_benign_tumors}")
  kpi2.metric(label="Quantidade de Tumores Malignos", value=f"{total_maligning_tumors}")
  
  st.markdown('#### Valores Médios dos dados filtrados')
  avg_radius_mean = filtered_df['radius_mean'].mean()
  avg_perimeter_mean = filtered_df['perimeter_mean'].mean()
  avg_area_mean = filtered_df['area_mean'].mean()
  avg_concavity_mean = filtered_df['concavity_mean'].mean()
  avg_concave_points_mean = filtered_df['concavity_mean'].mean()
  avg_symmetry_mean = filtered_df['symmetry_mean'].mean()
  
  # KPIs de valores médios
  kpi3, kpi4, kpi5 = st.columns(3)
  kpi3.metric(label="Raio Médio", value=f"{avg_radius_mean:,.2f}")
  kpi4.metric(label="Perímetro Médio", value=f"{avg_perimeter_mean:,.2f}")
  kpi5.metric(label="Área Média", value=f"{avg_area_mean:,.2f}")
  
  kpi6, kpi7, kpi8 = st.columns(3)
  kpi6.metric(label="Concavidade Média", value=f"{avg_concavity_mean:,.2f}")
  kpi7.metric(label="Ponto Côncavos Médio", value=f"{avg_concave_points_mean:,.2f}")
  kpi8.metric(label="Simetria Média", value=f"{avg_symmetry_mean:,.2f}")
  
  fig_mean_area = px.histogram(
    filtered_df, 
    x="area_mean", 
    color="diagnosis",
    title='Contagem das Áreas dos Tumores'
  )
  st.plotly_chart(fig_mean_area, use_container_width=True)

  fig_scatter_matrix = px.scatter_matrix (
    filtered_df,
    dimensions=['area_mean', 'radius_mean', 'perimeter_mean', 'concavity_mean', 'symmetry_mean'],
    color='diagnosis',
    title='Matriz de Dispersão - Média da Área, Raio, Perimetro, Concavidade e Simetria',
    width=800,
    height=800
  )
  st.plotly_chart(fig_scatter_matrix, use_container_width=True)

  st.markdown("""
  #### 5.⁠ ⁠Soluções e Insights
  A partir dessa análise, os insights principais incluem:

  - Priorização de Cirurgia para Tumores Malignos: Tumores com maior área, raio e concavidade devem ser priorizados para intervenção cirúrgica.

  - Monitoramento de Tumores Benignos: Tumores com características que indicam menor gravidade, como tamanho e concavidade menores, podem ser monitorados com métodos menos invasivos.

  - Atenção aos Tumores em Evolução: Tumores que demonstram crescimento rápido ou mudanças significativas na forma, mesmo que inicialmente benignos, devem ser acompanhados de perto.
    
  """)
  
else:
  st.write(f"Arquivo '{csv_file}' não encontrado. Por favor, coloque o arquivo na mesma pasta que este script.")
