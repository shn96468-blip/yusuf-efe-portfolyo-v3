# app_final.py dosyasındaki mevcut generate_ai_explanation fonksiyonunu bu kodla DEĞİŞTİRİN

# --- 5. BUTON VE AI MANTIĞI ---
def toggle_content(key):
    if st.session_state.content_key == key: st.session_state.content_key = None
    else: st.session_state.content_key = key

# AKIL ASİSTANININ HER SORUYA CEVAP VERMESİ İÇİN GÜNCELLENMİŞ FONKSİYON
def generate_ai_explanation(topic):
    topic_clean = topic.strip().upper()
    response = ""
    
    if topic_clean:
        # Konu tanıma kontrolü kaldırıldı. Her konuya genel bir başlık verilecek.
        response = f"""
## 💻 Akıl Konu Anlatımı: {topic_clean} 🎉
        
### 💡 Konu Açıklaması

Bu alana, {topic_clean} konusuyla ilgili detaylı yapay zeka tarafından üretilmiş açıklama gelecektir. Lütfen buraya manuel olarak Akıl Asistanı'nın cevabını girin.

Örn: 'Rasyonel Sayılar, iki tam sayının birbirine oranı şeklinde yazılabilen sayılardır...'

"""
    else:
        response = f"""## ⚠️ Akıl Asistanı Uyarısı: Lütfen bir konu adı veya soru yazınız."""
        
    st.session_state.ai_response = response
    st.session_state.last_topic = topic
