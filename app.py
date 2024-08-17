import streamlit as st
import pandas as pd
import plotly_express as px

car_data = pd.read_csv('vehicles_us.csv')  # leer los datos

print(car_data.head())

st.header('Analisis de autos usados')
hist_button = st.button('Construccion histograma')

# Botón para generar el histograma
if st.button('Mostrar Histograma'):
    st.write("Histograma de la distribución de Precios")
    fig = px.histogram(car_data, x="price", title="Distribución de Precios de Vehículos",
                       color_discrete_sequence=px.colors.qualitative.Set1)  # crear un histograma
    st.plotly_chart(fig)

scatter_button = st.button('Construccion gráfico de dispersión aqui')

# Botón para generar el gráfico de dispersión
car_data['condition'] = car_data['condition'].astype('category')

if st.button('Mostrar Gráfico de Dispersión'):

    st.write("Gráfico de dispersión de 'Precio' contra 'Condicion'")

    # Crear el gráfico de dispersión con diferenciación de colores basada en 'condition'
    fig = px.scatter(car_data,
                     x='price',
                     y='condition',
                     color='condition',
                     title="Precio vs Condición de Vehículos",
                     hover_data=["model_year", "odometer"],
                     color_discrete_sequence=px.colors.qualitative.Set2)  # Colores claros

    st.plotly_chart(fig)

st.write("### Desafío Extra: Generar Gráficos con Casillas de Verificación")

# Casilla de verificación para el histograma
if st.checkbox('Generar Histograma'):
    st.write("Histograma de la columna 'x'")
    fig = px.histogram(car_data, x="price", title="Distribución de Precios de Vehículos",
                       color_discrete_sequence=px.colors.qualitative.Set1)
    st.plotly_chart(fig)
