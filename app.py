import streamlit as st
import pandas as pd
import plotly_express as px

car_data = pd.read_csv('streamlit/vehicles_us.csv')  # leer los datos

print(car_data.head())

st.header('Analisis de autos usados')
hist_button = st.button('Construccion histograma')

# Botón para generar el histograma
if st.button('Mostrar Histograma'):

    st.write("Histograma de la columna 'x'")
    fig = px.histogram(car_data, x='x', nbins=5)
    st.plotly_chart(fig)

scatter_button = st.button('Construccion gráfico de dispersión')

# Botón para generar el gráfico de dispersión
if st.button('Mostrar Gráfico de Dispersión'):

    st.write("Gráfico de dispersión de 'x' contra 'y'")
    fig = px.scatter(car_data, x='x', y='y')
    st.plotly_chart(fig)

st.write("### Desafío Extra: Generar Gráficos con Casillas de Verificación")

# Casilla de verificación para el histograma
if st.checkbox('Generar Histograma'):
    st.write("Histograma de la columna 'x'")
    fig = px.histogram(car_data, x='x', nbins=5, title='Histograma de X')
    st.plotly_chart(fig)
