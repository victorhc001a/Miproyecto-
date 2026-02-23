import streamlit as st
import pandas as pd

# -----------------------------
# CONFIG (siempre primero)
# -----------------------------
st.set_page_config(page_title="Proyecto Python Fundamentals", page_icon="✅", layout="wide")


# -----------------------------
# TEMA DE LA PAGINA
# -----------------------------
def apply_custom_css() -> None:
    css = """
    <style>
        /* App background */
        .stApp {
            background: linear-gradient(120deg, #FFFFFF 0%, #EEF3FB 60%, #FFFFFF 100%);
            color: #1B2430;
        }

        /* Sidebar */
        section[data-testid="stSidebar"] {
            background-color: #171D2A;
            border-right: 1px solid rgba(255,255,255,0.06);
        }
        section[data-testid="stSidebar"] * {
            color: #E8EEF9 !important;
        }

        /* Hide Streamlit default footer/menu */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}

        /* Containers */
        .dmc-hero {
            background: #F5F7FB;
            border: 1px solid #DDE6F5;
            border-radius: 18px;
            padding: 22px 24px;
            box-shadow: 0 10px 25px rgba(23, 29, 42, 0.08);
        }
        .dmc-card {
            background: #F5F7FB;
            border: 1px solid #DDE6F5;
            border-radius: 16px;
            padding: 16px 18px;
            box-shadow: 0 8px 20px rgba(23, 29, 42, 0.06);
        }
        .dmc-muted {
            color: #5B6777;
        }

        /* Buttons */
        div.stButton > button {
            border-radius: 12px;
            border: 1px solid #DDE6F5;
            padding: 0.55rem 0.9rem;
        }
        div.stButton > button:hover {
            border-color: #249CEC;
        }

        /* Inputs */
        div[data-baseweb="input"] > div {
            border-radius: 12px !important;
        }
        div[data-baseweb="select"] > div {
            border-radius: 12px !important;
        }

        /* Dataframe */
        .stDataFrame {
            border-radius: 14px;
            overflow: hidden;
        }

        /* Tarjeta para TITULOS (opcional, estilo imagen) */
        .title-card{
            background-color: white;
            padding: 16px;
            border-radius: 15px;
            border: 2px solid #e5e7eb;
            box-shadow: 0 8px 20px rgba(0,0,0,0.08);
            text-align: center;
            margin-bottom: 14px;
        }
        .title-card h1{
            color: #111827 !important;
            margin: 0;
            font-weight: 800;
        }

        /* Estilo tipo dmc-card para contenedores con borde (evita error removeChild) */
        div[data-testid="stVerticalBlockBorderWrapper"]{
            background: #F5F7FB;
            border: 1px solid #DDE6F5 !important;
            border-radius: 16px !important;
            padding: 16px 18px !important;
            box-shadow: 0 8px 20px rgba(23, 29, 42, 0.06) !important;
        }

    </style>
    """
    st.markdown(css, unsafe_allow_html=True)


def title_card(text: str) -> None:
    """Título con el mismo look de tu imagen (caja blanca + borde)."""
    st.markdown(f"""
        <div class="title-card">
            <h1>{text}</h1>
        </div>
    """, unsafe_allow_html=True)


# --------
# HOME
# --------
def render_home() -> None:
    title_card("📚 Proyecto Fundamentos de Programación 💻")

    st.markdown(
        """
        <div class="dmc-hero">
            <p class="dmc-muted" style="margin:0;">
                Aplicación interactiva en Streamlit que integra conceptos de programación:
                variables, estructuras de datos, control de flujo, funciones, programación funcional y Programación Orientada a Objetos.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")
    c1, c2 = st.columns([1.25, 1])

    with c1:
        st.markdown("### Bienvenidos a la aplicación")
        st.write("**📝 Realizado por:** _victor Huamani Curo_")
        st.write("**📝 Módulo:** Python Fundamentals – Módulo 1")
        st.write("**📝 Año:** 2026")

    with c2:
        st.markdown("### Tecnologías utilizadas")
        st.markdown(
            """
            <div class="dmc-hero">
                <p class="dmc-muted" style="margin:0;">
                    ✨ Python<br>
                    ✨ Streamlit<br>
                    ✨ Pandas
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )


# -----------------------------------------
# EJERCICIO 1 – Variables y Condicionales
# -----------------------------------------
def render_ejercicio_1() -> None:
    title_card("📊 Ejercicio 1 – Variables y Condicionales")

    st.write("Verificador de presupuesto: compara **presupuesto vs gasto**")
    presupuesto = st.number_input("Presupuesto", min_value=0.0, value=100.0, step=10.0, key="e1_presupuesto")
    gasto = st.number_input("Gasto", min_value=0.0, value=50.0, step=10.0, key="e1_gasto")

    if st.button("Evaluar presupuesto", key="e1_btn"):
        diferencia = presupuesto - gasto
        if gasto <= presupuesto:
            st.success("✅ El gasto está dentro del presupuesto.")
        else:
            st.warning("⚠️ El gasto excede el presupuesto.")
        st.write(f"**La diferencia es:** {diferencia:.2f}")


# ------------------------------------
# EJERCICIO 2 – Listas y Diccionarios
# ------------------------------------
def render_ejercicio_2() -> None:
    title_card("📊 Ejercicio 2 – Listas y Diccionarios")
    st.caption("Registro de actividades financieras en una lista de diccionarios")

    if "e2_actividades" not in st.session_state:
        st.session_state["e2_actividades"] = []

    left, right = st.columns([1, 1.35])

    with left:
        with st.container(border=True):
            e2_nombre = st.text_input("Nombre de la actividad", value="", key="e2_nombre")
            e2_tipo = st.selectbox(
                "Tipo",
                options=["Ingreso", "Gasto", "Inversión", "Ahorro"],
                index=2,
                key="e2_tipo"
            )
            e2_presupuesto = st.number_input(
                "Presupuesto (S/)",
                min_value=0.0,
                value=1000.0,
                step=50.0,
                key="e2_presupuesto"
            )
            e2_gasto_real = st.number_input(
                "Gasto real (S/)",
                min_value=0.0,
                value=0.0,
                step=50.0,
                key="e2_gasto_real"
            )

            add_e2 = st.button("Agregar actividad", key="e2_add")
            clear_e2 = st.button("Limpiar lista", key="e2_clear")

            if add_e2:
                if not e2_nombre.strip():
                    st.warning("Ingrese un **nombre** para la actividad.")
                else:
                    st.session_state["e2_actividades"].append({
                        "nombre": e2_nombre.strip(),
                        "tipo": e2_tipo,
                        "presupuesto": float(e2_presupuesto),
                        "gasto_real": float(e2_gasto_real),
                    })
                    st.success("Actividad agregada.")

            if clear_e2:
                st.session_state["e2_actividades"] = []
                st.info("Lista limpiada.")

    with right:
        with st.container(border=True):
            st.markdown("**Actividades registradas**")

            actividades = st.session_state["e2_actividades"]
            if not actividades:
                st.info("No hay actividades registradas.")
                return

            df = pd.DataFrame(actividades)
            st.dataframe(df, use_container_width=True, hide_index=True)

            st.write("")
            st.markdown("**Estado por actividad**")
            for i, act in enumerate(actividades, start=1):
                presupuesto = act["presupuesto"]
                gasto_real = act["gasto_real"]
                ok = gasto_real <= presupuesto
                diff = presupuesto - gasto_real
                estado = "En presupuesto" if ok else "EXCEDIDA"
                st.write(
                    f"{i}. **{act['nombre']}** ({act['tipo']}): {estado} | Diferencia: S/ {diff:,.2f}"
                )


# ---------------------------------------------------------
# EJERCICIO 3 – Funciones y Programación Funcional
# ---------------------------------------------------------
def render_ejercicio_3() -> None:
    title_card("📊 Ejercicio 3 – Funciones y Programación Funcional")
    st.caption("Cálculo de retorno esperado usando función + map/lambda")

    if "e3_actividades" not in st.session_state:
        st.session_state["e3_actividades"] = []

    def calcular_retorno(actividad: dict, tasa: float, meses: int) -> float:
        return float(actividad["presupuesto"]) * float(tasa) * int(meses)

    top_a, top_b = st.columns([1, 1.2])

    with top_a:
        st.markdown("**1) Define actividades (para este ejercicio)**")
        e3_nombre = st.text_input("Nombre de la actividad", key="e3_nombre")
        e3_presupuesto = st.number_input(
            "Presupuesto (S/)",
            min_value=0.0,
            value=1000.0,
            step=50.0,
            key="e3_presupuesto"
        )

        add_e3 = st.button("Agregar", key="e3_add")
        clear_e3 = st.button("Limpiar", key="e3_clear")

        if add_e3:
            if not e3_nombre.strip():
                st.warning("Ingrese un **nombre**.")
            else:
                st.session_state["e3_actividades"].append({
                    "nombre": e3_nombre.strip(),
                    "presupuesto": float(e3_presupuesto)
                })
                st.success("Actividad agregada.")

        if clear_e3:
            st.session_state["e3_actividades"] = []
            st.info("Lista limpiada.")

    with top_b:
        st.markdown("**2) Parámetros del retorno**")
        e3_tasa = st.slider(
            "Tasa (por mes)",
            min_value=0.0,
            max_value=1.0,
            value=0.05,
            step=0.01,
            key="e3_tasa"
        )
        e3_meses = st.number_input("Meses", min_value=1, value=6, step=1, key="e3_meses")
        calc_e3 = st.button("Calcular retorno", key="e3_calc")

    st.write("")

    with st.container(border=True):
        st.markdown("**Resultados**")

        actividades = st.session_state["e3_actividades"]
        if not actividades:
            st.info("Agregue al menos una actividad para calcular retornos.")
            return

        if calc_e3:
            retornos = list(map(lambda a: calcular_retorno(a, e3_tasa, e3_meses), actividades))
            df = pd.DataFrame({
                "nombre": [a["nombre"] for a in actividades],
                "presupuesto": [a["presupuesto"] for a in actividades],
                "tasa": [e3_tasa] * len(actividades),
                "meses": [e3_meses] * len(actividades),
                "retorno_esperado": retornos,
            })
            st.dataframe(df, use_container_width=True, hide_index=True)
            st.write(f"Retorno total esperado: **S/ {sum(retornos):,.2f}**")
        else:
            st.info("Defina actividades y presione **Calcular retorno**")

# -------------------------------------------------
# EJERCICIO 4 – Programación Orientada a Objetos
# -------------------------------------------------
class Actividad:
    def __init__(self, nombre: str, tipo: str, presupuesto: float, gasto_real: float) -> None:
        self.nombre = nombre
        self.tipo = tipo
        self.presupuesto = float(presupuesto)
        self.gasto_real = float(gasto_real)

    def esta_en_presupuesto(self) -> bool:
        return self.gasto_real <= self.presupuesto

    def mostrar_info(self) -> str:
        diff = self.presupuesto - self.gasto_real
        estado = "En presupuesto" if self.esta_en_presupuesto() else "EXCEDIDA"
        return (
            f"Actividad: {self.nombre} | Tipo: {self.tipo} | "
            f"Presupuesto: S/ {self.presupuesto:,.2f} | "
            f"Gasto real: S/ {self.gasto_real:,.2f} | "
            f"Estado: {estado} | Diferencia: S/ {diff:,.2f}"
        )


def render_ejercicio_4() -> None:
    title_card("📊 Ejercicio 4 – Programación Orientada a Objetos (POO)")
    st.caption("Modelado de actividad financiera con clase y métodos")

    if "e4_objetos" not in st.session_state:
        st.session_state["e4_objetos"] = []

    left, right = st.columns([1, 1.35])

    with left:
        with st.container(border=True):
            e4_nombre = st.text_input("Nombre", key="e4_nombre")
            e4_tipo = st.selectbox("Tipo", ["Ingreso", "Gasto", "Inversión", "Ahorro"], index=0, key="e4_tipo")
            e4_presupuesto = st.number_input("Presupuesto (S/)", min_value=0.0, value=1200.0, step=50.0, key="e4_presupuesto")
            e4_gasto_real = st.number_input("Gasto real (S/)", min_value=0.0, value=0.0, step=50.0, key="e4_gasto_real")

            add_e4 = st.button("Crear objeto Actividad", key="e4_add")
            clear_e4 = st.button("Limpiar", key="e4_clear")

            if add_e4:
                if not e4_nombre.strip():
                    st.warning("Ingrese un **nombre**.")
                else:
                    obj = Actividad(e4_nombre.strip(), e4_tipo, e4_presupuesto, e4_gasto_real)
                    st.session_state["e4_objetos"].append(obj)
                    st.success("Objeto creado y registrado.")

            if clear_e4:
                st.session_state["e4_objetos"] = []
                st.info("Lista de objetos limpiada.")

    with right:
        with st.container(border=True):
            st.markdown("**Objetos creados**")

            objs = st.session_state["e4_objetos"]
            if not objs:
                st.info("Aún no hay objetos creados.")
                return

            for i, obj in enumerate(objs, start=1):
                st.write(f"**{i}.** {obj.mostrar_info()}")
                if obj.esta_en_presupuesto():
                    st.success("✅ Cumple el presupuesto")
                else:
                    st.warning("⚠️ No cumple el presupuesto")
                st.write("---")


# -------------
# Menú lateral
# -------------
def main() -> None:
    apply_custom_css()

    # Logo seguro (no rompe si no existe)
    try:
        st.sidebar.image("DMC.png", use_container_width=True)
    except Exception:
        st.sidebar.markdown("### DMC INSTITUTE")

    st.sidebar.markdown("## Navegación")
    st.sidebar.caption("Selecciona una página")

    page = st.sidebar.selectbox(
        "Menú",
        ["Home", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4"],
        key="page_select",
        label_visibility="collapsed",
    )

    if page == "Home":
        render_home()
    elif page == "Ejercicio 1":
        render_ejercicio_1()
    elif page == "Ejercicio 2":
        render_ejercicio_2()
    elif page == "Ejercicio 3":
        render_ejercicio_3()
    elif page == "Ejercicio 4":
        render_ejercicio_4()


if __name__ == "__main__":
    main()