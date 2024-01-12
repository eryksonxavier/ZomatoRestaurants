import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Home",
    page_icon="🎲"
)


# image_path = 'Documents/repos/dashboards/logo.png' =========> Não estou conseguindo fazer com que abra pelo arquivo

# image_path='C:/Users/EngKa/Documents/repos/pa_ftc/zomato.png'
image = Image.open('zomato.png')
st.sidebar.image( image, width=280 )

st.sidebar.markdown( '# Zomato Restaurants' )
st.sidebar.markdown( '### Seja bem vindo(a) ao estudo dos dados da empresa Zomato Restaurants' )
st.sidebar.markdown( """---""" )

st.write( "# Zomato Restaurants Data Dashboard" )

st.markdown(
""" Seja bem vindo ao Dashboard dinâmico da empresa Zomato Restaurants,
    este dashboard foi construído para o acompanhamento das métricas da empresa baseado em 4 visões importantes para o negócio: Visão Geográfica, Visão Paises, Visão Cidades e Visão Cozinhas.
    
    ### Como utilizar esse Dashboard?
    - Visão Geográfica:    
        - Acompanhamento da distribuição geográfica dos restaurantes, clusterizado por regiões (continentes, países e cidades)     
    - Visão Países:    
        - Acompanhamento dos indicadores de crescimento dos restaurantes e satisfação dos clientes.       
    - Visão Cidades: 
        - Acompanhamento dos indicadores dos restaurantes, as cidades com mais restaurantes cadastrados, as com melhor média de avaliação e etc.
    - Visão Culinárias:
        - Acompanhamento dos melhores e piores restaurantes e culinárias
    ### Ask for Help - Entre em contato com o desenvolvedor:
    - Discord: eryksonxavier
    - Email: erykson.soares@gmail.com
    - LinkedIn: https://www.linkedin.com/in/eryksonsoares/
    - GitHub: https://github.com/eryksonxavier
"""
)

#st.sidebar.markdown( """---""" )

st.sidebar.markdown('### Powered by Erykson Xavier')