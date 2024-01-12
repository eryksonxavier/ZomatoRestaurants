########################################################
#              Carregando bibliotecas
########################################################

import pandas as pd #biblioteca para tratamento dos dados
import plotly as pl #biblioteca para plotarmos os graficos
import haversine as hs #biblioteca para fazermos o calculo da localização dos restaurantes usando as coordenadas disponibilizadas
import inflection #biblioteca com diversas funções para fazermos mudanças em strings, por exemplo, converter de letra maisucula para minuscula e etc...
import numpy as np
import plotly.express as px
import folium
from folium.plugins import MarkerCluster
import streamlit as st
from streamlit_folium import folium_static
from PIL import Image

st.set_page_config(page_title = 'Visão Geográfica', layout='wide', page_icon = '🌎')

########################################################
#              Carregando dados tratados
########################################################

file_path = 'dataset/dados_processados.csv'
data = pd.read_csv(file_path)


#==========================================================================================================
#-------------------------------------------FUNÇÕES--------------------------------------------------------
#==========================================================================================================

#--------------------------------FUNÇÃO PARA PLOTAR O MAPA:-------------------------------------------------

def mapa(data):
	f = folium.Figure(width=1920, height=1080)
	m = folium.Map(max_bounds=True).add_to(f)
	marker_cluster = MarkerCluster().add_to(m)
	for _, line in data.iterrows():
	
		name = line["restaurant_name"]
		price_for_two = line["average_cost_for_two"]
		cuisine = line["cuisines"]
		currency = line["currency"]
		rating = line["aggregate_rating"]
		color = f'{line["color_name"]}'

		html = "<p><strong>{}</strong></p>"
		html += "<p>Price: {},00 ({}) para dois"
		html += "<br />Type: {}"
		html += "<br />Aggragate Rating: {}/5.0"
		html = html.format(name, price_for_two, currency, cuisine, rating)

		popup = folium.Popup(
			folium.Html(html, script=True),
			max_width=500,
		)

		folium.Marker(
			[line["latitude"], line["longitude"]],
			popup=popup,
			icon=folium.Icon(color=color, icon="home", prefix="fa"),
		).add_to(marker_cluster)

	folium_static(m, width=1280, height=720)


#==========================================================================================================
#-------------------------------------------LAYOUT STREAMLIT-----------------------------------------------
#==========================================================================================================
st.markdown('# :earth_americas: Visão Geográfica')
st.markdown('##### Abaixo você encontrará informações úteis para análise geral e geográfica do negócio:')


#==========================================================================================================
#-------------------------------------------SIDEBAR--------------------------------------------------------
#==========================================================================================================


image = Image.open('zomato.png')
st.sidebar.image( image, width=280 )

st.sidebar.markdown('# Zomato Restaurants')
st.sidebar.markdown('##### *Conecting people with experiences*')
st.sidebar.write("""---""")


st.sidebar.markdown('## Selecione os países que deseja analisar:')
countries = st.sidebar.multiselect(
        "Escolha os Paises que Deseja visualizar os Restaurantes",
        data.loc[:, "country"].unique().tolist(),
        default=['India','Australia','Brazil','Canada','England','United States of America'],
)


st.sidebar.markdown("### Dados Tratados")

processed_data = pd.read_csv("dataset/dados_processados.csv")

st.sidebar.download_button(
    label="Download",
    data=processed_data.to_csv(index=False, sep=";"),
    file_name="dados.csv",
    mime="text/csv",
)

st.sidebar.write("""---""")
st.sidebar.write('Powered by Erykson Xavier')

#---------------------------------ATIVAÇÃO DOS FILTROS DO SIDEBAR------------------------------------------

paises_selecionados = data['country'].isin(countries)
data = data.loc[paises_selecionados,:]


#==========================================================================================================
#-------------------------------------------MAINPAGE-------------------------------------------------------
#==========================================================================================================

with st.container():
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        qtd_restaurantes = len(data['restaurant_id'].unique())
        col1.metric('Restaurantes Cadastrados:', qtd_restaurantes)
        
    with col2:
        qtd_paises = len(data['country'].unique())
        col2.metric('Países Atendidos:', qtd_paises)
        
    with col3:
        qtd_cidades = len(data['city'].unique())
        col3.metric('Cidades Atendidas:', qtd_cidades)
        
    with col4:
        colunas = ['restaurant_id', 'votes']
        df2 = data.loc[:,colunas].groupby(['restaurant_id']).max().reset_index()
        qtd_total_avaliacoes = df2['votes'].sum()
        col4.metric('Avaliações Totais:', qtd_total_avaliacoes)
        
    with col5:
        tipos_de_culinarias = len(data['cuisines'].unique())
        col5.metric('Tipos de culinárias:', tipos_de_culinarias)

with st.container():
   mapa(data)





