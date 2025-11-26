import streamlit as st
import random

st.set_page_config(page_title="Generador de Bandas", page_icon="🎸", layout="centered")

st.markdown("""
    <style>
    .title { font-size: 46px; font-weight: 900; text-align: center; color: #E91E63; margin-bottom: 10px; }
    .subtitle { text-align: center; font-size: 20px; color: #555; margin-bottom: 30px; }
    .band-name-box {
        background: linear-gradient(135deg, #ff6f91, #ff9671);
        padding: 20px; border-radius: 18px; color: white;
        font-size: 32px; text-align: center; margin-top: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.25); font-weight: 700;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='title'>🎸 Generador de Nombres de Bandas</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Crea nombres épicos, ridículos o legendarios para tu próxima banda</div>", unsafe_allow_html=True)

adjetivos = ["Cósmicos","Eléctricos","Rotos","Despiertos","Ancestros","Flotantes","Héreticos", "Sagrados","Flameantes"
             "Magnéticos","Caóticos","Octagenarios","Fánaticos","Prohibidos","Dementes","Celestes","Errantes","Infinitos","Estúpidos","Atontados","Nauseabundos","Aguerridos",
             "Ocultos","Cuánticos","Salvajes","Místicos","Gloriosos","Brujos","Hechiceros","Indómitos","Dionisiacos"]

sustantivos = ["Molcajetes","Dragones","Cactus","Esqueletos","Astronautas","Peregrinos","Gatos","Inodoros","Calcetines"
               "Dinosaurios","Guerreros","Cometas","Píxeles","Cafés","Magos","Pescadores","Sadistas","Militares","Soldados"
               "Vikingos","Caballos","Tronos","Monolitos","Trenes","Cerdos","Terricolas","Alienígenas","Inmortales"]

estilos = ["del Desierto","del Inframundo","Intergalácticos","del Caribe","del Futuro","Del Infierno","Esquizofrenicos","Satanicos"
           "de la Montaña","Radioactivos","del Cosmos","de Tijuana","de Saturno","de la Jungla","del Olimpo"]

def generar_banda():
    a = random.choice(adjetivos)
    b = random.choice(sustantivos)
    c = random.choice(estilos)
    return random.choice([f"{b} {a}", f"{a} {b}", f"{b} {c}"])

if st.button("🎵 Generar Nombre de Banda", use_container_width=True):
    nombre = generar_banda()
    st.markdown(f"<div class='band-name-box'>{nombre}</div>", unsafe_allow_html=True)
    st.code(nombre)
