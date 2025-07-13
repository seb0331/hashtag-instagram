import streamlit as st
import openai

st.set_page_config(page_title="Générateur de Hashtags Instagram", page_icon="📱")
st.title("📱 Générateur de Hashtags Instagram avec IA")
st.markdown("Entrez une description de votre vidéo pour obtenir des **hashtags optimisés pour le top 1**.")

openai.api_key = st.secrets["OPENAI_API_KEY"]

description = st.text_area("✍️ Description de la vidéo Instagram :", height=150)

if st.button("🚀 Générer les hashtags"):
    if not description.strip():
        st.warning("Veuillez entrer une description.")
    else:
        with st.spinner("Génération des hashtags en cours..."):
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "Tu es un expert des réseaux sociaux qui génère les meilleurs hashtags Instagram."},
                        {"role": "user", "content": f"Génère les meilleurs hashtags pour cette vidéo : {description}. Donne-les sur une seule ligne, sans explication, uniquement les hashtags séparés par des espaces."}
                    ],
                    temperature=0.7,
                    max_tokens=100
                )
                hashtags = response['choices'][0]['message']['content']
                st.success("🎉 Hashtags générés avec succès !")
                st.text_area("📌 Hashtags suggérés :", value=hashtags.strip(), height=100)
            except Exception as e:
                st.error(f"Erreur lors de l'appel à l'API : {e}")
