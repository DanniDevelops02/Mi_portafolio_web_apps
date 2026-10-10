from pathlib import Path

import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Portafolio · Aplicaciones de IA",
    page_icon="🌊",
    layout="wide",
)

# =====================================================================
#  CONTENIDO EDITABLE: cambia aquí textos, enlaces e imágenes
# =====================================================================
ETIQUETA = "Portafolio · Daniel Flórez"
TITULO = "Aplicaciones multimodales"
SUBTITULO = (
    "Una colección de aplicaciones web que exploran cómo la inteligencia "
    "artificial se integra con voz, imagen, datos y el mundo físico."
)

URL_RECURSOS = "https://sites.google.com/view/aplicacionesdeia/inicio"
TEXTO_RECURSOS = "Ver micrositio de la asignatura"

SIDEBAR_TITULO = "Aplicaciones multimodales."
SIDEBAR_TEXTO = (
    "En este portafolio, exploramos la variedad de modalidades con las que podemos "
    "diseñar interacciones en aplicaciones para uso en la vida real. Utilizamos herramientas "
    "de inteligencia artificial para potenciar nuestras capacidades y desbloquear nuevas formas "
    "de aprovechar las plataformas tecnológicas. "
)

# Cada bloque { ... } es una tarjeta. Aparecen de 3 en 3, en el orden de esta lista.
APPS = [
    {
        "titulo": "Aplicación de introducción",
        "descripcion": "Este fue nuestro primer acercamiento a Streamlit y Github.",
        "imagen": "sergey-kolesov-mermaid-sharpen.jpg",
        "url": "https://01appintro-sakccxqvzjtehnd6tkhxnu.streamlit.app/",
        "boton": "Abrir introducción",
    },
    {
        "titulo": "Texto a audio",
        "descripcion": "Esta aplicación utiliza IA básica para convertir texto escrito en audio.",
        "imagen": "Childrens_Storybook.jpg",
        "url": "https://02textoaaudio-e7a7ia4qwuljkwhdgzpbgx.streamlit.app/",
        "boton": "¡Crea un audio!",
    },
    {
        "titulo": "Conversión de voz a texto",
        "descripcion": "Una aplicación que usa la conversión de voz a texto.",
        "imagen": "OIG8.jpg",
        "url": "https://traductorw.streamlit.app/",
        "boton": "Abrir voz a texto",
    },
    {
        "titulo": "Transcriptor de audio y video",
        "descripcion": "Cómo realizamos transcripciones de audio y video.",
        "imagen": "OIG3.jpg",
        "url": "https://transcript-whisper.streamlit.app/",
        "boton": "Abrir transcriptor",
    },
    {
        "titulo": "Reconocimiento de objetos",
        "descripcion": "Cómo se detectan objetos en imágenes.",
        "imagen": "txt_to_audio.png",
        "url": "https://yolov5cmc.streamlit.app/",
        "boton": "Abrir YOLO",
    },
    {
        "titulo": "Análisis de imagen",
        "descripcion": "La capacidad de análisis sobre imágenes.",
        "imagen": "OIG4.jpg",
        "url": "https://vision2-gpt4o.streamlit.app/",
        "boton": "Abrir visión",
    },
    {
        "titulo": "Sistema ciberfísico",
        "descripcion": "La capacidad de interacción con el mundo físico.",
        "imagen": "OIG6.jpg",
        # OJO: esta URL es la misma que "Análisis de imagen". Revísala.
        "url": "https://vision2-gpt4o.streamlit.app/",
        "boton": "Abrir sistema ciberfísico",
    },
    {
        "titulo": "Entrenando modelos",
        "descripcion": "Cómo puedes usar tu propio modelo entrenado.",
        "imagen": "OIG5.jpg",
        "url": "https://xn3pg24ztuv6fdiqon8qn3.streamlit.app/",
        "boton": "Abrir modelo entrenado",
    },
    {
        "titulo": "Análisis de datos",
        "descripcion": "Cómo se pueden analizar datos usando agentes.",
        "imagen": "data_analisis.png",
        "url": "https://dataagente.streamlit.app/",
        "boton": "Abrir análisis de datos",
    },
    {
        "titulo": "Generación en contexto",
        "descripcion": "Una aplicación que usa RAG a partir de un documento PDF.",
        "imagen": "Chat_pdf.png",
        "url": "https://chatpdf-cc.streamlit.app/",
        "boton": "Abrir RAG",
    },
]

# =====================================================================
#  ESTILO (paleta fría basada en #3f71a6)
# =====================================================================
PRIMARIO = "#3f71a6"
OSCURO = "#1b2f45"
CLARO = "#eaf2f9"
SUAVE = "#a9c7e3"

st.markdown(
    f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=Inter:wght@400;500;600&display=swap');

    html, body, [class*="css"], .stApp {{
        font-family: 'Inter', sans-serif;
        font-size: 1.05rem;
    }}
    .stApp {{
        background: linear-gradient(180deg, #f6fafd 0%, {CLARO} 100%);
    }}
    .block-container {{
        max-width: 1100px;
        padding-top: 3rem;
        padding-bottom: 4rem;
    }}

    /* Hero */
    .hero {{ text-align: center; padding: 1rem 0 .5rem 0; }}
    .hero .etiqueta {{
        color: {PRIMARIO};
        letter-spacing: .25em;
        text-transform: uppercase;
        font-size: .85rem;
        font-weight: 600;
    }}
    .hero h1 {{
        font-family: 'Playfair Display', serif;
        font-size: 3.2rem;
        color: {OSCURO};
        margin: .3rem 0 .6rem 0;
        line-height: 1.1;
    }}
    .hero p {{
        color: #4d6479;
        font-size: 1.2rem;
        max-width: 680px;
        margin: 0 auto;
    }}
    .linea {{
        width: 70px; height: 4px; border-radius: 4px;
        background: {PRIMARIO};
        margin: 1.4rem auto 1rem auto;
    }}

    /* Tarjetas */
    [data-testid="stVerticalBlockBorderWrapper"] {{
        background: white;
        border: 1px solid {SUAVE}66 !important;
        border-radius: 18px !important;
        box-shadow: 0 8px 24px rgba(63, 113, 166, .08);
        padding: .5rem .6rem .8rem .6rem;
        transition: transform .2s ease, box-shadow .2s ease;
    }}
    [data-testid="stVerticalBlockBorderWrapper"]:hover {{
        transform: translateY(-3px);
        box-shadow: 0 14px 32px rgba(63, 113, 166, .16);
    }}

    /* Imágenes con proporción uniforme */
    [data-testid="stImage"] img {{
        width: 100%;
        aspect-ratio: 16 / 10;
        object-fit: cover;
        border-radius: 14px;
    }}
    .sin-imagen {{
        aspect-ratio: 16 / 10;
        border-radius: 14px;
        background: {CLARO};
        color: {PRIMARIO};
        display: flex; align-items: center; justify-content: center;
        font-weight: 600;
    }}

    .tarjeta-titulo {{
        font-family: 'Playfair Display', serif;
        font-size: 1.3rem;
        font-weight: 600;
        color: {OSCURO};
        margin: .7rem 0 .3rem 0;
        min-height: 2.6em;
        line-height: 1.3;
    }}
    .tarjeta-desc {{
        color: #4d6479;
        font-size: .98rem;
        min-height: 3.2em;
        margin-bottom: .6rem;
    }}

    /* Botones de enlace */
    .stLinkButton a, [data-testid^="stBaseLinkButton"] {{
        background: {PRIMARIO} !important;
        color: white !important;
        border: none !important;
        border-radius: 999px !important;
        font-weight: 600;
        padding: .5rem 1.4rem;
        transition: all .2s ease;
    }}
    .stLinkButton a:hover, [data-testid^="stBaseLinkButton"]:hover {{
        background: {OSCURO} !important;
        color: white !important;
    }}

    /* Sidebar */
    [data-testid="stSidebar"] {{ background: {OSCURO}; }}
    [data-testid="stSidebar"] * {{ color: #e6f0f9 !important; }}

    #MainMenu, footer {{ visibility: hidden; }}
    </style>
    """,
    unsafe_allow_html=True,
)

# =====================================================================
#  FUNCIONES AUXILIARES
# =====================================================================
BASE = Path(__file__).parent


def mostrar_imagen(nombre: str) -> None:
    """Busca la imagen primero en la carpeta 'imagenes/' y luego junto a Intro.py."""
    for carpeta in (BASE / "imagenes", BASE):
        ruta = carpeta / nombre
        if ruta.is_file():
            st.image(Image.open(ruta), use_container_width=True)
            return
    st.markdown('<div class="sin-imagen">Imagen no encontrada</div>', unsafe_allow_html=True)


# =====================================================================
#  PÁGINA
# =====================================================================
with st.sidebar:
    st.subheader(SIDEBAR_TITULO)
    st.write(SIDEBAR_TEXTO)

st.markdown(
    f"""
    <div class="hero">
        <div class="etiqueta">{ETIQUETA}</div>
        <h1>{TITULO}</h1>
        <p>{SUBTITULO}</p>
        <div class="linea"></div>
    </div>
    """,
    unsafe_allow_html=True,
)

_, centro, _ = st.columns([1, 1.4, 1])
with centro:
    st.link_button(TEXTO_RECURSOS, URL_RECURSOS, use_container_width=True)

st.write("")
st.write("")

# Cuadrícula de 3 columnas
for i in range(0, len(APPS), 3):
    columnas = st.columns(3, gap="medium")
    for columna, app in zip(columnas, APPS[i : i + 3]):
        with columna:
            with st.container(border=True):
                mostrar_imagen(app["imagen"])
                st.markdown(
                    f'<div class="tarjeta-titulo">{app["titulo"]}</div>'
                    f'<div class="tarjeta-desc">{app["descripcion"]}</div>',
                    unsafe_allow_html=True,
                )
                st.link_button(
                    app.get("boton", "Abrir aplicación"),
                    app["url"],
                    use_container_width=True,
                )
    st.write("")
