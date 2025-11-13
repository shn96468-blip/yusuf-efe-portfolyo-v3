import streamlit as st
import os

# --- 1. SABİT İÇERİKLER ---
GOOGLE_LINK_BASLANGIC = "https://www.google.com/search?q="
YOUTUBE_LINK_BASLANGIS = "https://www.youtube.com/results?search_query="

# KRİTİK DEĞİŞİKLİK: Soru çözme linkini doğrudan verilen siteye ayarlıyoruz.
TESTCOZ_ONLINE_LINK = "https://testcoz.online" 


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
    """Verilen sorgu için Google, YouTube veya Test Çöz linki oluşturur."""
    
    if search_engine == "youtube":
        # Video araması: Tonguç'a yönlendir
        search_query = f"{query} tonguç 7. sınıf konu anlatımı"
        link_baslangic = YOUTUBE_LINK_BASLANGIS
    
    elif search_engine == "testcoz_quiz":
        # Soru çözme: TESTCOZ.ONLINE linkini doğrudan döndür
        return TESTCOZ_ONLINE_LINK
    
    else: # Google veya ders notu aramaları için
        search_query = f"{query} 7. Sınıf Konu Anlatımı"
        link_baslangic = GOOGLE_LINK_BASLANGIC
    
    # URL'ye uygun hale getir
    final_query = search_query.replace(' ', '+')
    
    return f"{link_baslangic}{final_query}"


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

        # --- B. SORU ÇÖZME KUTUCUĞU (TESTCOZ.ONLINE) ---
        with col_quiz:
            st.link_button(
                "✅ Test Çöz - Yeni Nesil Sorular", 
                url=get_search_link("", "testcoz_quiz"), 
                type="secondary", 
                help="TESTCOZ.ONLINE sitesinde 7. Sınıf Testlerini ve Yazılı Sorularını açar."
            )
        
        # --- C. VİDEO İZLE KUTUCUĞU (TONGUÇ YOUTUBE ARAMA) ---
        with col_video:
            st.link_button(
                "📺 Tüm Tonguç Videolarını Gör", 
                url=get_search_link(subject_data['title'], "youtube"), 
                type="secondary",
                help=f"Bu buton, YouTube'da '{subject_data['title']} tonguç 7. sınıf konu anlatımı' araması yapar."
            )
        
        st.markdown("---")
        
        # --- KONULARA GÖRE ÖZEL ARAMA LİNKLER
