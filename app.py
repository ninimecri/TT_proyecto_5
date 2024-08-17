import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar datos
car_data = pd.read_csv('vehicles_us.csv')

# Mostrar las primeras filas del DataFrame
print(car_data.head())

# Encabezado de la aplicación
st.header('Proyecto 6: Análisis de Autos Usados')

# Botón para generar el histograma
if st.button('Mostrar Histograma'):
    st.write("Histograma de la distribución de Precios")
    fig_hist = px.histogram(car_data, x="price", title="Distribución de Precios de Vehículos",
                            color_discrete_sequence=px.colors.qualitative.Set1)
    st.plotly_chart(fig_hist)

# Convertir 'condition' a categórica para el gráfico de dispersión
car_data['condition'] = car_data['condition'].astype('category')

# Botón para generar el gráfico de dispersión
if st.button('Mostrar Gráfico de Dispersión'):
    st.write("Gráfico de dispersión de 'Precio' contra 'Condición'")
    fig_scatter = px.scatter(car_data,
                             x='price',
                             y='condition',
                             color='condition',
                             title="Precio vs Condición de Vehículos",
                             hover_data=["model_year", "odometer"],
                             color_discrete_sequence=px.colors.qualitative.Set2)
    st.plotly_chart(fig_scatter)

# Casilla de verificación para un histograma interactivo
if st.checkbox('Mostrar Histograma Interactivo'):
    st.write("Histograma Interactivo de la columna 'price'")
    fig_hist_interactive = px.histogram(car_data, x="price", title="Distribución de Precios de Vehículos",
                                        color_discrete_sequence=px.colors.qualitative.Set1)
    fig_hist_interactive.update_layout(
        xaxis_title='Precio',
        yaxis_title='Frecuencia',
        xaxis=dict(
            title='Precio',
            showgrid=True,
            zeroline=False
        ),
        yaxis=dict(
            title='Frecuencia',
            showgrid=True,
            zeroline=False
        )
    )
    st.plotly_chart(fig_hist_interactive)

# Casilla de verificación para el gráfico de dispersión
if st.checkbox('Mostrar Gráfico de Dispersión Interactivo'):
    st.write("Gráfico de dispersión de 'Precio' contra 'Condición'")
    fig_scatter_interactive = px.scatter(car_data,
                                         x='price',
                                         y='condition',
                                         color='condition',
                                         title="Precio vs Condición de Vehículos",
                                         hover_data=["model_year", "odometer"],
                                         color_discrete_sequence=px.colors.qualitative.Set2)
    fig_scatter_interactive.update_layout(
        xaxis_title='Precio',
        yaxis_title='Condición',
        xaxis=dict(
            title='Precio',
            showgrid=True,
            zeroline=False
        ),
        yaxis=dict(
            title='Condición',
            showgrid=True,
            zeroline=False,
            type='category'
        )
    )
    st.plotly_chart(fig_scatter_interactive)
