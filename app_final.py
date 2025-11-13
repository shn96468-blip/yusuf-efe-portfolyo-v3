import streamlit as st

# --- 1. STREAMLIT DURUM YÖNETİMİ (Session State) ---
if 'content_key' not in st.session_state:
    st.session_state.content_key = None 

# AI asistanı (Akıl) için durum yönetimi.
if 'ai_response' not in st.session_state:
    st.session_state.ai_response = "Konuyu yazın ve Akıl'dan Konu Anlatmasını isteyin. (Örn: Fiiller)"
    st.session_state.last_topic = ""

# --- BUTON TIKLAMA İŞLEVLERİ ---

# Manuel Konu Anlatımı Butonları için
def toggle_content(key):
    if st.session_state.content_key == key:
        st.session_state.content_key = None
    else:
        st.session_state.content_key = key

# Yapay Zeka (Akıl) Butonu için (Genişletilmiş Konular ve Sohbet Yasağı)
def generate_ai_explanation(topic):
    topic_lower = topic.lower().strip()
    response = ""

    # --- 7. SINIF MATEMATİK KONULARI ---
    if "rasyonel sayılar" in topic_lower or "rasyonel sayılarla işlemler" in topic_lower:
        response = """
        ## 🧠 Akıl Konu Anlatımı: Rasyonel Sayılar
        
        **Tanım:** Rasyonel sayılar, $a$ bir tam sayı ve $b$ sıfırdan farklı bir tam sayı olmak üzere, $\\frac{a}{b}$ şeklinde yazılabilen sayılardır.
        
        **İşlemler:** Paydalar eşitlenerek toplama/çıkarma, paylar çarpılıp paya, paydalar çarpılıp paydaya yazılarak çarpma yapılır. Bölmede ters çevirip çarpma kuralı uygulanır.
        """
    elif "tam sayılar" in topic_lower:
        response = """
        ## 🧠 Akıl Konu Anlatımı: Tam Sayılar
        
        **Tanım:** Tam sayılar, pozitif ($1, 2, 3, ...$), negatif ($-1, -2, -3, ...$) ve sıfırın oluşturduğu kümedir. $\\mathbb{Z}$ ile gösterilir.
        
        **Toplama:** Aynı işaretliler toplanır, ortak işaret verilir. Farklı işaretlilerde büyükten küçük çıkarılır, büyüğün işareti verilir.
        """
    elif "cebirsel ifadeler" in topic_lower:
        response = """
        ## 🧠 Akıl Konu Anlatımı: Cebirsel İfadeler
        
        **Tanım:** En az bir bilinmeyen (değişken) ve işlem içeren ifadelerdir. Örneğin, $3x + 5$
        
        **Temel Kavramlar:** Değişken (x, y), Katsayı (x'in önündeki sayı), Sabit Terim (yanında değişken olmayan sayı).
        """
    
    # --- YENİ EKLENEN TÜRKÇE KONULARI ---
    elif "fiiller" in topic_lower or "eylem" in topic_lower:
        response = """
        ## 🧠 Akıl Konu Anlatımı: Fiiller (Eylemler)
        
        **Tanım:** Fiiller, bir iş, oluş veya durum bildiren kelimelerdir. Cümledeki hareketi veya yargıyı belirtir. Fiillerin köküne genellikle '-mek, -mak' mastar ekini getirebiliriz.
        """
    elif "ek fiil" in topic_lower:
        response = """
        ## 🧠 Akıl Konu Anlatımı: Ek Fiil (Ek Eylem)
        
        **Tanım:** Ek fiil, iki temel görevi olan 'imek' fiilidir (im, isen, idir, idi, imiş, ise).
        
        **Görevleri:** 1. İsimleri yüklem yapar. 2. Basit zamanlı fiilleri birleşik zamanlı yapar.
        """
    elif "zarflar" in topic_lower:
        response = """
        ## 🧠 Akıl Konu Anlatımı: Zarflar (Belirteçler)
        
        **Tanım:** Zarflar, fiilleri, fiilimsileri, sıfatları ve bazen de başka zarfları **zaman, durum, miktar, yer-yön** ve **soru** bakımından belirten kelimelerdir.
        
        **Türleri:** Durum Zarfı, Zaman Zarfı, Miktar Zarfı, Yer-Yön Zarfı ve Soru Zarfı.
        """
        
    # --- DİĞER TÜM KONULAR REDDEDİLİR (Sohbet Yasağı) ---
    else:
        response = f"""
        ## ⚠️ Akıl Asistan Uyarısı
        
        **'{topic[:20].upper() + ('...' if len(topic) > 20 else '')}'** şu an için anlatabileceğim konular arasında değildir. 
        
        Ben sadece 7. Sınıf **Matematik ve Dil Bilgisi** ana konularını anlatmak üzere programlanmış bir öğrenci asistanıyım ve **sohbet özelliğim kapalıdır.**
        """
        
    st.session_state.ai_response = response
    st.session_state.last_topic = topic

# --- 2. TÜM İÇERİKLERİN YENİ VE DETAYLI TANIMI ---
COACH_CONTENT = """
## 💡 Koç Modülü - Öğrenci Koçluğu ve Rehberlik
### 🗓️ Rehberlik Konuları
* **Zaman Yönetimi:** Günlük rutin oluşturma ve derslere ayrılan sürenin belirlenmesi.
* **Pomodoro Tekniği:** 25 dakika çalışma, 5 dakika mola tekniği ile odaklanmayı artırma.
"""

MATH_CONTENT = """
## 📘 Matematik - Konu Anlatımı ve Özet
### 1. ÜNİTE: TAM SAYILARLA İŞLEMLER
* Tam Sayılarla Toplama, Çıkarma, Çarpma ve Bölme İşlemi
* Tam Sayıların Kuvveti, Tam Sayı Problemleri

### 2. ÜNİTE: RASYONEL SAYILAR VE İŞLEMLER
* Rasyonel Sayılar (Gösterimi, Sıralaması)
* Rasyonel Sayılarla İşlemler

### 3. ÜNİTE: CEBİRSEL İFADELERDEN EŞİTLİK VE DENKLEMLERE
* Cebirsel İfadeler, Eşitlik ve Denklem

### 4. ÜNİTE: ORAN ORANTIDAN YÜZDELERE
* Oran ve Orantı, Yüzdeler

### 5. ÜNİTE: DOĞRULAR VE AÇILARDAN ÇOKGENLER, ÇEMBER VE DAİREYE
* Doğrular ve Açılar, Çokgenler, Çember ve Daire

### 6. ÜNİTE: VERİ ANALİZİNDEN CİSİMLERİN FARKLI YÖNDEN GÖRÜNÜMLERİNE
* Veri Analizi, Cisimlerin Farklı Yönlerden Görünümleri
"""

TURKISH_CONTENT = """
## 📝 Türkçe - Konu Anlatımı ve Özet
### 📄 Anlam Bilgisi Konuları
* Sözcükte Anlam, Cümlede Anlam, Parçada Anlam
* Tablo, Grafik, Görsel Yorumlama
* Metin Türleri, Söz Sanatları

### 📄 Dil, Yazım ve Noktalama Konuları
* Fiiller (Eylem), Ek Fiil, Zarflar
* Anlatım Bozuklukları, Yazım Kuralları, Noktalama İşaretleri
"""

SCIENCE_CONTENT = """
## 🧪 Fen Bilimleri - Konu Anlatımı ve Özet
### 1. ÜNİTE: GÜNEŞ SİSTEMİ VE ÖTESİ
* Uzay Araştırmaları, Güneş Sistemi Ötesi: Gök Cisimleri

### 2. ÜNİTE: HÜCRE VE BÖLÜNMELER
* Hücre (Yapısı), Mitoz ve Mayoz Bölünme

### 3. ÜNİTE: KUVVET VE ENERJİ
* Kütle ve Ağırlık İlişkisi, Kuvvet, İş ve Enerji İlişkisi, Enerji Dönüşümleri

### 4. ÜNİTE: SAF MADDE VE KARIŞIMLAR
* Maddenin Tanecikli Yapısı, Saf Maddeler, Karışımlar
* Karışımların Ayrılması, Evsel Atıklar ve Geri Dönüşüm
"""

SOCIAL_CONTENT = """
## 🌍 Sosyal Bilgiler - Konu Anlatımı ve Özet
### 1. ÜNİTE: BİREY VE TOPLUM
### 2. ÜNİTE: KÜLTÜR VE MİRAS
### 3. ÜNİTE: İNSANLAR, YERLER VE ÇEVRELER
### 4. ÜNİTE: BİLİM, TEKNOLOJİ VE TOPLUM

### 5. ÜNİTE: ÜRETİM, DAĞITIM VE TÜKETİM
### 6. ÜNİTE: ETKİN VATANDAŞLIK
### 7. ÜNİTE: KÜRESEL BAĞLANTILAR
"""

ENGLISH_CONTENT = """
## 🗣️ İngilizce - Konu Anlatımı ve Özet
### 1. DÖNEM KONULARI
* Appearance And Personality, Sports, Biographies, Wild Animals, Television

### 2. DÖNEM KONULARI
* Celebrations, Dreams, Public Buildings, Environment, Planets
"""

RELIGION_CONTENT = """
## 🕌 Din Kültürü ve Ahlak Bilgisi - Konu Anlatımı ve Özet
### 1. ÜNİTE: MELEKLER VE AHİRET İNANCI
* Görülen ve Görülemeyen Varlıklar, Melekler, Dünya ve Ahiret Hayatı

### 2. ÜNİTE: HAC VE KURBAN
* İslam’da Hac İbadeti ve Önemi, Haccın Yapılışı, Umre
* Kurban İbadeti ve Önemi, Hz.İsmail (a.s.)

### 3. ÜNİTE: AHLAKİ DAVRANIŞLAR
* Güzel Ahlaki Tutum ve Davranışlar, Hz. Salih (a.s.) - Felak Suresi

### 4. ÜNİTE: ALLAH’IN KULU VE ELÇİSİ: HZ. MUHAMMED (S.A.V.)
* Allah’ın Kulu ve Elçisi Hz. Muhammed (s.a.v.) - Kâfirun Suresi

### 5. ÜNİTE: İSLAM DÜŞÜNCESİNDE YORUMLAR
* Din Anlayışındaki Yorum Farklılıklarının Sebepleri, Yorum Biçimleri, Tasavvufi Yorumlar
"""

# Tüm içerikleri bir sözlükte toplama
CONTENT_MAP = {
    "mat_konu": MATH_CONTENT,
    "tr_konu": TURKISH_CONTENT,
    "sci_konu": SCIENCE_CONTENT,
    "soc_konu": SOCIAL_CONTENT,
    "eng_konu": ENGLISH_CONTENT,
    "rel_konu": RELIGION_CONTENT,
}


# --- 3. STREAMLIT SAYFA AYARLARI ---
st.set_page_config(layout="wide", page_title="Yusuf Efe Şahin | 7. Sınıf Eğitim Portalı")
st.title("👨‍🎓 Yusuf Efe Şahin | 7. Sınıf Eğitim Portalı")
st.markdown("---")

# 4. SEKMELERİN TANIMLANMASI
tab_coach, tab_math, tab_tr, tab_sci, tab_soc, tab_eng, tab_rel = st.tabs([
    "💡 Koç Modülü", 
    "🔢 Matematik İçerikleri", 
    "📝 Türkçe İçerikleri", 
    "🧪 Fen Bilimleri",
    "🌍 Sosyal Bilgiler",
    "🗣️ İngilizce",
    "🕌 Din Kültürü",
])

# --- DERS SEKMELERİ İÇİN GENEL FONKSİYON ---
def render_subject_tab(tab_context, subject_title, key_prefix):
    """Her ders sekmesini tek bir yapıda oluşturur."""
    
    konu_key = f"{key_prefix}_konu"
    pdf_key = f"{key_prefix}_pdf"
    deneme_key = f"{key_prefix}_deneme"
    
    with tab_context:
        st.header(f"{subject_title} Dersi İçerikleri")
        col_btn1, col_btn2, col_btn3 = st.columns(3)
        
        with col_btn1:
            button_label = "⬆️ Konuyu Gizle" if st.session_state.content_key == konu_key else "📄 Konu Anlatımı"
            st.button(button_label, type="primary", key=konu_key,
                      on_click=toggle_content, args=(konu_key,)) 
        with col_btn2:
            st.button("♦️ PDF Sonuç Kontrol", type="secondary", key=pdf_key)
        with col_btn3:
            st.button("🔥 Deneme Sınavı", type="secondary", key=deneme_key)
        
        st.markdown("---")
        
        # --- İÇERİK GÖSTERİM MANTIĞI (Tıklayınca Açılır/Kapanır) ---
        if st.session_state.content_key == konu_key:
            st.subheader(f"✨ {subject_title} Konu Anlatımı Detay")
            st.markdown(CONTENT_MAP[konu_key], unsafe_allow_html=True)
            st.markdown("---")
        else:
            st.info(f"Yukarıdaki '📄 Konu Anlatımı' butonuna tıklayarak {subject_title} dersi içeriğini görebilirsiniz.")

# ==============================================================================
# --- 5. TAB 0: KOÇ MODÜLÜ (Akıl Asistanı) ---
# ==============================================================================
with tab_coach:
    st.header("💡 Koç Modülü - Rehberlik ve Mentorluk")
    st.subheader("🤖 Yapay Zeka Asistanı (Akıl)")
    
    # Text input and button for the AI feature
    input_topic = st.text_input(
        "Konu Adını Yazınız (Örn: Rasyonel Sayılar, Fiiller)", 
        value=st.session_state.last_topic,
        key="topic_input"
    )
    
    # Tıklanınca AI açıklaması başlar
    ai_button = st.button(
        "Akıl'dan Konuyu Anlatmasını İste", 
        type="primary", 
        key="ai_generate",
        on_click=generate_ai_explanation,
        args=(input_topic,)
    )
    
    st.markdown("---")
    
    # AI yanıtını göster
    st.markdown(st.session_state.ai_response, unsafe_allow_html=True)
    st.markdown("---") 

    # Orijinal Koç Modülü Butonları ve İçeriği
    st.header("📝 Çalışma ve Rehberlik İçerikleri")
    col_coach_btn1, col_coach_btn2, col_coach_btn3 = st.columns(3)
    
    with col_coach_btn1:
        st.button("📝 Çalışma Planı Oluştur", type="secondary", key="coach_plan") 
    with col_coach_btn2:
        st.button("🧠 Motivasyon Teknikleri", type="secondary", key="coach_motivasyon")
    with col_coach_btn3:
        st.button("⏰ Pomodoro Zamanlayıcısı", type="secondary", key="coach_pomodoro")
    
    st.markdown("---")
    st.markdown(COACH_CONTENT, unsafe_allow_html=True)


# ==============================================================================
# --- 6. DERS SEKMELERİNİN ÇAĞRILMASI (Tüm Dersler) ---
# ==============================================================================
render_subject_tab(tab_math, "🔢 Matematik", "mat")
render_subject_tab(tab_tr, "📝 Türkçe", "tr")
render_subject_tab(tab_sci, "🧪 Fen Bilimleri", "sci")
render_subject_tab(tab_soc, "🌍 Sosyal Bilgiler", "soc")
render_subject_tab(tab_eng, "🗣️ İngilizce", "eng")
render_subject_tab(tab_rel, "🕌 Din Kültürü", "rel")
