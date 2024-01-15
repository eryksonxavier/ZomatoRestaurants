# Análise de dados para a Zomato Restaurants
Projeto do Curso de Ciência de Dados - by *Comunidade Data Science*
<br>
Veja o WebApp [aqui](https://zomatorestaurants-erykson.streamlit.app/)
---
## **Problema de negócio**
A Zomato é uma plataforma online de estreitamento das relações entre restaurantes e clientes, de modo que os clientes possam avaliar e encontrar suas experiências gastronômicas. Em 2015 a empresa estava rankeada em 99a colocação no Ranking Alexa.
Desta forma, conhecer a distribuição dos restaurantes cadastrados nos países, cidades e culinárias específicas em que atuam é primordial para o crescimento da plataforma.

## **Premissas da solução**
- Marketplace foi o modelo de negócio assumido.
- Os dados utilizados vieram da API da plataforma (https://developers.zomato.com/api/v2.1/search?entity_id=1&entity_type=city&start=1&count=20)
- Os dados foram acessados a partir da plataforma Kaggle (https://www.kaggle.com/datasets/akashram/zomato-restaurants-autoupdated-dataset?resource=download&select=zomato.csv)
- As quatro visões mais importantes são:
  - A visão por geografia
  - A visão por países
  - A visão por cidades
  - A visão por tipo de culinária

## **Estratégia de solução**
- A visão por geografia
  - Mapeamento de restaurantes únicos registrados
  - Mapeamento de cidades únicas registradas
  - Mapeamento do total de tipos de culinária registrados
  - Mapeamento das avaliações médias por pais através de cores
    
- A visão por países
  - Cobertura de restaurantes por pais
  - Cobertura de cidades por pais
  - Nota média por pais
  - Quantidade de avaliaçòes média por pais
  
- A visão por cidades
  - Cidades com mais restaurantes cadastrados
  - Cidades com restaurantes mais bem avaliados
  - Cidades com restaurantes mais mal avaliados
  - Cidades com mais tipos de culinária cadastradas
  
- A visão por tipo de culinária
  - Melhores restaurantes das cinco principais culinárias
  - Culinárias com mais restaurantes
  - Culinárias melhor avaliadas
  - Culinárias pior avaliadas
  - Representatividade relativa das dez culinárias mais comuns
  - Culinárias com mais serviço de delivery melhor avaliadas

## **Principais insights**
- Índia e EUA são os países com maior número de restaurantes e cidades cadastrados
- Indonésia e Índia são os países com maior quantidade média de avaliações
- À execessão do Brasil os 15 demais países tem notas médisa acima de 4.0/5.0 pontos
- Seis das dez cidades com maior número de restaurantes estão na Índia
- Três das sete cidades com avaliação abaixo de 2.5/5.0 estão no Brasil
- A culinária do Norte Indiano é a mais bem representada no banco de dados, representando 24,1% das dez culinárias mais comuns
- A culinária do Norte Indiano é também a que possui maior número de restaurantes que fazem delivery online, mantendo uma nota média de 4.04/5.0 ao redor do mundo

## **Conclusões**
- A Índia e sua culinária seguem sendo as mais populares no conjunto de dados da plataforma.
- Os restaurantes brasileiros cadastrados podem se beneficiar de incentivos para realizar melhorias

## **Próximos passos**
- Atualizar o banco de dados
- Desenvolver métricas mais específicas para entender aspectos a serem priorizados dos restaurantes do conjunto de dados
