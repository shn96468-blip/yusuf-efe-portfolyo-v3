# -*- coding: utf-8 -*-
# Kodlama sorununu aşmak için UTF-8 formatı korunmuştur.

import streamlit as st
import os
from google import genai
from google.genai.errors import APIError 

# --- 1. KÜTÜPHANE VE API KURULUMU ---

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


# --- 2. SESSION STATE (DURUM YÖNETİMİ) ---
if 'last_topic' not in st.session_state: st.session_state.last_topic = ""
if 'ai_response' not in st.session_state: st.session_state.ai_response = ""


# --- 3. API ÇAĞRISI FONKSİYONU ---
def generate_content_with_ai(topic_name):
    """Konu anlatımını API'den otomatik olarak çeken fonksiyon."""
    
    # PROMPT GÜNCELLENDİ: TÜRKÇE KARAKTER KULLANMAMA TALİMATI
    prompt = f"""
    Sen 7. sınıf öğrencilerine ders veren Akıl Öğretmensin. '{topic_name}' konusunu detaylı ve öğretici bir dille anlat. Cevabını Türkçe kelimeler kullanarak (Örn: sinif, ders, konular), ancak **sadece İngilizce harflerle (ı, ş, ç, ü, ö, ğ harflerini kullanmadan)** yaz. Cevabını mutlaka başlıklar ve madde işaretleri kullanarak formatla.
    """

    with st.spinner(f"👨‍🏫 Akıl Öğretmen, '{topic_name}' konusu için içeriği otomatik olarak hazırlıyor..."):
        try:
            # API çağrısı
            response = client.models.generate_content(
                model=MODEL,
                contents=prompt
            )
            
            # Kodlama hatasını atlamak için düzeltme tekrar uygulanır.
            clean_text = response.text.encode('utf-8', errors='ignore').decode('utf-8')
            
            # Cevabı session state'e kaydet
            st.session_state.ai_response = f"## 👨‍🏫 Akıl Ogretmen: {topic_name.upper()} Konu Anlatimi ✨\n\n" + clean_text.strip()
            st.session_state.last_topic = topic_name

        except APIError as e:
            st.session_state.ai_response = f"""
            ## ❌ API Hatası
            Akıl Ogretmen su an baglanti kuramiyor. Lutfen anahtarinizi kontrol edin. Hata Detayi: {e}
            """
        except Exception as e:
             st.session_state.ai_response = f"## ❌ Bir Hata Olustu: {e}"

# --- 4. SAYFA AYARLARI ---
st.set_page_config(layout="wide", page_title="Yusuf Efe Şahin | Akıl Öğretmen")
st.title("🎓 Yusuf Efe Şahin | Yapay Zeka Asistanı (Akıl Ogretmen)")
st.markdown("---")

# --- 5. ANA SAYFA KODU ---

st.header("❓ Akıl Ogretmen'e Sor")
st.markdown("Asagidaki kutucuga herhangi bir 7. sinif konusu yazin ve Akil Ogretmen'den detayli anlatim isteyin.")

# Konu adı girişi
topic_input = st.text_input(
    label="Konu Adini Yaziniz (Orn: Rasyonel Sayilar, Fiiller, Mitokondri)",
    placeholder="Konu Adi",
    label_visibility="collapsed"
)

# Buton
if st.button("Akil'dan Konuyu Anlatmasini İsteyin", type="primary"):
    if topic_input:
        generate_content_with_ai(topic_input)
    else:
        st.warning("Lutfen anlatilacak konunun adini yaziniz.")

st.markdown("---")

# Sonuç alanı
if st.session_state.ai_response:
    st.markdown(st.session_state.ai_response, unsafe_allow_html=True)
else:
    st.info("Konu anlatimini gormek icin yukariya bir konu yazip butona tiklayin.")
    
