import streamlit as st
import time

# --- OTURUM DURUMU (SESSION STATE) BAŞLANGIÇ AYARLARI ---
ADMIN_PASSWORD = "123"
MOCK_USERS = [
    {"username": "yusuf", "email": "yusuf@mail.com", "password_hash": "y123"},
    {"username": "efe", "email": "efe@mail.com", "password_hash": "e456"},
]

# Varsayılan Not Kartları (Sadece Matematik ve Python)
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
if st.session_state['music_enabled'] and st.session_state['music_url']:
    st.audio(
        st.session_state['music_url'], 
        format="audio/mp3", 
        start_time=0, 
        loop=True,
        html_attrs={"autoplay": "autoplay", "volume": st.session_state['music_volume']} 
    )

# --- CHAT BOT MANTIĞI (BASİT SİMÜLASYON) ---
def general_chat_portfolyo(mesaj):
    mesaj_lower = mesaj.lower().strip()
    basit_cevaplar = {"merhaba": "Selam, Portfolyo sitesine hoş geldin!", "nasılsın": "Çok iyi çalışıyorum, teşekkürler!", "proje": "Projelerim sayfasına göz atmak ister misin?", "hata": "Hata bildirimleri için Yorum alanını kullanabilirsin."}
    
    for kelime, cevap in basit_cevaplar.items():
        if kelime in mesaj_lower:
            return f"🤖 (Kanka): {cevap}"
    return f"🤖 (Kanka): Anladım. Ben Yusuf Efe Şahin'in AI asistanıyım. Projeleri merak ediyorsan, kartlardan birini seçebilirsin."


# --- BAŞLIK VE CSS AYARLARI ---
st.markdown(f'<style>h1, h2, h3, h4, h5, h6 {{color: #FFFFFF;}}</style>', unsafe_allow_html=True)
st.title(f"💼 Yusuf Efe Şahin Portfolyo")

# --- ZİYARETÇİ MODU (Admin değilse) ---
if not st.session_state['admin_mode']:

    # --- SES KONTROLLERİ (Ana Sayfa) ---
    col_kapat, col_ac, col_volume_slider = st.columns([1, 1, 6]) 

    if st.session_state['music_enabled']:
        with col_kapat:
            if st.button("🔊 Kapat", key="btn_kapat_ses", use_container_width=True):
                st.session_state['music_enabled'] = False
                st.rerun()
        with col_volume_slider:
            # Ses seviyesi kaydırıcısı
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
    # ... diğer duyuru renkleri
    
    # --- NAVİGASYON (SAYFA SEÇİM KARTLARI) ---
    st.header("🌐 Site Bölümleri")

    SAYFALAR = ["Hakkımda", "Projelerim", "İletişim", "Kanka Chat"]
    col_list = st.columns(len(SAYFALAR))

    for i, sayfa in enumerate(SAYFALAR):
        with col_list[i]:
            if st.button(f"{SAYFALAR[i]}", key=f"btn_{SAYFALAR[i]}", use_container_width=True):
                st.session_state['secilen_sayfa'] = SAYFALAR[i]
                st.rerun()

    st.markdown("---")
    secilen_sayfa = st.session_state['secilen_sayfa']
    st.subheader(f"✅ Seçili Sayfa: {secilen_sayfa}")

    
    # --- İÇERİK YAZDIRMA ---
    if secilen_sayfa != "Kanka Chat":
        icerik, simge = get_portfolyo_bilgisi(secilen_sayfa)

        st.markdown(f"## {simge} {secilen_sayfa}")
        st.markdown(f"**{icerik}**")
        
        if secilen_sayfa == "Projelerim":
             st.markdown("---")
             st.subheader("📚 Not Kartları")
             kart_isimleri = list(st.session_state['not_kartlari'].keys())
             cols_not = st.columns(len(kart_isimleri))

             for i, isim in enumerate(kart_isimleri):
                 with cols_not[i]:
                     with st.container(border=True):
                         st.markdown(f"**{isim}**")
                         st.caption(f"Konu: {st.session_state['not_kartlari'][isim]}")
                         if not st.session_state['user_logged_in']:
                             st.warning("Giriş Yapılmalı")
                         else:
                             st.success("Notlara Erişildi (Simülasyon)")
                             
        elif secilen_sayfa == "İletişim":
            st.markdown("---")
            st.markdown("### 📝 İletişim Formu")
            with st.form("iletisim_formu"):
                isim = st.text_input("Adınız Soyadınız")
                email = st.text_input("E-posta Adresiniz")
                mesaj = st.text_area("Mesajınız")
                if st.form_submit_button("Gönder (Simülasyon)"):
                    st.success(f"Teşekkürler, {isim}! Mesajınız başarıyla iletildi.")

    else:
        # KANKA CHAT BOT ALANI
        with st.expander("💬 KANKA Sohbet Alanını Aç"):
            st.header("💬 KANKA Sohbet Alanı")
            for chat in st.session_state.chat_history:
                with st.chat_message("user"):
                    st.markdown(chat["user"])
                with st.chat_message("robot"):
                    st.markdown(chat["robot"])
            
            kanka_mesaji = st.chat_input("Kanka'ya mesajınızı girin:", key="kanka_chat_input")
            if kanka_mesaji:
                robot_cevap = general_chat_portfolyo(kanka_mesaji)
                st.session_state.chat_history.append({"user": kanka_mesaji, "robot": robot_cevap})
                st.rerun()
            
            if st.session_state.chat_history and st.button("Sohbeti Temizle"):
                st.session_state.chat_history = []
                st.rerun()

    st.markdown("---")

# --- YÖNETİCİ VE YAN PANEL (SIDEBAR) AYARLARI ---
st.sidebar.title("Kullanıcı İşlemleri")

# YÖNETİCİ MODU
if st.session_state['admin_mode']:
    st.sidebar.subheader("⚙️ Yönetici Ayarları")
    st.sidebar.button("🔒 YÖNETİCİ ÇIKIŞI", on_click=lambda: (st.session_state.update({'admin_mode': False}), st.rerun()))
    
    # TEMA RENGİ AYARI
    new_color = st.sidebar.color_picker(
        "Uygulama Tema Rengini Seçin:", 
        st.session_state['app_color']
    )
    if new_color != st.session_state['app_color']:
        st.session_state['app_color'] = new_color
        st.rerun()
    
    # MÜZİK KONTROLÜ (Özel URL Düzeltmesi Burada)
    st.sidebar.markdown("---")
    st.sidebar.subheader("🎶 Müzik Ayarları")
    
    MUSIC_OPTIONS = {
        "Melodi 1": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3",
        "Piyano Melodisi": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3",
        "Özel Şarkı Linki Gir": "CUSTOM_URL",
        "Müzik Kapalı": ""
    }
    
    # Yönetici Ses Düzeyi
    yeni_volume = st.sidebar.slider("Yönetici Ses Seviyesi", 0.0, 1.0, st.session_state['music_volume'], step=0.1, key="admin_music_volume_slider")
    if yeni_volume != st.session_state['music_volume']:
        st.session_state['music_volume'] = yeni_volume
        st.rerun() 

    secilen_sarki_adi = st.sidebar.selectbox("Çalınacak Şarkıyı Seçin:", options=list(MUSIC_OPTIONS.keys()))
    yeni_url = MUSIC_OPTIONS[secilen_sarki_adi]
    
    if secilen_sarki_adi == "Özel Şarkı Linki Gir":
        custom_url_input = st.sidebar.text_input("MP3 Linkini Yapıştırın:", key="custom_music_url_input", value=st.session_state.get('music_url') if st.session_state.get('music_url') not in MUSIC_OPTIONS.values() else "")
        if custom_url_input:
             yeni_url = custom_url_input
        else:
             st.sidebar.warning("Lütfen geçerli bir MP3 linki girin.")
             yeni_url = st.session_state['music_url'] 

    # URL ve Müzik Açma/Kapama Kontrolü
    if yeni_url != st.session_state['music_url']:
        st.session_state['music_url'] = yeni_url
        st.session_state['music_enabled'] = bool(yeni_url) 
        st.rerun() 
    
    # DUYURU AYARLARI
    st.sidebar.markdown("---")
    st.sidebar.subheader("📢 Site Duyurusu")
    st.session_state['announcement'] = st.sidebar.text_area("Duyuru Metni:", value=st.session_state['announcement'])
    st.session_state['announcement_color'] = st.sidebar.selectbox("Duyuru Kutusu Rengi:", ["success", "info", "warning", "error"], index=["success", "info", "warning", "error"].index(st.session_state['announcement_color']))
    if st.sidebar.button("Duyuruyu Güncelle"):
        st.rerun()
    
    # SİSTEM KONTROLLERİ
    st.sidebar.markdown("---")
    st.sidebar.subheader("🚨 Sistem Kontrolleri")
    st.session_state['registration_allowed'] = st.sidebar.checkbox("Üye Kaydı Açık", st.session_state['registration_allowed'])
    st.session_state['user_login_allowed'] = st.sidebar.checkbox("Üye Girişi Açık", st.session_state['user_login_allowed'])

else:
    # ZİYARETÇİ VE ÜYE İŞLEMLERİ
    st.sidebar.button("🔒 Yönetici Girişi", on_click=lambda: st.session_state.update({'show_admin_login': True, 'show_user_login': False, 'show_user_register': False}))

    # YÖNETİCİ GİRİŞ FORMU
    if st.session_state['show_admin_login']:
        with st.sidebar.form("admin_login_form"):
            admin_pass = st.text_input("Yönetici Şifresi", type="password")
            if st.form_submit_button("Giriş Yap"):
                if admin_pass == ADMIN_PASSWORD:
                    st.session_state['admin_mode'] = True
                    st.session_state['show_admin_login'] = False
                    st.rerun()
                else:
                    st.error("Hatalı yönetici şifresi.")
    
    # ÜYE GİRİŞ/ÇIKIŞ
    if st.session_state['user_logged_in']:
        st.sidebar.success(f"Giriş Yapıldı: {st.session_state['current_user'].upper()}")
        st.sidebar.button("🚪 Üye Çıkışı", on_click=user_logout)
    else:
        st.sidebar.button("👤 Üye Girişi", on_click=lambda: st.session_state.update({'show_user_login': not st.session_state['show_user_login'], 'show_admin_login': False, 'show_user_register': False}))
        if st.session_state['show_user_login']:
            with st.sidebar.form("user_login_form"):
                user_name = st.text_input("Kullanıcı Adı")
                user_pass = st.text_input("Şifre", type="password")
                col1, col2 = st.columns(2)
                with col1:
                    st.form_submit_button("Giriş Yap", on_click=user_login, args=(user_name, user_pass))
                with col2:
                    if st.form_submit_button("Şifremi Unuttum"):
                         forgot_password_simulation(user_name or "Bilinmiyor", is_admin=False)
    
    # ÜYE KAYIT
    if st.session_state['registration_allowed'] and not st.session_state['user_logged_in']:
        st.sidebar.button("📝 Kaydol", on_click=lambda: st.session_state.update({'show_user_register': not st.session_state['show_user_register'], 'show_admin_login': False, 'show_user_login': False}))
        if st.session_state['show_user_register']:
            with st.sidebar.form("user_register_form"):
                st.text_input("Kullanıcı Adı (Kaydol)")
                st.text_input("E-posta Adresi")
                st.text_input("Şifre Belirle", type="password")
                if st.form_submit_button("Hesap Oluştur (Simülasyon)"):
                    st.info(f"Kayıt işlemi başarıyla simüle edildi! Lütfen giriş yapın.")
                    st.session_state['show_user_register'] = False
                    st.rerun()
    
st.sidebar.markdown("---")
st.sidebar.title("⭐ Yorumlar ve Geri Bildirim")

# Yorum Formu
with st.sidebar.form("geri_bildirim_formu", clear_on_submit=True):
    st.sidebar.write("Site hakkındaki yorumlarınızı buraya yazın.")
    st.selectbox("Konu:", ["Genel Yorum", "Hata Bildirimi", "Tasarım Önerisi", "Teşekkür"])
    st.text_area("Mesajınız:")
    if st.form_submit_button("Yorumu Gönder"):
        st.sidebar.success(f"Yorumunuz başarıyla iletildi!")

st.sidebar.markdown("---")
st.sidebar.caption("Geliştirici: Yusuf Efe Şahin | Portfolyo v2.0")
