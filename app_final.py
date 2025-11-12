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
        return ("""Merhaba, ben Yusuf Efe Şahin. Bu kişisel portfolyo sayfamda, teknoloji, yazılım ve tasarım alanındaki çalışmalarımı sergiliyorum. Yaratıcı projeler geliştirmeye ve sürekli öğrenmeye odaklıyım.""", "👨‍💻")
    elif baslik == "Projelerim":
        return ("""Yaptığım bazı öne çıkan projeler ve kullandığım teknolojiler aşağıdadır.

* **Portfolyo Sitesi (Streamlit/Python):** Yönetici ve üye panelli kişisel site.
* **Notlar:** Ders notlarına artık doğrudan ana menüden erişebilirsiniz. (7. Sınıf Konuları)""", "💡")
    return ("İçerik Bulunamadı.", "❓")


# --- GİRİŞ / ÇIKIŞ VE KONTROL FONKSİYONLARI ---
def user_login(username, password):
    if not st.session_state['user_login_allowed']:
        st.error("Üye girişi şu anda bakımdadır.")
        return
    for user in MOCK_USERS:
        if user["username"] == username and user["password_hash"] == password:
            st.session_state['user_logged_in'] = True
            st.session_state['current_user'] = username
            st.session_state['show_user_login'] = False
            st.success(f"Hoş geldiniz, {username.upper()}!") 
            time.sleep(1)
            st.rerun()
            return
    if len(username) > 0 and len(password) > 0:
         st.session_state['user_logged_in'] = True
         st.session_state['current_user'] = username
         st.session_state['show_user_login'] = False
         st.success(f"Hoş geldiniz, {username.upper()}! (Simülasyon Girişi Başarılı)")
         time.sleep(1)
         st.rerun()
    else:
        st.error("Kullanıcı adı veya şifre yanlış. (Demo: yusuf/y123)")

def user_login_as_guest():
    st.session_state['user_logged_in'] = True
    st.session_state['current_user'] = "ZİYARETÇİ"
    st.session_state['show_user_login'] = False
    st.success("Misafir olarak giriş yapıldı. Bazı özellikler kısıtlanmıştır.")
    time.sleep(1)
    st.rerun()


def user_logout():
    st.session_state['user_logged_in'] = False
    st.session_state['current_user'] = None
    st.session_state['show_user_login'] = False
    st.session_state['show_admin_login'] = False
    st.session_state['show_user_register'] = False
    st.rerun()

def forgot_password_simulation(email_or_username, is_admin=False):
    st.sidebar.warning("Sistem simülasyon modunda olduğundan, şifre sıfırlama kodu e-posta adresinize gönderilmiş gibi yapıldı.")
    time.sleep(1)
    if is_admin:
        st.sidebar.success(f" Yönetici Şifresi sıfırlama maili 'admin@portfolyo.com' adresine gönderildi.")
    else:
        st.sidebar.success(f" Kullanıcı şifresi sıfırlama kodu '{email_or_username}@mail.com' adresine gönderildi.")
        
# --- CHAT BOT MANTIĞI (7. Sınıfa Odaklı Detaylı Cevaplar Eklendi) ---
def general_chat_portfolyo(mesaj):
    mesaj_lower = mesaj.lower().strip()
    
    # 7. Sınıf Konu Cevapları
    if "rasyonel sayı" in mesaj_lower or "rasyonel nedir" in mesaj_lower:
        cevap = "🤖 (Kanka): Rasyonel sayılar, a ve b birer tam sayı olmak üzere, b'nin sıfır olmadığı durumlarda a/b şeklinde yazılabilen sayılardır. Kesirler ve ondalık sayılar da bu kümeye dahildir. Örneğin, 3/4 veya -1.5 birer rasyonel sayıdır."
    elif "koç" in mesaj_lower or "koçluk" in mesaj_lower:
        cevap = "🤖 (Kanka): Koçlarımız, 7. Sınıf konularında size özel ders programı hazırlama ve motivasyon konularında yardımcı olurlar. 'Ders Koçlarımız' sayfasından detaylı bilgiye ulaşabilirsiniz."
    elif "deneme" in mesaj_lower:
        cevap = "🤖 (Kanka): Deneme Sınavı bölümünden 7. Sınıf genel tekrar denemelerini çözebilir veya PDF Sonuç Kontrol bölümünden indirdiğin denemelerin sonuçlarını kontrol edebilirsin."
    elif "merhaba" in mesaj_lower or "selam" in mesaj_lower:
        cevap = "🤖 (Kanka): Merhaba! Ben senin 7. Sınıf konularında yardımcı olan AI asistanın Kanka. Sana nasıl yardımcı olabilirim?"
    else:
        cevap = f"🤖 (Kanka): Şu anda sadece 7. Sınıf konularına odaklanabiliyorum. Lütfen daha spesifik bir soru sorun veya Koçluk, Deneme, PDF gibi anahtar kelimeleri kullanın."
    
    return cevap

# --- DENEME SINAVI SORULARI (DAHA KAPSAMLI BİR DEMO İÇİN) ---
DENEME_SINAVI_SORULARI = [
    {"q": "7. Sınıfın en önemli matematik konularından biri nedir?", "a": ["Türev", "Rasyonel Sayılar", "Fonksiyon", "Trigonometri"], "c": "Rasyonel Sayılar", "ders": "Matematik"},
    {"q": "Türkçede eylemin anlam özelliğini belirtiniz: 'Uyumak'", "a": ["Kılış", "Durum", "Oluş", "Kip"], "c": "Durum", "ders": "Türkçe"},
    {"q": "Ahiret hayatının başlangıcı nedir?", "a": ["Kıyamet", "Haşir", "Ölüm", "Sırat"], "c": "Ölüm", "ders": "Din Kültürü"},
