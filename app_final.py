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
# NOT: Buraya özel butonlar için kırmızı border eklendi.
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
    
    /* Özel Buton Stili (Görsellerdeki Kırmızı Çerçeveli Butonlara Benzetildi) */
    .stButton>button:focus:not(:active) {
        border-color: #FF4B4B; 
        color: #FF4B4B;
        box-shadow: 0 0 0 0.2rem rgba(255, 75, 75, 0.25);
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
        "not_icerik": "**Ana Konu:** Temel Fonksiyonlar \n\nMatematik dersine ait detaylı notlara erişim izniniz var. (Simülasyon içeriği) \n\nBurada Temel Fonksiyonlar ile ilgili zenginleştirilmiş, gerçek içerik gösterilecektir.",
        "sorular": [
            {"q": " $(-5) + (+8)$ işleminin sonucu kaçtır?", "a": ["$-13$", "$+3$", "$-3$", "$+13$"], "c": "$+3$"},
            {"q": " $(-4) \\cdot (-2)$ işleminin sonucu kaçtır?", "a": ["$-8$", "$+8$", "$0$", "$+2$"], "c": "$+8$"},
        ]
    },
    "Türkçe": {
        "konu": "Sözcükte Anlam İlişkileri",
        "anlatim": "Sözcükler arasında eş anlamlılık (anlamdaş), zıt anlamlılık (karşıt) ve yakın anlamlılık gibi ilişkiler bulunur. \n\n**Örnek:** Ak ve Beyaz eş anlamlıdır. Uzun ve Kısa zıt anlamlıdır. ",
        "not_icerik": "**Ana Konu:** Sözcük Anlamı \n\nTürkçe dersine ait detaylı notlara erişim izniniz var. (Simülasyon içeriği) \n\nBurada Sözcük Anlamı ile ilgili zenginleştirilmiş, gerçek içerik gösterilecektir.",
        "sorular": [
            {"q": " 'Zengin' kelimesinin zıt anlamlısı nedir?", "a": ["Varlıklı", "Fakir", "Varlığa", "Cimri"], "c": "Fakir"},
            {"q": " Aşağıdaki kelime çiftlerinden hangisi eş anlamlıdır?", "a": ["Gürültü - Sessiz", "Hürriyet - Özgürlük", "İleri - Geri", "Aç - Tok"], "c": "Hürriyet - Özgürlük"},
        ]
    },
    "Fen Bilimleri": {
        "konu": "Atomun Yapısı ve Periyodik Sistem",
        "anlatim": "Madde atomlardan oluşur. Atom, çekirdek ve katmanlardan meydana gelir. Çekirdekte proton ve nötronlar, katmanlarda ise elektronlar bulunur. \n\n**Periyodik Sistem:** Elementlerin atom numaralarına göre düzenlendiği tablodur.",
        "not_icerik": "**Ana Konu:** Atom ve Periyodik Sistem \n\nFen Bilimleri dersine ait detaylı notlara erişim izniniz var. (Simülasyon içeriği) \n\nBurada Atom ve Periyodik Sistem ile ilgili zenginleştirilmiş, gerçek içerik gösterilecektir.",
        "sorular": [
            {"q": " Atomun çekirdeğinde bulunan pozitif yüklü parçacık hangisidir?", "a": ["Elektron", "Nötron", "Proton", "Molekül"], "c": "Proton"},
            {"q": " Periyodik sistemde elementler neye göre sıralanmıştır?", "a": ["Kütle numarası", "Yoğunluk", "Atom numarası", "Atom ağırlığı"], "c": "Atom numarası"},
        ]
    },
    "Din Kültürü ve Ahlak Bilgisi": { 
        "konu": "Melek ve Ahiret İnancı",
        "anlatim": "İslam dininde melekler, Allah'ın emirlerini yerine getiren nurdan yaratılmış varlıklardır. Ahiret inancı ise ölümden sonraki sonsuz yaşamın varlığına inanmaktır. \n\n**Dört Büyük Melek:** Cebrail, Mikail, İsrafil, Azrail.",
        "not_icerik": "**Ana Konu:** İnanç Esasları \n\nDin Kültürü dersine ait detaylı notlara erişim izniniz var. (Simülasyon içeriği) \n\nBurada İnanç Esasları ile ilgili zenginleştirilmiş, gerçek içerik gösterilecektir.",
        "sorular": [
            {"q": " Vahiy meleği olarak bilinen ve peygamberlere emirleri ileten melek hangisidir?", "a": ["Mikail", "İsrafil", "Azrail", "Cebrail"], "c": "Cebrail"},
            {"q": " Aşağıdakilerden hangisi ahiret hayatının aşamalarından biri değildir?", "a": ["Kıyamet", "Haşir", "Tevhid", "Mizan"], "c": "Tevhid"},
        ]
    },
    "Sosyal Bilgiler": {
        "konu": "İletişim ve İnsan İlişkileri",
        "anlatim": """İletişim, duygu, düşünce veya bilgilerin akla gelebilecek her türlü yolla bir kişiden diğerine aktarılmasıdır. Etkili iletişimde empati kurmak önemlidir. \n\n**Etkili İletişim:** 'Ben dili' kullanmak, göz teması kurmak.""", 
        "not_icerik": "**Ana Konu:** Temel Sosyal Kavramlar \n\nSosyal Bilgiler dersine ait detaylı notlara erişim izniniz var. (Simülasyon içeriği) \n\nBurada Temel Sosyal Kavramlar ile ilgili zenginleştirilmiş, gerçek içerik gösterilecektir.",
        "sorular": [
            {"q": " Aşağıdakilerden hangisi etkili iletişimi olumsuz etkiler?", "a": ["Empati kurmak", "Göz teması kurmak", "Yargılayıcı konuşmak", "Açık ve net konuşmak"], "c": "Yargılayıcı konuşmak"},
            {"q": " 'Kızgın olduğumu anlıyorum.' cümlesi hangi iletişim diline örnektir?", "a": ["Sen dili", "Ben dili", "Emir dili", "Vücut dili"], "c": "Ben dili"},
        ]
    }, # Sosyal Bilgiler tanımının kapanış parantezi buradadır.
    "İngilizce": {
        "konu": "Appearance and Personality (Görünüş ve Kişilik)",
        "anlatim": "İngilizce 7. sınıfın ilk konularından biri, insanların fiziksel görünümleri (tall, short, slim) ve kişilik özellikleri (generous, selfish, friendly) hakkında konuşmaktır. \n\n**Görünüş:** *He is tall and handsome.* \n**Kişilik:** *She is very kind and helpful.*",
        "not_icerik": "**Ana Konu:** Görünüş ve Kişilik \n\nİngilizce dersine ait detaylı notlara erişim izniniz var. (Simülasyon içeriği) \n\nBurada Görünüş ve Kişilik ile ilgili zenginleştirilmiş, gerçek içerik gösterilecektir.",
        "sorular": [
            {"q": " What does 'generous' mean?", "a": ["Cimri", "Cömert", "Yorgun", "Sinirli"], "c": "Cömert"},
            {"q": " 'O çok uzun ve zayıf.' cümlesinin İngilizcesi hangisidir?", "a": ["He is short and plump.", "She is kind and helpful.", "He is tall and slim.", "She is short and handsome."], "c": "He is tall and slim."},
        ]
    }
} 


# GENEL ARKA PLAN MÜZİĞİ İÇİN ÖRNEK MP3 LİNKİ
GENEL_FON_URL = "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3" 

# Session State Tanımlamaları
if 'admin_mode' not in st.session_state:
    st.session_state['admin_mode'] = False
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
if 'announcement' not in st.session_state:
    st.session_state['announcement'] = "🚀 Hoş geldiniz! 7. Sınıf Ders içeriklerini ve araçları keşfedin."
if 'announcement_color' not in st.session_state:
    st.session_state['announcement_color'] = 'success'
if 'secilen_modul' not in st.session_state:
    # Varsayılan modül: Ders Koçu (Görsellerdeki not yapısını temsil eder)
    st.session_state['secilen_modul'] = "Ders Koçu" 
    

# --- PORTFOLYO İÇERİK FONKSİYONU ---
def get_portfolyo_bilgisi(baslik):
    if baslik == "Hakkımda":
        return ("""Merhaba, ben Yusuf Efe Şahin. Bu kişisel portfolyo sayfamda, teknoloji, yazılım ve tasarım alanındaki çalışmalarımı sergiliyorum. Yaratıcı projeler geliştirmeye ve sürekli öğrenmeye odaklıyım.""", "👨‍💻")
    elif baslik == "Projelerim":
        return ("""Yaptığım bazı öne çıkan projeler ve kullandığım teknolojiler aşağıdadır.

* **Portfolyo Sitesi (Streamlit/Python):** Kişisel projelerimi sergilediğim ana alan.
* **Proje 2:** Python ile veri analizi ve görselleştirme çalışması.
* **Proje 3:** Web tabanlı basit bir uygulama geliştirme örneği.""", "💡")
    elif baslik == "İletişim":
        return ("""Sorularınız, iş teklifleri veya geri bildirimleriniz için benimle aşağıdaki yollarla iletişime geçebilirsiniz:
            
* **E-posta:** yusuf_efe_sahin@mail.com
* **LinkedIn:** /yusufeşahin
* **GitHub:** /yusufeşahinprojeler""", "📧")
    elif baslik == "Çeviri Aracı":
        return ("""Hızlı metin çevirisi yapabileceğiniz simülasyon aracıdır.""", "🌍")
    return ("İçerik Bulunamadı.", "❓")


# --- DERS NOTLARI / KOÇLARIMIZ / ÇALIŞMA ALANI ---
def render_ders_modulu(ders_adi, ders_veri, modul):
    st.subheader(f"✅ Seçili Sayfa: {ders_adi}")
    
    # Görsellerdeki yapıya benzetildi (Matematik Dersi Notları vb. başlık)
    st.markdown(f"## 📚 {ders_adi} Dersi Notları", unsafe_allow_html=True)
    
    # Modül Navigasyonu (Görsellerdeki Butonlar)
    col_pdf, col_koc, col_alan = st.columns(3)
    
    with col_pdf:
        if st.button("🔶 PDF Sonuç Kontrol", key="btn_pdf_kontrol", use_container_width=True):
            st.session_state['secilen_modul'] = "PDF Kontrol"
    with col_koc:
        if st.button("🔶 Ders Koçlarımız", key="btn_ders_koc", use_container_width=True):
            st.session_state['secilen_modul'] = "Ders Koçu"
    with col_alan:
        if st.button("🔶 Çalışma Alanı", key="btn_calisma_alan", use_container_width=True):
            st.session_state['secilen_modul'] = "Çalışma Alanı"
            
    st.markdown("---")

    # Modül İçeriği
    if modul == "Ders Koçu":
        st.header("💡 Ders Koçlarımız (Simülasyon)")
        st.info(f"👉 **Konu:** {ders_veri['konu']}")
        
        # Konu Adı Giriniz Alanı (İstediğiniz metin kutusu)
        st.markdown("##### Konu Adını Giriniz:")
        st.text_input("Arama Yapmak İstediğiniz Konu Adını Giriniz", label_visibility="collapsed")
        st.markdown("---")
        
        # Matematik/Sosyal Bilgiler Notları Yapısı (image_8e3b78.png)
        st.markdown(f"""
        <div style="background-color: #1E3147; padding: 10px; border-radius: 5px; margin-bottom: 10px;">
            <p style="color: white; font-weight: bold; margin: 0;">🔹 Ana Konu: {ders_veri['konu']}</p>
        </div>
        <div style="background-color: #38761D; color: white; padding: 10px; border-radius: 5px; margin-bottom: 15px;">
            {ders_adi} dersine ait detaylı notlara erişim izniniz var. (Simülasyon İçeriği)
        </div>
        <p>{ders_veri['not_icerik']}</p>
        """, unsafe_allow_html=True)
        
        # Konu Anlatımı
        st.subheader("📖 Detaylı Konu Anlatımı (Varsayılan içerik)")
        st.info(f"👉 **Konu:** {ders_veri['konu']}")
        st.markdown(ders_veri['anlatim']) 
        st.markdown("---")
        render_soru_cozumu(ders_adi, ders_veri['sorular'])

    elif modul == "PDF Kontrol":
        st.header("📄 PDF Sonuç Kontrol (Simülasyon)")
        st.warning("Bu modül sadece bir gösterimdir. Gerçek bir PDF kontrol fonksiyonu burada yer alacaktır.")
        st.file_uploader("Lütfen Cevap Anahtarını Kontrol Etmek İstediğiniz PDF'i Yükleyin:")

    elif modul == "Çalışma Alanı":
        st.header("🧠 Çalışma Alanı (Simülasyon)")
        st.warning("Bu modül sadece bir gösterimdir. Öğrencinin not alabileceği ve pratik yapabileceği bir alan olacaktır.")
        st.text_area("Çalışma Notlarınızı Buraya Yazın:", height=300)

    # Başka bir modül seçilirse veya ilk yüklendiğinde (Şu anki kodda 'Ders Koçu' varsayılan, bu kısım gereksiz ama korumak isterseniz kalabilir.)
    else: 
        st.header(f"📚 {ders_adi} Dersi (7. Sınıf)")
        st.info(f"👉 **Konu:** {ders_veri['konu']}")
        st.markdown("---")
        
        st.subheader("📖 Detaylı Konu Anlatımı")
        st.markdown(ders_veri['anlatim']) 
        st.markdown("---")
        
        render_soru_cozumu(ders_adi, ders_veri['sorular'])


# --- DERS SORU ÇÖZÜMÜ İŞLEVİ ---
def render_soru_cozumu(ders_adi, sorular):
    st.subheader(f"❓ {ders_adi} - Soru Çözüm Alanı (Quiz)")
    st.info("Aşağıdaki soruları yanıtlayarak konuyu ne kadar anladığınızı kontrol edin.")
    
    with st.form(f"quiz_form_{ders_adi}", clear_on_submit=False):
        kullanici_cevaplari = {}
        
        for i, q in enumerate(sorular):
            q_text = q['q']
            st.markdown(f"**Soru {i+1}:** {q_text}", unsafe_allow_html=True) 
            kullanici_cevaplari[f"q_{i}"] = st.radio(f"Cevabınız:", q['a'], key=f"q_radio_{ders_adi}_{i}")
            st.markdown("---")

        if st.form_submit_button("Cevapları Kontrol Et"):
            dogru_sayisi = 0
            st.subheader("Sonuçlar")
            
            for i, q in enumerate(sorular):
                secim = kullanici_cevaplari[f"q_{i}"]
                if secim == q['c']:
                    dogru_sayisi += 1
                    st.success(f"✅ Soru {i+1} Doğru! Cevap: {q['c']}")
                else:
                    st.error(f"❌ Soru {i+1} Yanlış. Sizin Cevabınız: {secim}, Doğru Cevap: {q['c']}")
            
            st.markdown(f"## 🎉 TOPLAM DOĞRU SAYINIZ: {dogru_sayisi} / {len(sorular)}")
            st.balloons()


# --- ÇEVİRİ ARACI İŞLEVİ ---
def render_cevirici():
    st.header("🌍 Çeviri Aracı (Simülasyon)")
    st.info("Girdiğiniz metin, burada seçtiğiniz dile çevrilmiş gibi gösterilecektir.")
    
    with st.form("cevirici_form", clear_on_submit=False):
        kaynak_metin = st.text_area("Çevrilecek Metni Giriniz:", height=150)
        
        col_dil1, col_dil2 = st.columns(2)
        with col_dil1:
            kaynak_dil = st.selectbox("Kaynak Dil:", options=["Türkçe", "İngilizce"])
        with col_dil2:
            hedef_dil = st.selectbox("Hedef Dil:", options=["İngilizce", "Türkçe", "Almanca", "İspanyolca"])
        
        if st.form_submit_button("Çevir"):
            if kaynak_metin:
                cevrilmis_metin = f"[{hedef_dil} Çevirisi]: {kaynak_metin.upper()} (Simülasyon Çevirisi Başarılı!)"
                st.success(f"Çeviri Tamamlandı ({kaynak_dil} -> {hedef_dil}):")
                st.code(cevrilmis_metin)
            else:
                st.warning("Lütfen çevrilecek metni giriniz.")

# --- BAŞLIK AYARLARI ---
st.title(f"💼 Yusuf Efe Şahin Portfolyo")

# --- ANA İÇERİK ALANI (Ziyaretçi Modu) ---

if not st.session_state['admin_mode']:
    # --- GENEL FON MÜZİĞİ KONTROLLERİ ---
    col_kapat, col_ac, col_volume_slider = st.columns([1, 1, 6]) 

    if st.session_state['music_enabled']:
        # Müzik çalma kodu
        st.audio(st.session_state['music_url'], format="audio/mp3", loop=True)
        
        with col_kapat:
            if st.button("🔊 Müzik Kapat", key="btn_kapat_ses", use_container_width=True):
                st.session_state['music_enabled'] = False
                st.rerun()
        with col_volume_slider:
            new_volume = st.slider("Müzik Ses Seviyesi", 0.0, 1.0, st.session_state['music_volume'], step=0.1, key="music_volume_slider")
            # Volume değişirse state'i güncelle ve rerun yap
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
    elif st.session_state['announcement_color'] == 'info':
        st.info(f"📣 {st.session_state['announcement']}")
    elif st.session_state['announcement_color'] == 'warning':
        st.warning(f"📣 {st.session_state['announcement']}")
    elif st.session_state['announcement_color'] == 'error':
        st.error(f"📣 {st.session_state['announcement']}")
    
    # --- NAVİGASYON (Portfolyo, Dersler ve Araçlar) ---
    st.header("🌐 Site Bölümleri ve 7. Sınıf Dersleri")

    PORTFOLYO_SAYFALAR = ["Hakkımda", "Projelerim", "İletişim"]
    ARACLAR_SAYFALAR = ["Çeviri Aracı"] 
    DERS_SAYFALAR = list(DEFAULT_DERSLER.keys())
    
    SAYFALAR = PORTFOLYO_SAYFALAR + DERS_SAYFALAR + ARACLAR_SAYFALAR
    
    # Ana Butonlar için dinamik sütun oluşturma
    cols = st.columns(len(SAYFALAR))
    for i, sayfa in enumerate(SAYFALAR):
        with cols[i]:
            if st.button(f"🔹 {sayfa}", key=f"btn_{sayfa}", use_container_width=True):
                st.session_state['secilen_sayfa'] = sayfa
                # Ders sayfasına geçildiğinde modül varsayılana ('Ders Koçu') ayarlansın
                if sayfa in DERS_SAYFALAR:
                    st.session_state['secilen_modul'] = "Ders Koçu" 
                else:
                    # Diğer sayfalarda modül seçimine gerek yok
                    st.session_state['secilen_modul'] = "Konu Anlatımı"
                st.rerun()
                
    st.markdown("---")
    secilen_sayfa = st.session_state['secilen_sayfa']

    
    # --- İÇERİK YAZDIRMA VE ÖZELLİK ÇAĞIRMA ---
    
    # 1. DERS SAYFASI İÇERİĞİ (Artık Modül Yapısı Kullanıyor)
    if secilen_sayfa in DERS_SAYFALAR:
        ders_veri = DEFAULT_DERSLER[secilen_sayfa]
        render_ders_modulu(secilen_sayfa, ders_veri, st.session_state['secilen_modul'])
        
    # 2. ÇEVİRİ ARACI
    elif secilen_sayfa == "Çeviri Aracı":
        render_cevirici()
        
    # 3. PORTFOLYO SAYFALARI (Hakkımda, Projelerim, İletişim)
    else:
        icerik, simge = get_portfolyo_bilgisi(secilen_sayfa)
        st.subheader(f"✅ Seçili Sayfa: {secilen_sayfa}")
        st.markdown(f"## {simge} {secilen_sayfa}")
        st.markdown(f"**{icerik}**")
        
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
    
    
    # DUYURU AYARLARI
    st.sidebar.markdown("---")
    st.sidebar.subheader("📢 Site Duyurusu")
    st.session_state['announcement'] = st.sidebar.text_area("Duyuru Metni:", value=st.session_state['announcement'])
    st.session_state['announcement_color'] = st.sidebar.selectbox("Duyuru Kutusu Rengi:", ["success", "info", "warning", "error"], index=["success", "info", "warning", "error"].index(st.session_state['announcement_color']))
    if st.sidebar.button("Duyuruyu Güncelle", key="btn_guncelle_duyuru"):
        st.rerun()

else:
    # YÖNETİCİ GİRİŞ BUTONU
    st.sidebar.button("🔒 Yönetici Girişi", on_click=lambda: st.session_state.update({'show_admin_login': True}))

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
    
st.sidebar.markdown("---")
st.sidebar.title("⭐ Yorumlar ve Geri Bildirim")

# Yorum Formu korundu
with st.sidebar.form("geri_bildirim_formu", clear_on_submit=True):
    st.sidebar.write("Site hakkındaki yorumlarınızı buraya yazın.")
    st.selectbox("Konu:", ["Genel Yorum", "Hata Bildirimi", "Tasarım Önerisi", "Teşekkür"])
    st.text_area("Mesajınız:")
    if st.form_submit_button("Yorumu Gönder"):
        st.sidebar.success(f"Yorumunuz başarıyla iletildi!")

st.sidebar.markdown("---")
st.sidebar.caption("Geliştirici: Yusuf Efe Şahin | Portfolyo v2.0")
