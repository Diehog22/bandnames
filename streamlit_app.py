import streamlit as st
import random

st.set_page_config(page_title="Generador de Bandas", page_icon="🎸", layout="centered")

st.markdown("""
    <style>
    body {
        background-color: #000000;
    }
    .title { 
        font-size: 46px; 
        font-weight: 900; 
        text-align: center; 
        color: #39ff14; 
        margin-bottom: 10px; 
    }
    .subtitle { 
        text-align: center; 
        font-size: 20px; 
        color: #00ff66; 
        margin-bottom: 30px; 
    }
    .band-name-box {
        background: #000000;
        padding: 20px; 
        border-radius: 18px; 
        color: #39ff14;
        border: 2px solid #39ff14;
        font-size: 32px; 
        text-align: center; 
        margin-top: 20px;
        box-shadow: 0 0 20px #39ff14;
        font-weight: 700;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='title'>🎸 Generador de Nombres de Bandas</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Modo Terminal Hacker — Verde Neón</div>", unsafe_allow_html=True)

adjetivos = [
    "Cósmicos","Eléctricos","Rotos","Despiertos","Ancestros","Flotantes","Héreticos", "Sagrados",
    "Flameantes","Magnéticos","Caóticos","Octagenarios","Fánaticos","Prohibidos","Dementes","Celestes",
    "Errantes","Infinitos","Estúpidos","Atontados","Nauseabundos","Aguerridos","Ocultos","Cuánticos",
    "Salvajes","Místicos","Gloriosos","Brujos","Obesos,"Tercermundistas","Indómitos","Dionisiacos","Primitivos",
    "Homosexuales","Aplastantes"
]

sustantivos = [
    "Molcajetes","Dragones","Cactus","Esqueletos","Astronautas","Peregrinos","Gatos","Inodoros",
    "Calcetines","Trituradores","Calabazas","Dinosaurios","Políticos","Guerreros","Cometas","Píxeles","Cafés",
    "Magos","Pescadores","Sadistas","Militares","Soldados","Hechiceros","Vagabundos","Vikingos","Caballos","Tronos",
    "Monolitos","Trenes","Cerdos","Terricolas","Alienígenas","Inmortales","Guerrilleros","Hombres de Negocio"
]

estilos = [
    "del Desierto","del Inframundo","Intergalácticos","del Caribe","del Futuro","Del Infierno",
    "Esquizofrenicos","Satanicos","Travestis","del Soviet","de la Montaña","Radioactivos","del Cosmos",
    "de Tijuana","de Saturno","de la Jungla","del Olimpo","Terrorificos","De Ecatepec"
]

def generar_banda():
    a = random.choice(adjetivos)
    b = random.choice(sustantivos)
    c = random.choice(estilos)
    return random.choice([f"{b} {a}", f"{a} {b}", f"{b} {c}"])

if st.button("🎵 Generar Nombre de Banda", use_container_width=True):
    nombre = generar_banda()
    st.markdown(f"<div class='band-name-box'>{nombre}</div>", unsafe_allow_html=True)
    st.code(nombre)
