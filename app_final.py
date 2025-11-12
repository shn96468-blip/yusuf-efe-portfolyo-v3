import streamlit as st
# import random # Artık Kelime Kartları kullanılmadığı için Random kütüphanesine gerek kalmadı.
# import time # Artık kullanılmıyor.

# --- SÖZLÜK YÜKLEME ARTIK SADECE DEMO İÇİN KALDI ---
# Sözlük yükleme fonksiyonu koddan tamamen kaldırılabilir, 
# ancak Koç Modülü içindeki metinlerin anlaşılması için içeriği tutuyorum.

# --- SABİT METİNLER VE İÇERİK ---
MATH_CONTENT = """
## 📘 Matematik - Konu Anlatımı ve Özet
<div style='background-color: #26292e; padding: 10px; border-radius: 5px;'>
    <p>🔑 Konu: 7. Sınıf Matematik Tüm Üniteler</p>
</div>

### 📄 Detaylı Konu Özeti
7. Sınıf Matematik dersi 6 ana üniteden oluşmaktadır.

#### Tam Sayılarda Dört İşlem (Detaylı Anlatım)
1. **Toplama İşlemi:**
    * **Aynı İşaretliler:** Değerler toplanır, ortak işaret sonuca konur.
        * Örnek 1: $+5 + (+3) = +8$
        * Örnek 2: $-5 + (-3) = -8$
    * **Farklı İşaretliler:** Mutlak değeri büyük olandan küçük olan çıkarılır ve mutlak değeri büyük olanın işareti sonuca konur.
        * Örnek 1: $+8 + (-3) = +5$
        * Örnek 2: $-8 + (+3) = -5$

2. **Çıkarma İşlemi:**
    * Çıkarma işlemi, çıkan sayının **ters işaretlisini** eklemeye dönüştürülür (Toplama kuralına dönüştürülür).
        * Örnek: $10 - (-3)$ işlemi $10 + (+3) = 13$ olur.
        * Örnek: $-10 - (+3)$ işlemi $-10 + (-3) = -13$ olur.

3. **Çarpma/Bölme İşlemi:**
    * **Aynı İşaretliler:** Sonuç her zaman **pozitiftir (+)**.
        * Örnek: $(+5) \times (+3) = +15$
        * Örnek: $(-5) \times (-3) = +15$
    * **Farklı İşaretliler:** Sonuç her zaman **negatiftir (-)**.
        * Örnek: $(+10) \div (-2) = -5$
        * Örnek: $(-10) \div (+2) = -5$
"""
TURKISH_CONTENT = """
## 📖 Türkçe - Konu Anlatımı ve Özet
<div style='background-color: #26292e; padding: 10px; border-radius: 5px;'>
    <p>🔑 Konu: 7. Sınıf Türkçe Tüm Konular</p>
</div>

### 📄 Detaylı Konu Anlatımı
7. Sınıf Türkçe dersi, dil bilgisi, anlam bilgisi ve yazma becerileri üzerine odaklanır.

#### 1. Anlam Bilgisi (Sözcük, Cümle ve Paragrafta Anlam)
* **Sözcükte Anlam:** Gerçek, mecaz ve terim anlam. (Örn: 'Sıcak' ev (Gerçek), 'Sıcak' karşılama (Mecaz)).
* **Cümlede Anlam:** Öznel (kişisel görüş) ve Nesnel (kanıtlanabilir) yargılar. Neden-Sonuç, Amaç-Sonuç cümleleri.
* **Paragrafta Anlam:** Ana fikir, yardımcı fikirler, başlık ve konunun belirlenmesi.

#### 2. Dil Bilgisi (Fiiller ve Ekler)
* **Fiiller (Eylemler):** İş, oluş, durum bildirirler.
* **Kip ve Kişi Ekleri:**
    * **Haber Kipleri (Zaman Bildirir):** Görülen Geçmiş (-di), Duyulan Geçmiş (-miş), Şimdiki (-yor), Gelecek (-ecek), Geniş (-r).
    * **Dilek Kipleri (Dilek/Şart Bildirir):** Gereklilik (-meli), Şart (-sa), İstek (-e), Emir (Eki yoktur).
"""

# --- 2. STREAMLIT SAYFA AYARLARI ---
st.set_page_config(layout="wide", page_title="Yusuf Efe Şahin | 7. Sınıf Eğitim Portalı")

# --- 3. BAŞLIK VE SEKME YAPISI ---
st.title("👨‍🎓 Yusuf Efe Şahin | 7. Sınıf Eğitim Portalı")
st.markdown("---")

# Sadece 3 sekme kaldı: Koç, Matematik ve Türkçe
tab1, tab2, tab3 = st.tabs([
    "💡 Koç Modülü", 
    "🔢 Matematik İçerikleri", 
    "📝 Türkçe İçerikleri", 
])

# --- 4. TAB 1: KOÇ MODÜLÜ ---
with tab1:
    st.header("💡 Koç Modülü (Cebirsel İfadeler)")
    
    # Koç Cevap Bloğu
    st.markdown(
        """
        <div style='background-color: #38761d; padding: 15px; border-radius: 8px;'>
            <p style='color: white; margin: 0;'>Koç Cevabı: 'tam sayılarda toplama nedir'</p>
            <p style='color: #e0e0e0; font-size: 14px; margin-top: 10px;'>'konusuyla ilgili sana özel olarak hazırladığım ekstra alıştırmalar ve 7. sınıf müfredatındaki en kritik 3 bilgi notunu içeren bir özet hazırlıyorum. Unutma, pratik yapmak başarıyı getirir!'</p>
        </div>
        """, unsafe_allow_html=True
    )

    st.markdown("---")
    
    # Koç Açıklama Bloğu
    st.markdown(
        """
        <div style='background-color: #8fbc94; padding: 10px; border-radius: 5px;'>
            <p style='color: #1a1a1a; margin: 0;'>**Koç Açıklaması - Konu: Cebirsel İfadeler **</p>
        </div>
        """, unsafe_allow_html=True
    )
    st.markdown(MATH_CONTENT.replace("## 📘 Matematik", "## Matematik").replace("### 📄 Detaylı Konu Özeti", ""), unsafe_allow_html=True) 

    # Sesli Çıktı Simülasyonu
    st.markdown("---")
    st.subheader("🔊 Sesli Robot Çıktısı (Simülasyon)")
    st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3", start_time=182)
    st.caption("(Yukarıdaki ses bileşeni, konunun sesli olarak okunduğunu simüle eder.)")

# --- 5. TAB 2: MATEMATİK İÇERİKLERİ ---
with tab2:
    st.header("🔢 Matematik Dersi İçerikleri")
    col_math_btn1, col_math_btn2, col_math_btn3 = st.columns(3)
    
    with col_math_btn1:
        st.button("📄 Konu Anlatımı", type="primary")
    with col_math_btn2:
        st.button("♦️ PDF Sonuç Kontrol", type="secondary")
    with col_math_btn3:
        st.button("🔥 Deneme Sınavı", type="secondary")
    
    st.markdown("---")
    st.markdown(MATH_CONTENT, unsafe_allow_html=True)


# --- 6. TAB 3: TÜRKÇE İÇERİKLERİ ---
with tab3:
    st.header("📝 Türkçe Dersi İçerikleri")
    col_tr_btn1, col_tr_btn2, col_tr_btn3 = st.columns(3)

    with col_tr_btn1:
        st.button("📄 Konu Anlatımı ve Özet", type="primary")
    with col_tr_btn2:
        st.button("♦️ Hikaye Analizi", type="secondary")
    with col_tr_btn3:
        st.button("🔥 Yazım Kılavuzu", type="secondary")

    st.markdown("---")
    st.markdown(TURKISH_CONTENT, unsafe_allow_html=True)
