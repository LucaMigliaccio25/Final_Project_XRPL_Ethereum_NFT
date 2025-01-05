import streamlit as st
import json
from utils import create_and_transfer_nft

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

# Sezione: Creazione NFT
with col1:
    st.header("Crea NFT - Avatar")
    if st.button("Crea NFT"):
        try:
            st.write("Creazione dell'NFT in corso...")
            # Creazione NFT
            contract_address, NFT_token_id, token_id, token_uri = create_and_transfer_nft(
                seed_company, product_uri, initial_metadata, taxon, seed_receiver=seed_receiver
            )
            
            # Salva i dati del token in un file JSON
            data = {"token_id": token_id, "token_uri": token_uri}
            with open("token_data.json", "w") as f:
                json.dump(data, f)

            # Mostra dettagli NFT
            st.success("NFT creato con successo!")
            st.json(data)
            st.image(initial_image_path, caption="Immagine Avatar Creato", use_container_width=True)
        except Exception as e:
            st.error(f"Errore durante la creazione dell'NFT: {e}")
