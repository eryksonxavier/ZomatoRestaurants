########################################################
#              Carregando bibliotecas
########################################################

import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
import streamlit as st

st.set_page_config(page_title = 'Visão de Cidades', layout = 'wide', page_icon = '🌆')

########################################################
#              Carregando dados tratados
########################################################

file_path = 'dataset/dados_processados.csv'
data = pd.read_csv(file_path)





########################################################
#              Layout da barra lateral
########################################################

st.sidebar.image('zomato.png', width=200, )

st.sidebar.markdown('# Zomato Restaurants')
st.sidebar.markdown('##### *Conecting people with experiences*')
st.sidebar.markdown("""---""")



paises_selec = st.sidebar.multiselect(label='Selecione os países', 
                       options=['Philippines', 'Brazil', 'Australia', 'United States of America',
       'Canada', 'Singapure', 'United Arab Emirates', 'India',
       'Indonesia', 'New Zeland', 'England', 'Qatar', 'South Africa',
       'Sri Lanka', 'Turkey'],
                       default = ['Philippines', 'Brazil', 'Australia', 'United States of America',
       'Canada', 'Singapure', 'United Arab Emirates', 'India',
       'Indonesia', 'New Zeland', 'England', 'Qatar', 'South Africa',
       'Sri Lanka', 'Turkey'])


#Vinculando os widgets aos dados
linhas_selecionadas = data['country'].isin(paises_selec)
data = data.loc[linhas_selecionadas, :]

st.sidebar.markdown('##### Powered by Erykson Xavier')


########################################################
#              Layout do corpo da página
########################################################


st.markdown("# :city_sunset: Visão de Cidades")

with st.container():
    #st.header('Container 1')
    df_aux = (data[['city', 'restaurant_id', 'country']]
    .groupby(['city', 'country'])
    .count()
    .sort_values(by='restaurant_id', ascending=False)
    .reset_index()).head(10)
    ####
    fig = px.bar(x=df_aux.city, 
                y=df_aux.restaurant_id, 
                color=df_aux.country, 
                labels={'x':'Cidades', 'y':'Número de restaurantes'},
                title='Dez cidades com mais restaurantes registrados')
    st.plotly_chart(fig, use_container_width=True)
    
    
with st.container():
    col1, col2 = st.columns(2)
    #st.header('Container 2')
    with col1:
        df_aux = (data[data['aggregate_rating'] > 4][['city', 'country', 'restaurant_name']]
        .groupby(['city', 'country'])
        .nunique()
        .sort_values(by='restaurant_name', ascending=False)
        .reset_index()).head(7)
        ###
        fig = px.bar(x=df_aux.city, 
            y=df_aux.restaurant_name,
            color=df_aux.country,
            labels={'x':'Cidades', 'y':'Número de restaurantes'},
            title='Sete cidades com mais restaurantes com nota maior que 4.0')
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        df_aux = (data[data['aggregate_rating'] < 2.5][['city', 'country', 'restaurant_name']]
        .groupby(['city', 'country'])
        .nunique()
        .sort_values(by='restaurant_name', ascending=False)
        .reset_index()).head(7)
        ###
        fig = px.bar(x=df_aux.city, 
            y=df_aux.restaurant_name,
            color=df_aux.country,
            labels={'x':'Cidades', 'y':'Número de restaurantes'},
            title='Sete cidades com mais restaurantes com nota menor 2.5')
        st.plotly_chart(fig, use_container_width=True)
    
with st.container():
    #st.header('Container 3')
    df_aux = (data[['city', 'country', 'cuisines']]
    .groupby(['city', 'country'])
    .nunique()
    .sort_values(by='cuisines', ascending=False)
    .reset_index()).head(10)
    ###
    fig = px.bar(x=df_aux.city, 
        y=df_aux.cuisines,
        title='Dez cidades com mais culinárias diferentes',
        labels={'x':'Cidades', 'y':'Número de culinárias diferentes'},
        color=df_aux.country)
    st.plotly_chart(fig, use_container_width=True)