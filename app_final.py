# -*- coding: utf-8 -*-
# Kodlama sorununu çözmek için dosyanın en üstüne UTF-8 ayarı eklenmiştir.

import streamlit as st
import os
from google import genai
from google.genai.errors import APIError 

# --- 1. KÜTÜPHANE VE API KURULUMU ---

# secrets.toml dosyasından API anahtarını güvenli şekilde yükler.
try:
    if 'GEMINI_API_KEY' not in st.secrets:
        st.error("⚠️ GEMINI_API_KEY bulunamadı. Lütfen Streamlit Cloud Secrets paneline ekleyin.")
        st.stop()
    
    # Gemini istemcisini API anahtarıyla başlat
    client = genai.Client(api_key=st.secrets['GEMINI_API_KEY'])
    MODEL = 'gemini-2.5-flash' 

except Exception as e:
    st.error(f"API İstemcisi Başlatılamadı: {e}")
    st.stop()


# --- 2. İÇERİK TANIMLARI ---
# Yapay Zeka tarafından doldurulacak içerikler için başlangıç mesajı.
INITIAL_MESSAGE = "Yapay Zeka (AI) bu içeriği otomatik olarak dolduracak. Lütfen butona tıklayın."
TURKISH_CONTENT = INITIAL_MESSAGE
MATH_CONTENT = INITIAL_MESSAGE
SCIENCE_CONTENT = INITIAL_MESSAGE
SOCIAL_CONTENT = INITIAL_MESSAGE


# --- 3. SESSION STATE (DURUM YÖNETİMİ) ---
if 'content_key' not in st.session_state: st.session_state.content_key = None 
if 'ai_contents' not in st.session_state:
    # Yapay Zeka tarafından üretilen içerikleri depolamak için bir sözlük
    st.session_state.ai_contents = {
        "tr_konu": TURKISH_CONTENT,
        "mat_konu": MATH_CONTENT,
        "sci_konu": SCIENCE_CONTENT,
        "soc_konu": SOCIAL_CONTENT,
    }

# --- HARİTALAR VE SABİTLER ---
CONTENT_MAP = st.session_state.ai_contents


# --- 5. BUTON MANTIĞI VE API ÇAĞRISI ---
def generate_content_with_ai(subject_title, content_key):
    """Konu anlatımını API'den otomatik olarak çeken fonksiyon."""
    
    # Eğer içerik daha önce üretilmemişse 
    if st.session_state.ai_contents.get(content_key) == INITIAL_MESSAGE:
        
        prompt = f"""
        Sen 7. sınıf öğrencilerine ders veren Akıl Öğretmensin. {subject_title} dersinin 1. dönem temel konularını detaylı ve öğretici bir dille anlat. Cevabını mutlaka başlıklar, kalınlaştırmalar ve madde işaretleri kullanarak formatla. Türkçe karakterleri kullanmaktan çekinme (ç, ş, ı, ü, ö, ğ).
        """

        with st.spinner(f"👨‍🏫 Akıl Öğretmen, '{subject_title}' dersi içeriğini otomatik olarak hazırlıyor..."):
            try:
                # API çağrısı
                response = client.models.generate_content(
                    model=MODEL,
                    contents=prompt
                )
                # Cevabı session state'e kaydet
                # UTF-8 sorunu için tüm cevaplarda strip() kullanarak temizleme yapılır.
                st.session_state.ai_contents[content_key] = f"## 👨‍🏫 {subject_title} Detaylı Konu Anlatımı ✨\n\n" + response.text.strip()

            except APIError as e:
                st.session_state.ai_contents[content_key] = f"""
                ## ❌ API Hatası
                Akıl Öğretmen şu an bağlantı kuramıyor. Lütfen anahtarınızı kontrol edin. Hata Detayı: {e}
                """
            except Exception as e:
                 st.session_state.ai_contents[content_key] = f"## ❌ Bir Hata Oluştu: {e}"


def toggle_content(key, subject_title):
    # Eğer buton gizleniyorsa, sadece gizle
    if st.session_state.content_key == key: 
        st.session_state.content_key = None
    else:
        # Eğer butona ilk kez basılıyorsa, içeriği üret
        generate_content_with_ai(subject_title, key)
        st.session_state.content_key = key


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
        
        # Deneme butonu kaldırıldı.
        col_btn1, col_btn2 = st.columns(2) 
        
        with col_btn1:
            button_label = "⬆️ Konuyu Gizle" if st.session_state.content_key == konu_key else "📄 Detaylı Konu Anlatımı (OTOMATİK)"
            # Fonksiyon çağrısına subject_title eklendi
            st.button(button_label, type="primary", key=konu_key, on_click=toggle_content, args=(konu_key, subject_title)) 
                      
        with col_btn2: 
            st.button("♦️ PDF Sonuç Kontrol (MANUEL)", type="secondary", key=f"{key_prefix}_pdf_kontrol")
            
        st.markdown("---")
        
        # KONU ANLATIMI EKRANI
        if st.session_state.content_key == konu_key:
            st.subheader(f"✨ {subject_title} Dersi Konu Listesi") 
            for konu in konu_listesi: st.markdown(f"* **{konu}**")
            st.markdown("---")

            # OTOMATİK ÜRETİLEN KONU İÇERİĞİ BURADA GÖRÜNÜR
            st.subheader("📘 Otomatik Detaylı Konu Anlatımı")
            st.markdown(st.session_state.ai_contents.get(konu_key), unsafe_allow_html=True)
            st.markdown("---")
            
        else:
            st.info(f"Yukarıdaki butona tıklayarak {subject_title} dersi detaylı konu anlatımını otomatik olarak görebilirsiniz.")

# ==============================================================================
# --- 9. DERS SEKMELERİNİN ÇAĞRILMASI ---
# ==============================================================================
render_subject_tab(tab_math, "Matematik", "mat")
render_subject_tab(tab_tr, "Türkçe", "tr")
render_subject_tab(tab_sci, "Fen Bilimleri", "sci")
render_subject_tab(tab_soc, "Sosyal Bilgiler", "soc")
