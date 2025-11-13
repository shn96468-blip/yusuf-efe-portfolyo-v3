import streamlit as st
import os

# --- 1. SABİT İÇERİKLER ---
GOOGLE_LINK_BASLANGIC = "https://www.google.com/search?q="
TONGUC_KANAL_LINK = "https://www.youtube.com/@tonguc7"
TESTCOZ_ONLINE_LINK = "https://www.testcoz.com/" 

# --- 2. DERS VE KONU TANIMLARI (Sadece Türkçe kaldı) ---

SUBJECT_MAP = {
    "tr": {
        "title": "📝 Türkçe",
        "topics": ["Fiiller", "Zarflar", "Cümlede Anlam"],
    }
}


# --- 3. SAYFA AYARLARI ---

# Sayfa başlığını da Türkçe dersine özel yaptık.
st.set_page_config(layout="wide", page_title="Yusuf Efe Şahin | Türkçe Dersi Portalı")
st.title("👨‍🎓 Yusuf Efe Şahin | Türkçe Dersi Portalı")
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

        # A. DERS NOTLARI (GOOGLE LİNKİ) - Benzersiz Anahtar
        with col_notes:
            st.link_button(
                "📝 Detaylı Ders Notlarını Bul", 
                url=get_search_link(subject_data['title'], "google"),
                type="secondary",
                key=f"notes_{subject_key}",
            )
        
        # B. SORU ÇÖZME (TESTCOZ) - Benzersiz Anahtar
        with col_quiz:
            st.link_button(
                "✅ Test Çöz - Yeni Nesil Sorular", 
                url=get_search_link("", "testcoz_quiz"), 
                type="primary", 
                key=f"quiz_{subject_key}",
            )
        
        # C. VİDEO İZLE (TONGUÇ KANAL) - Benzersiz Anahtar
        with col_video:
            st.link_button(
                "📺 Tonguç Akademi 7. Sınıf Kanalı", 
                url=get_search_link("", "tonguc_kanal"), 
                type="primary",
                key=f"tonguc_{subject_key}",
            )
        
        st.markdown("---")
        
        # KONULARA GÖRE HIZLI ERİŞİM (GOOGLE ARAMA)
        st.subheader("Konulara Göre Hızlı Erişim (Google Arama)")
        
        # Konular 3 sütunda gösteriliyor
        cols_content = st.columns(3)
        
        for i, topic in enumerate(subject_data.get('topics', [])):
            col = cols_content[i % 3]
            google_link = get_search_link(topic, "google")
            
            with col:
                st.markdown(f"**📚 {topic}**")
                # Konu adı ile birleştirilmiş benzersiz anahtar
                st.link_button("Notları Google'da Bul", url=google_link, type="secondary", key=f"topic_{subject_key}_{topic}_g")
                st.markdown("---")


# --- 6. SEKMELERİN TANIMLANMASI VE ÇAĞRILMASI (Sadece Türkçe) ---
# Tek bir sekme olduğu için st.tabs'ın döndürdüğü listenin ilk elemanını alıyoruz.
tab_tr = st.tabs([
    SUBJECT_MAP["tr"]["title"]
])[0]

render_subject_tab(tab_tr, "tr")
