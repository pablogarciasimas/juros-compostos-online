import streamlit as st
import streamlit.components.v1 as components

# Metatag de verificação do Google AdSense
components.html(
    """
    <meta name="google-adsense-account" content="ca-pub-9780795734195092">
    """,
    height=0
)

st.set_page_config(page_title="Calculadora de Juros Compostos", layout="centered")

st.title("📈 Calculadora de Juros Compostos")
st.caption("Projeto gratuito: juros-compostos-online")

# Entrada de dados
capital = st.number_input("Digite o capital inicial (R$)", min_value=0.0, format="%.2f")
taxa = st.number_input("Digite a taxa de juros (% ao mês)", min_value=0.0, format="%.2f")
tempo = st.number_input("Digite o tempo (em meses)", min_value=1, step=1)

# Cálculo
if st.button("Calcular"):
    montante = capital * (1 + taxa/100) ** tempo
    st.success(f"📊 Após {tempo} meses, o montante será de: **R$ {montante:,.2f}**")
