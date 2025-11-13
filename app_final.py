import streamlit as st
import os

# --- 1. SABİT İÇERİKLER ---
GOOGLE_LINK_BASLANGIC = "https://www.google.com/search?q="
TONGUC_KANAL_LINK = "https://www.youtube.com/@tonguc7"
YOUTUBE_LINK_BASLANGIS = "https://www.youtube.com/results?search_query="

# Test çözme linkini sizin verdiğiniz URL'ye ayarlıyoruz.
TESTCOZ_ONLINE_LINK = "https://www.testcoz.com/" 

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
    """Verilen sorgu için arama linki oluşturur."""
    
    if search_engine == "testcoz_quiz":
        return TESTCOZ_ONLINE_LINK
    
    elif search_engine == "tonguc_kanal":
        return TONGUC_KANAL_LINK

    else: # Google araması (Hızlı Erişim için)
        search_query = f"{query} 7. Sınıf Konu Anlatımı"
        final_query = search_query.replace(' ', '+')
        return f"{GOOGLE_LINK_BASLANGIC}{final_query}"


# --- 5. DERS SEKMELERİNİ ÇİZME VE İÇERİK MANTIĞI ---
def render_subject_tab(tab_context, subject_key):
    subject_data = SUBJECT_MAP[subject_key]
    
    with tab_context:
        st.header(f"✨ {subject_data['title']} Dersi")
        
        # 3 Düğme (Not, Test, Video) Oluşturma
        col_notes, col_quiz, col_video = st.columns(3)

        # --- A. DERS NOTLARI KUTUCUĞU (GOOGLE LİNKİ) ---
        with col_notes:
            st.link_button(
                "📝 Detaylı Ders Notlarını Bul", 
                url=get_search_link(subject_data['title'], "google"),
                type="secondary",
                # KRİTİK: Benzersiz anahtar eklendi
                key=f"notes_{subject_key}",
                help=f"Bu buton, Google'da '{subject_data['title']} 7. Sınıf Konu Anlatımı' araması yapar."
            )
        
        # --- B. SORU ÇÖZME KUTUCUĞU (TESTCOZ.COM DİREKT LİNK) ---
        with col_quiz:
            st.link_button(
                "✅ Test Çöz - Yeni Nesil Sorular", 
                url=get_search_link("", "testcoz_quiz"), 
                type="primary", 
                # KRİTİK: Benzersiz anahtar eklendi
                key=f"quiz_{subject_key}",
                help="Doğrudan testcoz.com sitesini açar."
            )
        
        # --- C. VİDEO İZLE KUTUCUĞU (TONGUÇ KANAL DİREKT LİNK) ---
        with col_video:
            st.link_button(
                "📺 Tonguç Akademi 7. Sınıf Kanalı", 
                url=get_search_link("", "tonguc_kanal"), 
                type="primary",
                # KRİTİK: Benzersiz anahtar eklendi
                key=f"tonguc_{subject_key}",
                help=f"YouTube'da Tonguç Akademi 7. Sınıf kanalını doğrudan açar."
            )
        
        st.markdown("---")
        
        # --- KONULARA GÖRE HIZLI ERİŞİM (GOOGLE ARAMA) ---
        st.subheader("Konulara Göre Hızlı Erişim (Google Arama)")
        st.info("Aşağıdaki konulara tıklayarak, ders notlarını Google'da hızla bulabilirsiniz.")
        
        # Hızlı erişim için 3 düğme
        cols_content = st.columns(3)
        
        for i, topic in enumerate(subject_data.get('topics', [])):
            col = cols_content[i % 3]
            
            # Google Arama Linki
            google_link = get_search_link(topic, "google")
            
            with col:
                st.markdown(f"**📚 {topic}**")
                # KRİTİK: Konu adı ile birleştirilmiş benzersiz anahtar
                st.link_button("Notları Google'da Bul", url=google_link, type="secondary", key=f"topic_{subject_key}_{topic}_g")
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
