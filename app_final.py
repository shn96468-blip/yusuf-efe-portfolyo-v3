import streamlit as st
import time

# --- OTURUM DURUMU (SESSION STATE) BAŞLANGIÇ AYARLARI ---
ADMIN_PASSWORD = "123"
MOCK_USERS = [
    {"username": "yusuf", "email": "yusuf@mail.com", "password_hash": "y123"},
    {"username": "efe", "email": "efe@mail.com", "password_hash": "e456"},
]

# Varsayılan Not Kartları
DEFAULT_NOTLAR = {
    "Matematik": "Temel Fonksiyonlar",
    "Türkçe": "Dil Bilgisi Kuralları",
    "Din Kültürü": "Temel Kavramlar",
    "Tarih": "Önemli Olaylar ve Dönemler",
    "Sosyal Bilgiler": "Temel Sosyal Kavramlar", 
}

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
if 'quiz_params' not in st.session_state:
    st.session_state['quiz_params'] = None


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
        return ("Yaptığım bazı öne çıkan projeler ve kullandığım teknolojiler aşağıdadır.\n\n* **Portfolyo Sitesi (Streamlit/Python):** Yönetici ve üye panelli kişisel site.\n* **Notlar:** Ders notlarına artık doğrudan ana menüden erişebilirsiniz.", "💡")
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

def guest_login():
    """Yeni eklenen ziyaretçi (guest) girişi."""
    st.session_state['user_logged_in'] = True
    st.session_state['current_user'] = "ZİYARETÇİ"
    st.session_state['show_user_login'] = False
    st.session_state['show_admin_login'] = False
    st.session_state['show_user_register'] = False
    st.success("Ziyaretçi olarak giriş yapıldı. Kısıtlı notlara erişebilirsiniz.")
    time.sleep(1)
    st.rerun()
        
# --- MÜZİK ÇALMA MANTIĞI (Yorum Satırı Yapıldı) ---
# if st.session_state['music_enabled'] and st.session_state['music_url']:
#     st.audio(
#         st.session_state['music_url'], 
#         format="audio/mp3", 
#         start_time=0, 
#         loop=True
#     )

# --- CHAT BOT MANTIĞI ---
def general_chat_portfolyo(mesaj):
    mesaj_lower = mesaj.lower().strip()
    
    ders_cevaplari = {
        "fonksiyon nedir": "Matematikte bir fonksiyon, her girdiyi tam olarak bir çıktıya eşleyen bir kuraldır.",
        "pythonda değişken": "Python'da değişkenler, bilgileri depolamak için kullanılan bellek konumlarıdır.",
        "osmanlı": "Osmanlı İmparatorluğu, 1299'dan 1922'ye kadar var olmuş büyük bir devlettir.",
        "merhaba": "Selam, Portfolyo sitesine hoş geldin! Dersler hakkında veya projelerim hakkında soru sorabilirsin.",
        "proje": "Projelerim sayfasına göz atmak ister misin?",
        "hata": "Hata bildirimleri için Yorum alanını kullanabilirsin."
    }

    for kelime, cevap in ders_cevaplari.items():
        if kelime in mesaj_lower:
            return f"🤖 (Kanka): {cevap}"
            
    return f"🤖 (Kanka): Anladım. Ben Yusuf Efe Şahin'in AI asistanıyım. Hangi ders içeriğiyle ilgili bilgi almak istiyorsun? (Örn: 'Pythonda değişken nedir?' gibi.)"

# --- BAŞLIK VE CSS AYARLARI ---
st.markdown(f'<style>h1, h2, h3, h4, h5, h6 {{color: #FFFFFF;}}</style>', unsafe_allow_html=True)
st.title(f"💼 Yusuf Efe Şahin Portfolyo")

# --- ZİYARETÇİ MODU (Admin değilse) ---
if not st.session_state['admin_mode']:

    # --- SES KONTROLLERİ ---
    col_kapat, col_ac, col_volume_slider = st.columns([1, 1, 6]) 

    if st.session_state['music_enabled']:
        with col_kapat:
            if st.button("🔊 Kapat", key="btn_kapat_ses", use_container_width=True):
                st.session_state['music_enabled'] = False
                st.rerun()
        with col_volume_slider:
            new_volume = st.slider("Ses Seviyesi", 0.0, 1.0, st.session_state['music_volume'], step=0.1, key="music_volume_slider")
            if new_volume != st.session_state['music_volume']:
                st.session_state['music_volume'] = new_volume
                st.rerun()
    elif st.session_state['music_url']: 
        with col_ac:
            if st.button("🔇 Aç", key="btn_ac_ses", use_container_width=True):
                st.session_state['music_enabled'] = True
                st.rerun()
    
    st.markdown("---")
    
    # Duyuru Mesajı
    if st.session_state['announcement_color'] == 'success':
        st.success(f"📣 {st.session_state['announcement']}")
    
    # --- NAVİGASYON (İletişim ve Test Çöz Eklendi) ---
    st.header("🌐 Site Bölümleri (Dersler Dahil)")

    DERS_ISIMLERI = list(DEFAULT_NOTLAR.keys()) 
    SAYFALAR = ["Hakkımda", "Projelerim", "İletişim", "Kanka Chat", "Test Çöz"] + DERS_ISIMLERI 
    
    num_cols_for_nav = 5
    cols_nav = st.columns(num_cols_for_nav)
    
    for i, sayfa in enumerate(SAYFALAR):
        with cols_nav[i % num_cols_for_nav]:
            if st.button(f"{sayfa}", key=f"btn_{sayfa}", use_container_width=True):
                st.session_state['secilen_sayfa'] = sayfa
                # Test Çöz'e geçildiğinde eski quiz parametrelerini sıfırla
                if sayfa != "Test Çöz":
                     st.session_state['quiz_params'] = None
                st.rerun()

    st.markdown("---")
    secilen_sayfa = st.session_state['secilen_sayfa']
    st.subheader(f"✅ Seçili Sayfa: {secilen_sayfa}")

    
    # --- İÇERİK YAZDIRMA (YENİ MANTIK) ---
    
    # 1. DERS SAYFASI İÇERİĞİ
    if secilen_sayfa in DERS_ISIMLERI:
        st.header(f"📚 {secilen_sayfa} Dersi Notları")
        konu
