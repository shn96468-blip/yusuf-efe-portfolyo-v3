import streamlit as st
import os

# --- 1. SABİT İÇERİKLER ---
GOOGLE_LINK_BASLANGIC = "https://www.google.com/search?q="
YOUTUBE_LINK_BASLANGIS = "https://www.youtube.com/results?search_query="

# KRİTİK: Test çözme linkini sizin verdiğiniz URL'ye ayarlıyoruz.
TESTCOZ_ONLINE_LINK = "https://www.testcoz.com/" 

# --- 2. DERS VE KONU TANIMLARI (Sadece Matematik tutuldu) ---

SUBJECT_DATA = {
    "key": "mat",
    "title": "🔢 Matematik",
    "topics": ["Tam Sayılarla İşlemler", "Rasyonel Sayılar", "Cebirsel İfadeler"],
}


# --- 3. SAYFA AYARLARI ---

st.set_page_config(layout="wide", page_title="Yusuf Efe Şahin | 7. Sınıf Portal")
st.title("👨‍🎓 Yusuf Efe Şahin | 7. Sınıf Ders Portalı")
st.markdown("---")


# --- 4. ARAMA FONKSİYONLARI ---
def get_search_link(query, search_engine):
    """Verilen sorgu için arama linki oluşturur."""
    
    if search_engine == "testcoz_quiz":
        # TESTCOZ.COM DİREKT LİNKİ
        return TESTCOZ_ONLINE_LINK
    
    elif search_engine == "tonguc_video_search":
        # TONGUÇ 7. SINIF VİDEO ARAMA SORGUSU
        search_query = f"{query} tonguç akademi 7. sınıf konu anlatımı"
        final_query = search_query.replace(' ', '+')
        return f"{YOUTUBE_LINK_BASLANGIS}{final_query}"

    else: # Google araması (Ders Notları veya Hızlı Erişim için)
        search_query = f"{query} 7. Sınıf Konu Anlatımı"
        final_query = search_query.replace(' ', '+')
        return f"{GOOGLE_LINK_BASLANGIC}{final_query}"


# --- 5. MATEMATİK İÇERİĞİNİ DOĞRUDAN YAZDIRMA ---

# Sekme yapısını tamamen kaldırdık. İçerik doğrudan ana sayfada yer alacak.
subject_key = SUBJECT_DATA["key"]
subject_title = SUBJECT_DATA["title"]
subject_topics = SUBJECT_DATA["topics"]

st.header(f"✨ {subject_title} Dersi")

# 3 KUTUCUK (Buton) Oluşturma
col_notes, col_quiz, col_video = st.columns(3)

# --- A. DERS NOTLARI KUTUCUĞU (GOOGLE LİNKİ) ---
with col_notes:
    st.link_button(
        "📝 Detaylı Ders Notlarını Bul", 
        url=get_search_link(subject_title, "google"),
        type="primary", 
        help=f"Bu buton, Google'da '{subject_title} 7. Sınıf Konu Anlatımı' araması yapar."
    )

# --- B. SORU ÇÖZME KUTUCUĞU (TESTCOZ.COM DİREKT LİNK) ---
with col_quiz:
    st.link_button(
        "✅ Test Çöz - Yeni Nesil Sorular", 
        url=get_search_link("", "testcoz_quiz"), 
        type="secondary", 
        help="Doğrudan testcoz.com sitesini açar."
    )

# --- C. VİDEO İZLE KUTUCUĞU (TONGUÇ YOUTUBE ARAMASI) ---
with col_video:
    st.link_button(
        "📺 Tonguç Akademi 7. Sınıf Videoları", 
        url=get_search_link(subject_title, "tonguc_video_search"), 
        type="secondary",
        help=f"YouTube'da '{subject_title} tonguç akademi 7. sınıf konu anlatımı' araması yapar."
    )

st.markdown("---")

# --- KONULARA GÖRE HIZLI ERİŞİM (GOOGLE ARAMA) ---
st.subheader("Konulara Göre Hızlı Erişim (Google Arama)")
st.info("Aşağıdaki konulara tıklayarak, ders notlarını Google'da hızla bulabilirsiniz.")

cols_content = st.columns(3)

for i, topic in enumerate(subject_topics):
    col = cols_content[i % 3]
    
    # Google Arama Linki (Notlar için)
    google_link = get_search_link(topic, "google")
    
    with col:
        st.markdown(f"**📚 {topic}**")
        # Key parametresini direkt konuya eşitledik, bu da stabiliteyi artırır.
        st.link_button("Notları Google'da Bul", url=google_link, type="primary", key=f"{subject_key}_{topic}_g")
        st.markdown("---")
