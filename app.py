

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Telco Customer Churn EDA", layout="wide")

class DataAnalyzer:

    def __init__(self, df):
        self.df = df

    def dataset_info(self):
        buffer = []
        self.df.info(buf=buffer)
        return buffer

    def variable_types(self):
        numeric = self.df.select_dtypes(include=np.number).columns.tolist()
        categorical = self.df.select_dtypes(exclude=np.number).columns.tolist()
        return numeric, categorical

    def missing_values(self):
        return self.df.isnull().sum()

    def descriptive_stats(self):
        return self.df.describe()

    def mode_values(self):
        return self.df.mode().iloc[0]


st.sidebar.title("Menú")
menu = st.sidebar.radio(
    "Navegación",
    ["Home", "Carga del Dataset", "Análisis Exploratorio (EDA)", "Conclusiones"]
)


if menu == "Home":

    st.title(" Análisis Exploratorio de Clientes - Telco Churn")

    st.markdown("""
    Esta aplicación permite realizar un **Análisis Exploratorio de Datos (EDA)** del dataset
    **TelcoCustomerChurn**, con el objetivo de identificar patrones asociados a la fuga de clientes.

    El análisis se centra en comprender el comportamiento de los clientes mediante
    estadísticas descriptivas y visualizaciones interactivas.
    """)

    st.subheader(" Datos del Autor")

    st.write("**Nombre:** Victor Huamani")
    st.write("**Curso / Especialización:** Python for Analytics")
    st.write("**Año:** 2026")

    st.subheader(" Dataset")

    st.write("""
    El dataset contiene información sobre clientes de una empresa de telecomunicaciones,
    incluyendo:

    - Datos demográficos
    - Servicios contratados
    - Facturación mensual
    - Tiempo de permanencia
    - Estado de abandono (Churn)
    """)

    st.subheader(" Tecnologías utilizadas")

    st.write("""
    - Python
    - Pandas
    - NumPy
    - Streamlit
    - Matplotlib
    - Seaborn
    """)

elif menu == "Carga del Dataset":

    st.title("Carga del Dataset")

    file = st.file_uploader("Sube el archivo TelcoCustomerChurn.csv", type=["csv"])

    if file is not None:

        df = pd.read_csv(file)

        st.success("Archivo cargado correctamente")

        st.subheader("Vista previa")
        st.dataframe(df.head())

        st.subheader("Dimensiones del dataset")

        col1, col2 = st.columns(2)

        col1.metric("Filas", df.shape[0])
        col2.metric("Columnas", df.shape[1])

        st.session_state["df"] = df

    else:
        st.warning("Debes cargar un archivo CSV para continuar")

elif menu == "Análisis Exploratorio (EDA)":

    if "df" not in st.session_state:
        st.warning("Primero debes cargar el dataset")
    else:

        df = st.session_state["df"]

        analyzer = DataAnalyzer(df)

        st.title("Análisis Exploratorio de Datos")

        tabs = st.tabs([
            "Info General",
            "Tipos de Variables",
            "Estadísticas",
            "Valores Faltantes",
            "Distribuciones",
            "Variables Categóricas",
            "Numérico vs Categórico",
            "Categórico vs Categórico",
            "Análisis Dinámico",
            "Hallazgos"
        ])

        
        with tabs[0]:

            st.subheader("Información general")

            st.write("Tipos de datos:")
            st.write(df.dtypes)

            st.write("Valores nulos:")
            st.write(analyzer.missing_values())

    
        with tabs[1]:

            numeric, categorical = analyzer.variable_types()

            col1, col2 = st.columns(2)

            with col1:
                st.subheader("Variables Numéricas")
                st.write(numeric)
                st.write(f"Total: {len(numeric)}")

            with col2:
                st.subheader("Variables Categóricas")
                st.write(categorical)
                st.write(f"Total: {len(categorical)}")

        with tabs[2]:

            st.subheader("Estadísticas descriptivas")

            st.dataframe(analyzer.descriptive_stats())

            st.subheader("Moda")

            st.write(analyzer.mode_values())

    
        with tabs[3]:

            st.subheader(" Analisis de valores faltantes")

            missing = analyzer.missing_values()

            fig, ax = plt.subplots()
            missing.plot(kind="bar", ax=ax)
            plt.xticks(rotation=90)

            st.pyplot(fig)

       
        with tabs[4]:

            st.subheader(" Distribucion de variables numéricas")

            numeric, _ = analyzer.variable_types()

            var = st.selectbox(" Selecciona variable numérica", numeric)

            fig, ax = plt.subplots()

            sns.histplot(df[var], kde=True, ax=ax)

            st.pyplot(fig)

       
        with tabs[5]:

            st.subheader("Análisis de variables categóricas")

            _, cat = analyzer.variable_types()

            var = st.selectbox("Selecciona variable categórica", cat)

            counts = df[var].value_counts()

            fig, ax = plt.subplots()

            sns.barplot(x=counts.index, y=counts.values, ax=ax)

            plt.xticks(rotation=45)

            st.pyplot(fig)

      
        with tabs[6]:

            st.subheader("Numérico vs Categórico")

            num_var = st.selectbox("Variable numérica", ["MonthlyCharges", "tenure"])
            cat_var = "Churn"

            fig, ax = plt.subplots()

            sns.boxplot(x=df[cat_var], y=df[num_var], ax=ax)

            st.pyplot(fig)

       
        with tabs[7]:

            st.subheader("Categórico vs Categórico")

            cat_vars = ["Contract", "InternetService", "PaymentMethod"]

            var = st.selectbox("Selecciona variable", cat_vars)

            table = pd.crosstab(df[var], df["Churn"])

            st.dataframe(table)

            table.plot(kind="bar", stacked=True)

            st.pyplot(plt)

        
        with tabs[8]:

            st.subheader("Análisis dinámico")

            numeric, _ = analyzer.variable_types()

            col = st.selectbox("Variable numérica", numeric)

            min_val = float(df[col].min())
            max_val = float(df[col].max())

            value = st.slider("Filtrar valor", min_val, max_val)

            filtered = df[df[col] >= value]

            st.write("Datos filtrados", filtered.shape)

            st.dataframe(filtered.head())

        with tabs[9]:

            st.subheader("Hallazgos clave")

            st.write("""
            - Los clientes con contratos mensuales presentan mayor churn.
            - Los clientes con menor tenure tienen mayor probabilidad de abandonar.
            - Los cargos mensuales más altos muestran mayor variabilidad en churn.
            - Los servicios adicionales influyen en la retención.
            - Los métodos de pago electrónicos están asociados a mayor churn.
            """)


elif menu == "Conclusiones":

    st.title("Conclusiones del análisis")

    st.write("""
    1. Los clientes con contratos mensuales presentan mayor tasa de abandono.
    2. Los clientes nuevos (tenure bajo) tienen mayor probabilidad de churn.
    3. Los clientes con cargos mensuales altos presentan mayor variabilidad en abandono.
    4. Servicios adicionales como soporte técnico y seguridad online ayudan a retener clientes.
    5. Analizar estos patrones permite diseñar estrategias de retención más efectivas.
    """)
    