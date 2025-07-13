import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="Générateur de Hashtags Instagram", page_icon="📱")
st.title("📱 Générateur de Hashtags pour Instagram")

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

description = st.text_area("📝 Décris ta vidéo Instagram :", placeholder="Ex : Une vidéo de danse TikTok au bord de la mer...")

langue = st.selectbox("🌍 Langue des hashtags :", ["Français", "Anglais"])

if st.button("🚀 Générer les meilleurs hashtags"):

    if not description.strip():
        st.warning("👉 Merci de décrire ta vidéo avant de générer les hashtags.")
    else:
        system_prompt = (
            "Tu es un expert en stratégie de viralité sur Instagram. "
            "Génère uniquement une liste des meilleurs hashtags (sans autre texte), séparés par des espaces, "
            f"pour une vidéo décrite ainsi : {description}. "
            f"Langue : {langue.lower()}."
        )

        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": system_prompt},
                ],
                temperature=0.7,
                max_tokens=200
            )

            hashtags = response.choices[0].message.content.strip()
            st.success("✅ Hashtags générés avec succès :")
            st.code(hashtags)

        except Exception as e:
            st.error(f"❌ Erreur lors de l'appel à l'API : {str(e)}")
