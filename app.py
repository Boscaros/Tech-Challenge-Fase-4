import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import subprocess
import urllib.request
import requests
from PIL import Image
from io import BytesIO

from utils import url_predicao

st.title('Variação do Preço por Barril do Petróleo Bruto Brent (FOB)')
# st.write('# Dados')

st.write('# Projeto Final')

st.write('## Preço do Petróleo')
paragraphs = [
        "Análise da Flutuação do Preço do Petróleo ao Longo do Tempo.",
        "Este estudo examina a dinâmica do preço do petróleo em diferentes períodos. É possível ajustar as datas de referência e observar a tabela e o gráfico correspondentes à variação do preço conforme a data selecionada."
    ]

for paragraph in paragraphs:
        st.write(paragraph)

# Carregar o arquivo Excel usando pandas
df = pd.read_csv("https://raw.githubusercontent.com/Boscaros/Previs-o-Preco-Petr-leo/refs/heads/main/base%20preco%20pretoleo.csv", sep=';')

# Exibir os dados no Streamlit

data_inicial_padrao = pd.to_datetime('1987-05-20').date()
data_final_padrao = pd.to_datetime('2025-01-21').date()
    
data_inicial = st.date_input("Data Inicial", value=data_inicial_padrao, max_value=pd.to_datetime('2025-01-21').date())
data_final = st.date_input("Data Final", value=data_final_padrao, min_value=pd.to_datetime('1987-05-10').date())

# Modificando o Nome das Colunas
df.rename(columns={'Data': 'data', 'Preço do Petróleo': 'preco'}, inplace=True)
df['preco'] = df['preco'].str.replace(',', '.')
df['preco'] = df['preco'].astype(float)
df['data'] = pd.to_datetime(df['data']).dt.date

df_filtrado = df[(df['data'] >= data_inicial) & (df['data'] <= data_final)]

x = df_filtrado['data']
y = df_filtrado['preco']

plt.plot(df_filtrado['data'], df_filtrado['preco'], marker='o')
plt.xlabel('Data')
plt.ylabel('Preço')
plt.title('Preço ao longo dos anos')

st.pyplot(plt)

st.markdown("<hr>", unsafe_allow_html=True)

st.write('## Prevendo o valor do barril de Petróleo com Prophet')
paragraphs = [
        "Para prever os valores do barril do Petróleo dos próximos 30 dias usei o modelo de Machine Learning Prophet.",
        "A previsão do Prophet teve um MAPE de 2.84%.",
    ]

for paragraph in paragraphs:
        st.write(paragraph, format='markdown')
url_predicao = "https://raw.githubusercontent.com/Boscaros/Tech-Challenge-Fase-4/refs/heads/main/previs%C3%A3o%20preco%20petroleo.png"
st.image(url_predicao, use_column_width=True, caption="Previsão")

st.write('Fonte: Código Python disponível no Github')
st.write('Clique [aqui](https://github.com/Boscaros/Tech-Challenge-Fase-4/blob/main/Machine_Learning_Pre%C3%A7o_do_Petr%C3%B3leo.ipynb)')

st.markdown("<hr>", unsafe_allow_html=True)

st.write('## Dashboard Power Bi')
paragraphs = [
        'O Dashboard mostra as varições do preço ao longo dos anos',
        'Para acessar todos os recursos, recomendo clicar no link e baixar o arquivo do Power Bi.'
    ]

for paragraph in paragraphs:
    st.write(paragraph)

    img_url = "https://raw.githubusercontent.com/Boscaros/Tech-Challenge-Fase-4/refs/heads/main/preco%20petroleo%20pbi.png"

st.image(img_url, use_column_width=True, caption="Foto do Dashboard")

st.write('Clique [aqui](https://github.com/Boscaros/Tech-Challenge-Fase-4/blob/main/Pre%C3%A7o%20Petroleo.pbix) para abrir o arquivo Power BI no Github')

st.markdown("<hr>", unsafe_allow_html=True)



st.markdown('<p class="footer"> Tech Challenge Fase 4 - Thiago Boscaro </p)', unsafe_allow_html=True)
