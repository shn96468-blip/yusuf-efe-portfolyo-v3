import streamlit as st
import os

# --- 1. KÜTÜPHANE VE API KURULUMU ---

# --- 2. İÇERİK TANIMLARI ---
# Sadece kalan 4 dersin içerikleri tanımlanmıştır.
try:
    # Dikkat: Bu metinler content dosyalarınızın içinde tanımlı olmalıdır.
    MATH_CONTENT = "## 📘 Matematik Konu Anlatımı Detayı"
    TURKISH_CONTENT = "## 📝 Türkçe Konu Anlatımı Detayı" 
    SCIENCE_CONTENT = "## 🧪 Fen Konu Anlatımı Detayı"
    SOCIAL_CONTENT = "## 🌍 Sosyal Bilgiler Konu Anlatımı Detayı"

    MATH_VIDEOS = {} # Video haritaları tutulsa da kullanılmayacaktır.
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

# Sadece kalan 4 dersin konuları için tanıma mantığı korunmuştur.
def generate_ai_explanation(topic):
    topic_lower = topic.lower().strip()
    response = ""
    
    # 1. TÜRKÇE (DİL BİLGİSİ VE ANLAM)
    if any(k in topic_lower for k in ["fiil", "ek fiil", "zarf", "anlatım bozukluğu", 
                                     "yazım", "noktalama", "sözcükte anlam", "cümlede anlam", 
                                     "parçada anlam", "metin türü", "söz sanatı", "tablo", "grafik", "görsel"]):
        response = f"## 💻 Akıl Konu Anlatımı: {topic.upper()} (TÜRKÇE) 🎉"
        
    # 2. MATEMATİK
    elif any(k in topic_lower for k in ["tam sayı", "rasyonel", "cebirsel", "denklem", 
                                        "oran", "orantı", "yüzde", "doğrular", "açılar", 
                                        "çokgen", "çember", "daire", "veri analiz", "cisim"]):
        response = f"## 🧠 Akıl Konu Anlatımı: {topic.upper()} (MATEMATİK) 🎉"

    # 3. FEN BİLİMLERİ
    elif any(k in topic_lower for k in ["güneş sistemi", "uzay", "hücre", "mitoz", "mayoz", 
                                        "kütle", "ağırlık", "kuvvet", "enerji", "saf madde", 
                                        "karışım", "ışık", "ayna", "mercek", "üreme", 
                                        "elektrik devresi", "ampul", "gök cisimleri", "gelişme", "büyüme"]):
        response = f"## 🧪 Akıl Konu Anlatımı: {topic.upper()} (FEN BİLİMLERİ) 🎉"

    # 4. SOSYAL BİLGİLER
    elif any(k in topic_lower for k in ["birey ve toplum", "kültür ve miras", "insanlar yerler çevreler", 
                                        "bilim teknoloji toplum", "üretim dağıtım tüketim", 
                                        "etkin vatandaşlık", "küresel bağlantı", "üretim", "dağıtım", "tüketim"]):
        response = f"## 🌍 Akıl Konu Anlatımı: {topic.upper()} (SOSYAL BİLGİLER) 🎉"
        
    else:
        response = f"""## ⚠️ Akıl Asistanı Uyarısı: '{topic.upper()}' şu an için anlatabileceğim ana ders konuları arasında değildir."""
        
    st.session_state.ai_response = response
    st.session_state.last_topic = topic

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

# --- 8. DERS SEKMELERİ İÇİN GENEL FONKSİYON ---
# Sadece Konu Anlatımı, PDF ve Deneme Sınavı butonları kalmıştır.
def render_subject_tab(tab_context, subject_title, key_prefix):
    konu_key = f"{key_prefix}_konu"
    pdf_key = f"{key_prefix}_pdf"; deneme_key = f"{key_prefix}_deneme"
    
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
            st.subheader(f"✨ {subject_title} Konu Anlatımı Detay") 
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
