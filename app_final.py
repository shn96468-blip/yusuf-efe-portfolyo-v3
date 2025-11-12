import streamlit as st

# --- SABİT METİNLER VE İÇERİK ---

# Matematik Konu Anlatımı
MATH_CONTENT = """
## 📘 Matematik - Konu Anlatımı ve Özet
<div style='background-color: #26292e; padding: 10px; border-radius: 5px;'>
    <p>🔑 Konu: 7. Sınıf Matematik Tüm Üniteler</p>
</div>
### 📄 Detaylı Konu Özeti
7. Sınıf Matematik dersi 6 ana üniteden oluşmaktadır. (Tam Sayılar, Rasyonel Sayılar, Cebirsel İfadeler, Oran-Orantı, Yüzdeler, Geometri)

#### Tam Sayılarda Dört İşlem (Özet)
1. **Toplama İşlemi:** Aynı işaretli sayılar toplanır. Farklı işaretlilerde mutlak değeri büyük olandan küçük olan çıkarılır.
2. **Çıkarma İşlemi:** Çıkan sayının işareti ters çevrilip toplama yapılır.
3. **Çarpma/Bölme:** Aynı işaretliler (+) Pozitif, farklı işaretliler (-) Negatif sonuç verir.
"""

# Türkçe Konu Anlatımı
TURKISH_CONTENT = """
## 📖 Türkçe - Konu Anlatımı ve Özet
<div style='background-color: #26292e; padding: 10px; border-radius: 5px;'>
    <p>🔑 Konu: 7. Sınıf Türkçe Tüm Konular</p>
</div>
### 📄 Detaylı Konu Anlatımı
7. Sınıf Türkçe dersi, dil bilgisi, anlam bilgisi ve yazma becerileri üzerine odaklanır.

#### 1. Anlam Bilgisi
* **Sözcükte Anlam:** Gerçek, mecaz ve terim anlam.
* **Cümlede Anlam:** Öznel (kişisel görüş) ve Nesnel (kanıtlanabilir) yargılar.
* **Paragrafta Anlam:** Ana fikir, yardımcı fikirler.

#### 2. Dil Bilgisi
* **Fiiller (Eylemler):** İş, oluş, durum bildirirler.
* **Kip ve Kişi Ekleri:** Haber Kipleri (Zaman), Dilek Kipleri (Şart, Gereklilik).
"""

# Fen Bilimleri Konu Anlatımı
SCIENCE_CONTENT = """
## 🔬 Fen Bilimleri - Konu Anlatımı ve Özet
<div style='background-color: #26292e; padding: 10px; border-radius: 5px;'>
    <p>🔑 Konu: 7. Sınıf Fen Bilimleri Tüm Üniteler</p>
</div>
### 📄 Detaylı Konu Özeti
7. Sınıf Fen Bilimleri dersi:

#### 1. Güneş Sistemi ve Ötesi
* **Uzay Kirliliği:** Dünya yörüngesinde bulunan ve herhangi bir işlevi kalmamış, insan yapımı cisimlerin tümüdür.
* **Teleskop Çeşitleri:** Optik (Mercekli ve Aynalı), Radyo Teleskoplar.

#### 2. Hücre
* **Hücre Yapıları:** Çekirdek, Sitoplazma, Hücre Zarı.
* **Organeller:** Mitokondri (Enerji), Ribozom (Protein), Lizozom (Sindirim).
"""

# Sosyal Bilgiler Konu Anlatımı
SOCIAL_CONTENT = """
## 🌎 Sosyal Bilgiler - Konu Anlatımı ve Özet
<div style='background-color: #26292e; padding: 10px; border-radius: 5px;'>
    <p>🔑 Konu: 7. Sınıf Sosyal Bilgiler Tüm Üniteler</p>
</div>
### 📄 Detaylı Konu Özeti
7. Sınıf Sosyal Bilgiler dersi:

#### 1. İletişim ve İnsan İlişkileri
* **Etkili İletişim:** Empati kurma, Ben dili kullanma.
* **Kitle İletişim Araçları:** Basın, radyo, televizyon ve internetin toplum üzerindeki etkileri.

#### 2. Ülkemizin Kaynakları
* **Ekonomik Faaliyetler:** Tarım, Hayvancılık, Sanayi, Hizmet Sektörleri.
* **Yerleşmeyi Etkileyen Faktörler:** Doğal Faktörler (İklim, Yer şekilleri), Beşerî Faktörler (Ulaşım, Sanayi).
"""

# İngilizce Konu Anlatımı
ENGLISH_CONTENT = """
## 🗣️ İngilizce - Konu Anlatımı ve Özet
<div style='background-color: #26292e; padding: 10px; border-radius: 5px;'>
    <p>🔑 Konu: 7. Sınıf İngilizce Tüm Üniteler</p>
</div>
### 📄 Detaylı Konu Özeti
7. Sınıf İngilizce dersi genel olarak:

#### 1. Times and Routines (Zaman ve Rutinler)
* **Simple Present Tense:** Geniş zaman yapıları, günlük rutinler ve alışkanlıklar. (Örn: I **go** to school every day.)

#### 2. Adjectives (Sıfatlar)
* **Comparatives:** İki şeyi karşılaştırma (-er than / more than). (Örn: A dog is **faster than** a cat.)
* **Superlatives:** Üstünlük derecesi (the -est / the most). (Örn: Everest is **the highest** mountain.)
"""

# Din Kültürü Konu Anlatımı
RELIGION_CONTENT = """
## 🕌 Din Kültürü ve Ahlak Bilgisi - Konu Anlatımı ve Özet
<div style='background-color: #26292e; padding: 10px; border-radius: 5px;'>
    <p>🔑 Konu: 7. Sınıf Din Kültürü Tüm Üniteler</p>
</div>
### 📄 Detaylı Konu Özeti
7. Sınıf Din Kültürü dersi:

#### 1. Melek ve Ahiret İnancı
* **Melekler:** Allah'ın (c.c.) emirlerini yerine getiren, nurdan yaratılmış varlıklardır. (Cebrail, Mikail, İsrafil, Azrail)
* **Ahiret İnancı:** Dünya hayatından sonraki sonsuz yaşam inancıdır.

#### 2. Namaz ve İbadet
* **Namaz Çeşitleri:** Farz, Vacip ve Sünnet namazlar.
* **İbadetin Önemi:** Allah'a (c.c.) karşı sorumluluk bilincini ve şükrü ifade etme.
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
        # Buton etiketi benzersiz yapıldı
        st.button("📄 Matematik Konu Anlatımı", type="primary") 
    with col_math_btn2:
        st.button("♦️ Matematik PDF Sonuç Kontrol", type="secondary")
    with col_math_btn3:
        st.button("🔥 Matematik Deneme Sınavı", type="secondary")
    
    st.markdown("---")
    st.markdown(MATH_CONTENT, unsafe_allow_html=True)


# --- 5. TAB 2: TÜRKÇE İÇERİKLERİ ---
with tab2:
    st.header("📝 Türkçe Dersi İçerikleri")
    col_tr_btn1, col_tr_btn2, col_tr_btn3 = st.columns(3)

    with col_tr_btn1:
        # Buton etiketi benzersiz yapıldı
        st.button("📄 Türkçe Konu Anlatımı ve Özet", type="primary") 
    with col_tr_btn2:
        st.button("♦️ Türkçe Hikaye Analizi", type="secondary")
    with col_tr_btn3:
        st.button("🔥 Türkçe Yazım Kılavuzu", type="secondary")

    st.markdown("---")
    st.markdown(TURKISH_CONTENT, unsafe_allow_html=True)

# --- 6. TAB 3: FEN BİLİMLERİ İÇERİKLERİ ---
with tab3:
    st.header("🧪 Fen Bilimleri Dersi İçerikleri")
    col_fen_btn1, col_fen_btn2, col_fen_btn3 = st.columns(3)
    
    with col_fen_btn1:
        # Buton etiketi benzersiz yapıldı
        st.button("📄 Fen Konu Anlatımı", type="primary") 
    with col_fen_btn2:
        st.button("🔬 Fen Laboratuvar Deneyleri", type="secondary")
    with
