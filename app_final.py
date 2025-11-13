import streamlit as st
import os

# --- 1. SABİT İÇERİKLER ---
GOOGLE_LINK_BASLANGIC = "https://www.google.com/search?q="
YOUTUBE_LINK_BASLANGIC = "https://www.youtube.com/results?search_query="

# Soru Çözme linkini olduğu gibi bıraktık.
SORU_COZME_LINK = "https://www.ornek-sorucozme-sitesi.com" 


# --- 2. DERS VE KONU TANIMLARI ---

SUBJECT_MAP = {
    "tr": {
        "title": "📝 Türkçe",
        "topics": ["Fiiller", "Zarflar", "Cümlede Anlam"],
    },
    "mat": {
        "title": "🔢 Matematik",
        "topics": ["Tam Sayılarla İşlemler", "Rasyonel Sayılar", "Cebirsel İfadeler"],
    },
    "sci": {
        "title": "🧪 Fen Bilimleri",
        "topics": ["Güneş Sistemi", "Hücre ve Bölünmeler", "Kuvvet ve Enerji"],
    },
    "soc": {
        "title": "🌍 Sosyal Bilgiler",
        "topics": ["Birey ve Toplum", "Kültür ve Miras", "Bilim ve Teknoloji"],
    }
}


# --- 3. SAYFA AYARLARI ---
st.set_page_config(layout="wide", page_title="Yusuf Efe Şahin | 7. Sınıf Portal")
st.title("👨‍🎓 Yusuf Efe Şahin | 7. Sınıf Ders Portalı")
st.markdown("---")


# --- 4. ARAMA FONKSİYONLARI ---
def get_search_link(query, search_engine):
    """Verilen sorgu için Google veya YouTube arama linki oluşturur."""
    query = f"{query} 7. Sınıf Konu Anlatımı" # Arama sorgusuna sınıf seviyesini ekledik
    query = query.replace(' ', '+') # URL'ye uygun hale getir
    
    if search_engine == "google":
        return f"{GOOGLE_LINK_BASLANGIC}{query}"
    elif search_engine == "youtube":
        return f"{YOUTUBE_LINK_BASLANGIC}{query}"
    return "#"


# --- 5. DERS SEKMELERİNİ ÇİZME VE İÇERİK MANTIĞI ---
def render_subject_tab(tab_context, subject_key):
    subject_data = SUBJECT_MAP[subject_key]
    
    with tab_context:
        st.header(f"✨ {subject_data['title']} Dersi")
        
        # 3 KUTUCUK (Buton) Oluşturma
        col_notes, col_quiz, col_video = st.columns(3)

        # --- A. DERS NOTLARI KUTUCUĞU (GOOGLE ARAMA) ---
        with col_notes:
            st.link_button(
                "📝 Ders Notlarını İnternetten Al", 
                url=get_search_link(subject_data['title'], "google"), 
                type="primary", 
                help=f"Bu buton, Google'da '{subject_data['title']} 7. Sınıf Konu Anlatımı' araması yapar."
            )

        # --- B. SORU ÇÖZME KUTUCUĞU (HARİCİ LİNK) ---
        with col_quiz:
            st.link_button(
                "❓ Soru Çözme / Deneme", 
                url=SORU_COZME_LINK, 
                type="secondary", 
                help="Farklı bir sayfada Soru Çözme Platformunu açar."
            )
        
        # --- C. VİDEO İZLE KUTUCUĞU ---
        with col_video:
            st.link_button(
                "📺 Tüm Videoları Gör", 
                url=get_search_link(subject_data['title'], "youtube"), 
                type="secondary",
                help=f"Bu buton, YouTube'da '{subject_data['title']} 7. Sınıf Konu Anlatımı' araması yapar."
            )
        
        st.markdown("---")
        
        # --- KONULARA GÖRE ÖZEL ARAMA LİNKLERİ ---
        st.subheader("Konulara Göre Hızlı Erişim")
        st.info("Aşağıdaki konulara tıklayarak, doğrudan o konunun ders notlarına veya videolarına ulaşabilirsiniz.")
        
        cols_content = st.columns(3)
        
        for i, topic in enumerate(subject_data['topics']):
            col = cols_content[i % 3]
            
            # Google Arama Linki (Notlar için)
            google_link = get_search_link(topic, "google")
            # YouTube Arama Linki (Videolar için)
            youtube_link = get_search_link(topic, "youtube")
            
            with col:
                st.markdown(f"**📚 {topic}**")
                st.link_button("Notları Google'da Bul", url=google_link, type="primary", key=f"{subject_key}_{topic}_g")
                st.link_button("Videoyu YouTube'da Bul", url=youtube_link, type="secondary", key=f"{subject_key}_{topic}_y")
                st.markdown("---")


# --- 6. SEKMELERİN TANIMLANMASI VE ÇAĞRILMASI ---
tab_math, tab_tr, tab_sci, tab_soc = st.tabs([
    SUBJECT_MAP["mat"]["title"], 
    SUBJECT_MAP["tr"]["title"], 
    SUBJECT_MAP["sci"]["title"],
    SUBJECT_MAP["soc"]["title"]
])

render_subject_tab(tab_math, "mat")
render_subject_tab(tab_tr, "tr")
render_subject_tab(tab_sci, "sci")
render_subject_tab(tab_soc, "soc")
