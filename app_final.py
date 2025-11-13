import streamlit as st
import os
from google import genai
from google.genai import types

# --- 1. KÜTÜPHANE VE API KURULUMU ---

# API Anahtarını Streamlit secrets dosyasından yükle
API_KEY = None
client = None
try:
    if "GEMINI_API_KEY" in st.secrets:
        API_KEY = st.secrets["GEMINI_API_KEY"]
        client = genai.Client(api_key=API_KEY)
    else:
        st.error("API anahtarı 'secrets.toml' dosyasında tanımlanmadı. Akıl Öğretmen çalışmayacaktır.")
except Exception as e:
    st.error(f"API kurulum hatası: {e}")

# --- 2. İÇERİK TANIMLARI ---
# Bu içerikler artık konu anlatımına girmeyecek, sadece Konu Anlatımı sekmesinde listelenecek.
try:
    MATH_CONTENT = "## 📘 Matematik Konu Anlatımı Detayı"
    TURKISH_CONTENT = "## 📝 Türkçe Konu Anlatımı Detayı" 
    SCIENCE_CONTENT = "## 🧪 Fen Konu Anlatımı Detayı"
    SOCIAL_CONTENT = "## 🌍 Sosyal Bilgiler Konu Anlatımı Detayı"

    MATH_VIDEOS = {} 
    TURKISH_VIDEOS = {}
    SCIENCE_VIDEOS = {}
    SOCIAL_VIDEOS = {}

except Exception:
    pass 

# --- 3. SESSION STATE (DURUM YÖNETİMİ) ---
if 'content_key' not in st.session_state: st.session_state.content_key = None 
if 'ai_response' not in st.session_state:
    st.session_state.ai_response = "Konuyu yazın ve Akıl'dan Konu Anlatmasını isteyin. (Örn: Rasyonel, Kütle) VEYA Genel Bir Şey Sorun."
    st.session_state.last_topic = ""

# --- HARİTALAR VE SABİTLER ---
CONTENT_MAP = {
    "mat_konu": MATH_CONTENT, 
    "tr_konu": TURKISH_CONTENT, 
    "sci_konu": SCIENCE_CONTENT, 
    "soc_konu": SOCIAL_CONTENT, 
}
COACH_CONTENT = "## 💡 Koç Modülü - Öğrenci Koçluğu ve Rehberlik"


# --- 5. BUTON VE AI MANTIĞI ---
def toggle_content(key):
    if st.session_state.content_key == key: st.session_state.content_key = None
    else: st.session_state.content_key = key

# AKIL ASİSTANININ GEMINI ILE KONUYU OTOMATİK ANLATMASI İÇİN GÜNCELLENMİŞ FONKSİYON
def generate_ai_explanation(topic):
    topic_clean = topic.strip().upper()
    
    if not client or not API_KEY:
        st.session_state.ai_response = f"## ⚠️ API Hatası: Lütfen API anahtarınızı '.streamlit/secrets.toml' dosyasına girin."
        st.session_state.last_topic = topic
        return

    st.session_state.last_topic = topic
    
    if not topic_clean:
        st.session_state.ai_response = f"## ⚠️ Akıl Asistanı Uyarısı: Lütfen bir konu adı veya soru yazınız."
        return

    # Kullanıcıya yükleme (loading) mesajı göster
    with st.spinner(f"👨‍🏫 Akıl Öğretmen: **{topic_clean}** konusunu hazırlıyor..."):
        try:
            # Öğretmen talimatı (Prompt)
            prompt = f"""
            Sen 7. sınıf öğrencilerine ders anlatan tecrübeli ve motive edici bir öğretmensin. 
            'Öğretmen Tonu'nu kullanarak ve konuyu basit, anlaşılır adımlarla açıklayarak,
            '{topic}' konusunu en az 300 kelime olacak şekilde detaylıca anlat. 
            Cevabını doğrudan konu anlatımıyla başlat, giriş veya selamlama yapma.
            Önemli yerleri kalın (bold) yaparak ve kısa başlıklar (Markdown ##, ###) kullanarak formatla.
            """
            
            ai_response = client.models.generate_content(
                model='gemini-2.5-flash',
                contents=prompt
            ).text

            # Final cevap formatı
            st.session_state.ai_response = f"""
## 👨‍🏫 Akıl Öğretmen: {topic_clean} Konu Anlatımı ✨

{ai_response}
"""
        except Exception as e:
            st.session_state.ai_response = f"""
## 🚨 Hata: Akıl Öğretmen Cevap Veremedi
Yapay zeka servisine bağlanırken bir sorun oluştu. API kota/anahtar hatası olabilir.
"""


# --- 6. SAYFA AYARLARI ---
st.set_page_config(layout="wide", page_title="Yusuf Efe Şahin | 7. Sınıf Eğitim Portalı")
st.title("👨‍🎓 Yusuf Efe Şahin | 7. Sınıf Eğitim Portalı")
st.markdown("---")

# --- 7. SEKMELERİN TANIMLANMASI ---
tab_coach, tab_math, tab_tr, tab_sci, tab_soc = st.tabs([
    "💡 Koç Modülü", 
    "🔢 Matematik İçerikleri", 
    "📝 Türkçe İçerikleri", 
    "🧪 Fen Bilimleri",
    "🌍 Sosyal Bilgiler"
])

# --- 8. DERS SEKMELERİ İÇİN GENEL FONKSİYON (KONU LİSTELERİ EKLİ) ---
def render_subject_tab(tab_context, subject_title, key_prefix):
    konu_key = f"{key_prefix}_konu"
    pdf_key = f"{key_prefix}_pdf"; deneme_key = f"{key_prefix}_deneme"
    
    # Kalan 4 ders için detaylı konu listeleri
    if key_prefix == "tr":
        konu_listesi = [
            "Sözcükte Anlam", "Cümlede Anlam", "Parçada Anlam", "Tablo, Grafik, Görsel Yorumlama",
            "Metin Türleri", "Söz Sanatları", "Fiiller", "Ek Fiil", "Zarflar", 
            "Anlatım Bozuklukları", "Yazım Kuralları", "Noktalama İşaretleri"
        ]
    elif key_prefix == "mat":
        konu_listesi = [
            "Tam Sayılarla İşlemler (1. Ünite)", "Rasyonel Sayılar ve İşlemleri (2. Ünite)", 
            "Cebirsel İfadelerden Eşitlik ve Denklemlere (3. Ünite)", 
            "Oran Orantıdan Yüzdelere (4. Ünite)", "Doğrular ve Açılar, Çokgenler, Çember ve Daire (5. Ünite)",
            "Veri Analizinden Cisimlerin Farklı Yönlerden Görünümlerine (6. Ünite)"
        ]
    elif key_prefix == "sci":
        konu_listesi = [
            "Güneş Sistemi ve Ötesi (1. Ünite)", "Hücre ve Bölünmeler (2. Ünite)", 
            "Kuvvet ve Enerji (3. Ünite)", "Saf Madde ve Karışımlar (4. Ünite)", 
            "Işığın Madde ile Etkileşimi (5. Ünite)", "Canlılarda Üreme, Büyüme ve Gelişme (6. Ünite)", 
            "Elektrik Devreleri (7. Ünite)"
        ]
    elif key_prefix == "soc":
        konu_listesi = [
            "Birey ve Toplum (1. Ünite)", "Kültür ve Miras (2. Ünite)", 
            "İnsanlar, Yerler ve Çevreler (3. Ünite)", "Bilim, Teknoloji ve Toplum (4. Ünite)", 
            "Üretim, Dağıtım ve Tüketim (5. Ünite)", "Etkin Vatandaşlık (6. Ünite)", 
            "Küresel Bağlantılar (7. Ünite)"
        ]
    else:
        konu_listesi = ["Bu derse ait Konu Listesi Henüz Eklenmedi."]

    
    with tab_context:
        st.header(f"{subject_title} Dersi İçerikleri")
        
        # SADECE 3 BUTON KALDI
        col_btn1, col_btn2, col_btn3 = st.columns(3) 
        
        with col_btn1:
            button_label = "⬆️ Konuyu Gizle" if st.session_state.content_key == konu_key else "📄 Konu Anlatımı"
            st.button(button_label, type="primary", key=konu_key, on_click=toggle_content, args=(konu_key,)) 
                      
        with col_btn2: st.button("♦️ PDF Sonuç Kontrol", type="secondary", key=pdf_key)
        with col_btn3: st.button("🔥 Deneme Sınavı", type="secondary", key=deneme_key)
        
        st.markdown("---")
        
        if st.session_state.content_key == konu_key:
            st.subheader(f"✨ {subject_title} Dersi Konu Listesi") 
            
            # KONU LİSTESİNİ GÖSTER
            for konu in konu_listesi:
                st.markdown(f"* **{konu}**")
            
            st.markdown("---")

            # KONU ANLATIMI DETAY METNİNİ GÖSTER
            st.subheader("📘 Konu Anlatımı Detay")
            # BU BÖLÜM ARTIK SADECE MANUAL İÇERİK İÇİN KALDI
            st.markdown(CONTENT_MAP.get(konu_key, "İçerik Bulunamadı. Lütfen ilgili içerik dosyanızı kontrol edin."), unsafe_allow_html=True)
            st.markdown("---")
            
        else:
            st.info(f"Yukarıdaki butona tıklayarak {subject_title} dersi içeriğini görebilirsiniz.")

# ==============================================================================
# --- 9. KOÇ MODÜLÜ ---
# ==============================================================================
with tab_coach: 
    st.header("💡 Koç Modülü - Rehberlik ve Mentorluk")
    
    st.info("YouTube video arama motoru, uygulama kararlılığı için kaldırılmıştır.")
    st.markdown("---")

    st.subheader("🤖 Yapay Zeka Asistanı (Akıl)")
    
    input_topic = st.text_input(
        "Konu Adını Yazınız (Örn: Rasyonel Sayılar, Söz Sanatları, Mitoz)", 
        value=st.session_state.last_topic, key="topic_input"
    )
    
    st.button(
        "Akıl'dan Konuyu Anlatmasını İsteyin", 
        type="secondary", key="ai_generate",
        on_click=generate_ai_explanation, args=(input_topic,)
    )
    
    st.markdown("---")
    st.markdown(st.session_state.ai_response, unsafe_allow_html=True)
    st.markdown("---") 

    st.header("📝 Çalışma ve Rehberlik İçerikleri") 
    col_coach_btn1, col_coach_btn2, col_coach_btn3 = st.columns(3)
    
    with col_coach_btn1: st.button("📝 Çalışma Planı Oluştur", type="secondary", key="coach_plan") 
    with col_coach_btn2: st.button("🧠 Motivasyon Teknikleri", type="secondary", key="coach_motivasyon")
    with col_coach_btn3: st.button("⏰ Pomodoro Zamanlayıcısı", type="secondary", key="coach_pomodoro")
    
    st.markdown("---")
    st.markdown(COACH_CONTENT, unsafe_allow_html=True)


# ==============================================================================
# --- 10. DERS SEKMELERİNİN ÇAĞRILMASI ---
# ==============================================================================
render_subject_tab(tab_math, "🔢 Matematik", "mat")
render_subject_tab(tab_tr, "📝 Türkçe", "tr")
render_subject_tab(tab_sci, "🧪 Fen Bilimleri", "sci")
render_subject_tab(tab_soc, "🌍 Sosyal Bilgiler", "soc")
