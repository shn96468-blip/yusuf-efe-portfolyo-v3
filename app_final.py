import streamlit as st
import os

# --- 1. SABİT İÇERİKLER (LÜTFEN DOLDURUN) ---
# Kullanıcı bu butonlara tıkladığında bu metinler görünecektir.

MANUEL_NOTLAR = """
### 📝 Detaylı Ders Notları Alanı

Buraya, 7. sınıf ders konularının **özetlerini** ve **detaylı açıklamalarını** içeren metinlerinizi yapıştırın. Markdown (başlık, kalın yazı) kullanabilirsiniz.

Örn: **Rasyonel Sayılar Nedir?**
Payı ve paydası tam sayı olan ve paydası sıfır olmayan her sayıya rasyonel sayı denir.
* Gösterimi: a/b şeklindedir.
* Örnek: 1/2, -3/4, 5 gibi.
"""

SORU_COZME_LINK = "https://www.ornek-sorucozme-sitesi.com" # Buraya deneme sınavı/soru sitesi linki ekleyin
YOUTUBE_LINK_BASLANGIC = "https://www.youtube.com/results?search_query=" # YouTube arama linkinin başlangıcı


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

# --- 3. SESSION STATE (DURUM YÖNETİMİ) ---
if 'active_tab' not in st.session_state: st.session_state.active_tab = "mat"
if 'active_content' not in st.session_state: st.session_state.active_content = None 


# --- 4. BUTON MANTIĞI ---
def set_active_content(content_type):
    """Aktif içeriği (Notlar, Soru, Video) ayarlar."""
    if st.session_state.active_content == content_type:
        st.session_state.active_content = None # Aynı butona tekrar basılırsa içeriği kapat
    else:
        st.session_state.active_content = content_type

def set_active_tab(tab_key):
    st.session_state.active_tab = tab_key
    st.session_state.active_content = None # Sekme değiştiğinde alt içeriği sıfırla


# --- 5. SAYFA AYARLARI ---
st.set_page_config(layout="wide", page_title="Yusuf Efe Şahin | 7. Sınıf Portalı")
st.title("👨‍🎓 Yusuf Efe Şahin | 7. Sınıf Ders Portalı")
st.markdown("---")

# --- 6. DERS SEKMELERİNİ ÇİZME VE İÇERİK MANTIĞI ---
def render_subject_tab(tab_context, subject_key):
    subject_data = SUBJECT_MAP[subject_key]
    
    with tab_context:
        st.header(f"✨ {subject_data['title']} Dersi")
        
        # 3 KUTUCUK (Buton) Oluşturma
        col_notes, col_quiz, col_video = st.columns(3)

        with col_notes:
            # Ders Notları Kutucuğu
            notes_button_label = "✅ Notları Kapat" if st.session_state.active_content == f"{subject_key}_notes" else "📝 Detaylı Ders Notları"
            st.button(
                notes_button_label, 
                key=f"{subject_key}_notes_btn", 
                type="primary", 
                on_click=set_active_content, 
                args=(f"{subject_key}_notes",)
            )

        with col_quiz:
            # Soru Çözme Kutucuğu (Doğrudan Link)
            st.link_button(
                "❓ Soru Çözme / Deneme", 
                url=SORU_COZME_LINK, 
                type="secondary", 
                help="Farklı bir sayfada Soru Çözme Platformunu açar."
            )
        
        with col_video:
            # Video Kutucuğu
            video_button_label = "✅ Videoları Kapat" if st.session_state.active_content == f"{subject_key}_video" else "📺 Video İzle"
            st.button(
                video_button_label, 
                key=f"{subject_key}_video_btn", 
                type="secondary",
                on_click=set_active_content,
                args=(f"{subject_key}_video",)
            )
        
        st.markdown("---")
        
        # --- İÇERİK GÖRÜNTÜLEME ALANI ---
        
        # 1. Ders Notları İçeriği
        if st.session_state.active_content == f"{subject_key}_notes":
            st.subheader(f"📘 {subject_data['title']} Ders Notları")
            st.markdown(MANUEL_NOTLAR)
            st.markdown("---")
            
        # 2. Video Arama İçeriği
        elif st.session_state.active_content == f"{subject_key}_video":
            st.subheader(f"▶️ {subject_data['title']} Video Kaynakları")
            st.info("Aşağıdaki konulara tıklayarak doğrudan YouTube'da arama yapabilir ve ilgili videoları izleyebilirsiniz.")
            
            # Konu linklerini listele
            cols_link = st.columns(2)
            for i, topic in enumerate(subject_data['topics']):
                youtube_query = f"{topic} 7. Sınıf Konu Anlatımı"
                youtube_link = f"{YOUTUBE_LINK_BASLANGIC}{youtube_query.replace(' ', '+')}"
                
                with cols_link[i % 2]:
                    st.markdown(f"* [{topic} Konu Anlatımı]({youtube_link})")
            st.markdown("---")

        else:
            # Hiçbir şey seçilmediğinde
            st.info("Yukarıdaki seçeneklerden birini seçerek ders notlarına, soru çözme platformuna veya videolara ulaşabilirsiniz.")


# --- 7. SEKMELERİN TANIMLANMASI VE ÇAĞRILMASI ---
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
