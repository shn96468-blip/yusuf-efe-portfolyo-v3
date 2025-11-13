import streamlit as st

# --- 1. STREAMLIT DURUM YÖNETİMİ (Session State) ---
# Manuel içerik gösterimini kontrol eder (Ders Sekmeleri için).
if 'content_key' not in st.session_state:
    st.session_state.content_key = None 

# AI asistanı için durum yönetimi.
if 'ai_response' not in st.session_state:
    st.session_state.ai_response = "Konuyu yazın ve Gemini'ye tıklayarak konu anlatımını başlatın. (Örn: Tam Sayılar)"
    st.session_state.last_topic = ""

# --- BUTON TIKLAMA İŞLEVLERİ ---

# Manuel Konu Anlatımı Butonları için
def toggle_content(key):
    if st.session_state.content_key == key:
        st.session_state.content_key = None
    else:
        st.session_state.content_key = key

# Yapay Zeka (Gemini) Butonu için
def generate_ai_explanation(topic):
    topic_lower = topic.lower().strip()
    
    if "rasyonel sayılar" in topic_lower:
        response = """
        ## 🧠 Akıl Konu Anlatımı: Rasyonel Sayılar
        
        **Tanım:** Rasyonel sayılar, $a$ bir tam sayı ve $b$ sıfırdan farklı bir tam sayı olmak üzere, $\\frac{a}{b}$ şeklinde yazılabilen sayılardır.
        
        **İşlemler:**
        * **Toplama/Çıkarma:** Paydalar eşitlenmelidir.
        * **Çarpma:** Paylar çarpılıp paya, paydalar çarpılıp paydaya yazılır.
        """
    elif "tam sayılar" in topic_lower:
        response = """
        ## 🧠 Akıl Konu Anlatımı: Tam Sayılar
        
        **Tanım:** Tam sayılar, pozitif doğal sayılar ($1, 2, 3, ...$), negatif doğal sayılar ($-1, -2, -3, ...$) ve sıfırın oluşturduğu kümedir.
        
        **Toplama Kuralları:**
        1.  **Aynı İşaretliler:** Toplanır, ortak işaret sonuca yazılır. (Örn: $-5 + (-3) = -8$)
        2.  **Farklı İşaretliler:** Büyük sayıdan küçük sayı çıkarılır, büyük sayının işareti verilir. (Örn: $-10 + 4 = -6$)
        """
    else:
        # Sohbeti reddeden ve sadece konuya odaklanmayı isteyen kısım
        response = f"""
        ## ⚠️ Akıl Asistan Uyarısı
        
        **'{(topic[:20] + '...') if len(topic) > 20 else topic}'** şu an için anlatabileceğim konular arasında değildir. 
        
        Ben sadece 7. Sınıf konularını anlatmak üzere programlanmış bir öğrenci asistanıyım ve **sohbet özelliğim kapalıdır.** Lütfen sadece **Rasyonel Sayılar** veya **Tam Sayılar** gibi bir ders konusu yazınız.
        """
        
    st.session_state.ai_response = response
    st.session_state.last_topic = topic

# --- 2. TÜM İÇERİKLERİN TANIMI ---
COACH_CONTENT = """
## 💡 Koç Modülü - Öğrenci Koçluğu ve Rehberlik
### 🗓️ Rehberlik Konuları
* **Zaman Yönetimi:** Günlük rutin oluşturma ve derslere ayrılan sürenin belirlenmesi.
* **Pomodoro Tekniği:** 25 dakika çalışma, 5 dakika mola tekniği ile odaklanmayı artırma.
"""

MATH_CONTENT = """
## 📘 Matematik - Konu Anlatımı ve Özet
### 📄 Detaylı Konu Özeti
* Tam Sayılarla İşlemler
* Rasyonel Sayılar
* Cebirsel İfadeler
* Oran ve Orantı
"""
# Diğer ders içerikleri (TURKISH_CONTENT, SCIENCE_CONTENT, vb.) bu şekilde tanımlanmaya devam eder...

TURKISH_CONTENT = "..." # Kısaltıldı
SCIENCE_CONTENT = "..." # Kısaltıldı
SOCIAL_CONTENT = "..." # Kısaltıldı
ENGLISH_CONTENT = "..." # Kısaltıldı
RELIGION_CONTENT = "..." # Kısaltıldı

# Tüm içerikleri bir sözlükte toplama (Konu Anlatımı butonu için)
CONTENT_MAP = {
    "mat_konu": MATH_CONTENT,
    "tr_konu": TURKISH_CONTENT,
    "sci_konu": SCIENCE_CONTENT,
    "soc_konu": SOCIAL_CONTENT,
    "eng_konu": ENGLISH_CONTENT,
    "rel_konu": RELIGION_CONTENT,
}


# --- 3. STREAMLIT SAYFA AYARLARI ---
st.set_page_config(layout="wide", page_title="Yusuf Efe Şahin | 7. Sınıf Eğitim Portalı")
st.title("👨‍🎓 Yusuf Efe Şahin | 7. Sınıf Eğitim Portalı")
st.markdown("---")

# 4. SEKMELERİN TANIMLANMASI
tab_coach, tab_math, tab_tr, tab_sci, tab_soc, tab_eng, tab_rel = st.tabs([
    "💡 Koç Modülü", 
    "🔢 Matematik İçerikleri", 
    "📝 Türkçe İçerikleri", 
    "🧪 Fen Bilimleri",
    "🌍 Sosyal Bilgiler",
    "🗣️ İngilizce",
    "🕌 Din Kültürü",
])

# --- DERS SEKMELERİ İÇİN GENEL FONKSİYON ---
def render_subject_tab(tab_context, subject_title, key_prefix):
    """Her ders sekmesini tek bir yapıda oluşturur."""
    
    konu_key = f"{key_prefix}_konu"
    pdf_key = f"{key_prefix}_pdf"
    deneme_key = f"{key_prefix}_deneme"
    
    with tab_context:
        st.header(f"{subject_title} Dersi İçerikleri")
        col_btn1, col_btn2, col_btn3 = st.columns(3)
        
        with col_btn1:
            button_label = "⬆️ Konuyu Gizle" if st.session_state.content_key == konu_key else "📄 Konu Anlatımı"
            st.button(button_label, type="primary", key=konu_key,
                      on_click=toggle_content, args=(konu_key,)) 
        with col_btn2:
            st.button("♦️ PDF Sonuç Kontrol", type="secondary", key=pdf_key)
        with col_btn3:
            st.button("🔥 Deneme Sınavı", type="secondary", key=deneme_key)
        
        st.markdown("---")
        
        # --- İÇERİK GÖSTERİM MANTIĞI (Tıklayınca Açılır/Kapanır) ---
        if st.session_state.content_key == konu_key:
            st.subheader(f"✨ {subject_title} Konu Anlatımı Detay")
            st.markdown(CONTENT_MAP[konu_key], unsafe_allow_html=True)
            st.markdown("---")
        else:
            st.info(f"Yukarıdaki '📄 Konu Anlatımı' butonuna tıklayarak {subject_title} dersi içeriğini görebilirsiniz.")

# ==============================================================================
# --- 5. TAB 0: KOÇ MODÜLÜ (Akıl Asistanı) ---
# ==============================================================================
with tab_coach:
    st.header("💡 Koç Modülü - Rehberlik ve Mentorluk")
    st.subheader("🤖 Yapay Zeka Asistanı (Akıl)")
    
    # Text input and button for the AI feature
    input_topic = st.text_input(
        "Konu Adını Yazınız (Örn: Rasyonel Sayılar)", 
        value=st.session_state.last_topic,
        key="topic_input"
    )
    
    # Tıklanınca AI açıklaması başlar
    ai_button = st.button(
        "Akıl'dan Konuyu Anlatmasını İste", 
        type="primary", 
        key="ai_generate",
        on_click=generate_ai_explanation,
        args=(input_topic,)
    )
    
    st.markdown("---")
    
    # AI yanıtını göster
    st.markdown(st.session_state.ai_response, unsafe_allow_html=True)
    st.markdown("---") 

    # Orijinal Koç Modülü Butonları ve İçeriği
    st.header("📝 Çalışma ve Rehberlik İçerikleri")
    col_coach_btn1, col_coach_btn2, col_coach_btn3 = st.columns(3)
    
    with col_coach_btn1:
        st.button("📝 Çalışma Planı Oluştur", type="secondary", key="coach_plan") 
    with col_coach_btn2:
        st.button("🧠 Motivasyon Teknikleri", type="secondary", key="coach_motivasyon")
    with col_coach_btn3:
        st.button("⏰ Pomodoro Zamanlayıcısı", type="secondary", key="coach_pomodoro")
    
    st.markdown("---")
    st.markdown(COACH_CONTENT, unsafe_allow_html=True)


# ==============================================================================
# --- 6. DERS SEKMELERİNİN ÇAĞRILMASI (Tüm Dersler) ---
# ==============================================================================
render_subject_tab(tab_math, "🔢 Matematik", "mat")
render_subject_tab(tab_tr, "📝 Türkçe", "tr")
render_subject_tab(tab_sci, "🧪 Fen Bilimleri", "sci")
render_subject_tab(tab_soc, "🌍 Sosyal Bilgiler", "soc")
render_subject_tab(tab_eng, "🗣️ İngilizce", "eng")
render_subject_tab(tab_rel, "🕌 Din Kültürü", "rel")
