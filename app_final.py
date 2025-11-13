# -*- coding: utf-8 -*-

import streamlit as st
import os
from google import genai
from google.genai.errors import APIError 

# --- 1. KÜTÜPHANE VE API KURULUMU ---

try:
    if 'GEMINI_API_KEY' not in st.secrets:
        st.error("⚠️ GEMINI_API_KEY bulunamadi. Lutfen Streamlit Cloud Secrets paneline ekleyin.")
        st.stop()
    
    client = genai.Client(api_key=st.secrets['GEMINI_API_KEY'])
    MODEL = 'gemini-2.5-flash' 

except Exception as e:
    st.error(f"API Istemcisi Baslatilamadi: {e}")
    st.stop()


# --- 2. SESSION STATE (DURUM YÖNETİMİ) ---
if 'last_topic' not in st.session_state: st.session_state.last_topic = ""
if 'ai_response' not in st.session_state: st.session_state.ai_response = ""


# --- 3. API ÇAĞRISI FONKSİYONU ---
def generate_content_with_ai(topic_name):
    """Konu anlatımını API'den otomatik olarak çeken fonksiyon."""
    
    prompt = f"""
    Sen 7. sinif ogrencilerine ders veren Akil Ogretmensin. '{topic_name}' konusunu detayli ve ogretici bir dille anlat. Cevabini Turkce kelimeler kullanarak, basliklar ve madde isaretleri ile formatla. 
    """

    with st.spinner(f"👨‍🏫 Akil Ogretmen, '{topic_name}' konusu icin icerigi otomatik olarak hazirliyor..."):
        try:
            response = client.models.generate_content(
                model=MODEL,
                contents=prompt
            )
            
            # KRİTİK DÜZELTME: Hata veren karakterleri silen fonksiyon
            def remove_turkish_chars(text):
                tr_chars = {'ı':'i', 'ğ':'g', 'ü':'u', 'ş':'s', 'ö':'o', 'ç':'c', 'İ':'I', 'Ğ':'G', 'Ü':'U', 'Ş':'S', 'Ö':'O', 'Ç':'C'}
                for tr, en in tr_chars.items():
                    text = text.replace(tr, en)
                # Kalan tüm özel karakterleri ASCII dışı bırakarak hatayı engeller.
                return text.encode('ascii', 'ignore').decode('ascii')
            
            # Temizlenmis metni kullan
            clean_text = remove_turkish_chars(response.text)
            
            st.session_state.ai_response = f"## 👨‍🏫 Akil Ogretmen: {topic_name.upper()} Konu Anlatimi ✨\n\n" + clean_text.strip()
            st.session_state.last_topic = topic_name

        except APIError as e:
            st.session_state.ai_response = f"""
            ## ❌ API Hatasi
            Akil Ogretmen su an baglanti kuramiyor. Lutfen anahtarinizi kontrol edin. Hata Detayi: {e}
            """
        except Exception as e:
             # Eğer hata hala 'ascii' ise, bu son denememizdir.
             st.session_state.ai_response = f"## ❌ Bir Hata Olustu: {e}"

# --- 4. SAYFA AYARLARI ---
st.set_page_config(layout="wide", page_title="Yusuf Efe Sahin | Akil Ogretmen")
st.title("🎓 Yusuf Efe Sahin | Yapay Zeka Asistani (Akil Ogretmen)")
st.markdown("---")

# --- 5. ANA SAYFA KODU ---

st.header("❓ Akil Ogretmen'e Sor")
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
