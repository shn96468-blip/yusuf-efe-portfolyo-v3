import streamlit as st

# Streamlit'in sayfa durumunu (state) yönetmek için bir mekanizma kuralım
# Bu, butonların durumunu hatırlamamızı sağlar.
if 'page_selected' not in st.session_state:
    # Varsayılan olarak Koç Modülünü göster
    st.session_state.page_selected = 'coach' 
    st.session_state.content_show = False

# --- 1. TÜM İÇERİKLERİN TANIMI ---
COACH_CONTENT = """
## 💡 Koç Modülü - Öğrenci Koçluğu ve Rehberlik
<div style='background-color: #26292e; padding: 10px; border-radius: 5px;'>
    <p>🎓 Konu: Etkili Ders Çalışma Yöntemleri ve Zaman Yönetimi</p>
</div>
### 🗓️ Haftalık Çalışma Planı
* **Zaman Yönetimi:** Günlük rutin oluşturma ve derslere ayrılan sürenin belirlenmesi.
* **Pomodoro Tekniği:** 25 dakika çalışma, 5 dakika mola tekniği ile odaklanmayı artırma.
* **Verimli Not Alma:** Anahtar kelimeler ve zihin haritası kullanarak not tutma.
"""

MATH_CONTENT = """
## 📘 Matematik - Konu Anlatımı ve Özet
### 📄 Detaylı Konu Özeti
* Tam Sayılarla İşlemler
* Rasyonel Sayılar
* Cebirsel İfadeler
* Oran ve Orantı
* Yüzdeler
* Doğrular ve Açılar
"""

TURKISH_CONTENT = """
## 📝 Türkçe - Konu Anlatımı ve Özet
### 📄 Detaylı Konu Özeti
* Sözcükte Anlam
* Cümlede Anlam
* Paragrafta Anlam
* Fiiller (Eylem)
* Yazım Kuralları ve Noktalama İşaretleri
"""

SCIENCE_CONTENT = """
## 🧪 Fen Bilimleri - Konu Anlatımı ve Özet
### 📄 Detaylı Konu Özeti
* Güneş Sistemi ve Ötesi
* Hücre
* Kuvvet ve Enerji
* Saf Madde ve Karışımlar
* Işığın Maddeyle Etkileşimi
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
    "mat": MATH_CONTENT,
    "tr": TURKISH_CONTENT,
    "sci": SCIENCE_CONTENT,
    "soc": SOCIAL_CONTENT,
    "eng": ENGLISH_CONTENT,
    "rel": RELIGION_CONTENT,
}


# --- 2. STREAMLIT SAYFA AYARLARI ---
st.set_page_config(layout="wide", page_title="Yusuf Efe Şahin | 7. Sınıf Eğitim Portalı")
st.title("👨‍🎓 Yusuf Efe Şahin | 7. Sınıf Eğitim Portalı")
st.markdown("---")

# 3. SEKMELERİN TANIMLANMASI
tab_coach, tab_math, tab_tr, tab_sci, tab_soc, tab_eng, tab_rel = st.tabs([
    "💡 Koç Modülü", 
    "🔢 Matematik İçerikleri", 
    "📝 Türkçe İçerikleri", 
    "🧪 Fen Bilimleri",
    "🌍 Sosyal Bilgiler",
    "🗣️ İngilizce",
    "🕌 Din Kültürü",
])

# --- BUTON TIKLAMA İŞLEVİ (Callback) ---
def set_content_and_show(key):
    st.session_state.page_selected = key
    st.session_state.content_show = True

# --- DERS SEKMELERİ İÇİN GENEL FONKSİYON ---
def render_subject_tab(tab_context, subject_key, subject_title, content_key):
    """Her ders sekmesini tek bir yapıda oluşturur."""
    with tab_context:
        st.header(f"{subject_title} Dersi İçerikleri")
        col_btn1, col_btn2, col_btn3 = st.columns(3)
        
        with col_btn1:
            # Konu Anlatımı butonu: Tıklandığında içeriği göstermesi için state'i günceller
            st.button("📄 Konu Anlatımı", type="primary", key=f"{subject_key}_konu",
                      on_click=set_content_and_show, args=(content_key,)) 
        with col_btn2:
            st.button("♦️ PDF Sonuç Kontrol", type="secondary", key=f"{subject_key}_pdf")
        with col_btn3:
            st.button("🔥 Deneme Sınavı", type="secondary", key=f"{subject_key}_deneme")
        
        st.markdown("---")
        
        # Eğer bu sekme seçiliyse ve Konu Anlatımı butonu tıklandıysa, içeriği göster
        if st.session_state.page_selected == content_key and st.session_state.content_show:
            st.subheader(f"✨ {subject_title} Konu Anlatımı Detay")
            st.markdown(CONTENT_MAP[content_key], unsafe_allow_html=True)
            # İçeriği gösterdikten sonra, tekrar gizlenebilmesi için butona yer açar
            if st.button("⬆️ Konu Anlatımını Gizle", key=f"{subject_key}_hide"):
                st.session_state.content_show = False
                st.session_state.page_selected = 'coach' # Başka bir sekmeye yönlendirmemek için
        else:
            # Varsayılan veya buton tıklanmamış içerik
            st.info(f"Yukarıdaki '📄 Konu Anlatımı' butonuna tıklayarak {subject_title} dersi içeriğini görebilirsiniz.")
            
            # Ana içeriği göster (Örneğin, konu başlıkları)
            st.markdown(CONTENT_MAP[content_key], unsafe_allow_html=True)


# ==============================================================================
# --- 4. TAB 0: KOÇ MODÜLÜ ---
# ==============================================================================
with tab_coach:
    st.header("💡 Koç Modülü - Rehberlik ve Mentorluk")
    col_coach_btn1, col_coach_btn2, col_coach_btn3 = st.columns(3)
    
    with col_coach_btn1:
        st.button("📝 Çalışma Planı Oluştur", type="primary", key="coach_plan") 
    with col_coach_btn2:
        st.button("🧠 Motivasyon Teknikleri", type="secondary", key="coach_motivasyon")
    with col_coach_btn3:
        st.button("⏰ Pomodoro Zamanlayıcısı", type="secondary", key="coach_pomodoro")
    
    st.markdown("---")
    st.markdown(COACH_CONTENT, unsafe_allow_html=True)


# ==============================================================================
# --- 5. TAB 1: MATEMATİK İÇERİKLERİ ---
# ==============================================================================
render_subject_tab(tab_math, "mat", "🔢 Matematik", "mat")

# ==============================================================================
# --- 6. TAB 2: TÜRKÇE İÇERİKLERİ ---
# ==============================================================================
render_subject_tab(tab_tr, "tr", "📝 Türkçe", "tr")

# ==============================================================================
# --- 7. TAB 3: FEN BİLİMLERİ İÇERİKLERİ ---
# ==============================================================================
render_subject_tab(tab_sci, "fen", "🧪 Fen Bilimleri", "sci")

# ==============================================================================
# --- 8. TAB 4: SOSYAL BİLGİLER İÇERİKLERİ ---
# ==============================================================================
render_subject_tab(tab_soc, "sos", "🌍 Sosyal Bilgiler", "soc")

# ==============================================================================
# --- 9. TAB 5: İNGİLİZCE İÇERİKLERİ ---
# ==============================================================================
render_subject_tab(tab_eng, "ing", "🗣️ İngilizce", "eng")

# ==============================================================================
# --- 10. TAB 6: DİN KÜLTÜRÜ İÇERİKLERİ ---
# ==============================================================================
render_subject_tab(tab_rel, "din", "🕌 Din Kültürü", "rel")
