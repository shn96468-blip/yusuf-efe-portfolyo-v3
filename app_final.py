import streamlit as st
import os

# --- 1. KÜTÜPHANE VE API KURULUMU ---
# API bağımlılığı tamamen kaldırılmıştır. Uygulama stabil çalışacaktır.

# --- 2. İÇERİK TANIMLARI (MANUEL İÇERİK ALANI) ---
# Detaylı konu anlatımı için bu değişkenlerin içini doldurmalısınız.

TURKISH_CONTENT = """
## 📝 Fiiller (Eylemler) Konu Anlatımı ✨

Bu alana Türkçe dersi için hazırladığınız **detaylı konuyu** (Markdown kullanarak) yapıştırabilirsiniz. 

Örnek (Fiiller): Fiiller, bir cümlede iş, oluş, hareket veya durum bildiren sözcüklerdir. Bir eylemin gerçekleştiği zamanı ve eylemi kimin yaptığını (kişi) gösteren ekler alırlar.
"""

MATH_CONTENT = "## 📘 Matematik Konu Anlatımı Detayı (Lütfen içeriği buraya ekleyin.)"
SCIENCE_CONTENT = "## 🧪 Fen Bilimleri Konu Anlatımı Detayı (Lütfen içeriği buraya ekleyin.)"
SOCIAL_CONTENT = "## 🌍 Sosyal Bilgiler Konu Anlatımı Detayı (Lütfen içeriği buraya ekleyin.)"


MATH_VIDEOS = {} 
TURKISH_VIDEOS = {}
SCIENCE_VIDEOS = {}
SOCIAL_VIDEOS = {}


# --- 3. SESSION STATE (DURUM YÖNETİMİ) ---
if 'content_key' not in st.session_state: st.session_state.content_key = None 
# Bu kodda AI bölümü olmadığı için yapay zeka değişkenleri kaldırılmıştır.

# --- HARİTALAR VE SABİTLER ---
CONTENT_MAP = {
    "mat_konu": MATH_CONTENT, 
    "tr_konu": TURKISH_CONTENT, 
    "sci_konu": SCIENCE_CONTENT, 
    "soc_konu": SOCIAL_CONTENT, 
}

# --- 5. BUTON MANTIĞI ---
def toggle_content(key):
    if st.session_state.content_key == key: st.session_state.content_key = None
    else: st.session_state.content_key = key


# --- 6. SAYFA AYARLARI ---
st.set_page_config(layout="wide", page_title="Yusuf Efe Şahin | 7. Sınıf Eğitim Portalı")
st.title("👨‍🎓 Yusuf Efe Şahin | 7. Sınıf Eğitim Portalı")
st.markdown("---")

# --- 7. SEKMELERİN TANIMLANMASI (SADECE 4 DERS SEKMESİ) ---
tab_math, tab_tr, tab_sci, tab_soc = st.tabs([
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
        
        # Soru çözümü, deneme butonu gibi özellikler burada manuel olarak içerik eklenerek kullanılabilir.
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
            st.markdown(CONTENT_MAP.get(konu_key, "İçerik Bulunamadı. Lütfen app_final.py dosyasındaki CONTENT_MAP'i doldurun."), unsafe_allow_html=True)
            st.markdown("---")
            
        else:
            st.info(f"Yukarıdaki butona tıklayarak {subject_title} dersi içeriğini görebilirsiniz.")

# ==============================================================================
# --- 9. DERS SEKMELERİNİN ÇAĞRILMASI ---
# ==============================================================================
render_subject_tab(tab_math, "🔢 Matematik", "mat")
render_subject_tab(tab_tr, "📝 Türkçe", "tr")
render_subject_tab(tab_sci, "🧪 Fen Bilimleri", "sci")
render_subject_tab(tab_soc, "🌍 Sosyal Bilgiler", "soc")
