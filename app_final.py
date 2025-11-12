import streamlit as st
import time

# --- SİYAH EKRAN (KOYU TEMA) AYARLARI ---
# Bu ayarlar, Streamlit'in varsayılan koyu temasını zorlar ve bazı görsel bileşenlerin stilini düzenler.
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
    /* Ana arkaplanı koyu yapmak için */
    .stApp {
        background-color: #0E1117; 
        color: white;
    }
    /* Sidebar arkaplanı */
    .css-1d391kg { 
        background-color: #0E1117;
    }
    /* Ana başlık rengi */
    h1, h2, h3, h4, h5, h6 {
        color: #FF4B4B; /* Temel renginizi korur */
    }
    /* Metin kutuları ve inputlar için daha iyi kontrast */
    .stTextInput, .stTextArea, .stSelectbox {
        background-color: #262730;
        color: white;
        border: 1px solid #31333F;
    }
    /* Butonlar için daha iyi görünürlük */
    .stButton>button {
        color: white;
        border-color: #FF4B4B;
    }
    </style>
    """,
    unsafe_allow_html=True
)
# --- SİYAH EKRAN AYARLARI SONU ---


# --- OTURUM DURUMU (SESSION STATE) BAŞLANGIÇ AYARLARI ---
ADMIN_PASSWORD = "123"
MOCK_USERS = [
    {"username": "yusuf", "email": "yusuf@mail.com", "password_hash": "y123"},
    {"username": "efe", "email": "efe@mail.com", "password_hash": "e456"},
]

# Varsayılan Not Kartları - SADECE 7. Sınıf Konularına Odaklanıldı
DEFAULT_NOTLAR = {
    "Matematik": "Rasyonel Sayılar ve İşlemler (7. Sınıf)", 
    "Türkçe": "Fiiller ve Anlam Özellikleri (7. Sınıf)",     
    "Din Kültürü": "Melek ve Ahiret İnancı (7. Sınıf)",      
    "Tarih": "Orta Çağ ve Türk İslam Devletleri (7. Sınıf)", 
    "Sosyal Bilgiler": "Türk Tarihinde Yolculuk (7. Sınıf)", 
}

# PDF Cevap Anahtarları
DEFAULT_PDF_CEVAPLARI = {
    "DENEME_1": "ADBCBAADCC", 
    "MAT_KONU_2": "CBAAD",    
}

# Ders Koçları (İSİMLER TAMAMEN KALDIRILDI)
MOCK_KOCLAR = [
    {"ad": "Ders Koçu 1", "alan": "Matematik & Fen", "bio": "5 yıllık deneyimli koç. Analitik düşünme odaklı. Öğrenci başarılarını takip eder."},
    {"ad": "Ders Koçu 2", "alan": "Türkçe & Sosyal", "bio": "Sınav stratejileri ve motivasyon uzmanı. Birebir takiple ders programı hazırlar."},
    {"ad": "Ders Koçu 3", "alan": "Din Kültürü & İngilizce", "bio": "Birebir takiple öğrenci başarısı odaklı. Haftalık gelişim raporu sunar."},
]

# GENEL ARKA PLAN MÜZİĞİ İÇİN ÖRNEK MP3 LİNKİ
GENEL_FON_URL = "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3" 

# Session State Tanımlamaları (Mutlaka En Üstte Olmalı)
if 'admin_mode' not in st.session_state:
    st.session_state['admin_mode'] = False
if 'user_logged_in' not in st.session_state:
    st.session_state['user_logged_in'] = False
if 'current_user' not in st.session_state:
    st.session_state['current_user'] = None
if 'app_color' not in st.session_state:
    st.session_state['app_color'] = '#FF4B4B'
if 'secilen_sayfa' not in st.session_state:
    st.session_state['secilen_sayfa'] = "Hakkımda" 
if 'music_enabled' not in st.session_state:
    st.session_state['music_enabled'] = True 
if 'music_url' not in st.session_state:
    st.session_state['music_url'] = GENEL_FON_URL
if 'music_volume' not in st.session_state:
    st.session_state['music_volume'] = 0.5 
if 'show_admin_login' not in st.session_state:
    st.session_state['show_admin_login'] = False
if 'show_user_login' not in st.session_state:
    st.session_state['show_user_login'] = False
if 'show_user_register' not in st.session_state:
    st.session_state['show_user_register'] = False
if 'registration_allowed' not in st.session_state:
    st.session_state['registration_allowed'] = True
if 'user_login_allowed' not in st.session_state:
    st.session_state['user_login_allowed'] = True
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []
if 'announcement' not in st.session_state:
    st.session_state['announcement'] = "🚀 Hoş geldiniz! Portfolyomdaki projeleri keşfedin."
if 'announcement_color' not in st.session_state:
    st.session_state['announcement_color'] = 'success'
if 'not_kartlari' not in st.session_state:
    st.session_state['not_kartlari'] = DEFAULT_NOTLAR.copy()
if 'quiz_questions' not in st.session_state:
    st.session_state['quiz_questions'] = None 
if 'deneme_aktif' not in st.session_state:
    st.session_state['deneme_aktif'] = False
if 'deneme_konusu' not in st.session_state:
    st.session_state['deneme_konusu'] = ""
if 'pdf_cevaplari' not in st.session_state:
    st.session_state['pdf_cevaplari'] = DEFAULT_PDF_CEVAPLARI.copy() 


# --- PORTFOLYO İÇERİK FONKSİYONU ---
def get_portfolyo_bilgisi(baslik):
    if baslik == "Hakkımda":
        return ("Merhaba, ben Yusuf Efe Şahin. Bu kişisel portfolyo sayfamda, teknoloji, yazılım
