import streamlit as st
import pandas as pd
import re
import os
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go


def main():
    st.title("Proyecto Product Development - Fase final")

    # Configuración del menú lateral con botones
    menu = ["Inicio", "Modelo 1", "Modelo 2", "Modelo 3"]
    choice = st.sidebar.button("Inicio")
    if choice:
        mostrar_pagina_inicio()

    for modelo in menu[1:]:
        choice = st.sidebar.button(modelo)
        if choice:
            mostrar_modelo(int(modelo.split()[-1]))

def mostrar_pagina_inicio():
    st.header("Bienvenido a Proyecto Product Development")
    st.write("Fase final")

def mostrar_modelo(numero_modelo):
    st.header(f"Modelo {numero_modelo}")
    st.write(f"Contenido de la página del Modelo {numero_modelo}")

if __name__ == "__main__":
    main()


# Agregar una división en el Sidebar
st.sidebar.markdown("---")

# Agregar texto con el logo de Streamlit
st.sidebar.markdown(
        '<h6>Made in &nbsp<img src="https://streamlit.io/images/brand/streamlit-mark-color.png" alt="Streamlit logo" height="16">&nbsp by Jonathan Maldonado & Jose Carias</h6>',
        unsafe_allow_html=True,
    )

    

