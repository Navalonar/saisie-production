import streamlit as st
import gspread
from datetime import datetime
from oauth2client.service_account import ServiceAccountCredentials

# --------------------
# Authentification Google Sheet
# --------------------
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
credentials = ServiceAccountCredentials.from_json_keyfile_name("secrets.json", scope)
client = gspread.authorize(credentials)

# --------------------
# Paramètres du Google Sheet
# --------------------
sheet = client.open("Saisie de production BatiBG")
historique = sheet.worksheet("historique")
liste = sheet.worksheet("liste")

# --------------------
# Chargement des valeurs des listes déroulantes
# --------------------
agents = liste.col_values(1)[1:]
dossiers = liste.col_values(2)[1:]
traitements = liste.col_values(3)[1:]
taches = liste.col_values(4)[1:]

# --------------------
# UI - Formulaire Streamlit
# --------------------
st.title("📋 Formulaire de saisie de production")

agent = st.selectbox("👤 Agent", agents)
dossier = st.selectbox("📁 Dossier", dossiers)
traitement = st.selectbox("🛠️ Traitement", traitements)
tache = st.selectbox("📝 Tâche", taches)

col1, col2 = st.columns(2)
with col1:
    if st.button("🟢 Démarrer"):
        now = datetime.now().strftime("%
