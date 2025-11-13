# app_final.py dosyasındaki mevcut generate_ai_explanation fonksiyonunu bu kodla DEĞİŞTİRİN

# --- 5. BUTON VE AI MANTIĞI ---
def toggle_content(key):
    if st.session_state.content_key == key: st.session_state.content_key = None
    else: st.session_state.content_key = key

# AKIL ASİSTANININ SADECE KONUYU DETAYLI ANLATMASI İÇİN GÜNCELLENMİŞ FONKSİYON
def generate_ai_explanation(topic):
    topic_clean = topic.strip().upper()
    response = ""
    
    if topic_clean:
        response = f"""
## 👨‍🏫 Akıl Öğretmen: {topic_clean} Konu Anlatımı ✨
        
### 📚 Detaylı Konu Açıklaması

Sevgili öğrencim, **{topic_clean}** konusu ile ilgili *detaylı ve öğretici* açıklamayı doğrudan bu alana giriniz.

"""
    else:
        response = f"""## ⚠️ Akıl Asistanı Uyarısı: Lütfen bir konu adı veya soru yazınız."""
        
    st.session_state.ai_response = response
    st.session_state.last_topic = topic
