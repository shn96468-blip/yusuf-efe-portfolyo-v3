import streamlit as st
# Google API kütüphanesini buraya ekleyeceğiz
from googleapiclient.discovery import build # <--- Gerekli Kütüphane

# API anahtarınızı buraya yapıştırmalısınız
YOUTUBE_API_KEY = "BURAYA_ALDIĞINIZ_YOUTUBE_API_ANAHTARINI_YAZIN"
# Servisi başlatıyoruz
YOUTUBE_SERVICE = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY) 

# --- GEREKLİ YENİ FONKSİYON ---
def search_youtube_videos(query, max_results=5):
    """YouTube API'yi kullanarak video araması yapar."""
    try:
        # YouTube Arama İsteği
        search_response = YOUTUBE_SERVICE.search().list(
            q=query,
            part='snippet',
            type='video', # Sadece video sonuçlarını getir
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
        st.error(f"YouTube Arama Hatası: API anahtarınızı kontrol edin veya günlük kotanız bitmiş olabilir. Hata: {e}")
        return None

# --- YENİ ARAMA İŞLEVİ ---
def perform_youtube_search():
    """Arama çubuğundaki terimle YouTube'da arama yapar ve sonuçları kaydeder."""
    query = st.session_state.youtube_search_query
    
    if not query:
        st.session_state.search_results_youtube = None
        return

    # YouTube API'sini kullanarak gerçek arama yap
    results = search_youtube_videos(query, max_results=5) # 5 sonuç getirsin
    st.session_state.search_results_youtube = results

# --- DURUM YÖNETİMİ GÜNCELLEMELERİ ---
if 'youtube_search_query' not in st.session_state:
    st.session_state.youtube_search_query = ""
if 'search_results_youtube' not in st.session_state:
    st.session_state.search_results_youtube = None
    
# ... (toggle_content, toggle_video, generate_ai_explanation gibi diğer tüm fonksiyonlar burada kalacak) ...

# ... (Tüm ders içerikleri ve diğer sabitler burada kalacak) ...


# ==============================================================================
# --- 5. TAB 0: KOÇ MODÜLÜ (YouTube Arama Alanı) ---
# ==============================================================================
with tab_coach:
    st.header("💡 Koç Modülü - Rehberlik ve Mentorluk")
    
    # ----------------------------------------------------
    # GERÇEK YOUTUBE ARAMA ALANI (YENİ VE GÜNCELLENMİŞ)
    # ----------------------------------------------------
    st.subheader("📺 Ders Videosu Ara (YouTube Desteği)")
    col_search, col_button = st.columns([4, 1])
    
    with col_search:
        st.text_input(
            "YouTube'da ders videosu arayın (Örn: Rasyonel sayılar konu anlatımı)",
            key="youtube_search_query", # Yeni anahtar
            placeholder="Arama terimini buraya girin...",
        )
    with col_button:
        st.markdown("<br>", unsafe_allow_html=True)
        # Gerçek arama fonksiyonunu çağırıyoruz
        st.button("YouTube Ara", type="primary", on_click=perform_youtube_search)

    # ARAMA SONUÇLARINI GÖSTERME
    if st.session_state.search_results_youtube is not None:
        if st.session_state.search_results_youtube:
            st.success(f"'{st.session_state.youtube_search_query}' için {len(st.session_state.search_results_youtube)} sonuç bulundu:")
            st.markdown("---")
            
            # Her bir sonucu döngü ile göster
            for video in st.session_state.search_results_youtube:
                st.subheader(video['title'])
                
                # Küçük resmi ve video oynatıcısını yan yana gösterelim
                col_thumb, col_player = st.columns([1, 2])
                with col_thumb:
                    st.image(video['thumbnail'], caption="Küçük Resim")
                with col_player:
                    # Video ID'sini kullanarak st.video ile oynat
                    # Not: st.video, video URL'si yerine direkt ID ile çalışmak daha güvenilir olabilir.
                    st.video(video['url'], format="video/mp4") 
                
                # Video linkini de ekleyelim
                st.markdown(f"**Link:** [YouTube'da Aç]({video['url']})")
                st.markdown("---")
        else:
            st.warning(f"'{st.session_state.youtube_search_query}' terimiyle eşleşen bir video bulunamadı.")
            
    st.markdown("---")
    # ----------------------------------------------------

    st.subheader("🤖 Yapay Zeka Asistanı (Akıl)")
    # ... (Akıl Asistanı kodunun geri kalanı) ...


# ... (Diğer tüm ders sekmeleri burada kalacak) ...
