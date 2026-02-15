import streamlit as st 
import Funciones as fun 


st.title("Aplicacion de funciones")
capital=st.number_input("ingrese el capital:", 100, 10000,1000)
tiempo=st.number_input("ingrese el tiempo:", value=12)
tasa_interes=st.number_input("ingrese la tasa de interes:", value=0.05)

interes=fun.interes_simple(capital_inicial=capital, tiempo_meses=tiempo, tasa_interes=tasa_interes )
st.write("el interes simple es:", int(interes))

