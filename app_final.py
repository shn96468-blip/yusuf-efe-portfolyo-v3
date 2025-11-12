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
    </style>
    """,
    unsafe_allow_html=True
)

# --- OTURUM DURUMU (SESSION STATE) BAŞLANGIÇ AYARLARI ---
ADMIN_PASSWORD = "123" 

# 7. SINIF DERS VERİLERİ (Konu Anlatımı ve Quiz)
DEFAULT_DERSLER = {
    "Matematik": {
        "konu": "Tam Sayılarla Dört İşlem",
        "anlatim": "7. sınıf matematiğinde tam sayılar kümesini ve bu kümedeki toplama, çıkarma, çarpma ve bölme işlemlerini öğreniyoruz. \n\n**Örnek:** Aynı işaretli tam sayılar toplanırken işaret korunur. Farklı işaretli sayılar toplanırken büyük olanın işareti alınır.",
        "sorular": [
            {"q": " $(-5) + (+8)$ işleminin sonucu kaçtır?", "a": ["$-13$", "$+3$", "$-3$", "$+13$"], "c": "$+3$"},
            {"q": " $(-4) \\cdot (-2)$ işleminin sonucu kaçtır?", "a": ["$-8$", "$+8$", "$0$", "$+2$"], "c": "$+8$"},
        ]
    },
    "Türkçe": {
        "konu": "Sözcükte Anlam İlişkileri",
        "anlatim": "Sözcükler arasında eş anlamlılık (anlamdaş), zıt anlamlılık (karşıt) ve yakın anlamlılık gibi ilişkiler bulunur. \n\n**Örnek:** Ak ve Beyaz eş anlamlıdır. Uzun ve Kısa zıt anlamlıdır. ",
        "sorular": [
            {"q": " 'Zengin' kelimesinin zıt anlamlısı nedir?", "a": ["Varlıklı", "Fakir", "Varlığa", "Cimri"], "c": "Fakir"},
            {"q": " Aşağıdaki kelime çiftlerinden hangisi eş anlamlıdır?", "a": ["Gürültü - Sessiz", "Hürriyet - Özgürlük", "İleri - Geri", "Aç - Tok"], "c": "Hürriyet - Özgürlük"},
        ]
    },
    "Fen Bilimleri": {
        "konu": "Atomun Yapısı ve Periyodik Sistem",
        "anlatim": "Madde atomlardan oluşur. Atom, çekirdek ve katmanlardan meydana gelir. Çekirdekte proton ve nötronlar, katmanlarda ise elektronlar bulunur. \n\
