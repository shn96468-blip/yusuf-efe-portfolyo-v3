import streamlit as st
import os

# --- 1. KÜTÜPHANE VE API KURULUMU ---
# API bağımlılığı tamamen kaldırıldı. Uygulama stabil çalışacaktır.

# --- 2. İÇERİK TANIMLARI ---
# İçerikler manuel olarak girilmelidir. (Türkçe içeriği örnek olarak dolduruldu)

TURKISH_CONTENT = """
## 📝 Fiiller (Eylemler) Konu Anlatımı ✨

Sevgili öğrencim, Fiiller (Eylemler), bir cümlede iş, oluş, hareket veya durum bildiren sözcüklerdir. Bir eylemin gerçekleştiği zamanı ve eylemi kimin yaptığını (kişi) gösteren ekler alırlar.

### 1. Fiillerin Anlam Özellikleri
* **Kılış (İş) Fiilleri:** Nesne alabilen fiillerdir. Örnek: "Yazmak", "Okumak".
* **Durum Fiilleri:** Nesne almayan, öznenin durumunu bildiren fiillerdir. Örnek: "Uyumak", "Gülmek".
* **Oluş Fiilleri:** Zamanla kendiliğinden gerçekleşen değişikliklerdir. Örnek: "Sararmak", "Büyümek".
"""

MATH_CONTENT = "## 📘 Matematik Konu Anlatımı Detayı"
SCIENCE_CONTENT = "## 🧪 Fen Bilimleri Konu Anlatımı Detayı"
SOCIAL_CONTENT = "## 🌍 Sosyal Bilgiler Konu Anlatımı Detayı"


MATH_VIDEOS = {} 
TURKISH_VIDEOS = {}
SCIENCE_VIDEOS = {}
SOCIAL_VIDEOS = {}


# --- 3. SESSION STATE (DURUM YÖNETİMİ) ---
if 'content_key' not in st.session_state: st.session_state.content_key = None 
if 'ai_response' not in st.session_state:
    # Akıl Öğretmen bölümü için yer tutucu mesajı
    st.session_state.ai_response = "Konuyu yazın ve Akıl'dan Konu Anlatmasını isteyin. (Örn: Rasyonel, Kütle) VEYA Genel Bir Şey Sorun."
    st.session_state.last_topic = ""

# --- HARİTALAR VE SABİTLER ---
CONTENT_MAP = {
    "mat_konu": MATH_CONTENT, 
    "tr_konu": TURKISH_CONTENT, 
    "sci_konu": SCIENCE_CONTENT, 
    "soc_konu": SOCIAL_CONTENT, 
}

# --- 5. BUTON VE AI MANTIĞI ---
def toggle_content(key):
    if st.session_state.content_key == key: st.session_state.content_key = None
    else: st.session_state.content_key = key

# AKIL ASİSTANININ SADECE YER TUTUCU GÖSTEREN FONKSİYONU
def generate_ai_explanation(topic):
    topic_clean = topic.strip().upper()
    
    if not topic_clean:
        st.session_state.ai_response = f"## ⚠️ Akıl Asistanı Uyarısı: Lütfen bir konu adı veya soru yazınız."
        return

    st.session_state.last_topic = topic
    
    # API yok, bu yüzden manuel giriş için yer tutucu gösterilir.
    st.session_state.ai_response = f"""
## 👨‍🏫 Akıl Öğretmen: {topic_clean} Konu Anlatımı ✨

**Konu Anlatımı Detayı:** Lütfen **{topic_clean}** konusunun detaylı içeriğini bu alana giriniz. (Markdown formatını kullanabilirsiniz.)

"""


# --- 6. SAYFA AYARLARI ---
st.set_page_config(layout="wide", page_title="Yusuf Efe Şahin | 7. Sınıf Eğitim Portalı")
st.title("👨‍🎓 Yusuf Efe Şahin | 7. Sınıf Eğitim Portalı")
st.markdown("---")

# --- 7. SEKMELERİN TANIMLANMASI ---
tab_ai, tab_math, tab_tr, tab_sci, tab_soc = st.tabs([
    "🤖 Konu Anlatımı Asistanı", 
    "🔢 Matematik İçerikleri", 
    "📝 Türkçe İçerikleri", 
    "🧪 Fen Bilimleri",
    "🌍 Sosyal Bilgiler"
])

# --- 8. DERS SEKMELERİ İÇİN GENEL FONKSİYON ---
def render_subject_tab(tab_context, subject_title, key_prefix):
    konu_key = f"{key_prefix}_konu"
    pdf_key = f"{key_prefix}_pdf"; deneme_key = f"{key_prefix}_deneme"
    
    # Konu Listeleri
    if key_prefix == "tr":
        konu_listesi = ["Sözcükte Anlam", "Cümlede Anlam", "Parçada Anlam", "Fiiller", "Ek Fiil", "Zarflar", "Yazım Kuralları"]
    elif key_prefix == "mat":
        konu_listesi = ["Tam Sayılarla İşlemler", "Rasyonel Sayılar", "Cebirsel İfadeler", "Oran Orantı", "Doğrular ve Açılar"]
    elif key_prefix == "sci":
        konu_listesi = ["Güneş Sistemi", "Hücre ve Bölünmeler", "Kuvvet ve Enerji", "Saf Madde ve Karışımlar"]
    elif key_prefix == "soc":
        konu_listesi = ["Birey ve Toplum", "Kültür ve Miras", "İnsanlar, Yerler ve Çevreler", "Bilim ve Teknoloji"]
    else:
        konu_listesi = [f"Bu derse ait Konu Listesi Henüz Eklenmedi."]

    
    with tab_context:
        st.header(f"{subject_title} Dersi İçerikleri")
        
        col_btn1, col_btn2, col_btn3 = st.columns(3) 
        
        with col_btn1:
            button_label = "⬆️ Konuyu Gizle" if st.session_state.content_key == konu_key else "📄 Konu Anlatımı"
            st.button(button_label, type="primary", key=konu_key, on_click=toggle_content, args=(konu_key,)) 
                      
        with col_btn2: st.button("♦️ PDF Sonuç Kontrol", type="secondary", key=pdf_key)
        with col_btn3: st.button("🔥 Deneme Sınavı", type="secondary", key=deneme_key)
        
        st.markdown("---")
        
        if st.session_state.content_key == konu_key:
            st.subheader(f"✨ {subject_title} Dersi Konu Listesi") 
            for konu in konu_listesi: st.markdown(f"* **{konu}**")
            st.markdown("---")

            # Manuel olarak girilen detaylı konu içeriği burada görünür
            st.subheader("📘 Konu Anlatımı Detay (Manuel İçerik)")
            st.markdown(CONTENT_MAP.get(konu_key, "İçerik Bulunamadı. Lütfen ilgili içerik dosyanızı kontrol edin."), unsafe_allow_html=True)
            st.markdown("---")
            
        else:
            st.info(f"Yukarıdaki butona tıklayarak {subject_title} dersi içeriğini görebilirsiniz.")

# ==============================================================================
# --- 9. KONU ANLATIMI ASİSTANI (MANUEL YER TUTUCU) ---
# ==============================================================================
with tab_ai: 
    st.header("🤖 Akıl Öğretmen Asistanı - Konu Anlatımı")
    
    st.info("Bu asistan, API kullanmaz. Manuel içerik girişi yapmanız için bir arayüz sağlar.")
    st.markdown("---")

    st.subheader("❓ Akıl Öğretmen'e Sor")
    
    input_topic = st.text_input(
        "Konu Adını veya Sorunuzu Yazınız (Örn: Rasyonel Sayılar, Söz Sanatları, Mitoz)", 
        value=st.session_state.last_topic, key="topic_input"
    )
    
    st.button(
        "Akıl'dan Konuyu Anlatmasını İsteyin", 
        type="secondary", key="ai_generate",
        on_click=generate_ai_explanation, args=(input_topic,)
    )
    
    st.markdown("---")
    # Akıl Öğretmen cevabı (sadece yer tutucu mesajı)
    st.markdown(st.session_state.ai_response, unsafe_allow_html=True) 
    st.markdown("---") 


# ==============================================================================
# --- 10. DERS SEKMELERİNİN ÇAĞRILMASI ---
# ==============================================================================
render_subject_tab(tab_math, "🔢 Matematik", "mat")
render_subject_tab(tab_tr, "📝 Türkçe", "tr")
render_subject_tab(tab_sci, "🧪 Fen Bilimleri", "sci")
render_subject_tab(tab_soc, "🌍 Sosyal Bilgiler", "soc")
