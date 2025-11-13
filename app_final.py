import streamlit as st

# --- 1. STREAMLIT DURUM YÖNETİMİ (Session State) ---
# Bu, butonlara tıklandığında hangi içeriğin gösterileceğini kontrol eder.
if 'page_selected' not in st.session_state:
    st.session_state.page_selected = 'coach' 
    st.session_state.content_show = False
    
# --- BUTON TIKLAMA İŞLEVİ (Callback) ---
# Bu fonksiyon, Konu Anlatımı butonuna tıklandığında çalışır.
def set_content_and_show(key):
    st.session_state.page_selected = key
    st.session_state.content_show = True

# --- 2. TÜM İÇERİKLERİN TANIMI (Tek dosyada toplandı) ---

COACH_CONTENT = """
## 💡 Koç Modülü - Öğrenci Koçluğu ve Rehberlik
<div style='background-color: #26292e; padding: 10px; border-radius: 5px;'>
    <p>🎓 Konu: Etkili Ders Çalışma Yöntemleri ve Zaman Yönetimi</p>
</div>
### 🗓️ Haftalık Çalışma Planı
* **Zaman Yönetimi:** Günlük rutin oluşturma ve derslere ayrılan sürenin belirlenmesi.
* **Pomodoro Tekniği:** 25 dakika çalışma, 5 dakika mola tekniği ile odaklanmayı artırma.
"""

MATH_CONTENT = """
## 📘 Matematik - Konu Anlatımı ve Özet
### 📄 Detaylı Konu Özeti
* **Tam Sayılarla İşlemler:** Toplama, çıkarma, çarpma ve bölme kuralları.
* **Rasyonel Sayılar:** Gösterim, sıralama ve işlemler.
* **Cebirsel İfadeler:** Temel kavramlar ve dört işlem.
* **Oran ve Orantı:** Doğru ve ters orantı problemleri.
"""

TURKISH_CONTENT = """
## 📝 Türkçe - Konu Anlatımı ve Özet
### 📄 Detaylı Konu Özeti
* **Sözcükte Anlam:** Gerçek, mecaz ve terim anlam.
* **Cümlede Anlam:** Amaç-sonuç, neden-sonuç ve koşul cümleleri.
* **Paragrafta Anlam:** Ana fikir, yardımcı fikirler ve konu.
* **Fiiller (Eylem):** Kip, kişi ve zaman.
"""

SCIENCE_CONTENT = """
## 🧪 Fen Bilimleri - Konu Anlatımı ve Özet
### 📄 Detaylı Konu Özeti
* **Güneş Sistemi ve Ötesi:** Gezegenler, yıldızlar ve gök cisimleri.
* **Hücre:** Yapı ve görevleri.
* **Kuvvet ve Enerji:** İş, güç ve enerji dönüşümleri.
* **Saf Madde ve Karışımlar:** Elementler, bileşikler ve karışımların ayrılması.
"""

SOCIAL_CONTENT = """
## 🌍 Sosyal Bilgiler - Konu Anlatımı ve Özet
### 📄 Detaylı Konu Özeti
* **BİREY VE TOPLUM:** Roller, beklentiler ve sosyal değişim.
* **KÜLTÜR VE MİRAS:** Türk-İslam devletleri ve kültürel zenginlik.
* **İNSANLAR, YERLER VE ÇEVRELER:** Coğrafi konumlar ve iklim tipleri.
* **BİLİM, TEKNOLOJİ VE TOPLUM:** İletişim araçlarının gelişimi.
"""

ENGLISH_CONTENT = """
## 🗣️ İngilizce - Konu Anlatımı ve Özet
### 📄 Detaylı Konu Özeti
* **Appearance and Personality:** Dış görünüş ve karakter sıfatları.
* **Sports:** Spor dalları ve kuralları.
* **Biographies:** Geçmiş zaman (Past Tense) kullanımı.
* **Wild Animals:** Vahşi yaşam ve habitatlar.
"""

RELIGION_CONTENT = """
## 🕌 Din Kültürü ve Ahlak Bilgisi - Konu Anlatımı ve Özet
### 📄 Detaylı Konu Özeti
* **Melek ve Ahiret İnancı:** Meleklerin görevleri ve ahiret hayatı.
* **Hac ve Kurban İbadeti:** Hac menasikleri ve kurban çeşitleri.
* **Ahlaki Davranışlar:** Doğruluk, dürüstlük ve sorumluluk.
* **İslam Düşüncesinde Yorumlar:** Mezhepler ve din anlayışı.
"""

# Tüm içerikleri bir sözlükte toplama (Konu Anlatımı butonu için)
CONTENT_MAP = {
    "coach": COACH_CONTENT,
    "mat": MATH_CONTENT,
    "tr": TURKISH_CONTENT,
    "sci": SCIENCE_CONTENT,
    "soc": SOCIAL_CONTENT,
    "eng": ENGLISH_CONTENT,
    "rel": RELIGION_CONTENT,
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
def render_subject_tab(tab_context, subject_key, subject_title, content_key):
    """Her ders sekmesini tek bir yapıda oluşturur ve tıklama mantığını uygular."""
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
        
        # --- İÇERİK GÖSTERİM MANTIĞI (ESKİ SİSTEM) ---
        # Eğer bu dersin butonu tıklandıysa, içeriği gösterir.
        if st.session_state.page_selected == content_key and st.session_state.content_show:
            st.subheader(f"✨ {subject_title} Konu Anlatımı Detay")
            st.markdown(CONTENT_MAP[content_key], unsafe_allow_html=True)
            
            # İçeriği gizleme butonu
            if st.button("⬆️ Konu Anlatımını Gizle", key=f"{subject_key}_hide"):
                st.session_state.content_show = False
                st.session_state.page_selected = 'coach' 
        else:
            # Butona tıklanmadıysa varsayılan özet gösterilir.
            st.info(f"Yukarıdaki '📄 Konu Anlatımı' butonuna tıklayarak {subject_title} dersi içeriğini görebilirsiniz.")
            # Varsayılan içerik olarak, içeriğin tamamını göstermeyelim, sadece ipucu verelim.
            # st.markdown(CONTENT_MAP[content_key], unsafe_allow_html=True) 

# ==============================================================================
# --- 5. TAB 0: KOÇ MODÜLÜ ---
# ==============================================================================
# Koç Modülü, özel bir yapıdır ve content_show mantığını uygulamaz.
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
# --- 6. DERS SEKMELERİNİN ÇAĞRILMASI (Tüm Dersler) ---
# ==============================================================================
render_subject_tab(tab_math, "mat", "🔢 Matematik", "mat")
render_subject_tab(tab_tr, "tr", "📝 Türkçe", "tr")
render_subject_tab(tab_sci, "fen", "🧪 Fen Bilimleri", "sci")
render_subject_tab(tab_soc, "sos", "🌍 Sosyal Bilgiler", "soc")
render_subject_tab(tab_eng, "ing", "🗣️ İngilizce", "eng")
render_subject_tab(tab_rel, "din", "🕌 Din Kültürü", "rel")
