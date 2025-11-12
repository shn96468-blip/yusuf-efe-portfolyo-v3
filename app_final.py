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
        "anlatim": "Madde atomlardan oluşur. Atom, çekirdek ve katmanlardan meydana gelir. Çekirdekte proton ve nötronlar, katmanlarda ise elektronlar bulunur. \n\n**Periyodik Sistem:** Elementlerin atom numaralarına göre düzenlendiği tablodur.",
        "sorular": [
            {"q": " Atomun çekirdeğinde bulunan pozitif yüklü parçacık hangisidir?", "a": ["Elektron", "Nötron", "Proton", "Molekül"], "c": "Proton"},
            {"q": " Periyodik sistemde elementler neye göre sıralanmıştır?", "a": ["Kütle numarası", "Yoğunluk", "Atom numarası", "Atom ağırlığı"], "c": "Atom numarası"},
        ]
    },
     "Sosyal Bilgiler": {
        "konu": "İletişim ve İnsan İlişkileri",
        "anlatim": "İletişim, duygu, düşünce veya bilgilerin akla gelebilecek her türlü yolla bir kişiden diğerine aktarılmasıdır. Etkili iletişimde empati kurmak önemlidir. \n\n**Etkili İletişim:** 'Ben dili' kullanmak, göz teması kurmak.",
        "sorular": [
            {"q": " Aşağıdakilerden hangisi etkili iletişimi olumsuz etkiler?", "a": ["Empati kurmak", "Göz teması kurmak", "Yargılayıcı konuşmak", "Açık ve net konuşmak"], "c": "Yargılayıcı konuşmak"},
            {"q": " 'Kızgın olduğumu anlıyorum.' cümlesi hangi iletişim diline örnektir?", "a": ["Sen dili", "Ben dili", "Emir dili", "Vücut dili"], "c": "Ben dili"},
        ]
    },
     "İngilizce": {
        "konu": "Appearance and Personality (Görünüş ve Kişilik)",
        "anlatim": "İngilizce 7. sınıfın ilk konularından biri, insanların fiziksel görünümleri (tall, short, slim) ve kişilik özellikleri (generous, selfish, friendly) hakkında konuşmaktır. \n\n**Görünüş:** *He is tall and handsome.* \n**Kişilik:** *She is very kind and helpful.*",
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


# --- DERS SORU ÇÖZÜMÜ İŞLEVİ (GERİ GELDİ) ---
def render_soru_cozumu(ders_adi, sorular):
    st.subheader(f"❓ {ders_adi} - Soru Çözüm Alanı (Quiz)")
    st.info("Aşağıdaki soruları yanıtlayarak konuyu ne kadar anladığınızı kontrol edin.")
    
    # Her ders için ayrı bir form kullanmak için ders_adi'nı form key'ine ekleyelim
    with st.form(f"quiz_form_{ders_adi}", clear_on_submit=False):
        kullanici_cevaplari = {}
        
        for i, q in enumerate(sorular):
            q_text = q['q']
            # LaTeX içeren metinleri doğru göstermek için markdown kullanıldı
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


# --- ÇEVİRİ ARACI İŞLEVİ (GERİ GELDİ) ---
def render_cevirici():
    st.header("🌍 Çeviri Aracı (Simülasyon)")
    st.info("Girdiğiniz metin, burada seçtiğiniz dile çevrilmiş gibi gösterilecektir.")
    
    with st.form("cevirici_form", clear_on_submit=False):
        kaynak_metin = st.text_area("Çevrilecek Metni Giriniz:", height=150)
        
        col_dil1, col_dil2 = st.columns(2)
        with col_
