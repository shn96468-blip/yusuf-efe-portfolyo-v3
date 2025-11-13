import streamlit as st
# HATA ÇÖZÜMÜ: Gerekli kütüphaneler doğruca tanımlanmalı
try:
    from googleapiclient.discovery import build 
except ImportError:
    st.error("Gerekli 'google-api-python-client' kütüphanesi bulunamadı. Lütfen 'requirements.txt' dosyasını kontrol edin ve kütüphaneyi kurun.")
    build = None # Hata durumunda build'i None yapıyoruz

# --- API AYARLARI ---
# BURAYI KENDİ ALDIĞINIZ YOUTUBE API ANAHTARINIZ İLE DEĞİŞTİRİN
YOUTUBE_API_KEY = "BURAYA_ALDIĞINIZ_YOUTUBE_API_ANAHTARINI_YAZIN" 

if build:
    try:
        YOUTUBE_SERVICE = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)
    except Exception:
        st.warning("YouTube servisi başlatılamadı. API anahtarınızı kontrol edin.")
        YOUTUBE_SERVICE = None
else:
    YOUTUBE_SERVICE = None

# --- 1. STREAMLIT DURUM YÖNETİMİ (Session State) ---
if 'content_key' not in st.session_state:
    st.session_state.content_key = None 
if 'video_key' not in st.session_state: 
    st.session_state.video_key = None 

# AI asistanı (Akıl) için durum yönetimi.
if 'ai_response' not in st.session_state:
    st.session_state.ai_response = "Konuyu yazın ve Akıl'dan Konu Anlatmasını isteyin. (Örn: Rasyonel, Kütle) VEYA Genel Bir Şey Sorun."
    st.session_state.last_topic = ""
    
# YouTube Arama Durumu
if 'youtube_search_query' not in st.session_state:
    st.session_state.youtube_search_query = ""
if 'search_results_youtube' not in st.session_state:
    st.session_state.search_results_youtube = None

# --- VİDEO URL TANIMLARI (Dersler İçin Sabit Linkler) ---
# ... (Önceki kodunuzdaki tüm ders videoları buraya kopyalanmalıdır) ...
MATH_VIDEOS = {
    "Rasyonel Sayılar": "https://www.youtube.com/watch?v=k-D5xQ6U6fA",
    "Tam Sayılarla İşlemler": "https://www.youtube.com/watch?v=J3-gC-B0zV8",
    "Cebirsel İfadeler": "https://www.youtube.com/watch?v=e_n0WvU7N0Q",
}
TURKISH_VIDEOS = {
    "Fiiller ve Ek Fiil": "https://www.youtube.com/watch?v=iM0E8uA_4kM",
    "Söz Sanatları": "https://www.youtube.com/watch?v=Xz7K9qN7fEw",
}
# Diğer derslerin video sözlükleri buraya kopyalanmalı

ALL_VIDEOS_MAP = {
    "mat": MATH_VIDEOS,
    "tr": TURKISH_VIDEOS,
    # Diğer derslerin kısaltmaları ve video sözlükleri buraya eklenmeli
}

# --- YENİ İŞLEV: GERÇEK YOUTUBE ARAMASI ---
def search_youtube_videos(query, max_results=5):
    """YouTube API'yi kullanarak video araması yapar."""
    if not YOUTUBE_SERVICE:
        return None # Servis yoksa arama yapma
        
    try:
        search_response = YOUTUBE_SERVICE.search().list(
            q=query,
            part='snippet',
            type='video',
            maxResults=max_results
        ).execute()

        videos = []
        for item in search_response.get('items', []):
            videos.append({
                'title': item['snippet']['title'],
                'video_id': item['id']['videoId'],
                'url': f"https://www.youtube.com/watch?v={item['id']['videoId']}",
                'thumbnail': item['snippet']['thumbnails']['default']['url']
            })
        return videos
        
    except Exception as e:
        # API hatasını terminalde göstermek için st.error kullanıyoruz
        st.error(f"YouTube Arama Hatası: API Anahtarınızı kontrol edin (veya kotanız bitmiş olabilir). Detay: {e}")
        return None

def perform_youtube_search():
    """Arama çubuğundaki terimle YouTube'da arama yapar ve sonuçları kaydeder."""
    query = st.session_state.youtube_search_query
    
    if not query:
        st.session_state.search_results_youtube = []
        return

    results = search_youtube_videos(query, max_results=5) 
    st.session_state.search_results_youtube = results

# --- BUTON TIKLAMA İŞLEVLERİ (Aynı Kaldı) ---

def toggle_content(key):
    if st.session_state.content_key == key:
        st.session_state.content_key = None
    else:
        st.session_state.content_key = key
        st.session_state.video_key = None 

def toggle_video(key):
    if st.session_state.video_key == key:
        st.session_state.video_key = None
    else:
        st.session_state.video_key = key
        st.session_state.content_key = None 

# YAPAY ZEKANIN ÇOK UZUN OLDUĞU İÇİN BURADA KISALTILMIŞ HALİ VARDIR.
def generate_ai_explanation(topic):
    topic_lower = topic.lower().strip()
    response = ""

    if "rasyonel" in topic_lower:
        response = """
        ## 🧠 Akıl Konu Anlatımı: Rasyonel Sayılar
        Rasyonel sayılar, a/b şeklinde yazılabilen sayılar kümesidir.
        ***💡 İpucu:*** Bu konuyla ilgili sabit videolar için **"Matematik İçerikleri"** sekmesine gidin. YouTube'da arama yapmak için yukarıdaki arama çubuğunu kullanın!
        """
    # ... (Diğer tüm ders konu anlatım kodları buraya kopyalanmalı) ...
    
    # Genel Sohbet Alanı
    else:
        response = f"## 💬 Genel Bilgi Modülü (Sohbet): '{topic}'. Ders konuları dışındaki sorularınız için Akıl Asistanı size genel yanıtlar verebilir."
        
    st.session_state.ai_response = response
    st.session_state.last_topic = topic

# --- 2. TÜM İÇERİKLERİN TANIMI (Kısaltılmış) ---
COACH_CONTENT = """
## 💡 Koç Modülü - Öğrenci Koçluğu ve Rehberlik
### 🗓️ Rehberlik Konuları
* **Zaman Yönetimi:** Günlük rutin oluşturma.
"""
MATH_CONTENT = "## 📘 Matematik - Konu Anlatımı ve Özet: Tam Sayılar, Rasyonel Sayılar..."
TURKISH_CONTENT = "## 📝 Türkçe - Konu Anlatımı ve Özet: Fiiller, Söz Sanatları..."
SCIENCE_CONTENT = "## 🧪 Fen Bilimleri - Konu Anlatımı ve Özet: Hücre, Kuvvet, Saf Madde..."
SOCIAL_CONTENT = "## 🌍 Sosyal Bilgiler - Konu Anlatımı ve Özet: Birey, Kültür, Üretim..."
ENGLISH_CONTENT = "## 🗣️ İngilizce - Konu Anlatımı ve Özet: Appearance, Personality, Sports..."
RELIGION_CONTENT = "## 🕌 Din Kültürü ve Ahlak Bilgisi - Konu Anlatımı ve Özet: Melekler, Hac, Ahlak..."

CONTENT_MAP = {
    "mat_konu": MATH_CONTENT, "tr_konu": TURKISH_CONTENT, "sci_konu": SCIENCE_CONTENT, 
    "soc_konu": SOCIAL_CONTENT, "eng_konu": ENGLISH_CONTENT, "rel_konu": RELIGION_CONTENT,
}

# --- 3. STREAMLIT SAYFA AYARLARI ---
st.set_page_config(layout="wide", page_title="Yusuf Efe Şahin | 7. Sınıf Eğitim Portalı")
st.title("👨‍🎓 Yusuf Efe Şahin | 7. Sınıf Eğitim Portalı")
st.markdown("---")

# 4. SEKMELERİN TANIMLANMASI (NameError çözümü için doğru sıralama ve tanım)
tab_coach, tab_math, tab_tr, tab_sci, tab_soc, tab_eng, tab_rel = st.tabs([
    "💡 Koç Modülü", 
    "🔢 Matematik İçerikleri", 
    "📝 Türkçe İçerikleri", 
    "🧪 Fen Bilimleri",
    "🌍 Sosyal Bilgiler",
    "🗣️ İngilizce",
    "🕌 Din Kültürü",
]) # <<< NameError çözümü: Tüm sekmeler burada doğru ve eksiksiz tanımlanmıştır.

# --- DERS SEKMELERİ İÇİN GENEL FONKSİYON ---
def render_subject_tab(tab_context, subject_title, key_prefix):
    """Her ders sekmesini tek bir yapıda oluşturur."""
    
    konu_key = f"{key_prefix}_konu"
    video_key = f"{key_prefix}_video"
    pdf_key = f"{key_prefix}_pdf"
    deneme_key = f"{key_prefix}_deneme"
    
    video_list = ALL_VIDEOS_MAP.get(key_prefix, {})
    
    with tab_context:
        st.header(f"{subject_title} Dersi İçerikleri")
        col_btn1, col_btn2, col_btn3, col_btn4 = st.columns(4) 
        
        with col_btn1:
            button_label = "⬆️ Konuyu Gizle" if st.session_state.content_key == konu_key else "📄 Konu Anlatımı"
            st.button(button_label, type="primary", key=konu_key,
                      on_click=toggle_content, args=(konu_key,)) 
            
        with col_btn2:
            video_button_label = "⬇️ Videoları Gizle" if st.session_state.video_key == video_key else "▶️ Sabit Video İzle"
            btn_type = "primary" if video_list else "secondary" 
            st.button(video_button_label, type=btn_type, key=video_key,
                      on_click=toggle_video, args=(video_key,))
                      
        with col_btn3:
            st.button("♦️ PDF Sonuç Kontrol", type="secondary", key=pdf_key)
        with col_btn4:
            st.button("🔥 Deneme Sınavı", type="secondary", key=deneme_key)
        
        st.markdown("---")
        
        if st.session_state.content_key == konu_key:
            st.subheader(f
