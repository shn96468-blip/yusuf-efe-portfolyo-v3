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
    # Aynı butona tekrar tıklanırsa (gizle), None yapar.
    if st.session_state.content_key == key:
        st.session_state.content_key = None
    # Başka bir butona tıklanırsa, yeni içeriği gösterir.
    else:
        st.session_state.content_key = key

# Yapay Zeka (Gemini) Butonu için
def generate_ai_explanation(topic):
    # Bu kısım, Gemini modelinin konuyu anlattığı yerdir.
    # Ben (Gemini) olduğum için, doğrudan konuyu anlatıyorum.
    
    if "rasyonel sayılar" in topic.lower():
        response = """
        ## 🧠 Gemini Konu Anlatımı: Rasyonel Sayılar
        
        **Tanım:** Rasyonel sayılar, $a$ bir tam sayı ve $b$ sıfırdan farklı bir tam sayı olmak üzere, $\\frac{a}{b}$ şeklinde yazılabilen sayılardır. Kesir çizgisi, aslında bir bölme işlemidir.
        
        **İşlemler:**
        * **Toplama/Çıkarma:** Paydalar eşitlenmelidir.
        * **Çarpma:** Paylar çarpılıp paya, paydalar çarpılıp paydaya yazılır.
        * **Bölme:** Birinci rasyonel sayı aynen yazılır, ikinci rasyonel sayı ters çevrilip çarpılır.
        """
    elif "tam sayılar" in topic.lower():
        response = """
        ## 🧠 Gemini Konu Anlatımı: Tam Sayılar
        
        **Tanım:** Tam sayılar, pozitif doğal sayılar ($1, 2, 3, ...$), negatif doğal sayılar ($-1, -2, -3, ...$) ve sıfırın oluşturduğu kümedir. $\\mathbb{Z}$ sembolü ile gösterilir.
        
        **Toplama Kuralları:**
        1.  **Aynı İşaretliler:** Toplanır, ortak işaret sonuca yazılır. (Örn: $-5 + (-3) = -8$)
        2.  **Farklı İşaretliler:** Büyük sayıdan küçük sayı çıkarılır, sonucun işaretine büyük sayının işareti verilir. (Örn: $-10 + 4 = -6$)
        """
    else:
        # Genel ve genişletilebilir yanıt
        response = f"""
        ## 🧠 Gemini Konu Anlatımı: "{topic.upper()}"
        
        **'{topic}'** konusunu sizin için kısa ve öz bir şekilde açıklıyorum: Bu konu, genellikle bir dersin temel kavramlarından birini oluşturur ve öğrencinin bu alandaki bilgiyi sağlamlaştırmasına yardımcı olur.
        
        **Önemli Not:** Şu an için detaylı ve uzman düzeyinde anlatımımız **Matematik dersindeki Rasyonel Sayılar ve Tam Sayılar** konularıyla sınırlıdır. Lütfen bu konuları deneyerek yapay zeka asistanının çalışmasını test edin.
        """
        
    st.session_state.ai_response = response
    st.session_state.last_topic = topic

# --- 2. TÜM İÇERİKLERİN TANIMI ---
COACH_CONTENT = """
## 💡 Koç Modülü - Öğrenci Koçluğu ve Rehberlik
<div style='background-color: #26292e; padding: 10px; border-radius: 5px;'>
    <p>🎓 Konu: Etkili Ders Çalışma Yöntemleri ve Zaman Yönetimi</p>
</div>
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

TURKISH_CONTENT = """
## 📝 Türkçe - Konu Anlatımı ve Özet
### 📄 Detaylı Konu Özeti
* Sözcükte Anlam
* Cümlede Anlam
* Paragrafta Anlam
* Fiiller (Eylem)
"""

SCIENCE_CONTENT = """
## 🧪 Fen Bilimleri - Konu Anlatımı ve Özet
### 📄 Detaylı Konu Özeti
* Güneş Sistemi ve Ötesi
* Hücre
* Kuvvet ve Enerji
* Saf Madde ve Karışımlar
"""

SOCIAL_CONTENT = """
## 🌍 Sosyal Bilgiler - Konu Anlatımı ve Özet
### 📄 Detaylı Konu Özeti
* BİREY VE TOPLUM
* KÜLTÜR VE MİRAS
* İNSANLAR, YERLER VE ÇEVRELER
* BİLİM, TEKNOLOJİ VE TOPLUM
"""

ENGLISH_CONTENT = """
## 🗣️ İngilizce - Konu Anlatımı ve Özet
### 📄 Detaylı Konu Özeti
* Appearance and Personality (Dış Görünüş ve Karakter)
* Sports (Spor)
* Biographies (Biyografiler)
* Wild Animals (Vahşi Hayvanlar)
"""

RELIGION_CONTENT = """
## 🕌 Din Kültürü ve Ahlak Bilgisi - Konu Anlatımı ve Özet
### 📄 Detaylı Konu Özeti
* Melek ve Ahiret İnancı
* Hac ve Kurban İbadeti
* Ahlaki Davranışlar
* İslam Düşüncesinde Yorumlar
"""

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
    
    # Her buton için tekil KEY tanımlıyoruz
    konu_key = f"{key_prefix}_konu"
    pdf_key = f"{key_prefix}_pdf"
    deneme_key = f"{key_prefix}_deneme"
    
    with tab_context:
        st.header(f"{subject_title} Dersi İçerikleri")
        col_btn1, col_btn2, col_btn3 = st.columns(3)
        
        with col_btn1:
            # Konu Anlatımı butonu: Tıklandığında toggle_content çalışır.
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
# --- 5. TAB 0: KOÇ MODÜLÜ (Gemini Özelliği Eklendi) ---
# ==============================================================================
with tab_coach:
    st.header("💡 Koç Modülü - Rehberlik ve Mentorluk")
    st.subheader("🤖 Yapay Zeka Asistanı (Gemini)")
    
    # Text input and button for the AI feature
    input_topic = st.text_input(
        "Konu Adını Yazınız (Örn: Rasyonel Sayılar)", 
        value=st.session_state.last_topic,
        key="topic_input"
    )
    
    # Tıklanınca AI açıklaması başlar
    ai_button = st.button(
        "Gemini'den Konuyu Anlatmasını İste", 
        type="primary", 
        key="ai_generate",
        on_click=generate_ai_explanation,
        args=(input_topic,) # text_input değerini fonksiyona parametre olarak gönderir
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
