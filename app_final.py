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

# YENİ DERS VERİLERİ (Örnek içerikler)
DEFAULT_DERSLER = {
    "Matematik": {
        "konu": "Rasyonel Sayılar",
        "anlatim": "Rasyonel sayılar, $a$ bir tam sayı ve $b$ sıfırdan farklı bir tam sayı olmak üzere, $\\frac{a}{b}$ şeklinde yazılabilen sayılardır. Kesirler, ondalık sayılar ve tam sayılar bu kümeye dahildir. Örneğin, $\\frac{3}{4}$, $-2.5$ ve $5$ birer rasyonel sayıdır.",
        "sorular": [
            {"q": "Aşağıdakilerden hangisi rasyonel sayıdır?", "a": ["$\\sqrt{2}$", "$\\pi$", "$\\frac{1}{3}$", "Hiçbiri"], "c": "$\\frac{1}{3}$"},
            {"q": "$-1$ sayısının rasyonel karşılığı nedir?", "a": ["$\\frac{0}{1}$", "$\\frac{1}{0}$", "$\\frac{-1}{1}$", "$\\frac{-1}{0}$"], "c": "$\\frac{-1}{1}$"},
        ]
    },
    "Türkçe": {
        "konu": "Fiilde Anlam Kayması",
        "anlatim": "Fiilde anlam kayması (zaman/kip kayması), bir eylemin bir kip veya zaman ekiyle çekimlenmesine rağmen, başka bir kip veya zamanın anlamını taşımasıdır. Örneğin, 'Yarın Ankara'ya gidiyor' cümlesinde 'gidiyor' şimdiki zaman eki almasına rağmen, gelecek zaman anlamı taşır.",
        "sorular": [
            {"q": "Hangi cümlede anlam kayması vardır?", "a": ["Dün ders çalıştım.", "Her sabah koşarım.", "Otobüs şimdi kalkacak.", "Nasrettin Hoca bir gün göle maya çalar."], "c": "Nasrettin Hoca bir gün göle maya çalar."},
            {"q": "Hangi zaman kipi, gelecek zaman anlamı taşır?", "a": ["Geniş Zaman", "Şimdiki Zaman", "Görülen Geçmiş Zaman", "Gereklilik Kipi"], "c": "Şimdiki Zaman"},
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
    st.session_state['announcement'] = "🚀 Hoş geldiniz! Portfolyomdaki projeleri keşfedin."
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


# --- DERS SORU ÇÖZÜMÜ İŞLEVİ ---
def render_soru_cozumu(ders_adi, sorular):
    st.subheader(f"❓ {ders_adi} - Soru Çözüm Alanı")
    st.info("Aşağıdaki soruları yanıtlayarak konuyu ne kadar anladığınızı kontrol edin.")
    
    # Her ders için ayrı bir form kullanmak için ders_adi'nı form key'ine ekleyelim
    with st.form(f"quiz_form_{ders_adi}", clear_on_submit=False):
        kullanici_cevaplari = {}
        
        for i, q in enumerate(sorular):
            q_text = q['q']
            # Cevap seçeneklerinde LaTeX kullanıldığı için unsafe_allow_html=True eklenmeli
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
            
            if dogru_sayisi == len(sorular):
                st.info("Tebrikler, konuyu başarıyla tamamladınız!")
            elif dogru_sayisi > 0:
                 st.warning("Çalışmaya devam! Yanlışlarınızı kontrol edin.")
