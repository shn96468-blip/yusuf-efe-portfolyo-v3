# -*- coding: utf-8 -*-

import streamlit as st
import os
from google import genai
from google.genai.errors import APIError 

# --- 1. KÜTÜPHANE VE API KURULUMU ---

try:
    if 'GEMINI_API_KEY' not in st.secrets:
        # Hata mesajındaki Türkçe karakterleri (ı, ş, ü) sildik.
        st.error("⚠️ GEMINI_API_KEY bulunamadi. Lutfen Streamlit Cloud Secrets paneline ekleyin.")
        st.stop()
    
    client = genai.Client(api_key=st.secrets['GEMINI_API_KEY'])
    MODEL = 'gemini-2.5-flash' 

except Exception as e:
    st.error(f"API Istemcisi Baslatilamadi: {e}")
    st.stop()


# --- 2. SESSION STATE (DURUM YÖNETİMİ) ---
if 'last_question' not in st.session_state: st.session_state.last_question = ""
if 'ai_response' not in st.session_state: st.session_state.ai_response = ""


# --- 3. API ÇAĞRISI FONKSİYONU ---
def generate_answer_with_ai(question):
    """API'den cevap çeken ve Türkçe karakterleri temizleyen fonksiyon."""
    
    # Prompt, 7. sınıf seviyesinde bir cevap ister.
    prompt = f"""
    Sen 7. sinif ogrencilerine ders veren bir Yapay Zeka Asistanisin. Asagidaki soruya detayli ve ogretici bir dille cevap ver:
    SORU: "{question}"
    Cevabini basliklar ve madde isaretleri kullanarak formatla.
    """

    with st.spinner(f"👨‍🏫 Akil Ogretmen, sorunuzu ('{question}') cevapliyor..."):
        try:
            response = client.models.generate_content(
                model=MODEL,
                contents=prompt
            )
            
            # KRİTİK DÜZELTME: Hata veren Türkçe karakterleri silen fonksiyon
            def remove_turkish_chars(text):
                tr_chars = {'ı':'i', 'ğ':'g', 'ü':'u', 'ş':'s', 'ö':'o', 'ç':'c', 'İ':'I', 'Ğ':'G', 'Ü':'U', 'Ş':'S', 'Ö':'O', 'Ç':'C'}
                for tr, en in tr_chars.items():
                    text = text.replace(tr, en)
                # Kalan tüm özel karakterleri ASCII dışı bırakarak hatayı engeller.
                return text.encode('ascii', 'ignore').decode('ascii')
            
            # Temizlenmis metni kullan
            clean_text = remove_turkish_chars(response.text)
            
            st.session_state.ai_response = f"## 📚 AKIL OGRETMEN'DEN CEVAP:\n\n" + clean_text.strip()
            st.session_state.last_question = question

        except APIError as e:
            st.session_state.ai_response = f"""
            ## ❌ API Hatasi
            Yapay Zeka Asistani su an baglanti kuramiyor. Lutfen anahtarinizi kontrol edin. Hata Detayi: {e}
            """
        except Exception as e:
             # Eğer hata hala 'ascii' ise, son deneme basarisiz demektir.
             st.session_state.ai_response = f"## ❌ Bir Hata Olustu: {e}"

# --- 4. SAYFA AYARLARI ---
st.set_page_config(layout="wide", page_title="Yusuf Efe Sahin | Yapay Zeka Asistani")
st.title("🎓 Yusuf Efe Sahin | 7. Sınıf Yapay Zeka Asistanı")
st.markdown("---")

# --- 5. ANA SAYFA KODU ---

st.header("❓ Bana Herhangi Bir Şey Sor")
st.markdown("7. sınıf dersleriyle ilgili bir soru sor (Örn: Rasyonel sayılar nedir?).")

# Soru girişi
question_input = st.text_input(
    label="Sorunuzu Yazınız",
    placeholder="Sorunuz...",
    label_visibility="collapsed"
)

# Buton
if st.button("Cevap Ver", type="primary"):
    if question_input:
        generate_answer_with_ai(question_input)
    else:
        st.warning("Lutfen bir soru yaziniz.")

st.markdown("---")

# Sonuç alanı
if st.session_state.ai_response:
    st.markdown(st.session_state.ai_response, unsafe_allow_html=True)
else:
    st.info("Cevabi gormek icin yukariya bir soru yazip butona tiklayin.")
