import streamlit as st
import os

# HATA ÇÖZÜMÜ: Gerekli kütüphaneler doğruca tanımlanmalı
try:
    # Bu kütüphane YouTube API ile konuşmak için GEREKLİDİR
    from googleapiclient.discovery import build 
except ImportError:
    st.warning("Gerekli 'google-api-python-client' kütüphanesi bulunamadı. Lütfen 'requirements.txt' dosyasını kontrol edin ve yükleyin.")
    build = None

# --- 1. API AYARLARI ---
# BURAYI KENDİ ALDIĞINIZ YOUTUBE API ANAHTARINIZ İLE DEĞİŞTİRİN
YOUTUBE_API_KEY = "BURAYA_ALDIĞINIZ_YOUTUBE_API_ANAHTARINI_YAZIN" 

YOUTUBE_SERVICE = None
if build:
    try:
        # API anahtarı boş değilse servisi başlat
        if YOUTUBE_API_KEY and YOUTUBE_API_KEY != "BURAYA_ALDIĞINIZ_YOUTUBE_API_ANAHTARINI_YAZIN":
            YOUTUBE_SERVICE = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)
        else:
            # API anahtarı ayarlanmadıysa uyarı ver
            st.info("YouTube API Anahtarı AYARLANMADI. YouTube arama özelliği çalışmayacaktır.")
    except Exception:
        st.error("YouTube servisi başlatılırken bir hata oluştu. API kotanızı kontrol edin.")
        YOUTUBE_SERVICE = None

# --- 2. STREAMLIT DURUM YÖNETİMİ (Session State) ---
if 'content_key' not in st.session_state:
    st.session_state.content_key = None 
if 'video_key' not in st.session_state: 
    st.session_state.video_key = None 
if 'ai_response' not in st.session_state:
    st.session_state.ai_response = "Konuyu yazın ve Akıl'dan Konu Anlatmasını isteyin. (Örn: Rasyonel, Kütle) VEYA Genel Bir Şey Sorun."
    st.session_state.last_topic = ""
if 'youtube_search_query' not in st.session_state:
    st.session_state.youtube_search_query = ""
if 'search_results_youtube' not in st.session_state:
    st.session_state.search_results_youtube = None

# --- 3. MODÜLER İÇERİKLERİ İÇE AKTARMA (Örnek Data) ---
# DİKKAT: Bu kısmı kendi modül dosyalarınıza göre düzenlemelisiniz.
try:
    # Bu değişkenlerin modüler dosyalarınızda (math_content.py vb.) tanımlandığını varsayıyoruz
    # Eğer bu değişkenler tanımlı değilse, uygulamanızda "İçerik Bulunamadı" hatası alırsınız.
    
    # Örnek İçerikler (Eğer modülleriniz çalışmıyorsa bunları kullanabilirsiniz):
    MATH_CONTENT = "## 📘 Matematik Konu Anlatımı ve Özet"
    TURKISH_CONTENT = "## 📝 Türkçe Konu Anlatımı ve Özet"
    SCIENCE_CONTENT = "## 🧪 Fen Konu Anlatımı ve Özet"
    RELIGION_CONTENT = "## 🕌 Din Kültürü Konu Anlatımı ve Özet"
    ENGLISH_CONTENT = "## 🗣️ İngilizce Konu Anlatımı ve Özet"
    SOCIAL_CONTENT = "## 🌍 Sosyal Bilgiler Konu Anlatımı ve Özet"

    MATH_VIDEOS = {"Rasyonel Sayılar": "https://www.youtube.com/watch?v=k-D5xQ6U6fA"}
    TURKISH_VIDEOS = {"Fiiller": "https://www.youtube.com/watch?v=iM0E8uA_4kM"}
    SCIENCE_VIDEOS = {"Mitoz Bölünme": "https://www.youtube.com/watch?v=Kz6pZ7kH3qQ"}
    ENGLISH_VIDEOS = {}
    RELIGION_VIDEOS = {}
    SOCIAL_VIDEOS = {}

except Exception:
    pass # Hata olsa bile uygulama çökmeyecek şekilde ayarladık

# --- 4. SABİT LİNK HARİTALARI ---
ALL_VIDEOS_MAP = {
    "mat": MATH_VIDEOS, "tr": TURKISH_VIDEOS, "sci": SCIENCE_VIDEOS,
    "soc": SOCIAL_VIDEOS, "eng": ENGLISH_VIDEOS, "rel": RELIGION_VIDEOS,
}
CONTENT_MAP = {
    "mat_konu": MATH_CONTENT, "tr_konu": TURKISH_CONTENT, "sci_konu": SCIENCE_CONTENT, 
    "soc_konu": SOCIAL_CONTENT, "eng_konu": ENGLISH_CONTENT, "rel_konu": RELIGION_CONTENT,
}
COACH_CONTENT = """
## 💡 Koç Modülü - Öğrenci Koçluğu ve Rehberlik
* **Zaman Yönetimi:** Günlük rutin oluşturma.
"""

# --- 5. YENİ İŞLEV: GERÇEK YOUTUBE ARAMASI ---
def search_youtube_videos(query, max_results=5):
    """YouTube API'yi kullanarak video araması yapar."""
    if not YOUTUBE_SERVICE:
        return None 
        
    try:
        search_response = YOUTUBE_SERVICE.search().list(
            q=query + " ders konu anlatımı",
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
        st.error(f"YouTube Arama Hatası: API kotanız bitmiş olabilir veya anahtarınız yanlış. Detay: {e}")
        return None

def perform_youtube_search():
    """Arama çubuğundaki terimle YouTube'da arama yapar ve sonuçları kaydeder."""
    query = st.session_state.youtube_search_query
    
    if not query:
        st.session_state.search_results_youtube = []
        return

    results = search_youtube_videos(query, max_results=5) 
    st.session_state.search_results_youtube = results

# --- 6. BUTON TIKLAMA İŞLEVLERİ ve AI MANTIĞI ---

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

# YAPAY ZEKANIN KISALTILMIŞ KONU ANLATIM FONKSİYONU
def generate_ai_explanation(topic):
    topic_lower = topic.lower().strip()
    response = ""
    # Sizin istediğiniz tüm konu eşleştirmeleri buraya eklendi (Görüntülere göre)
    if "rasyonel" in topic_lower or "tam sayı" in topic_lower or "cebirsel" in topic_lower or "oran" in topic_lower or "yüzde" in topic_lower:
        response = f"## 🧠 Akıl Konu Anlatımı: {topic.upper()} (MATEMATİK)"
    elif "fiil" in topic_lower or "ek eylem" in topic_lower or "söz sanatları" in topic_lower:
        response = f"## 💻 Akıl Konu Anlatımı: {topic.upper()} (TÜRKÇE)"
    elif "kütle" in topic_lower or "mitoz" in topic_lower or "mayoz" in topic_lower:
        response = f"## 🧪 Akıl Konu Anlatımı: {topic.upper()} (FEN)"
    
    else:
        response = f"""
        ## ⚠️ Akıl Asistan Uyarısı
        '{topic.upper()}' şu an için anlatabileceğim ana ders konuları arasında değildir. 
        """
        
    st.session_state.ai_response = response
    st.session_state.last_topic = topic


# --- 7. STREAMLIT SAYFA AYARLARI ---
st.set_page_config(layout="wide", page_title="Yusuf Efe Şahin | 7. Sınıf Eğitim Portalı")
st.title("👨‍🎓 Yusuf Efe Şahin | 7. Sınıf Eğitim Portalı")
st.markdown("---")

# 8. SEKMELERİN TANIMLANMASI (NameError'ı çözen kısım)
tab_coach, tab_math, tab_tr, tab_sci, tab_soc, tab_eng, tab_rel = st.tabs([
    "💡 Koç Modülü", 
    "🔢 Matematik İçerikleri", 
    "📝 Türkçe İçerikleri", 
    "🧪 Fen Bilimleri",
    "🌍 Sosyal Bilgiler",
    "🗣️ İngilizce",
    "🕌 Din Kültürü",
])

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
            btn_type = "secondary" # Sabit videoları öne çıkarmıyoruz
            st.button(video_button_label, type=btn_type, key=video_key,
                      on_click=toggle_video, args=(video_key,))
                      
        with col_btn3:
            st.button("♦️ PDF Sonuç Kontrol", type="secondary", key=pdf_key)
        with col_btn4:
            st.button("🔥 Deneme Sınavı", type="secondary", key=deneme_key)
        
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
            
            st.caption("Not: Bu listedeki videolar önceden belirlenmiştir. Tüm YouTube kanallarında arama yapmak için Koç Modülü'ne gidin.")
            
        elif st.session_state.video_key == video_key and not video_list:
            st.warning(f"{subject_title} dersi için henüz bir sabit video listesi eklenmemiştir.")
        
        else:
            st.info(f"Yukarıdaki butonlara tıklayarak {subject_title} dersi içeriğini ve sabit videolarını görebilirsiniz.")

# ==============================================================================
# --- 9. TAB 0: KOÇ MODÜLÜ (YouTube Arama Alanı) ---
# ==============================================================================
with tab_coach: 
    st.header("💡 Koç Modülü - Rehberlik ve Mentorluk")
    
    # ----------------------------------------------------
    # GERÇEK YOUTUBE ARAMA ALANI
    # ----------------------------------------------------
    st.subheader("📺 Ders Videosu Ara (Tüm YouTube Kanalları)")
    
    if not YOUTUBE_SERVICE:
         st.warning("YouTube Arama Motoru şu anda devre dışı. Lütfen API anahtarınızı kodda doğru ayarlayın.")
    else:
        col_search, col_button = st.columns([4, 1])
        
        with col_search:
            st.text_input(
                "YouTube'da ders videosu arayın (Örn: Rasyonel sayılar konu anlatımı)",
                key="youtube_search_query", 
                placeholder="Arama terimini buraya girin...",
            )
        with col_button:
            st.markdown("<br>", unsafe_allow_html=True)
            st.button("YouTube Ara", type="primary", on_click=perform_youtube_search)

        # ARAMA SONUÇLARINI GÖSTERME
        if st.session_state.search_results_youtube is not None:
            if st.session_state.search_results_youtube:
                st.success(f"'{st.session_state.youtube_search_query}' için {len(st.session_state.search_results_youtube)} sonuç bulundu:")
                st.markdown("---")
                
                for video in st.session_state.search_results_youtube:
                    st.subheader(video['title'])
                    col_thumb, col_player = st.columns([1, 2])
                    with col_thumb:
                        st.image(video['thumbnail'], caption="Küçük Resim")
                    with col_player:
                        st.video(video['url'], format="video/mp4") 
                    st.markdown(f"**Link:** [YouTube'da Aç]({video['url']})")
                    st.markdown("---")
            else:
                st.warning(f"'{st.session_state.youtube_search_query}' terimiyle eşleşen bir video bulunamadı.")
            
    st.markdown("---")
    # ----------------------------------------------------

    st.subheader("🤖 Yapay Zeka Asistanı (Akıl)")
    
    input_topic = st.text_input(
        "Konu Adını Yazınız (Örn: Rasyonel Sayılar, Söz Sanatları, Mitoz)", 
        value=st.session_state.last_topic,
        key="topic_input"
    )
    
    ai_button = st.button(
        "Akıl'dan Konuyu Anlatmasını İsteyin", 
        type="secondary", 
        key="ai_generate",
        on_click=generate_ai_explanation,
        args=(input_topic,)
    )
    
    st.markdown("---")
    st.markdown(st.session_state.ai_response, unsafe_allow_html=True)
    st.markdown("---") 

    st.header("📝 Çalışma ve Rehberlik İçerikleri")
    col_coach_btn1, col_coach_btn2, col_coach_btn3 = st.columns(3)
    
    with col_coach_btn1:
        st.button("📝 Çalışma Planı Oluştur", type="secondary", key="coach_plan") 
    with col_coach_btn2:
        st.button("🧠 Motivasyon Teknikleri", type="secondary", key="coach_motivasyon")
    with col_coach_btn3:
        st.button("⏰ Pomodoro Zamanlayıcısı", type="secondary", key="coach_pomodoro")
    
    st.markdown("---")
    st.markdown(COACH_CONTENT, unsafe_allow_html=True)


# ==============================================================================
# --- 10. DERS SEKMELERİNİN ÇAĞRILMASI (Tüm Dersler) ---
# ==============================================================================
render_subject_tab(tab_math, "🔢 Matematik", "mat")
render_subject_tab(tab_tr, "📝 Türkçe", "tr")
render_subject_tab(tab_sci, "🧪 Fen Bilimleri", "sci")
render_subject_tab(tab_soc, "🌍 Sosyal Bilgiler", "soc")
render_subject_tab(tab_eng, "🗣️ İngilizce", "eng")
render_subject_tab(tab_rel, "🕌 Din Kültürü", "rel")
