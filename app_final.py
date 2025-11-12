import streamlit as st
import time

# --- SAYFA VE TEMA AYARLARI ---
st.set_page_config(
    page_title="Yusuf Efe Şahin | Portfolyo",
    layout="wide",
    page_icon="💼",
    initial_sidebar_state="expanded"
)

# Koyu Temayı zorlamak için CSS enjeksiyonu
st.markdown(
    """
    <style>
    /* Genel koyu arkaplan ve renk ayarları korundu */
    .stApp {
        background-color: #0E1117; 
        color: white;
    }
    .css-1d391kg { 
        background-color: #0E1117;
    }
    h1, h2, h3, h4, h5, h6 {
        color: #FF4B4B; 
    }
    .stTextInput, .stTextArea, .stSelectbox {
        background-color: #262730;
        color: white;
        border: 1px solid #31333F;
    }
    .stButton>button {
        color: white;
        border-color: #FF4B4B;
    }
    
    /* Görseldeki buton kenarlıkları için özel stil ekliyoruz */
    .stButton>button {
        color: white;
        border-color: #FF4B4B; /* Kırmızı/Turuncu ton */
        border-width: 2px;
        font-weight: bold;
    }
    
    /* Özel Buton Stili (Hover/Focus) */
    .stButton>button:focus:not(:active) {
        border-color: #FF4B4B; 
        color: #FF4B4B;
        box-shadow: 0 0 0 0.2rem rgba(255, 75, 75, 0.25);
    }
    
    /* Konu kutusu stili (Görseldeki mavi kutu) */
    .stAlert {
        background-color: #1E3147 !important; /* Mavi-Koyu Ton */
        color: white !important;
        border-left: 5px solid #FF4B4B !important; /* Kırmızı vurgu */
    }
    
    /* Konu kutusunun ikonunu ve başlığını hizalama */
    .css-1f9e236.e1qvo95c1 { /* Streamlit Info/Warning/Success div'inin içindeki metin */
        font-size: 1.1rem;
        font-weight: 600;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- OTURUM DURUMU (SESSION STATE) BAŞLANGIÇ AYARLARI ---
ADMIN_PASSWORD = "123" 

# 7. SINIF DERS VERİLERİ (Konu Anlatımı ve Quiz/Test Soruları)
DEFAULT_DERSLER = {
    "Matematik": {
        "konu": "7. Sınıf Matematik Tüm Üniteler", 
        "anlatim": """7. Sınıf Matematik dersi 6 ana üniteden oluşmaktadır:
        
* **1. Ünite (Tam Sayılar):** Pozitif ve negatif tam sayılarla toplama, çıkarma, çarpma ve bölme işlemleri, üslü ifadeler. **Örnek:** $-5 + 8 = 3$, $4 \cdot (-2) = -8$.
* **2. Ü
