import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')

st.header("Tablero interactivo sobre datos de vehiculos usados")

hist_button = st.button('Construir histograma') # crear un botón

if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

build_scatter = st.checkbox('Construir un scatterplot')

if build_scatter:
    st.write('Construyendo un grafico de dispercion')
    
    fig = px.scatter(car_data, x="odometer", y="price") # crear un gráfico de dispersión
    st.plotly_chart(fig, use_container_width=True)
    
build_lineplot = st.checkbox('Construir lineplot')

if build_lineplot:
    st.write('---')
    
    car_line = car_data.groupby(['date_posted','condition'])['price'].mean().reset_index()
    fig = px.line(car_line, x="date_posted", y="price", color='condition')
    st.plotly_chart(fig, use_container_width=True)
