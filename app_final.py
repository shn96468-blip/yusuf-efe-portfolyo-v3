# app_final.py dosyasındaki mevcut generate_ai_explanation fonksiyonunu bu kodla DEĞİŞTİRİN

# --- 5. BUTON VE AI MANTIĞI ---
def toggle_content(key):
    if st.session_state.content_key == key: st.session_state.content_key = None
    else: st.session_state.content_key = key

# AKIL ASİSTANININ ÖĞRETMEN GİBİ ANLATMASI İÇİN GÜNCELLENMİŞ FONKSİYON
def generate_ai_explanation(topic):
    topic_clean = topic.strip().upper()
    response = ""
    
    if topic_clean:
        response = f"""
## 👨‍🏫 Akıl Öğretmen: {topic_clean} Konusu 🎉
        
### ✨ Öğretmen Açıklaması

Sevgili öğrencim, **{topic_clean}** konusu ile ilgili *detaylı ve öğretici* açıklamayı bu alana girebilirsin. Öğretmen olarak, konuyu anladıktan sonra **mutlaka örnek sorular çözmeni** öneriyorum. 📚

**Unutma:** Başarı, düzenli ve planlı çalışmanın sonucudur!

"""
    else:
        response = f"""## ⚠️ Akıl Asistanı Uyarısı: Lütfen bir konu adı veya soru yazınız."""
        
    st.session_state.ai_response = response
    st.session_state.last_topic = topic
