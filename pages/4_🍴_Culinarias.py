########################################################
#              Carregando bibliotecas
########################################################

import pandas as pd
import numpy as np
import plotly.express as px
import inflection
import plotly.graph_objs as go
import streamlit as st


st.set_page_config(page_title = 'Visão de Culinárias', layout = 'wide', page_icon = '🍴')

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

nota_inicial, nota_final = st.sidebar.select_slider(label='Escolha o intervalo de notas',
                         options=[0. , 0.5, 1. , 1.5, 2. , 2.5, 3. , 3.5, 4. , 4.5, 5.0],
                         value=(0, 5))
st.sidebar.write('Você escolheu notas entre', nota_inicial, 'e', nota_final)

#Vinculando os widgets aos dados
linhas_selecionadas = data['country'].isin(paises_selec)
data = data.loc[linhas_selecionadas, :]
linhas_selecionadas = (data['aggregate_rating'] >= nota_inicial) & (data['aggregate_rating'] <= nota_final)
data = data.loc[linhas_selecionadas, :]

st.sidebar.markdown('##### Powered by Erykson Xavier')



########################################################
#              Layout do corpo da página
########################################################


# tab1, tab2 = st.tabs(['Visão de Culinárias', '_'])
st.markdown("# :fork_and_knife: Visão de Culinárias")

# with tab1:
    
with st.container():
    cols = ['aggregate_rating', 'restaurant_id', 'restaurant_name', 'average_cost_for_two', 'currency', 'votes', 'country', 'city']
    
    best_JP = (data[data.cuisines == 'Japanese'][cols]
    .sort_values(by=['aggregate_rating', 'restaurant_id'], ascending=[False, True])
    .head(1).reset_index(drop=True))

    best_BR = (data[data.cuisines == 'Brazilian'][cols]
    .sort_values(by=['aggregate_rating', 'restaurant_id'], ascending=[False, True])
    .head(1).reset_index(drop=True))

    best_IT = (data[data.cuisines == 'Italian'][cols]
    .sort_values(by=['aggregate_rating', 'restaurant_id'], ascending=[False, True])
    .head(1).reset_index(drop=True))

    best_IN = (data[data.cuisines == 'Indian'][cols]
    .sort_values(by=['aggregate_rating', 'restaurant_id'], ascending=[False, True])
    .head(1).reset_index(drop=True))

    best_AB = (data[data.cuisines == 'Arabian'][cols]
    .sort_values(by=['aggregate_rating', 'restaurant_id'], ascending=[False, True])
    .head(1).reset_index(drop=True))
    col1, col2, col3, col4, col5 = st.columns(5)
    #Plotando as métricas
    with col1:
        #Japonesa
        st.metric(label=f'Japonesa: {best_JP.restaurant_name[0]}', 
                value=f'{best_JP.aggregate_rating[0]}/5.0',
                help=f"""
                País: {best_JP.country[0]} \n
                Cidade: {best_JP.city[0]} \n
                Preço para duas pessoas: {best_JP.currency[0]}{best_JP.average_cost_for_two[0]} 
                """
                )

    with col2:
        #Brasileira
        st.metric(label=f'Brasileira: {best_BR.restaurant_name[0]}', 
            value=f'{best_BR.aggregate_rating[0]}/5.0',
            help=f"""
            País: {best_BR.country[0]} \n
            Cidade: {best_BR.city[0]} \n
            Preço para duas pessoas: {best_BR.currency[0]}{best_BR.average_cost_for_two[0]} 
            """
            )
    
    with col3:
        #Italiana
        st.metric(label=f'Italiana: {best_IT.restaurant_name[0]}', 
                value=f'{best_IT.aggregate_rating[0]}/5.0',
                help=f"""
                País: {best_IT.country[0]} \n
                Cidade: {best_IT.city[0]} \n
                Preço para duas pessoas: {best_IT.currency[0]}{best_IT.average_cost_for_two[0]} 
                """
                )
    
    with col4:
        #Indiana
        st.metric(label=f'Indiana: {best_IN.restaurant_name[0]}', 
                value=f'{best_IN.aggregate_rating[0]}/5.0',
                help=f"""
                País: {best_IN.country[0]} \n
                Cidade: {best_IN.city[0]} \n
                Preço para duas pessoas: {best_IN.currency[0]}{best_IN.average_cost_for_two[0]} 
                """
                )

    with col5:
        #Árabe
        st.metric(label=f'Árabe: {best_AB.restaurant_name[0]}', 
                value=f'{best_AB.aggregate_rating[0]}/5.0',
                help=f"""
                País: {best_AB.country[0]} \n
                Cidade: {best_AB.city[0]} \n
                Preço para duas pessoas: {best_AB.currency[0]}{best_AB.average_cost_for_two[0]} 
                """
                )
    
    
with st.container():
    # st.header('Cont3')
    df_aux = (data[['cuisines', 'restaurant_id']]
          .groupby('cuisines')
          .count()
          .sort_values(by='restaurant_id', ascending=False)
          .reset_index()).head(10)
    fig = px.bar(x=df_aux.cuisines, 
                y=df_aux.restaurant_id, 
                title="Dez tipos de culinária com maior número de restaurantes", 
                labels={'x': '', 'y':'Quantidade de restaurantes'})
    st.plotly_chart(fig, use_container_width=True)
    
with st.container():
    col1, col2 = st.columns(2)
    with col1:
    # st.header('Cont2')
        df_aux = data.loc[data.cuisines != 'Others', :]
        df_aux = (df_aux[['cuisines', 'aggregate_rating']]
        .groupby('cuisines')
        .mean()
        .sort_values(by='aggregate_rating', ascending=False)
        .reset_index()).head(10)
        fig = px.bar(x=df_aux.cuisines, 
                    y=df_aux.aggregate_rating, 
                    title="Dez tipos de culnária melhor avaliados", 
                    labels={'x': 'Tipos de culinária', 'y':'Média de notas'})
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        df_aux = data.loc[data.cuisines != 'Others', :]
        df_aux = (df_aux[['cuisines', 'aggregate_rating']]
        .groupby('cuisines')
        .mean()
        .sort_values(by='aggregate_rating', ascending=True)
        .reset_index()).head(10)
        fig = px.bar(x=df_aux.cuisines, 
                    y=df_aux.aggregate_rating, 
                    title="Dez tipos de culinária pior avaliados", 
                    labels={'x': 'Tipos de culinária', 'y':'Média de notas'})
        st.plotly_chart(fig, use_container_width=True)
    
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        df_aux = (data[['cuisines', 'restaurant_id']]
            .groupby('cuisines')
            .count()
            .sort_values(by='restaurant_id', ascending=False)
            .reset_index()).head(10)
        fig = px.pie(df_aux,
                    values='restaurant_id',
                    names='cuisines',
                    title="Parcela de mercado das dez culinárias mais comuns",
                    color_discrete_sequence=px.colors.qualitative.Antique)
        st.plotly_chart(fig, use_container_width=True)
        
    with col2:
        df_aux = data.loc[data.cuisines != 'Others', :]
        df_aux = (df_aux[['cuisines', 'has_online_delivery', 'aggregate_rating']]
                .groupby('cuisines')
                .agg({'has_online_delivery': 'sum', 'aggregate_rating':'mean'})
                .round(2)
                .sort_values(by='has_online_delivery', ascending=False)
                .reset_index()).head(10)

        fig = px.sunburst(df_aux, 
                        path = ['cuisines', 'has_online_delivery'], 
                        values = 'has_online_delivery',
                color = 'aggregate_rating', 
                color_continuous_scale = 'PuBu',
                color_continuous_midpoint = np.average(df_aux['aggregate_rating']),
                title='Culinárias com mais serviço de delivery e suas notas')
        fig = fig.update_layout(coloraxis_colorbar_title='Nota média') 
        st.plotly_chart(fig, use_container_width=True)