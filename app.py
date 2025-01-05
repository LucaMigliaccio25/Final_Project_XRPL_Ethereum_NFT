import streamlit as st

# Configurazione iniziale dell'interfaccia
st.set_page_config(page_title="Creazione NFT Dinamico", layout="centered")

# Titolo dell'app
st.title("Creazione di un NFT Dinamico su Ethereum")

# Layout: Colonne per azioni
st.subheader("Azioni disponibili")
col1, col2 = st.columns(2)
