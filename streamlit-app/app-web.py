import streamlit as st
from src.utils import calc_anio
import matplotlib.pyplot as plt
import numpy as np

if "mensajes" not in st.session_state:
    st.session_state["mensajes"] = list()

messages = st.container(height=800)
if prompt := st.chat_input("Say something"):
    st.session_state["mensajes"].append(("user", prompt))
    if prompt.isdigit():
        st.session_state["edad"] = int(prompt)
        st.session_state["anio"] = calc_anio(st.session_state["edad"])
        resp = f"Naciste en el año {st.session_state['anio']}\nAcá tenés un gráfico de tu edad en función del año:"
    else:
        resp = "Por favor ingresá un número entero para poder calcular tu año de nacimiento"
    st.session_state["mensajes"].append(("assistant", resp))
for mensaje in st.session_state["mensajes"]:
    messages.chat_message(mensaje[0]).write(mensaje[1])


values = st.slider("Seleccioná tu edad", 0, 100, 45,1)
if values is not None:
        st.session_state["edad"] = values
        st.session_state["anio"] = calc_anio(st.session_state["edad"])

if "edad" in st.session_state:
    x = np.arange(st.session_state["anio"],st.session_state["anio"]+st.session_state["edad"]+1)
    y = np.arange(0,st.session_state["edad"]+1)
    fig, ax = plt.subplots()
    ax.plot(x,y)
    ax.grid(True)
    ax.set_ylabel("edad")
    ax.set_xlabel("año")
    messages.pyplot(fig)

