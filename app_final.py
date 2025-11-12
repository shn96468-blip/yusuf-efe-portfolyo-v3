import streamlit as st

# --- İÇERİK DOSYALARINI İÇE AKTARMA (IMPORT) ---
# DİKKAT: İçerik dosyalarınızın (math_content.py, science_content.py, vb.) mevcut ve doğru olması gerekir.
from math_content import MATH_CONTENT
from turkish_content import TURKISH_CONTENT
from english_content import ENGLISH_CONTENT
from religion_content import RELIGION_CONTENT
from history_content import SOCIAL_CONTENT 

try:
    from science_content import SCIENCE_CONTENT 
except ImportError:
    # science_content.py dosyası eksikse, hata vermeden uyarı göstermesini sağlar
    SCIENCE_CONTENT = """## ⚠️ Eksik Dosya Uyarısı
    Fen Bilimleri içeriği, 'science_content.py' dosyasından içe aktarılamadı.
    Lütfen bu dosyayı oluşturup içine 'SCIENCE_CONTENT' değişkenini tanımlayın.
    """

# --- 2. STREAMLIT SAYFA AYARLARI ---
st.set_page_config(layout="wide", page_title="Yusuf Efe Şahin | 7. Sınıf Eğitim Portalı")

# --- 3. BAŞLIK VE SEKME YAPISI ---
st.title("👨‍🎓 Yusuf Efe Şahin | 7. Sınıf Eğitim Portalı")
st.markdown("---")

# 6 ana ders sekmesi oluşturuldu
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "🔢 Matematik İçerikleri", 
    "📝 Türkçe İçerikleri", 
    "🧪 Fen Bilimleri",
    "🌍 Sosyal Bilgiler",
    "🗣️ İngilizce",
    "🕌 Din Kültürü",
])

# --- 4. TAB 1: MATEMATİK İÇERİKLERİ ---
with tab1:
    st.header("🔢 Matematik Dersi İçerikleri")
    col_math_btn1, col_math_btn2, col_math_btn3 = st.columns(3)
    
    with col_math_btn1:
        # Buton kısa başlık + Hata önleyici benzersiz 'key' eklendi
        st.button("📄 Konu Anlatımı", type="primary", key="mat_konu") 
    with col_math_btn2:
        st.button("♦️ PDF Sonuç Kontrol", type="secondary", key="mat_pdf")
    with col_math_btn3:
        st.button("🔥 Deneme Sınavı", type="secondary", key="mat_deneme")
    
    st.markdown("---")
    st.markdown(MATH_CONTENT, unsafe_allow_html=True)


# --- 5. TAB 2: TÜRKÇE İÇERİKLERİ ---
with tab2:
    st.header("📝 Türkçe Dersi İçerikleri")
    col_tr_btn1, col_tr_btn2, col_tr_btn3 = st.columns(3)

    with col_tr_btn1:
        # Buton kısa başlık + Hata önleyici benzersiz 'key' eklendi
        st.button("📄 Konu Anlatımı", type="primary", key="turk_konu") 
    with col_tr_btn2:
        st.button("♦️ Hikaye Analizi", type="secondary", key="turk_analiz")
    with col_tr_btn3:
        st.button("🔥 Yazım Kılavuzu", type="secondary", key="turk_yazim")

    st.markdown("---")
    st.markdown(TURKISH_CONTENT, unsafe_allow_html=True)

# --- 6. TAB 3: FEN BİLİMLERİ İÇERİKLERİ ---
with tab3:
    st.header("🧪 Fen Bilimleri Dersi İçerikleri")
    col_fen_btn1, col_fen_btn2, col_fen_btn3 = st.columns(3)
    
    with col_fen_btn1:
        # Buton kısa başlık + Hata önleyici benzersiz 'key' eklendi
        st.button("📄 Konu Anlatımı", type="primary", key="fen_konu") 
    with col_fen_btn2:
        st.button("🔬 Laboratuvar Deneyleri", type="secondary", key="fen_deney")
    with col_fen_btn3:
        st.button("🔥 Ünite Testi", type="secondary", key="fen_test")
    
    st.markdown("---")
    st.markdown(SCIENCE_CONTENT, unsafe_allow_html=True)

# --- 7. TAB 4: SOSYAL BİLGİLER İÇERİKLERİ ---
with tab4:
    st.header("🌍 Sosyal Bilgiler Dersi İçerikleri")
    col_sosyal_btn1, col_sosyal_btn2, col_sosyal_btn3 = st.columns(3)
    
    with col_sosyal_btn1:
        # Buton kısa başlık + Hata önleyici benzersiz 'key' eklendi
        st.button("📄 Konu Anlatımı", type="primary", key="sos_konu") 
    with col_sosyal_btn2:
        st.button("📜 Tarihi Olaylar", type="secondary", key="sos_olay")
    with col_sosyal_btn3:
        st.button("🔥 Coğrafya Bilgisi", type="secondary", key="sos_cografya")
    
    st.markdown("---")
    st.markdown(SOCIAL_CONTENT, unsafe_allow_html=True)

# --- 8. TAB 5: İNGİLİZCE İÇERİKLERİ ---
with tab5:
    st.header("🗣️ İngilizce Dersi İçerikleri")
    col_ing_btn1, col_ing_btn2, col_ing_btn3 = st.columns(3)
    
    with col_ing_btn1:
        # Buton kısa başlık + Hata önleyici benzersiz 'key' eklendi
        st.button("📄 Konu Anlatımı", type="primary", key="ing_konu") 
    with col_ing_btn2:
        st.button("💬 Konuşma Alıştırması", type="secondary", key="ing_konusma")
    with col_ing_btn3:
        st.button("🔥 Kelime Testi", type="secondary", key="ing_test")
    
    st.markdown("---")
    st.markdown(ENGLISH_CONTENT, unsafe_allow_html=True)

# --- 9. TAB 6: DİN KÜLTÜRÜ İÇERİKLERİ ---
with tab6:
    st.header("🕌 Din Kültürü ve Ahlak Bilgisi Dersi İçerikleri")
    col_din_btn1, col_din_btn2, col_din_btn3 = st.columns(3)
    
    with col_din_btn1:
        # Buton kısa başlık + Hata önleyici benzersiz 'key' eklendi
        st.button("📄 Konu Anlatımı", type="primary", key="din_konu") 
    with col_din_btn2:
        st.button("🕋 Kavram Özetleri", type="secondary", key="din_kavram")
    with col_din_btn3:
        st.button("🔥 Soru Çözümü", type="secondary", key="din_soru")
    
    st.markdown("---")
    st.markdown(RELIGION_CONTENT, unsafe_allow_html=True)
