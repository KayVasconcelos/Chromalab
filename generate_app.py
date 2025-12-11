#!/usr/bin/env python3
# -*- coding: utf-8 -*-

code = """import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase, WebRtcMode
import cv2
import mediapipe as mp
import numpy as np
import av

st.set_page_config(page_title="Chromalab", layout="wide")

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

PALETAS = {
    "Nenhuma": None,
    "Quente Claro": (0, 140, 255),
    "Frio Claro": (255, 191, 0),
    "Quente Escuro": (0, 0, 128),
    "Frio Escuro": (128, 0, 0),
}

class VideoProcessor(VideoTransformerBase):
    def __init__(self):
        self.color_choice = None
        self.opacity = 0.4

    def recv(self, frame):
        img = frame.to_ndarray(format="bgr24")
        
        if not self.color_choice or self.color_choice == "Nenhuma":
            return av.VideoFrame.from_ndarray(img, format="bgr24")

        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = face_mesh.process(img_rgb)

        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                h, w, c = img.shape
                points = []
                for landmark in face_landmarks.landmark:
                    x, y = int(landmark.x * w), int(landmark.y * h)
                    points.append([x, y])
                
                points = np.array(points, dtype=np.int32)
                hull = cv2.convexHull(points)

                color_bgr = PALETAS.get(self.color_choice)
                if color_bgr is not None:
                    overlay = img.copy()
                    cv2.fillConvexPoly(overlay, hull, color_bgr)
                    img = cv2.addWeighted(overlay, self.opacity, img, 1 - self.opacity, 0)

        return av.VideoFrame.from_ndarray(img, format="bgr24")

st.markdown("<h1 style='text-align: center;'>Chromalab</h1>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 3, 1])

with col1:
    st.info("Etapa: Temperatura")
    st.write("Vamos observar se sua pele reage melhor a tons quentes ou frios.")
    st.progress(33)
    st.caption("Progresso: 1/3")

with col2:
    selected_palette = st.select_slider(
        "Selecione o filtro para testar:",
        options=["Nenhuma", "Quente Claro", "Frio Claro", "Quente Escuro", "Frio Escuro"]
    )

    ctx = webrtc_streamer(
        key="chromalab-feed",
        mode=WebRtcMode.SENDRECV,
        rtc_configuration={"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]},
        media_stream_constraints={"video": True, "audio": False},
        video_processor_factory=VideoProcessor,
        async_processing=True,
    )

    if ctx.video_processor:
        ctx.video_processor.color_choice = selected_palette
        ctx.video_processor.opacity = 0.35

with col3:
    st.warning("Dicas de Analise")
    st.markdown("1. Iluminacao: Use luz natural.\\n2. Olheiras: Veja se suavizam.\\n3. Labios: Note se ganham cor.")
"""

with open("app.py", "w", encoding="utf-8") as f:
    f.write(code)

print("✓ app.py criado com sucesso")
