import streamlit as st

# --- 1. STREAMLIT DURUM YÖNETİMİ (Session State) ---
if 'content_key' not in st.session_state:
    st.session_state.content_key = None 

# AI asistanı (Akıl) için durum yönetimi.
if 'ai_response' not in st.session_state:
    st.session_state.ai_response = "Konuyu yazın ve Akıl'dan Konu Anlatmasını isteyin. (Örn: Rasyonel, Kütle) VEYA Genel Bir Şey Sorun."
    st.session_state.last_topic = ""

# --- BUTON TIKLAMA İŞLEVLERİ ---

def toggle_content(key):
    # Manuel Konu Anlatımı Butonları için
    if st.session_state.content_key == key:
        st.session_state.content_key = None
    else:
        st.session_state.content_key = key

# YAPAY ZEKA (AKIL) FONKSİYONU - TÜM DERSLER AKTİF, ÇOK UZUN CEVAPLAR
def generate_ai_explanation(topic):
    topic_lower = topic.lower().strip()
    response = ""

    # Eğer konu boşsa uyarı ver
    if not topic_lower:
        st.session_state.ai_response = "## ⚠️ Uyarı: Lütfen bir konu yazın!"
        st.session_state.last_topic = ""
        return
        
    # ===============================================
    # 7. SINIF MATEMATİK KONULARI (ESNEK EŞLEŞTİRME)
    # ===============================================
    if "rasyonel" in topic_lower:
        response = """
        ## 🧠 Akıl Konu Anlatımı: Rasyonel Sayılar (Öğretmen Detayında!)
        
        **Tanım ve Kavramlar:** Rasyonel sayılar, $a$ bir tam sayı ve $b$ sıfırdan farklı bir tam sayı olmak üzere, $\\frac{a}{b}$ şeklinde yazılabilen sayılar kümesidir ($\\mathbb{Q}$). Her tam sayı paydası 1 olan bir rasyonel sayıdır.
        
        **Toplama ve Çıkarma:** Temel kural, **paydaların eşit olmasıdır**. Paydalar eşitlendikten sonra, sadece paylar toplanır/çıkarılır.
        * **Örnek:** $\\frac{1}{2} + \\frac{1}{4} = \\frac{2}{4} + \\frac{1}{4} = \\mathbf{\\frac{3}{4}}$
        """
    elif "tam sayı" in topic_lower:
        response = """
        ## 🧠 Akıl Konu Anlatımı: Tam Sayılar (Öğretmen Detayında!)
        
        **Kümeler:** Negatif sayılar, pozitif sayılar ve nötr olan sıfır (0) tam sayıları oluşturur ($\\mathbb{Z}$).
        
        **Kuvvet Kuralı:** Negatif bir tam sayının **çift kuvvetleri pozitif** olurken, **tek kuvvetleri negatif** olur. (Örn: $(-5)^2 = +25$, $(-5)^3 = -125$)
        """
    elif "cebirsel" in topic_lower or "ifadeler" in topic_lower:
        response = """
        ## 🧠 Akıl Konu Anlatımı: Cebirsel İfadeler (Öğretmen Detayında!)
        
        **Tanım ve Yapı:** En az bir değişken (bilinmeyen) içeren ifadelerdir. Örn: $\\mathbf{3x + 5}$.
        
        **Temel Kavramlar:**
        1.  **Değişken:** $x, y, a$ gibi harfler.
        2.  **Katsayı:** Değişkenin önündeki sayı.
        3.  **Sabit Terim:** Yanında değişken bulunmayan sayı.
        """
    elif "oran" in topic_lower or "yüzde" in topic_lower:
        response = """
        ## 🧠 Akıl Konu Anlatımı: Oran, Orantı ve Yüzdeler (Öğretmen Detayında!)
        
        **Oran:** İki çokluğun birbirine bölünerek karşılaştırılmasıdır.
        
        **Orantı:** İki veya daha fazla oranın birbirine eşitliğidir.
        
        **Yüzdeler:** Bir çokluğun 100 parçaya bölünmesiyle elde edilen parçaların belirtilmesidir. $\\% $ sembolü ile gösterilir.
        * **Örnek:** 200'ün $\%15$'i $\\rightarrow 200 \\cdot \\frac{15}{100} = 30$
        """
    
    # ===============================================
    # 7. SINIF TÜRKÇE KONULARI (ESNEK EŞLEŞTİRME)
    # ===============================================
    elif "fiil" in topic_lower or "ek eylem" in topic_lower or "zarf" in topic_lower:
        response = """
        ## 🧠 Akıl Konu Anlatımı: Fiiller, Ek Fiil ve Zarflar (Öğretmen Detayında!)
        
        **Fiiller (Eylemler):** Bir iş, oluş veya durum bildirir.
        
        **Ek Fiil (Ek Eylem):** İsimleri yüklem yapmak veya Basit Zamanlı Fiili Birleşik Zamanlı Yapmak.
        
        **Zarflar (Belirteçler):** Fiilin nasıl, ne zaman yapıldığını belirtir. (Örn: Çocuk **hızlı** koşuyor.)
        """
    elif "söz sanatları" in topic_lower or "benzetme" in topic_lower or "abartma" in topic_lower:
        response = """
        ## 🧠 Akıl Konu Anlatımı: Söz Sanatları (Öğretmen Detayında!)
        
        **1. Benzetme (Teşbih):** Zayıfın güçlüye benzetilmesi. (Örn: dişleri **inci gibi**.)
        
        **2. Kişileştirme (Teşhis):** İnsan özelliklerinin cansızlara verilmesi. (Örn: Yorgun **bulutlar**.)
        """

    # ===============================================
    # 7. SINIF FEN BİLİMLERİ KONULARI
    # ===============================================
    elif "hücre" in topic_lower or "mitoz" in topic_lower or "mayoz" in topic_lower:
        response = """
        ## 🧠 Akıl Konu Anlatımı: Hücre ve Bölünmeler (Öğretmen Detayında!)
        
        **Hücre:** Canlıların en küçük yapısal birimi.
        
        **1. Mitoz Bölünme:** Büyüme ve onarım. Ana hücre ile **aynı** kromozom sayısına sahip **2 yeni hücre** oluşur ($2n \\rightarrow 2n$).
        
        **2. Mayoz Bölünme:** Üreme hücrelerini oluşturmak. Kromozom sayısı **yarıya iner** ($2n \\rightarrow n$). 
        """
    elif "kütle" in topic_lower or "ağırlık" in topic_lower:
        response = """
        ## 🧠 Akıl Konu Anlatımı: Kütle ve Ağırlık İlişkisi (Öğretmen Detayında!)
        
        * **Kütle (m):** Madde miktarı. **Değişmez**. Birimi kg.
        * **Ağırlık (G):** Yer çekimi kuvveti. **Değişir**. Birimi Newton (N).
        """
        
    # ===============================================
    # 7. SINIF SOSYAL BİLGİLER KONULARI
    # ===============================================
    elif "kültür" in topic_lower or "miras" in topic_lower:
        response = """
        ## 🧠 Akıl Konu Anlatımı: Kültür ve Miras (Öğretmen Detayında!)
        
        **Kültür:** Bir toplumun maddi ve manevi tüm değerlerinin bütünüdür.
        
        **Miras:** Somut (yapılar, yemekler) ve Soyut (gelenekler, inançlar) olarak ayrılır.
        """
    elif "birey" in topic_lower or "toplum" in topic_lower or "rol" in topic_lower or "statü" in topic_lower:
        response = """
        ## 🧠 Akıl Konu Anlatımı: Birey ve Toplum (Rol ve Statü)
        
        **Statü:** Bireyin toplumdaki pozisyonu (Örn: Öğrenci).
        
        **Rol:** Statü gereği beklenen davranışlar (Örn: Öğrencinin ders çalışması).
        """
        
    # ===============================================
    # 7. SINIF DİN KÜLTÜRÜ KONULARI
    # ===============================================
    elif "melek" in topic_lower or "ahiret" in topic_lower:
        response = """
        ## 🧠 Akıl Konu Anlatımı: Melekler ve Ahiret İnancı
        
        **Melekler:** Nurdan yaratılmış, Allah'ın emirlerine itaat eden varlıklar.
        
        **Ahiret İnancı:** Dünya hayatından sonraki ebedi hayat.
        """
    elif "hac" in topic_lower or "kurban" in topic_lower or "umre" in topic_lower:
        response = """
        ## 🧠 Akıl Konu Anlatımı: Hac ve Kurban İbadeti
        
        **Hac:** İslam'ın beş şartından biri. Belirli zamanda Kâbe'yi ziyaret.
        
        **Kurban:** Allah'a yaklaşmak amacıyla hayvan kesmek. Paylaşmayı öğretir.
        """
        
    # ===============================================
    # 7. SINIF İNGİLİZCE KONULARI
    # ===============================================
    elif "appearance" in topic_lower or "personality" in topic_lower:
        response = """
        ## 🧠 Akıl Konu Anlatımı: Appearance and Personality
        
        **Appearance (Görünüş):** Dış görünüşü tarif eder. (Tall, Short, Slim)
        
        **Personality (Kişilik):** Karakteri tarif eder. (Kind, Generous)
        """
    elif "sports" in topic_lower or "biographies" in topic_lower:
        response = """
        ## 🧠 Akıl Konu Anlatımı: Sports and Biographies
        
        **Sports:** Fiillerle kullanımı: **Play** (Football), **Go** (Swimming), **Do** (Karate).
        
        **Biographies:** Hayat hikayesi anlatan metinler.
        """
        
    # ===============================================
    # DİĞER TÜM KONULAR (SOHBET ALANI VE GENEL BİLGİ)
    # ===============================================
    else:
        # Sohbet/Genel Bilgi Alanı (Artık hata vermeyecek)
        st.session_state.last_topic = topic
        
        response = f"""
        ## 💬 Genel Bilgi Modülü (Sohbet): "{topic}"
        
        Ders konuları dışında sorduğunuz **"{topic}"** ile ilgili genel bilgi modülüm şu anda aktif.
        
        **Akıl Asistanı Notu:** Size genel bir asistan olarak yardımcı olabilirim (Örn: 'Dünyanın en yüksek dağı hangisidir?').
        
        ***Unutmayın:*** Eğer 7. Sınıf konularını arıyorsanız (Örn: **Rasyonel**, **Cebirsel**, **Fiil**), lütfen sadece anahtar kelimeleri kullanın.
        """
        
    st.session_state.ai_response = response
    st.session_state.last_topic = topic

# --- 2. TÜM İÇERİKLERİN TANIMI ---
COACH_CONTENT = """
## 💡 Koç Modülü - Öğrenci Koçluğu ve Rehberlik
### 🗓️ Rehberlik Konuları
* **Zaman Yönetimi:** Günlük rutin oluşturma ve derslere ayrılan sürenin belirlenmesi.
* **Pomodoro Tekniği:** 25 dakika çalışma, 5 dakika mola tekniği ile odaklanmayı artırma.
"""

MATH_CONTENT = """
## 📘 Matematik - Konu Anlatımı ve Özet
### 1. ÜNİTE: TAM SAYILARLA İŞLEMLER
### 2. ÜNİTE: RASYONEL SAYILAR VE İŞLEMLER
### 3. ÜNİTE: CEBİRSEL İFADELERDEN EŞİTLİK VE DENKLEMLERE
### 4. ÜNİTE: ORAN ORANTIDAN YÜZDELERE
### 5. ÜNİTE: DOĞRULAR VE AÇILARDAN ÇOKGENLER, ÇEMBER VE DAİREYE
### 6. ÜNİTE: VERİ ANALİZİNDEN CİSİMLERİN FARKLI YÖNDEN GÖRÜNÜMLERİNE
"""

TURKISH_CONTENT = """
## 📝 Türkçe - Konu Anlatımı ve Özet
### 📄 Anlam Bilgisi Konuları
* Sözcükte Anlam, Cümlede Anlam, Parçada Anlam, Söz Sanatları
### 📄 Dil, Yazım ve Noktalama Konuları
* Fiiller (Eylem), Ek Fiil, Zarflar, Anlatım Bozuklukları
"""

SCIENCE_CONTENT = """
## 🧪 Fen Bilimleri - Konu Anlatımı ve Özet
### 1. ÜNİTE: GÜNEŞ SİSTEMİ VE ÖTESİ
### 2. ÜNİTE: HÜCRE VE BÖLÜNMELER
### 3. ÜNİTE: KUVVET VE ENERJİ (Kütle ve Ağırlık)
### 4. ÜNİTE: SAF MADDE VE KARIŞIMLAR
### 5. ÜNİTE: IŞIĞIN MADDE İLE ETKİLEŞİMİ
### 6. ÜNİTE: CANLILARDA ÜREME, BÜYÜME VE GELİŞME
### 7. ÜNİTE: ELEKTRİK DEVRELERİ
"""

SOCIAL_CONTENT = """
## 🌍 Sosyal Bilgiler - Konu Anlatımı ve Özet
### 1. ÜNİTE: BİREY VE TOPLUM
### 2. ÜNİTE: KÜLTÜR VE MİRAS
### 3. ÜNİTE: İNSANLAR, YERLER VE ÇEVRELER
### 4. ÜNİTE: BİLİM, TEKNOLOJİ VE TOPLUM
"""

ENGLISH_CONTENT = """
## 🗣️ İngilizce - Konu Anlatımı ve Özet
### 1. DÖNEM KONULARI
* Appearance And Personality, Sports, Biographies
### 2. DÖNEM KONULARI
* Celebrations, Dreams, Public Buildings
"""

RELIGION_CONTENT = """
## 🕌 Din Kültürü ve Ahlak Bilgisi - Konu Anlatımı ve Özet
### 1. ÜNİTE: MELEKLER VE AHİRET İNANCI
### 2. ÜNİTE: HAC VE KURBAN
### 3. ÜNİTE: AHLAKİ DAVRANIŞLAR
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
        "Konu Adını Yazınız (Örn: Rasyonel, Kütle, Fiil) VEYA Genel Bir Şey Sorun", 
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
