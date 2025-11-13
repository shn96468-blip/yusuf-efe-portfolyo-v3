# -*- coding: utf-8 -*-
import streamlit as st
import os
from google import genai
from google.genai.errors import APIError 

# ... (API kurulum kodları) ... 

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

        # ... (Hata yönetim kodları) ... 

# ... (Sayfa kodunun geri kalanı) ...
