import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase, WebRtcMode
import cv2
import numpy as np
import av
from PIL import Image, ImageDraw
import io

st.set_page_config(page_title="Chromalab - Análise de Colorimetria", layout="wide", initial_sidebar_state="expanded")

# Paletas de cores para análise (RGB para exibição, BGR para OpenCV)
PALETAS_COLORIMETRIA = {
    "Primavera": {
        "cores_rgb": [(255, 200, 124), (255, 218, 158), (255, 240, 200), (200, 220, 100), (150, 200, 150)],
        "descricao": "Tons claros, quentes e frescos",
    },
    "Verão": {
        "cores_rgb": [(220, 200, 220), (180, 180, 200), (150, 180, 220), (200, 220, 240), (240, 200, 180)],
        "descricao": "Tons frios, suaves e pastel",
    },
    "Outono": {
        "cores_rgb": [(255, 180, 120), (240, 140, 80), (200, 100, 60), (180, 120, 80), (220, 160, 100)],
        "descricao": "Tons quentes, profundos e terrosos",
    },
    "Inverno": {
        "cores_rgb": [(255, 50, 100), (100, 150, 200), (50, 50, 100), (200, 100, 150), (100, 200, 255)],
        "descricao": "Tons frios, intensos e puros",
    },
}

class VideoProcessor(VideoTransformerBase):
    def __init__(self):
        self.show_palette = False
        self.palette_name = "Primavera"

    def recv(self, frame):
        img = frame.to_ndarray(format="bgr24")
        
        if not self.show_palette:
            return av.VideoFrame.from_ndarray(img, format="bgr24")

        # Desenhar paleta na parte inferior do vídeo
        h, w, c = img.shape
        palette_height = 80
        palette_y = h - palette_height
        
        palette_colors = PALETAS_COLORIMETRIA[self.palette_name]["cores_rgb"]
        color_width = w // len(palette_colors)
        
        for i, color_rgb in enumerate(palette_colors):
            x1 = i * color_width
            x2 = (i + 1) * color_width
            color_bgr = (color_rgb[2], color_rgb[1], color_rgb[0])
            cv2.rectangle(img, (x1, palette_y), (x2, h), color_bgr, -1)
        
        return av.VideoFrame.from_ndarray(img, format="bgr24")

st.markdown("<h1 style='text-align: center;'>🎨 Chromalab — Análise de Colorimetria</h1>", unsafe_allow_html=True)
st.markdown("Descubra qual paleta de cores realça melhor sua tez natural", unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.header("Controles da Análise")
    
    palette_selected = st.radio(
        "Selecione a paleta para testar:",
        options=list(PALETAS_COLORIMETRIA.keys()),
        captions=[PALETAS_COLORIMETRIA[p]["descricao"] for p in PALETAS_COLORIMETRIA.keys()]
    )
    
    show_palette_in_video = st.checkbox("Mostrar paleta no vídeo", value=True)
    
    st.markdown("---")
    st.subheader("Dicas de Análise")
    st.markdown("""
    - **Iluminação**: Use luz natural de frente
    - **Foco**: Observe o rosto e o pescoço
    - **Olheiras**: Veja se suavizam ou escurecem
    - **Lábios**: Note se ganham vitalidade
    - **Pele**: Observe se fica luminosa ou opaca
    """)

# --- MAIN AREA ---
col_camera, col_info = st.columns([3, 1])

with col_camera:
    st.subheader("Câmera de Análise")
    ctx = webrtc_streamer(
        key="chromalab-analysis",
        mode=WebRtcMode.SENDRECV,
        rtc_configuration={"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]},
        media_stream_constraints={"video": True, "audio": False},
        video_processor_factory=VideoProcessor,
        async_processing=True,
    )
    
    if ctx.video_processor:
        ctx.video_processor.show_palette = show_palette_in_video
        ctx.video_processor.palette_name = palette_selected

with col_info:
    st.subheader("Paleta Atual")
    
    # Mostrar paleta de cores
    colors = PALETAS_COLORIMETRIA[palette_selected]["cores_rgb"]
    
    # Criar imagem com as cores
    palette_img = Image.new("RGB", (150, 250), color=(240, 240, 240))
    draw = ImageDraw.Draw(palette_img)
    
    color_height = 250 // len(colors)
    for i, color in enumerate(colors):
        y1 = i * color_height
        y2 = (i + 1) * color_height
        draw.rectangle([0, y1, 150, y2], fill=color)
    
    st.image(palette_img, use_column_width=True)
    
    st.markdown(f"**{palette_selected}**")
    st.markdown(f"_{PALETAS_COLORIMETRIA[palette_selected]['descricao']}_")

# --- RESULTADO E RECOMENDAÇÕES ---
st.markdown("---")
st.subheader("Análise Recomendada")

tab1, tab2, tab3, tab4 = st.tabs(["Primavera", "Verão", "Outono", "Inverno"])

with tab1:
    st.markdown("""
    **Características**: Tons claros, quentes e frescos
    - Cores ideais: Coral, pêssego, verde-menta, amarelo claro
    - Melhor para: Peles com subtom quente e claro
    - Efeito: Realça luminosidade natural
    """)

with tab2:
    st.markdown("""
    **Características**: Tons frios, suaves e pastel
    - Cores ideais: Rosa suave, azul pastel, lavanda
    - Melhor para: Peles com subtom frio e delicado
    - Efeito: Cria contraste elegante
    """)

with tab3:
    st.markdown("""
    **Características**: Tons quentes, profundos e terrosos
    - Cores ideais: Laranja queimado, marrom, dourado
    - Melhor para: Peles com subtom quente e profundo
    - Efeito: Adiciona profundidade e riqueza
    """)

with tab4:
    st.markdown("""
    **Características**: Tons frios, intensos e puros
    - Cores ideais: Magenta, azul royal, preto
    - Melhor para: Peles com subtom frio e contraste alto
    - Efeito: Cria impacto e sofisticação
    """)
