import streamlit as st

# Dati XRPL
seed_company = "sEd7uhRLEHf7sELoTUiKTcDwgn3zvdA"
seed_receiver = "sEd7vJWGo5cYxju2raWQ1yQSFPgVejN"
product_uri = "https://diadenn.vercel.app/product/mike-wind-1"
taxon = 0

# Percorsi immagini locali (avatar/digital twin)
initial_image_path = "data/images/stregone.png"  # Immagine per la creazione
updated_image_path = "data/images/stregone_update.png"  # Immagine per l'aggiornamento

# Metadati
initial_metadata = "data/metadata/metadata_stregone.json"
updated_metadata = "data/metadata/metadata_stregone_update.json"

# Configurazione iniziale dell'interfaccia
st.set_page_config(page_title="Creazione NFT Dinamico", layout="centered")

# Titolo dell'app
st.title("Creazione di un NFT Dinamico su Ethereum")

# Layout: Colonne per azioni
st.subheader("Azioni disponibili")
col1, col2 = st.columns(2)
