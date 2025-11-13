import streamlit as st
import os

# --- 1. SABİT İÇERİKLER (APISIZ VE STABIL) ---
GOOGLE_LINK_BASLANGIC = "https://www.google.com/search?q="
TONGUC_CHANNEL_LINK = "https://www.youtube.com/@tongucakademi" 

# TEST ÇÖZME İÇİN GÜVENİLİR ARAMA SORGUSU (Google'da TESTCOZ'u arasın)
TESTCOZ_SEARCH_QUERY = "testcoz.online 7. sınıf test çöz" 

# --- KRİTİK MANUEL İÇERİK BÖLÜMÜ ---
# LÜTFEN İÇERİKLERİ AŞAĞIDAKİ ALANLARA YAPIŞTIRIN!

# Not: Matematik notları örneği düzeltildi ve temizlendi.
MATH_NOTES = """
## 📘 7. Sınıf Matematik Ana Konu Anlatımı

### Tam Sayılarla Toplama ve Çıkarma İşlemi
* Pozitif iki tam sayı toplanırken sayıların işareti dikkate alınmadan toplanır. Sonuca artı (+) işareti yazılır. Örn: (+5) + (+2) = (+7)
* Negatif iki tam sayı toplanırken sayılar, işaretler dikkate alınmadan toplanır. Sonuca (-) işareti yazılır. Örn: (-5) + (-2) = (-7)
* Ters (zıt) işaretli iki tam sayı toplanırken... (Lütfen geri kalan içeriği buradan devam ettirin)
"""

TURKISH_NOTES = """
## 📝 Türkçe Ders Notları (Lütfen burayı doldurun)
Buraya, Fiiller, Zarflar, Cümlede Anlam gibi konularınızın detaylı notlarını yazın.
"""
SCIENCE_NOTES = """
## 🧪 Fen Bilimleri Ders Notları (Lütfen burayı doldurun)
Buraya, Güneş Sistemi, Hücre ve Bölünmeler, Kuvvet ve Enerji konularınızın detaylı notlarını yazın.
"""
SOCIAL_NOTES = """
## 🌍 Sosyal Bilgiler Ders Notları (Lütfen burayı doldurun)
Buraya, Birey ve Toplum, Kültür ve Miras gibi konularınızın detaylı notlarını yazın.
"""

NOTES_MAP = {
    "mat": MATH_NOTES,
    "tr": TURKISH_NOTES,
    "sci": SCIENCE_NOTES,
    "soc": SOCIAL_NOTES,
}


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


# --- 3. SESSION STATE VE SAYFA AYARLARI ---
# Not: Hata çözümü için st.session_state'in kontrolü baştan yapılıyor.
if 'active_content' not in st.session_state: st.session_state.active_content = None 

st.set_page_config(layout="wide", page_title="Yusuf Efe Şahin | 7. Sınıf Portal")
st.title("👨‍🎓 Yusuf Efe Şahin | 7. Sınıf Ders Portalı")
st.markdown("---")

def set_active_content(content_type):
    # Bu fonksiyon, tıklandığında içeriği açıp kapamaya yarar.
    if st.session_state.active_content == content_type: st.session_state.active_content = None
    else: st.session_state.active_content = content_type


# --- 4. ARAMA FONKSİYONLARI ---
def get_search_link(query, search_engine):
    """Verilen sorgu için arama linki oluşturur."""
    
    if search_engine == "testcoz_quiz":
        # TESTCOZ.ONLINE için Google Arama linki
        query = TESTCOZ_SEARCH_QUERY.replace(' ', '+')
        return f"{GOOGLE_LINK_BASLANGIC}{query}"
    
    elif search_engine == "tonguc_channel":
        # TONGUÇ KANAL LİNKİ
        return TONGUC_CHANNEL_LINK

    else: # Google araması (Hızlı Erişim/Notlar için)
        search_query = f"{query} 7. Sınıf Konu Anlatımı"
        final_query = search_query.replace(' ', '+')
        return f"{GOOGLE_LINK_BASLANGIC}{final_query}"


# --- 5. DERS SEKMELERİNİ ÇİZME VE İÇERİK MANTIĞI ---
def render_subject_tab(tab_context, subject_key):
    subject_data = SUBJECT_MAP[subject_key]
    
    with tab_context:
        st.header(f"✨ {subject_data['title']} Dersi")
        
        # 3 KUTUCUK (Buton) Oluşturma
        col_notes, col_quiz, col_video = st.columns(3)
        notes_key = f"{subject_key}_notes"

        # --- A. DERS NOTLARI KUTUCUĞU (MANUEL İÇERİK GÖSTERİMİ) ---
        with col_notes:
            notes_button_label = "⬆️ Notları Kapat" if st.session_state.active_content == notes_key else "📝 Detaylı Ders Notları"
            st.button(
                notes_button_label, 
                key=f"{subject_key}_notes_btn", 
                type="primary", 
                on_click=set_active_content, 
                args=(notes_key,),
                help="Koda manuel eklenmiş detaylı ders notlarını gösterir."
            )

        # --- B. SORU ÇÖZME KUTUCUĞU (TESTCOZ.ONLINE GOOGLE ARAMASI) ---
        with col_quiz:
            st.link_button(
                "✅ Test Çöz - Yeni Nesil Sorular", 
                url=get_search_link("", "testcoz_quiz"), 
                type="secondary", 
                help="Google'da 'testcoz.online 7. sınıf test çöz' araması yapar."
            )
        
        # --- C. VİDEO İZLE KUTUCUĞU (TONGUÇ KANAL LİNKİ) ---
        with col_video:
            st.link_button(
                "📺 Tonguç Akademi Kanalı", 
                url=get_search_link("", "tonguc_channel"), 
                type="secondary",
                help="Doğrudan Tonguç Akademi YouTube kanalını açar."
            )
        
        st.markdown("---")
        
        # --- İÇERİK GÖRÜNTÜLEME ALANI ---
        if st.session_state.active_content == notes_key:
            st.subheader(f"📘 {subject_data['title']} Ders Notları")
            st.markdown(NOTES_MAP.get(subject_key, "### Bu ders için not içeriği henüz eklenmedi. Lütfen kodu düzenleyin."))
            st.markdown("---")
        
        else:
            # Konulara göre hızlı arama linkleri
            st.subheader("Konulara Göre Hızlı Erişim (Google Arama)")
            st.info("Aşağıdaki konulara tıklayarak, ders notlarını Google'da hızla bulabilirsiniz.")
            
            cols_content = st.columns(3)
            
            for i, topic in enumerate(subject_data['topics']):
                col = cols_content[i % 3]
                
                # Google Arama Linki (Notlar için)
                google_link = get_search_link(topic, "google")
                
                with col:
                    st.markdown(f"**📚 {topic}**")
                    st.link_button("Notları Google'da Bul", url=google_link, type="primary", key=f"{subject_key}_{topic}_g")
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
