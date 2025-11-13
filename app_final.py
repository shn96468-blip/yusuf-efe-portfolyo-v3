import streamlit as st
import os

# NOT: YouTube API ile ilgili tüm importlar ve tanımlamalar (googleapiclient, YOUTUBE_API_KEY, YOUTUBE_SERVICE) bu versiyondan çıkarılmıştır.

# --- 1. KÜTÜPHANE VE API KURULUMU (Temizlenmiş) ---
# YouTube API bağımlılığı kalmadığı için bu bölüm basitleştirilmiştir.
# Eğer başka kütüphane kullanıyorsanız buraya ekleyebilirsiniz.


# --- 2. İÇERİK TANIMLARI ---
# DİKKAT: Bu değişkenlerin math_content.py, turkish_content.py gibi dosyalarınızda doğru tanımlandığından emin olun.
try:
    # Örnek içerikler (Hata vermemesi için geçici değerler)
    MATH_CONTENT = "## 📘 Matematik Konu Anlatımı Detayı (Modülden Okundu)"
    TURKISH_CONTENT = "## 📝 Türkçe Konu Anlatımı Detayı (Modülden Okundu)"
    SCIENCE_CONTENT = "## 🧪 Fen Konu Anlatımı Detayı (Modülden Okundu)"
    RELIGION_CONTENT = "## 🕌 Din Kültürü Konu Anlatımı Detayı (Modülden Okundu)"
    ENGLISH_CONTENT = "## 🗣️ İngilizce Konu Anlatımı Detayı (Modülden Okundu)"
    SOCIAL_CONTENT = "## 🌍 Sosyal Bilgiler Konu Anlatımı Detayı (Modülden Okundu)"

    MATH_VIDEOS = {"Rasyonel Sayılar": "https://www.youtube.com/watch?v=k-D5xQ6U6fA"}
    TURKISH_VIDEOS = {}
    SCIENCE_VIDEOS = {}
    RELIGION_VIDEOS = {}
    ENGLISH_VIDEOS = {}
    SOCIAL_VIDEOS = {}

except Exception:
    pass 

# --- 3. SESSION STATE (DURUM YÖNETİMİ) ---
if 'content_key' not in st.session_state: st.session_state.content_key = None 
if 'video_key' not in st.session_state: st.session_state.video_key = None 
if 'ai_response' not in st.session_state:
    st.session_state.ai_response = "Konuyu yazın ve Akıl'dan Konu Anlatmasını isteyin. (Örn: Rasyonel, Kütle) VEYA Genel Bir Şey Sorun."
    st.session_state.last_topic = ""

# --- HARİTALAR VE SABİTLER ---
ALL_VIDEOS_MAP = {
    "mat": MATH_VIDEOS, "tr": TURKISH_VIDEOS, "sci": SCIENCE_VIDEOS,
    "soc": SOCIAL_VIDEOS, "eng": ENGLISH_VIDEOS, "rel": RELIGION_VIDEOS,
}
CONTENT_MAP = {
    "mat_konu": MATH_CONTENT, "tr_konu": TURKISH_CONTENT, "sci_konu": SCIENCE_CONTENT, 
    "soc_konu": SOCIAL_CONTENT, "eng_konu": ENGLISH_CONTENT, "rel_konu": RELIGION_CONTENT,
}
COACH_CONTENT = "## 💡 Koç Modülü - Öğrenci Koçluğu ve Rehberlik"


# --- 4. YOUTUBE ARAMA FONKSİYONLARI (Kaldırılmıştır) ---
# Bu kısım kaldırıldığı için fonksiyonlar da silinmiştir.


# --- 5. BUTON VE AI MANTIĞI ---
def toggle_content(key):
    if st.session_state.content_key == key: st.session_state.content_key = None
    else: st.session_state.content_key = key; st.session_state.video_key = None 

def toggle_video(key):
    if st.session_state.video_key == key: st.session_state.video_key = None
    else: st.session_state.video_key = key; st.session_state.content_key = None 

# HATA ÇÖZÜMÜ: Matematik konularını tanıyan mantık güncellenmiştir.
def generate_ai_explanation(topic):
    topic_lower = topic.lower().strip()
    response = ""
    
    # MATEMATİK: ORAN, YÜZDE, CEBİRSEL, vb. kesin tanınır.
    if "rasyonel" in topic_lower or "tam sayı" in topic_lower or "cebirsel" in topic_lower or "oran" in topic_lower or "yüzde" in topic_lower:
        response = f"## 🧠 Akıl Konu Anlatımı: {topic.upper()} (MATEMATİK) 🎉"
        
    elif "fiil" in topic_lower or "ek eylem" in topic_lower or "söz sanatları" in topic_lower:
        response = f"## 💻 Akıl Konu Anlatımı: {topic.upper()} (TÜRKÇE) 🎉"
    
    elif "kütle" in topic_lower or "mitoz" in topic_lower or "mayoz" in topic_lower:
        response = f"## 🧪 Akıl Konu Anlatımı: {topic.upper()} (FEN) 🎉"
    
    else:
        # Sohbet özelliği olmadığı için sadece konuyu anlatamadığı uyarısı verilir.
        response = f"""## ⚠️ Akıl Asistanı Uyarısı: '{topic.upper()}' şu an için anlatabileceğim ana ders konuları arasında değildir."""
        
    st.session_state.ai_response = response
    st.session_state.last_topic = topic

# --- 6. SAYFA AYARLARI ---
st.set_page_config(layout="wide", page_title="Yusuf Efe Şahin | 7. Sınıf Eğitim Portalı")
st.title("👨‍🎓 Yusuf Efe Şahin | 7. Sınıf Eğitim Portalı")
st.markdown("---")

# --- 7. SEKMELERİN TANIMLANMASI ---
tab_coach, tab_math, tab_tr, tab_sci, tab_soc, tab_eng, tab_rel = st.tabs([
    "💡 Koç Modülü", 
    "🔢 Matematik İçerikleri", 
    "📝 Türkçe İçerikleri", 
    "🧪 Fen Bilimleri",
    "🌍 Sosyal Bilgiler",
    "🗣️ İngilizce",
    "🕌 Din Kültürü",
])

# --- 8. DERS SEKMELERİ İÇİN GENEL FONKSİYON ---
def render_subject_tab(tab_context, subject_title, key_prefix):
    konu_key = f"{key_prefix}_konu"; video_key = f"{key_prefix}_video"
    pdf_key = f"{key_prefix}_pdf"; deneme_key = f"{key_prefix}_deneme"
    video_list = ALL_VIDEOS_MAP.get(key_prefix, {})
    
    with tab_context:
        st.header(f"{subject_title} Dersi İçerikleri")
        col_btn1, col_btn2, col_btn3, col_btn4 = st.columns(4) 
        
        with col_btn1:
            button_label = "⬆️ Konuyu Gizle" if st.session_state.content_key == konu_key else "📄 Konu Anlatımı"
            st.button(button_label, type="primary", key=konu_key, on_click=toggle_content, args=(konu_key,)) 
            
        with col_btn2:
            video_button_label = "⬇️ Videoları Gizle" if st.session_state.video_key == video_key else "▶️ Sabit Video İzle"
            st.button(video_button_label, type="secondary", key=video_key, on_click=toggle_video, args=(video_key,))
                      
        with col_btn3: st.button("♦️ PDF Sonuç Kontrol", type="secondary", key=pdf_key)
        with col_btn4: st.button("🔥 Deneme Sınavı", type="secondary", key=deneme_key)
        
        st.markdown("---")
        
        if st.session_state.content_key == konu_key:
            st.subheader(f"✨ {subject_title} Konu Anlatımı Detay") 
            st.markdown(CONTENT_MAP.get(konu_key, "İçerik Bulunamadı."), unsafe_allow_html=True)
            st.markdown("---")
            
        elif st.session_state.video_key == video_key and video_list: 
            st.subheader(f"▶️ {subject_title} Dersi Sabit Video Listesi")
            for topic, url in video_list.items():
                st.markdown(f"**📚 Konu:** {topic}")
                st.video(url, format="video/mp4") 
                st.markdown("---")
            st.caption("Not: Tüm YouTube kanallarında arama özelliği kaldırılmıştır.")
            
        elif st.session_state.video_key == video_key and not video_list:
            st.warning(f"{subject_title} dersi için henüz bir sabit video listesi eklenmemiştir.")
        
        else:
            st.info(f"Yukarıdaki butonlara tıklayarak {subject_title} dersi içeriğini ve sabit videolarını görebilirsiniz.")

# ==============================================================================
# --- 9. KOÇ MODÜLÜ (YOUTUBE ARAMA ALANI KALDIRILDI) ---
# ==============================================================================
with tab_coach: 
    st.header("💡 Koç Modülü - Rehberlik ve Mentorluk")
    
    # YouTube Arama kısmı tamamen kaldırılmıştır.
    st.info("YouTube video arama motoru, uygulama kararlılığı için kaldırılmıştır.")
    st.markdown("---")

    st.subheader("🤖 Yapay Zeka Asistanı (Akıl)")
    
    input_topic = st.text_input(
        "Konu Adını Yazınız (Örn: Rasyonel Sayılar, Söz Sanatları, Mitoz)", 
        value=st.session_state.last_topic, key="topic_input"
    )
    
    st.button(
        "Akıl'dan Konuyu Anlatmasını İsteyin", 
        type="secondary", key="ai_generate",
        on_click=generate_ai_explanation, args=(input_topic,)
    )
    
    st.markdown("---")
    st.markdown(st.session_state.ai_response, unsafe_allow_html=True)
    st.markdown("---") 

    st.header("📝 Çalışma ve Rehberlik İçerikleri")
    col_coach_btn1, col_coach_btn2, col_coach_btn3 = st.columns(3)
    
    with col_coach_btn1: st.button("📝 Çalışma Planı Oluştur", type="secondary", key="coach_plan") 
    with col_coach_btn2: st.button("🧠 Motivasyon Teknikleri", type="secondary", key="coach_motivasyon")
    with col_coach_btn3: st.button("⏰ Pomodoro Zamanlayıcısı", type="secondary", key="coach_pomodoro")
    
    st.markdown("---")
    st.markdown(COACH_CONTENT, unsafe_allow_html=True)


# ==============================================================================
# --- 10. DERS SEKMELERİNİN ÇAĞRILMASI ---
# ==============================================================================
render_subject_tab(tab_math, "🔢 Matematik", "mat")
render_subject_tab(tab_tr, "📝 Türkçe", "tr")
render_subject_tab(tab_sci, "🧪 Fen Bilimleri", "sci")
render_subject_tab(tab_soc, "🌍 Sosyal Bilgiler", "soc")
render_subject_tab(tab_eng, "🗣️ İngilizce", "eng")
render_subject_tab(tab_rel, "🕌 Din Kültürü", "rel")
