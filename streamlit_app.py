import streamlit as st
from PIL import Image
st.set_page_config(
    page_title="La quête de Mirmandoule l'amoureux",
    page_icon="🏰",
    layout="centered",
    initial_sidebar_state="collapsed"
)
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=MedievalSharp&display=swap');
/* GLOBAL */
html, body, [class*="css"] {
    color: #000000 !important;
  font-family: "MedievalSharp", cursive;
  font-weight: 400;
  font-style: normal;

/* Fond */
.stApp {
    background-color: #f4ecd8;
}

/* Container principal */
.block-container {

    max-width: 700px;
    padding-top: 1rem;
    padding-bottom: 2rem;
    padding-left: 1rem;
    padding-right: 1rem;

    background-color: #fff8e7;
    border-radius: 15px;
    border: 2px solid #c9a86a;

}

/* Titres */
h1 {
    color: #000000 !important;
    font-size: 100px !important;
    font-family: "MedievalSharp", cursive;
    text-align: center;
}

h2 {
    color: #000000 !important;
    font-size: 24px !important;
            font-family: "MedievalSharp", cursive;
}

h3 {
    color: #000000 !important;
    font-size: 20px !important;
}

/* Texte normal */
p, div, span, label {
    color: #FF8C00 !important;
    font-size: 18px;
}

/* Boites medieval */
.medieval-box {

    background-color: #fff3cd;

    padding: 15px;

    border-radius: 10px;

    border: 1px solid #c9a86a;

    color: #000000 !important;

    font-size: 18px;

}

/* Boutons mobile friendly */
.stButton > button {

    width: 100%;

    height: 50px;

    font-size: 18px;

    border-radius: 10px;

}

/* Selectbox mobile */
.stSelectbox > div {

    font-size: 18px;

}

/* Input mobile */
.stTextInput input {

    font-size: 18px;

}

/* Progress bar spacing */
.stProgress {

    margin-top: 10px;

    margin-bottom: 20px;

}

/* Image responsive */
img {

    border-radius: 10px;

}

</style>
""", unsafe_allow_html=True)
# =========================
# DONNEES DU JEU
# =========================

LIEUX = [

    {
        "nom": "la basse-ville",
        "enigme": "Tu y retourne après les artisans",
        "options": [
            "La porte des Gauttiers",
            "La capitelle",
            "L'église Sainte-Foy",
            "La chapelle Sainte-Lucie",
            "Les boutiques d'art & d'artisanat"
        ],
        "reponse": "Les boutiques d'art & d'artisanat"
    },

    {
        "nom": "Les boutiques d'art & d'artisanat",
        "enigme": "Tu dois franchir cet homme pour m'atteindre",
        "options": [
            "La porte des Gauttiers",
            "La capitelle",
            "L'église Sainte-Foy",
            "La chapelle Sainte-Lucie",
            "Les boutiques d'art & d'artisanat"
        ],
        "reponse": "La porte des Gauttiers"
    },

    {
        "nom": "La porte des Gauttiers",
        "enigme": "Tu es passé devant au moins 5 foys",
        "options": [
            "La porte des Gauttiers",
            "La capitelle",
            "L'église Sainte-Foy",
            "La chapelle Sainte-Lucie",
            "Les boutiques d'art & d'artisanat"
        ],
        "reponse": "L'église Sainte-Foy"
    },

    {
        "nom": "L'église Sainte-Foy",
        "enigme": "Cha ch'appelle comme un coffre-fort",
        "options": [
            "La porte des Gauttiers",
            "La capitelle",
            "L'église Sainte-Foy",
            "La chapelle Sainte-Lucie",
            "Les boutiques d'art & d'artisanat"
        ],
        "reponse": "La chapelle Sainte-Lucie"
    },

    {
        "nom": "La chapelle Sainte-Lucie",
        "enigme": "On me présente en toute lettre",
        "options": [
            "La porte des Gauttiers",
            "La capitelle",
            "L'église Sainte-Foy",
            "La chapelle Sainte-Lucie",
            "Les boutiques d'art & d'artisanat"
        ],
        "reponse": "La capitelle"
    }

]

ENIGME_FINALE = {
    "question": "Quel est le point commun entre tous ces lieux ?",
    "reponse": "le coffre"
}

# =========================
# SESSION
# =========================

if "etape" not in st.session_state:
    st.session_state.etape = 0

if "termine" not in st.session_state:
    st.session_state.termine = False


# =========================
# TITRE
# =========================

st.title("🏰 La quête de Mirmandoule l'amoureux");font-color: #000000

st.markdown("""
<div class="medieval-box">
Bienvenue, belle aventurière.

Mirmandoule a dissimulé un trésor précieux dans ce village.

Résous toutes ces énigmes pour découvrir son emplacement.

Que ta quête commence...{color: #000000; font-family: "MedievalSharp"}
</div>
""", unsafe_allow_html=True)


# =========================
# CARTE
# =========================

image = Image.open("carte.png")
st.image(image, use_container_width=True)


# =========================
# PROGRESSION
# =========================

progress = st.session_state.etape / len(LIEUX)
st.progress(progress)

st.write(f"Progression : {st.session_state.etape} / {len(LIEUX)} lieux découverts")


# =========================
# ENIGMES
# =========================

if st.session_state.etape < len(LIEUX):

    lieu = LIEUX[st.session_state.etape]

    st.header(f"📍 Position actuelle : {lieu['nom']}")

    st.markdown(f"""
    <div class="medieval-box">
    <b>Énigme :</b><br>
    {lieu['enigme']}
    </div>
    """, unsafe_allow_html=True)

    choix = st.selectbox(
        "Choisis le prochain lieu :",
        lieu["options"],
        key=st.session_state.etape
    )

    if st.button("Valider"):

        if choix == lieu["reponse"]:

            st.success("✅ Bonne réponse ! Tu avances dans la quête.")

            st.session_state.etape += 1
            st.rerun()

        else:

            st.error("❌ Mauvaise réponse. Réfléchis encore...")


# =========================
# ENIGME FINALE
# =========================

elif not st.session_state.termine:

    st.header("🏆 Énigme finale")

    st.markdown("""
    <div class="medieval-box">
    Tu as découvert tous les lieux.

    Il ne reste qu'une ultime épreuve.

    Quel est le point commun entre tous ces lieux ?
    </div>
    """, unsafe_allow_html=True)

    reponse_finale = st.text_input("le coffreemplacement du trésor")

    if st.button("Révéler le trésor"):

        if reponse_finale.lower().strip() == ENIGME_FINALE["reponse"]:

            st.session_state.termine = True
            st.rerun()

        else:

            st.error("❌ Ce n'est pas la bonne réponse...")


# =========================
# VICTOIRE
# =========================

else:

    st.balloons()

    st.header("💎 TRÉSOR DÉCOUVERT 💎")

    st.markdown("""
    <div class="medieval-box">
    Félicitations, noble aventurier.

    Tu as prouvé ta sagesse, ton courage et ta valeur.

    Le trésor de Mirmandoule est désormais tien.

    🏆
    </div>
    """, unsafe_allow_html=True)

    if st.button("Recommencer la quête"):
        st.session_state.etape = 0
        st.session_state.termine = False
        st.rerun()