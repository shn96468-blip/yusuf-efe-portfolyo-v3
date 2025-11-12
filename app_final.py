import streamlit as st
import time

# --- OTURUM DURUMU (SESSION STATE) BAŞLANGIÇ AYARLARI ---
ADMIN_PASSWORD = "123"
MOCK_USERS = [
    {"username": "yusuf", "email": "yusuf@mail.com", "password_hash": "y123"},
    {"username": "efe", "email": "efe@mail.com", "password_hash": "e456"},
]

# Varsayılan Not Kartları (Sadece Matematik ve Python Kaldı)
DEFAULT_NOTLAR = {
    "Matematik": "Temel Fonksiyonlar",
    "Python": "Değişken Tipleri"
}

if 'admin_mode' not in st.session_state:
    st.session_state['admin_mode'] = False
if 'user_logged_in' not in st.session_state:
    st.session_state['user_logged_in'] = False
if 'current_user' not in st.session_state:
    st.session_state['current_user'] = None
if 'app_color' not in st.session_state:
    st.session_state['app_color'] = '#FF4B4B' # Portfolyo için Varsayılan Vurgu Rengi
if 'secilen_sayfa' not in st.session_state:
    st.session_state['secilen_sayfa'] = "Hakkımda" 
if 'music_enabled' not in st.session_state:
    st.session_state['music_enabled'] = True 
if 'music_url' not in st.session_state:
    st.session_state['music_url'] = "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"
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


# --- SAYFA AYARLARI ---
st.set_page_config(
    page_title="Yusuf Efe Şahin | Portfolyo",
    layout="wide",
    page_icon="💼" 
)

# --- PORTFOLYO İÇERİK FONKSİYONU ---
def get_portfolyo_bilgisi(baslik):
    if baslik == "Hakkımda":
        return ("Merhaba, ben Yusuf Efe Şahin. Bu kişisel portfolyo sayfamda, teknoloji, yazılım ve tasarım alanındaki çalışmalarımı sergiliyorum. Yaratıcı projeler geliştirmeye ve sürekli öğrenmeye odaklıyım.", "👨‍💻")
    elif baslik == "Projelerim":
        return ("Yaptığım bazı öne çıkan projeler ve kullandığım teknolojiler aşağıdadır:\n\n* **Portfolyo Sitesi (Streamlit/Python):** Yönetici ve üye panelli kişisel site.\n* **Not Kartları:** Matematik ve Python notlarına erişim.", "💡")
    elif baslik == "İletişim":
        return ("Bana ulaşmak için aşağıdaki formu kullanabilir veya sosyal medya hesaplarımdan yazabilirsiniz.\n\n* **E-posta:** yusuf_efe_sahin@mail.com (Simülasyon)\n* **LinkedIn:** /yusufefesahin (Simülasyon)", "📧")
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
    # Simülasyon Girişi
    if len(username) > 0 and len(password) > 0:
         st.session_state['user_logged_in'] = True
         st.session_state['current_user'] = username
         st.session_state['show_user_login'] = False
         st.success(f"Hoş geldiniz, {username.upper()}! (Simülasyon Girişi Başarılı)")
         time.sleep(1)
         st.rerun()
    else:
        st.error("Kullanıcı adı veya şifre yanlış. (Demo: yusuf/y123)")

def user_logout():
    st.session_state['user_logged_in'] = False
    st.session_state['current_user'] = None
    st.rerun()

def forgot_password_simulation(email_or_username, is_admin=False):
    st.sidebar.warning("Sistem simülasyon modunda olduğundan, şifre sıfırlama kodu e-posta adresinize gönderilmiş gibi yapıldı.")
    time.sleep(1)
    if is_admin:
        st.sidebar.success(f" Yönetici Şifresi sıfırlama maili 'admin@portfolyo.com' adresine gönderildi.")
    else:
        st.sidebar.success(f" Kullanıcı şifresi sıfırlama kodu '{email_or_username}@mail.com' adresine gönderildi.")


# --- MÜZİK ÇALMA MANTIĞI (Özel Link Kontrolü Burada) ---
if st.session_state['music_enabled'] and st.session
