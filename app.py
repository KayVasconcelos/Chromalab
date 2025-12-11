import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase, WebRtcMode, RTCConfiguration
import cv2
import numpy as np
import av
from PIL import Image, ImageDraw
import io
import base64
import google.generativeai as genai
from datetime import datetime

st.set_page_config(page_title="Chromalab - Análise de Colorimetria", layout="wide", initial_sidebar_state="expanded")

# Configurar Gemini API
GEMINI_API_KEY = st.secrets.get("GEMINI_API_KEY", "")
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)
else:
    st.sidebar.warning("⚠️ Chave GEMINI_API_KEY não configurada em secrets.toml")

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
        self.last_frame = None

    def recv(self, frame):
        img = frame.to_ndarray(format="bgr24")
        self.last_frame = img.copy()  # Guardar último frame
        
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
    
    # Botão para capturar foto
    st.markdown("---")
    capture_photo = st.button("📸 Capturar Foto", key="capture_btn", use_container_width=True)

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
    
    st.image(palette_img, width=150)
    
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

# --- ANÁLISE COM GEMINI ---
st.markdown("---")
st.subheader("💡 Análise Personalizada com IA")

if "captured_photo" not in st.session_state:
    st.session_state.captured_photo = None
if "gemini_analysis" not in st.session_state:
    st.session_state.gemini_analysis = None
if "last_frame" not in st.session_state:
    st.session_state.last_frame = None

# Capturar foto do vídeo em tempo real
if capture_photo and ctx.video_processor:
    try:
        # Capturar o último frame do processador de vídeo
        if ctx.video_processor.last_frame is not None:
            frame_bgr = ctx.video_processor.last_frame
            # Converter de BGR para RGB
            frame_rgb = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2RGB)
            st.session_state.captured_photo = Image.fromarray(frame_rgb)
            st.success("✅ Foto capturada! Clique em 'Analisar com Gemini' para análise.")
            st.rerun()
        else:
            st.warning("⚠️ Câmera ainda carregando, tente novamente em alguns segundos...")
    except Exception as e:
        st.error(f"Erro ao capturar foto: {e}")

# Exibir foto capturada
if st.session_state.captured_photo:
    st.image(st.session_state.captured_photo, caption="Foto Capturada", width=400)
    
    # Checkbox para modo demonstração
    col_demo, col_analyze = st.columns([1, 2])
    with col_demo:
        demo_mode = st.checkbox("🎭 Modo Demo (sem usar API)", value=False)
    
    with col_analyze:
        # Habilitar botão de análise
        if st.button("🤖 Analisar com Gemini", key="analyze_gemini", use_container_width=True):
            if demo_mode:
                # Modo demonstração - análise simulada
                demo_analysis = """
                ### 🎨 Análise de Colorimetria - Modo Demonstração

                #### 1. **Subtom da Pele**: Quente
                Sua pele apresenta um undertone quente com reflexos dourados naturais.

                #### 2. **Profundidade da Pele**: Médio
                Tom de pele médio, com boa absorção de pigmentos coloridos.

                #### 3. **Contraste Natural**: Médio-Alto
                Contraste agradável entre pele, cabelo e olhos.

                #### 4. **Melhor Estação Colorimétrica**: 🍂 **OUTONO**
                Sua análise sugere a estação Outono como ideal. Cores quentes, profundas e terrosas realçam sua beleza natural.

                #### 5. **Cores que Realçam** ✨
                - Laranja queimado e tons terra quentes
                - Marrom chocolate e caramelo
                - Dourado e cobre metálicos
                - Verde oliva e dourado
                - Vermelho-tijolo e burgundy

                #### 6. **Cores a Evitar** ❌
                - Rosa bebê muito pálido
                - Cinza muito frio
                - Branco puro (prefira creme ou marfim)
                - Azul gelado
                - Preto puro (prefira marrom escuro)

                #### 7. **Recomendações Práticas** 💄
                **Maquiagem**: Use tons quentes como bronze, cobre, terracota. Evite rosas muito frios.
                
                **Roupas**: Invista em tons de outono: laranja, marrom, ouro. Use dourado em acessórios.
                
                **Acessórios**: Ouro amarelo combina melhor que prata. Jóias em tons quentes são sua marca!

                ---
                *Esta é uma análise demonstrativa. Para análise personalizada com IA, desabilite o modo demo e use sua chave Gemini real.*
                """
                st.session_state.gemini_analysis = demo_analysis
                st.success("✅ Análise demonstrativa carregada!")
            elif GEMINI_API_KEY and GEMINI_API_KEY != "sua-chave-api-aqui":
                with st.spinner("🔄 Analisando foto..."):
                    try:
                        # Converter imagem para base64
                        img_bytes = io.BytesIO()
                        st.session_state.captured_photo.save(img_bytes, format="PNG")
                        img_base64 = base64.b64encode(img_bytes.getvalue()).decode()
                        
                        # Preparar prompt para análise
                        prompt = f"""
                        Você é um especialista em colorimetria e análise de tons de pele. 
                        Analise a foto fornecida com foco em:
                        
                        1. **Subtom da pele**: Identifique se é quente, frio ou neutro
                        2. **Profundidade da pele**: Luz, médio ou profundo
                        3. **Contraste natural**: Alto, médio ou baixo
                        4. **Melhor estação colorimétrica**: Primavera, Verão, Outono ou Inverno (baseado na análise)
                        5. **Cores que realçam**: Liste 5-7 cores específicas que melhor combinam com a tez
                        6. **Cores a evitar**: Liste 3-5 cores que podem diminuir a luminosidade natural
                        7. **Recomendações práticas**: Dicas para maquiagem, roupas e acessórios
                        
                        Forneça um feedback detalhado, personalizado e profissional em português.
                        """
                        
                        # Chamar Gemini API
                        model = genai.GenerativeModel("gemini-2.5-flash-image")
                        message = model.generate_content([
                            prompt,
                            {"mime_type": "image/png", "data": img_base64}
                        ])
                        
                        st.session_state.gemini_analysis = message.text
                        st.success("✅ Análise concluída!")
                        
                    except Exception as e:
                        error_msg = str(e)
                        if "429" in error_msg or "quota" in error_msg.lower():
                            st.error("⚠️ **Quota da API excedida!**\n\nVocê atingiu o limite gratuito do Gemini. Opções:\n\n1. **Aguarde**: Limites reset diariamente\n2. **Upgrade**: Adicione cartão em https://ai.google.dev/billing/overview\n3. **Use modo Demo**: Ative a opção acima para ver exemplo de análise")
                        else:
                            st.error(f"❌ Erro na análise: {error_msg}")
            else:
                st.warning("⚠️ Configure sua chave API Gemini no arquivo `.streamlit/secrets.toml`")


# Exibir resultado da análise
if st.session_state.gemini_analysis:
    st.markdown("---")
    st.subheader("📊 Resultado da Análise")
    st.markdown(st.session_state.gemini_analysis)
    
    # Opção de salvar resultado
    col_save, col_reset = st.columns([1, 1])
    with col_save:
        if st.button("💾 Salvar Análise", use_container_width=True):
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            st.session_state[f"analysis_{timestamp}"] = {
                "photo": st.session_state.captured_photo,
                "palette": palette_selected,
                "analysis": st.session_state.gemini_analysis,
                "timestamp": timestamp
            }
            st.success("✅ Análise salva no histórico!")
    
    with col_reset:
        if st.button("🔄 Nova Análise", use_container_width=True):
            st.session_state.captured_photo = None
            st.session_state.gemini_analysis = None
            st.rerun()
