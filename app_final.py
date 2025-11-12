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
    {"q": "Türk-İslam devletlerinin kurulduğu dönem hangisidir?", "a": ["İlk Çağ", "Orta Çağ", "Yakın Çağ", "Yeni Çağ"], "c": "Orta Çağ", "ders": "Tarih"},
    {"q": "Aşağıdaki rasyonel sayılardan hangisi en büyüktür?", "a": ["1/2", "-1/4", "3/4", "1/5"], "c": "3/4", "ders": "Matematik"},
]

# --- BAŞLIK AYARLARI ---
st.title(f"💼 Yusuf Efe Şahin Portfolyo")

# --- ZİYARETÇİ MODU (Admin değilse) ---
if not st.session_state['admin_mode']:

    # --- GENEL FON MÜZİĞİ KONTROLLERİ ---
    col_kapat, col_ac, col_volume_slider = st.columns([1, 1, 6]) 

    if st.session_state['music_enabled']:
        # Görünmez/Küçük müzik oynatıcı (Uygulamanın genelinde fon müziği çalması için)
        st.audio(st.session_state['music_url'], format="audio/mp3", loop=True)
        
        with col_kapat:
            if st.button("🔊 Müzik Kapat", key="btn_kapat_ses", use_container_width=True):
                st.session_state['music_enabled'] = False
                st.rerun()
        with col_volume_slider:
            new_volume = st.slider("Müzik Ses Seviyesi", 0.0, 1.0, st.session_state['music_volume'], step=0.1, key="music_volume_slider")
            if new_volume != st.session_state['music_volume']:
                st.session_state['music_volume'] = new_volume
                st.rerun()
    elif st.session_state['music_url']: 
        with col_ac:
            if st.button("🔇 Müzik Aç", key="btn_ac_ses", use_container_width=True):
                st.session_state['music_enabled'] = True
                st.rerun()
    
    st.markdown("---")
    
    # Duyuru Mesajı
    if st.session_state['announcement_color'] == 'success':
        st.success(f"📣 {st.session_state['announcement']}")
    
    # --- NAVİGASYON (Konu Seçimi Belirginleştirildi) ---
    st.header("🌐 Site Bölümleri ve Konu Seçimi (7. Sınıf Dersleri)")

    DERS_ISIMLERI = list(DEFAULT_NOTLAR.keys()) 
    SAYFALAR = ["Hakkımda", "Projelerim", "İletişim", "Kanka Chat", "Deneme Sınavı", "PDF Sonuç Kontrol", "Ders Koçlarımız", "Çalışma Alanı"] + DERS_ISIMLERI 
    
    # Ana Sayfa ve Proje Butonları
    ANA_SAYFA_BUTONLARI = ["Hakkımda", "Projelerim", "İletişim", "Kanka Chat"]
    col_ana = st.columns(len(ANA_SAYFA_BUTONLARI))
    for i, sayfa in enumerate(ANA_SAYFA_BUTONLARI):
        with col_ana[i]:
            if st.button(f"🔹 {sayfa}", key=f"btn_{sayfa}", use_container_width=True):
                st.session_state['secilen_sayfa'] = sayfa
                st.rerun()
                
    st.markdown("---")
    st.subheader("📚 Dersler, Denemeler ve Koçluk Alanı")
    
    # Dersler ve Koçluk Butonları
    DERS_VE_OZEL_BUTONLAR = ["Deneme Sınavı", "PDF Sonuç Kontrol", "Ders Koçlarımız", "Çalışma Alanı"] + DERS_ISIMLERI
    num_cols_for_nav = 6
    cols_nav = st.columns(num_cols_for_nav)

    for i, sayfa in enumerate(DERS_VE_OZEL_BUTONLAR):
        with cols_nav[i % num_cols_for_nav]:
            if st.button(f"🔸 {sayfa}", key=f"btn_{sayfa}", use_container_width=True):
                st.session_state['secilen_sayfa'] = sayfa
                st.rerun()


    st.markdown("---")
    secilen_sayfa = st.session_state['secilen_sayfa']
    st.subheader(f"✅ Seçili Sayfa: {secilen_sayfa}")

    
    # --- İÇERİK YAZDIRMA ---
    
    # 1. DERS SAYFASI İÇERİĞİ (SESLİ DERS KALDIRILDI)
    if secilen_sayfa in DERS_ISIMLERI:
        st.header(f"📚 {secilen_sayfa} Dersi Notları (7. Sınıf)")
        konu = st.session_state['not_kartlari'][secilen_sayfa]
        st.info(f"👉 Ana Konu: **{konu}**")
        st.markdown("---")
        
        st.subheader("📝 Detaylı Konu Anlatımı")
        st.markdown(f"Koçunuz tarafından hazırlanan detaylı **{konu}** anlatım özetleri burada yer alacaktır.")
        
        if st.session_state['user_logged_in'] and st.session_state['current_user'] != "ZİYARETÇİ":
            st.success(f"**{secilen_sayfa}** dersine ait detaylı notlara erişim izniniz var. (Simülasyon İçeriği)")
            st.markdown(f"Burada **{konu}** ile ilgili zenginleştirilmiş, gerçek içerik gösterilecektir.")
        else:
            st.warning("Bu dersin notlarının tamamını görmek için lütfen tam üye girişi yapın.")
            
    # 2. PORTFOLYO SAYFALARI (Hakkımda, Projelerim)
    elif secilen_sayfa in ["Hakkımda", "Projelerim"]:
        icerik, simge = get_portfolyo_bilgisi(secilen_sayfa)

        st.markdown(f"## {simge} {secilen_sayfa}")
        st.markdown(f"**{icerik}**")
    
    # 3. İLETİŞİM SAYFASI
    elif secilen_sayfa == "İletişim":
        st.header("📧 İletişim Bilgileri")
        st.markdown("""
            Sorularınız, iş teklifleri veya geri bildirimleriniz için benimle aşağıdaki yollarla iletişime geçebilirsiniz:
            
            * **E-posta:** yusuf_efe_sahin@mail.com (Simülasyon)
            * **LinkedIn:** /yusufeşahin (Simülasyon)
        """)
        
    # 4. KANKA CHAT BOT ALANI
    elif secilen_sayfa == "Kanka Chat":
        with st.expander("💬 KANKA Sohbet Alanını Aç"):
            st.header("💬 KANKA Sohbet Alanı (7. Sınıf Uzmanı)")
            for chat in st.session_state.chat_history:
                with st.chat_message("user"):
                    st.markdown(chat["user"])
                with st.chat_message("robot"):
                    st.markdown(chat["robot"])
            
            kanka_mesaji = st.chat_input("Kanka'ya 7. Sınıf konularıyla ilgili mesajınızı girin:", key="kanka_chat_input")
            if kanka_mesaji:
                robot_cevap = general_chat_portfolyo(kanka_mesaji)
                st.session_state.chat_history.append({"user": kanka_mesaji, "robot": robot_cevap})
                st.rerun()
    
    # 5. DENEME SINAVI SAYFASI
    elif secilen_sayfa == "Deneme Sınavı":
        st.header("📚 Deneme Sınavı Çöz (7. Sınıf)")
        st.info("Bu alandan 7. Sınıf seviyesinde karma deneme sınavı çözerek bilginizi test edebilirsiniz. **İsteyen öğrenci PDF indirip çözebilir, isteyen bu sayfada çözebilir.**")
        
        if not st.session_state['deneme_aktif']:
            if st.button("Denemeyi Başlat (5 Soru)", key="start_deneme_btn"):
                st.session_state['deneme_aktif'] = True
                st.session_state['deneme_konusu'] = "7. Sınıf Genel Tekrar (Demo)"
                st.session_state['quiz_questions'] = DENEME_SINAVI_SORULARI 
                st.session_state['quiz_submitted'] = False
                st.rerun()
        
        # Sınav Aktif ise Formu Göster
        if st.session_state['deneme_aktif'] and st.session_state['quiz_questions']:
            st.subheader(f"Aktif Deneme: {st.session_state['deneme_konusu']} ({len(st.session_state['quiz_questions'])} Soru)")
            
            with st.form("deneme_form"):
                kullanici_cevaplari = {}
                
                for i, q in enumerate(st.session_state['quiz_questions']):
                    q_text = q['q']
                    st.markdown(f"**Soru {i+1} ({q['ders']}):** {q_text}")
                    kullanici_cevaplari[f"q_{i}"] = st.radio(f"Cevabınız:", q['a'], key=f"q_radio_{i}")
                    st.markdown("---")

                if st.form_submit_button("Denemeyi Bitir ve Sonucu Gör"):
                    dogru_sayisi = 0
                    
                    st.subheader("Deneme Sonuçları")
                    
                    for i, q in enumerate(st.session_state['quiz_questions']):
                        secim = kullanici_cevaplari[f"q_{i}"]
                        
                        if secim == q['c']:
                            dogru_sayisi += 1
                            st.success(f"✅ Soru {i+1} (Doğru): {q['q']}")
                        else:
                            st.error(f"❌ Soru {i+1} (Yanlış): Doğru Cevap: {q['c']}")
                    
                    st.balloons()
                    st.markdown(f"## 🎉 TOPLAM DOĞRU SAYINIZ: {dogru_sayisi} / {len(st.session_state['quiz_questions'])}")
                    
                    st.session_state['deneme_aktif'] = False
                    st.session_state['quiz_questions'] = None
                    st.session_state['quiz_submitted'] = True
                    st.markdown("---")
                    if st.button("Yeni Deneme Başlat"):
                         st.rerun()

    
    # 6. PDF SONUÇ KONTROL SAYFASI
    elif secilen_sayfa == "PDF Sonuç Kontrol":
        st.header("📄 PDF/Döküman Sonuç Kontrolü")
        
        # PDF İndirme Simülasyonu
        st.markdown("### 📥 Dökümanları İndir (Simülasyon)")
        st.info("Aşağıdaki listeden dilediğiniz PDF'i indirebilir, çözdükten sonra cevaplarınızı bu sayfadan kontrol edebilirsiniz.")
        
        pdf_listesi = st.session_state['pdf_cevaplari'].keys()
        for kod in pdf_listesi:
            st.download_button(
                label=f"PDF İndir: {kod} ({len(st.session_state['pdf_cevaplari'][kod])} Soru)",
                data="Bu bir simülasyon PDF'idir. Gerçek içerik bulunmamaktadır.",
                file_name=f"{kod}_Deneme_7_Sinif.pdf",
                mime="application/pdf"
            )

        st.markdown("---")

        st.markdown("### ✅ Cevap Kontrolü")
        
        if not st.session_state['pdf_cevaplari']:
            st.warning("Kontrol edilecek aktif bir PDF dökümanı bulunmamaktadır. Yönetici eklemesini bekleyiniz.")
        else:
            with st.form("pdf_kontrol_formu", clear_on_submit=False):
                deneme_kodu = st.selectbox(
                    "Kontrol Edilecek Dökümanı Seçin:",
                    options=list(st.session_state['pdf_cevaplari'].keys()),
                    key="pdf_select"
                )
                cevap_anahtari_input = st.text_input(
                    "Kendi Cevaplarınızı Girin (Sadece Harfler, Örn: ADBCBAADCC):", 
                    max_chars=30,
                    key="cevap_input"
                )
                
                if st.form_submit_button("Sonuçları Kontrol Et"):
                    if not cevap_anahtari_input or not cevap_anahtari_input.isalpha():
                        st.error("Lütfen geçerli bir cevap dizisi girin (Sadece A, B, C, D harfleri olmalı).")
                    else:
                        girilen_cevaplar = cevap_anahtari_input.upper()
                        dogru_cevaplar = st.session_state['pdf_cevaplari'].get(deneme_kodu, "")
                        
                        if not dogru_cevaplar:
                            st.error("Seçilen dökümanın cevap anahtarı sistemde bulunamadı.")
                        else:
                            if len(girilen_cevaplar) != len(dogru_cevaplar):
                                st.warning(f"Girdiğiniz cevap sayısı ({len(girilen_cevaplar)}) ile döküman sorusu sayısı ({len(dogru_cevaplar)}) uyuşmuyor. Kontrol yine de yapıldı.")
                                
                            dogru_sayisi = 0
                            kontrol_limit = min(len(girilen_cevaplar), len(dogru_cevaplar))
                            
                            for i in range(kontrol_limit):
                                if girilen_cevaplar[i] == dogru_cevaplar[i]:
                                    dogru_sayisi += 1
                                    
                            yanlis_sayisi = kontrol_limit - dogru_sayisi
                            bos_sayisi = len(dogru_cevaplar) - kontrol_limit if len(dogru_cevaplar) > kontrol_limit else 0
                            
                            st.success(f"### 🎉 Kontrol Başarılı!")
                            st.markdown(f"**Döküman Kodu:** {deneme_kodu}")
                            st.markdown(f"**Toplam Soru Sayısı:** {len(dogru_cevaplar)}")
                            st.markdown(f"**Doğru Sayısı:** {dogru_sayisi}")
                            st.markdown(f"**Yanlış Sayısı:** {yanlis_sayisi}")
                            st.markdown(f"**Boş Sayısı (Eksik Cevap):** {bos_sayisi}")
                            st.markdown("---")
                            st.markdown(f"**(NOT: Net hesaplaması için 4 yanlışın 1 doğruyu götürmesi kuralı uygulanmamıştır. Simülasyon.)**")

    # 7. DERS KOÇLARIMIZ SAYFASI (İSİMLER SİLİNDİ)
    elif secilen_sayfa == "Ders Koçlarımız":
        st.header("👨‍🏫 Ders Koçlarımız")
        st.info("Başarıya giden yolda size destek olacak, alanında uzman koçlarımızla tanışın.")
        
        cols_koc = st.columns(3)
        for i, koc in enumerate(MOCK_KOCLAR):
            with cols_koc[i % 3]:
                with st.container(border=True):
                    # İSİM YERİNE SADECE GENEL TANIM KULLANILDI
                    st.subheader(f"Koç | {koc['alan']}") 
                    st.markdown(f"**Uzmanlık Alanı:** *{koc['alan']}*")
                    st.caption(koc['bio'])
                    if st.session_state['user_logged_in'] and st.session_state['current_user'] != "ZİYARETÇİ":
                        st.button("Randevu Talep Et (Simülasyon)", key=f"koc_randevu_{i}", use_container_width=True)
                    else:
                        st.warning("Randevu almak için tam üye girişi yapın.")

    # 8. KOÇ-ÖĞRENCİ ÇALIŞMA ALANI SAYFASI
    elif secilen_sayfa == "Çalışma Alanı":
        st.header("🎯 Koç-Öğrenci Çalışma Alanı")
        
        if st.session_state['user_logged_in'] and st.session_state['current_user'] != "ZİYARETÇİ":
            st.success(f"Hoş geldiniz, **{st.session_state['current_user'].upper()}**. Burası Koçunuzla birlikte planlama yapabileceğiniz alan.")
            
            st.markdown("---")
            st.subheader("🗓️ Haftalık Program (Demo)")
            st.markdown("""
            * **Pazartesi:** Rasyonel Sayılar Tekrarı (30 Soru)
            * **Salı:** Türkçe Fiiller Konu Anlatımı
            * **Çarşamba:** Deneme Sınavı Çözümü
            * **Perşembe:** Koç Görüşmesi (19:00)
            * **Cuma:** Sosyal Bilgiler Özet Çıkarma
            """)
            
            st.subheader("📝 Koçunuza Mesaj Gönderin")
            with st.form("koc_mesaj_formu", clear_on_submit=True):
                st.text_area("Koçunuza iletmek istediğiniz mesajı buraya yazın:", height=150)
                if st.form_submit_button("Mesajı Gönder"):
                    st.success("Mesajınız koçunuza başarıyla iletildi. En kısa sürede geri dönüş yapılacaktır.")
        else:
            st.warning("Bu alana erişmek için lütfen tam üye girişi yapın.")


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
    
    # MÜZİK KONTROLÜ
    st.sidebar.markdown("---")
    st.sidebar.subheader("🎶 Fon Müziği Ayarları")
    
    MUSIC_OPTIONS = {
        "Melodi 1 (Genel Fon)": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3",
        "Piyano Melodisi (Fon)": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3",
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
        if custom_url_input and custom_url_input.lower().endswith('.mp3'):
             yeni_url = custom_url_input
        else:
             st.sidebar.warning("Lütfen geçerli bir MP3 linki girin. (Örn: ...mp3)")
             yeni_url = st.session_state['music_url'] 
    
    if yeni_url != st.session_state['music_url']:
        st.session_state['music_url'] = yeni_url
        st.session_state['music_enabled'] = bool(yeni_url) 
        st.rerun() 
    
    # PDF YÖNETİMİ (YÖNETİCİ KONTROLÜ)
    st.sidebar.markdown("---")
    st.sidebar.subheader("📄 PDF Cevap Yönetimi")
    with st.sidebar.form("pdf_management_form", clear_on_submit=True):
        st.write("Yeni PDF Cevap Anahtarı Ekle")
        yeni_kod = st.text_input("Döküman Kodu (Örn: DENEME_3)", max_chars=15).upper()
        yeni_cevap = st.text_input("Cevap Anahtarı (Örn: ABCDC)", max_chars=30).upper()
        
        col_ekle, col_sil = st.columns(2)
        
        with col_ekle:
            if st.form_submit_button("Ekle/Güncelle"):
                if yeni_kod and yeni_cevap and yeni_cevap.isalpha():
                    st.session_state['pdf_cevaplari'][yeni_kod] = yeni_cevap
                    st.sidebar.success(f"'{yeni_kod}' kodu {len(yeni_cevap)} soru ile eklendi/güncellendi!")
                    time.sleep(1)
                    st.rerun()
                else:
                    st.sidebar.error("Lütfen Kodu ve sadece harflerden oluşan Cevap Anahtarını girin.")

    # Mevcut PDF'leri Listeleme ve Silme
    st.sidebar.markdown("#### Mevcut Dökümanlar")
    if st.session_state['pdf_cevaplari']:
        pdf_sil_secim = st.sidebar.selectbox(
            "Silinecek Dökümanı Seçin:",
            options=["Seçiniz"] + list(st.session_state['pdf_cevaplari'].keys()),
            key="pdf_sil_selectbox"
        )
        
        if pdf_sil_secim != "Seçiniz":
            st.sidebar.info(f"Kod: **{pdf_sil_secim}** ({len(st.session_state['pdf_cevaplari'][pdf_sil_secim])} Soru)")
            if st.sidebar.button(f"'{pdf_sil_secim}' Sil", key="btn_pdf_sil"):
                del st.session_state['pdf_cevaplari'][pdf_sil_secim]
                st.sidebar.success(f"Döküman '{pdf_sil_secim}' başarıyla silindi.")
                time.sleep(1)
                st.rerun()
    else:
        st.sidebar.warning("Sistemde kayıtlı PDF cevap anahtarı yok.")

    
    # DUYURU AYARLARI
    st.sidebar.markdown("---")
    st.sidebar.subheader("📢 Site Duyurusu")
    st.session_state['announcement'] = st.sidebar.text_area("Duyuru Metni:", value=st.session_state['announcement'])
    st.session_state['announcement_color'] = st.sidebar.selectbox("Duyuru Kutusu Rengi:", ["success", "info", "warning", "error"], index=["success", "info", "warning", "error"].index(st.session_state['announcement_color']))
    if st.sidebar.button("Duyuruyu Güncelle", key="btn_guncelle_duyuru"):
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
                    # Hata mesajı düzeltildi
                    st.error("Hatalı yönetici şifresi.") 
    
    # ÜYE GİRİŞ/ÇIKIŞ VE ZİYARETÇİ GİRİŞİ 
    if st.session_state['user_logged_in']:
        st.sidebar.success(f"Giriş Yapıldı: {st.session_state['current_user'].upper()}")
        st.sidebar.button("🚪 Üye Çıkışı", on_click=user_logout)
    else:
        # Standart Giriş Butonu
        st.sidebar.button("👤 Üye Girişi", on_click=lambda: st.session_state.update({'show_user_login': not st.session_state['show_user_login'], 'show_admin_login': False, 'show_user_register': False}))
        
        # Ziyaretçi Girişi Butonu
        st.sidebar.button("🟢 Ziyaretçi Girişi", on_click=user_login_as_guest)

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
