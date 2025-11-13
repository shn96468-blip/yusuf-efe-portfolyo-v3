import streamlit as st
import os

# --- 2. İÇERİK TANIMLARI (MANUEL İÇERİK ALANI) ---

# 1. DETAYLI KONU ANLATIMI İÇİN İÇERİK
TURKISH_CONTENT = """
## 📝 TÜRKÇE DERSİ DETAYLI KONU ANLATIM BAŞLIĞI
Bu alana Türkçe dersi için hazırladığınız **detaylı konuyu** (Markdown kullanarak) yapıştırmalısınız.
"""

TURKISH_DENEME_CONTENT = """
## 🔥 TÜRKÇE 1. DÖNEM GENEL TEKRAR SINAVI

Bu alana **1. dönem konularının tamamını kapsayan** soruları ve cevap anahtarını (Markdown kullanarak) yapıştırmalısınız.

Örnek Soru: 
**1. Soru:** Aşağıdakilerden hangisi durum fiilidir?
* A) Yazmak
* B) Uyudu
* C) Büyümek

**(Cevap: B)**
"""

MATH_CONTENT = "## 📘 Matematik Konu Anlatımı Detayı (Lütfen içeriği buraya ekleyin.)"
MATH_DENEME_CONTENT = "## 🔢 Matematik Dönem Tekrar Sınavı (Lütfen soruları buraya ekleyin.)"
SCIENCE_CONTENT = "## 🧪 Fen Bilimleri Konu Anlatımı Detayı"
SCIENCE_DENEME_CONTENT = "## 🧪 Fen Bilimleri Dönem Tekrar Sınavı"
SOCIAL_CONTENT = "## 🌍 Sosyal Bilgiler Konu Anlatımı Detayı"
SOCIAL_DENEME_CONTENT = "## 🌍 Sosyal Bilgiler Dönem Tekrar Sınavı"


# --- 3. SESSION STATE (DURUM YÖNETİMİ) ---
if 'content_key' not in st.session_state: st.session_state.content_key = None 
if 'test_active' not in st.session_state: st.session_state.test_active = False


# --- HARİTALAR VE SABİTLER ---
CONTENT_MAP = {
    "mat_konu": MATH_CONTENT, 
    "tr_konu": TURKISH_CONTENT, 
    "sci_konu": SCIENCE_CONTENT, 
    "soc_konu": SOCIAL_CONTENT, 
}
DENEME_MAP = {
    "mat_deneme": MATH_DENEME_CONTENT, 
    "tr_deneme": TURKISH_DENEME_CONTENT, 
    "sci_deneme": SCIENCE_DENEME_CONTENT, 
    "soc_deneme": SOCIAL_DENEME_CONTENT, 
}

# --- 5. BUTON MANTIĞI ---
def toggle_content(key):
    # Konu anlatımı butonuna basılınca test modunu kapat
    st.session_state.test_active = False
    if st.session_state.content_key == key: st.session_state.content_key = None
    else: st.session_state.content_key = key

def toggle_test(key_prefix):
    # Test butonuna basılınca konu anlatımını kapat
    st.session_state.content_key = None
    if st.session_state.test_active == key_prefix: st.session_state.test_active = False
    else: st.session_state.test_active = key_prefix

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
    deneme_key = f"{key_prefix}_deneme"
    
    # Konu Listeleri 
    if key_prefix == "tr":
        konu_listesi = ["Sözcükte Anlam", "Cümlede Anlam", "Parçada Anlam", "Fiiller", "Ek Fiil", "Zarflar"]
    elif key_prefix == "mat":
        konu_listesi = ["Tam Sayılarla İşlemler", "Rasyonel Sayılar", "Cebirsel İfadeler", "Oran Orantı", "Doğrular ve Açılar"]
    else:
        konu_listesi = [f"Bu derse ait Konu Listesi Henüz Eklenmedi."]

    
    with tab_context:
        st.header(f"{subject_title} Dersi İçerikleri")
        
        col_btn1, col_btn2, col_btn3 = st.columns(3) 
        
        with col_btn1:
            button_label = "⬆️ Konuyu Gizle" if st.session_state.content_key == konu_key else "📄 Detaylı Konu Anlatımı"
            st.button(button_label, type="primary", key=konu_key, on_click=toggle_content, args=(konu_key,)) 
                      
        with col_btn2: # Yer Tutucu Buton
            st.button("♦️ PDF Sonuç Kontrol", type="secondary", key=f"{key_prefix}_pdf_kontrol")
            
        with col_btn3:
            button_label_deneme = "⬆️ Denemeyi Gizle" if st.session_state.test_active == key_prefix else "🔥 1. Dönem Tekrar Sınavı"
            st.button(button_label_deneme, type="secondary", key=f"{key_prefix}_deneme_btn", on_click=toggle_test, args=(key_prefix,))
        
        st.markdown("---")
        
        # 8a. KONU ANLATIMI EKRANI
        if st.session_state.content_key == konu_key:
            st.subheader(f"✨ {subject_title} Dersi Konu Listesi") 
            for konu in konu_listesi: st.markdown(f"* **{konu}**")
            st.markdown("---")

            # MANUEL DETAYLI KONU İÇERİĞİ BURADA GÖRÜNÜR
            st.subheader("📘 Detaylı Konu Anlatımı")
            st.markdown(CONTENT_MAP.get(konu_key, "İçerik Bulunamadı. Lütfen app_final.py dosyasındaki CONTENT_MAP'i doldurun."), unsafe_allow_html=True)
            st.markdown("---")
        
        # 8b. DÖNEM TEKRAR SINAVI EKRANI
        elif st.session_state.test_active == key_prefix:
            # MANUEL DÖNEM TEKRAR SINAVI İÇERİĞİ BURADA GÖRÜNÜR
            st.markdown(DENEME_MAP.get(deneme_key, "Sınav içeriği bulunamadı. Lütfen app_final.py dosyasındaki DENEME_CONTENT değişkenini doldurun."), unsafe_allow_html=True)
            st.markdown("---")
            
        else:
            st.info(f"Yukarıdaki butonlara tıklayarak {subject_title} dersi detaylı içeriğini veya dönem tekrar sınavını görebilirsiniz.")

# ==============================================================================
# --- 9. DERS SEKMELERİNİN ÇAĞRILMASI ---
# ==============================================================================
render_subject_tab(tab_math, "🔢 Matematik", "mat")
render_subject_tab(tab_tr, "📝 Türkçe", "tr")
render_subject_tab(tab_sci, "🧪 Fen Bilimleri", "sci")
render_subject_tab(tab_soc, "🌍 Sosyal Bilgiler", "soc")
