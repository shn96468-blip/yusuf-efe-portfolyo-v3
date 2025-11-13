import streamlit as st

# --- 1. STREAMLIT DURUM YÖNETİMİ (Session State) ---
if 'content_key' not in st.session_state:
    st.session_state.content_key = None 

# AI asistanı (Akıl) için durum yönetimi.
if 'ai_response' not in st.session_state:
    st.session_state.ai_response = "Konuyu yazın ve Akıl'dan Konu Anlatmasını isteyin. (Örn: Rasyonel Sayılar, Melekler, Personality) veya Genel Konular Sorun."
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
        
        **Tanım ve Kavramlar:** Rasyonel sayılar, $a$ bir tam sayı ve $b$ sıfırdan farklı bir tam sayı olmak üzere, $\\frac{a}{b}$ şeklinde yazılabilen sayılar kümesidir ($\\mathbb{Q}$). Her tam sayı (örneğin 5) paydası 1 olan bir rasyonel sayıdır (5/1). Ondalık gösterim ve devirli ondalık gösterimler de rasyonel sayıları ifade etmenin farklı yollarıdır.

        **Toplama ve Çıkarma İşlemleri:** Rasyonel sayılarda toplama ve çıkarma yapmanın temel kuralı, **paydaların eşit olmasıdır**. Paydalar eşitlendikten sonra, sadece paylar toplanır veya çıkarılır. Payda aynen yazılır.
        * **Örnek 1 (Eşitleme):** $\\frac{1}{2} + \\frac{1}{4}$ işleminde paydalar 4'te eşitlenir. $\\frac{1 \\cdot 2}{2 \\cdot 2} + \\frac{1}{4} = \\frac{2}{4} + \\frac{1}{4} = \\mathbf{\\frac{3}{4}}$
        * **Örnek 2 (Tam Sayılarla):** $3 - \\frac{1}{5}$ işleminde $3 = \\frac{15}{5}$ kabul edilir. $\\frac{15}{5} - \\frac{1}{5} = \\mathbf{\\frac{14}{5}}$
        """
    elif "tam sayı" in topic_lower:
        response = """
        ## 🧠 Akıl Konu Anlatımı: Tam Sayılar (Öğretmen Detayında!)
        
        **Kümeler ve Gösterim:** Tam sayılar kümesi ($\\mathbb{Z}$), doğal sayılar kümesini ($\\mathbb{N}$) de içine alan daha geniş bir kümedir. Negatif sayılar ($-1, -2, -3, ...$), pozitif sayılar ($1, 2, 3, ...$) ve nötr olan sıfır (0) tam sayıları oluşturur. Sayı doğrusunun sağ tarafı pozitif, sol tarafı negatiftir.
        
        **Çıkarma İşlemi (Kural):** Çıkarma işlemi toplama işlemine dönüştürülür ve çıkan sayının işareti ters çevrilir.
        * **Örnek:** $(-7) - (-3) \\rightarrow (-7) + (+3) = \\mathbf{-4}$ 
        """
    elif "cebirsel" in topic_lower or "ifadeler" in topic_lower:
        response = """
        ## 🧠 Akıl Konu Anlatımı: Cebirsel İfadeler (Öğretmen Detayında!)
        
        **Tanım ve Yapı:** Cebirsel ifadeler, en az bir değişken (bilinmeyen) ve en az bir işlem içeren matematiksel ifadelerdir. Örneğin, 'Bir sayının 3 katının 5 fazlası' ifadesi $\\mathbf{3x + 5}$ şeklinde gösterilir. Toplama ve çıkarma yapılırken sadece **benzer terimler** (değişkeni ve üssü aynı olanlar) toplanıp çıkarılabilir.

        **Temel Kavramların Ayrımı:** Cebirsel ifadeleri anlamak için bu terimleri çok iyi bilmelisiniz:
        1.  **Değişken (Bilinmeyen):** $x, y, a$ gibi harflerle gösterilen semboldür.
        2.  **Katsayı:** Değişkenin önündeki sayıdır. 
        3.  **Sabit Terim:** Yanında değişken bulunmayan sayıdır. 
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
        
        **Fiiller (Eylemler):** Bir iş, oluş veya durum bildiren kelimelerdir. 
        
        **Ek Fiil (Ek Eylem):** 'İmek' fiilidir. İki hayati görevi vardır: İsimleri yüklem yapmak veya Basit Zamanlı Fiili Birleşik Zamanlı Yapmak.
        
        **Zarflar (Belirteçler):** Fiilin nasıl, ne zaman, ne kadar ve nereye yapıldığını belirten sözcüklerdir.
        * **Örnek (Durum):** 'Çocuk **hızlı** koşuyor.'
        """
    elif "söz sanatları" in topic_lower or "benzetme" in topic_lower or "abartma" in topic_lower:
        response = """
        ## 🧠 Akıl Konu Anlatımı: Söz Sanatları (Öğretmen Detayında!)
        
        **1. Benzetme (Teşbih):** Zayıf bir varlığın güçlü bir varlığa benzetilmesi. 
        * **Örnek:** 'Çocuğun dişleri **inci gibi** parlıyordu.'
        
        **2. Kişileştirme (Teşhis):** İnsan dışındaki varlıklara insan özellikleri yüklenmesi.
        * **Örnek:** 'Yorgun **bulutlar** şehre gözyaşı **döktü**.' 
        """

    # ===============================================
    # 7. SINIF FEN BİLİMLERİ KONULARI
    # ===============================================
    elif "hücre" in topic_lower or "mitoz" in topic_lower or "mayoz" in topic_lower:
        response = """
        ## 🧠 Akıl Konu Anlatımı: Hücre ve Bölünmeler (Öğretmen Detayında!)
        
        **Hücre:** Canlıların en küçük yapısal ve işlevsel birimidir.
        
        **1. Mitoz Bölünme:** Büyüme ve onarım için. Ana hücre ile **aynı** kromozom sayısına sahip **2 yeni hücre** oluşur ($2n \\rightarrow 2n$).
        
        **2. Mayoz Bölünme:** Üreme hücrelerini oluşturmak için. Kromozom sayısı **yarıya iner** ve genetik yapısı farklı **4 yeni hücre** oluşur ($2n \\rightarrow n$). 
        """
    elif "kütle" in topic_lower or "ağırlık" in topic_lower:
        response = """
        ## 🧠 Akıl Konu Anlatımı: Kütle ve Ağırlık İlişkisi (Öğretmen Detayında!)
        
        * **Kütle (m):** Madde miktarıdır. **Değişmez**. Ölçüm aracı **eşit kollu terazi**dir. Birimi kilogramdır (kg).
        * **Ağırlık (G):** Kütleye etki eden **yer çekimi kuvvetidir**. Gezegenlere göre **değişir**. Ölçüm aracı **dinamometre**dir. Birimi Newton (N)'dur.
        """
        
    # ===============================================
    # 7. SINIF SOSYAL BİLGİLER KONULARI
    # ===============================================
    elif "kültür" in topic_lower or "miras" in topic_lower:
        response = """
        ## 🧠 Akıl Konu Anlatımı: Kültür ve Miras (Öğretmen Detayında!)
        
        **Kültür:** Bir toplumun tarih boyunca ürettiği maddi ve manevi tüm değerlerin bütünüdür.
        
        **Kültürel Mirasın Unsurları:**
        1.  **Somut Miras (Maddi):** Gözle görülebilen eserler (Mimari, yemekler).
        2.  **Soyut Miras (Manevi):** Gelenekler, sözlü anlatımlar, inançlar.
        """
    elif "birey" in topic_lower or "toplum" in topic_lower or "rol" in topic_lower or "statü" in topic_lower:
        response = """
        ## 🧠 Akıl Konu Anlatımı: Birey ve Toplum (Rol ve Statü)
        
        **Statü:** Bireyin toplum içindeki pozisyonudur (Örn: Öğrenci).
        
        **Rol:** Sahip olunan statü gereği sergilenmesi beklenen davranışlardır (Örn: Öğrencinin ders çalışması).
        """
        
    # ===============================================
    # 7. SINIF DİN KÜLTÜRÜ KONULARI
    # ===============================================
    elif "melek" in topic_lower or "ahiret" in topic_lower:
        response = """
        ## 🧠 Akıl Konu Anlatımı: Melekler ve Ahiret İnancı
        
        **Melekler:** Nurdan yaratılmış, Allah'ın emirlerine itaat eden varlıklardır. (Cebrail, Mikail, İsrafil, Azrail)
        
        **Ahiret İnancı:** Dünya hayatından sonraki ebedi hayattır. Bu inanç, insanın davranışlarına yön verir.
        """
    elif "hac" in topic_lower or "kurban" in topic_lower or "umre" in topic_lower:
        response = """
        ## 🧠 Akıl Konu Anlatımı: Hac ve Kurban İbadeti
        
        **Hac:** İslam'ın beş şartından biri olup, imkan bulan Müslümanların Kâbe'yi ziyaret etmesidir. Belirli zamanlarda (Zilhicce) yapılır.
        
        **Kurban:** Allah'a yaklaşmak amacıyla, belirli şartları taşıyan hayvanı usulüne uygun kesmektir. Paylaşmayı öğretir.
        """
        
    # ===============================================
    # 7. SINIF İNGİLİZCE KONULARI
    # ===============================================
    elif "appearance" in topic_lower or "personality" in topic_lower:
        response = """
        ## 🧠 Akıl Konu Anlatımı: Appearance and Personality
        
        **Appearance (Görünüş):** Bir kişinin dış görünüşünü tarif etmek için kullanılır. (Tall, Short, Slim, Curly Hair)
        
        **Personality (Kişilik):** Bir kişinin karakterini tarif etmek için kullanılır. (Kind, Generous, Stubborn)
        """
    elif "sports" in topic_lower or "biographies" in topic_lower:
        response = """
        ## 🧠 Akıl Konu Anlatımı: Sports and Biographies
        
        **Sports (Sporlar):** Fiillerle birlikte kullanımı önemlidir: **Play** (Football), **Go** (Swimming), **Do** (Karate).
        
        **Biographies (Biyografiler):** Bir kişinin hayat hikayesini anlatan metinlerdir. Genellikle **Simple Past Tense (Geçmiş Zaman)** kullanılır.
        """
        
    # ===============================================
    # DİĞER TÜM KONULAR (SOHBET ALANI VE GENEL BİLGİ)
    # ===============================================
    else:
        # Bu kısım, ders konuları dışındaki tüm genel sorulara cevap verecek
        st.session_state.last_topic = topic
        
        # Google Search aracını kullanarak genel bir arama yapıp sonucu döndürelim.
        # Bu, Akıl Asistanı'nın genel bilgiye de erişebilmesini sağlar.
        try:
            search_result = google:search(queries=[topic])
            
            # Arama sonuçlarından ilkini alıp yanıt olarak kullanma
            if search_result:
                # Sonucu daha anlaşılır bir formatta sunalım
                response = f"""
                ## 💬 Genel Bilgi Modülü (Sohbet): "{topic}"
                
                Ders konuları dışında sorduğunuz **"{topic}"** ile ilgili bulabildiğim en alakalı bilgi:
                
                ---
                
                **Sonuç Özeti:**
                {search_result}
                
                ---
                
                **NOT:** Ben öncelikle bir öğrenci asistanıyım. Eğer 7. Sınıf konularını arıyorsanız, lütfen sadece **Rasyonel**, **Cebirsel**, **Fiil** veya **Kütle** gibi dersin anahtar kelimesini yazın.
                """
            else:
                 response = f"""
                ## 💬 Genel Bilgi Modülü (Sohbet)
                
                Ders konuları dışında sorduğunuz **"{topic}"** ile ilgili ne yazık ki bir bilgi bulamadım. Lütfen farklı bir ifadeyle tekrar deneyin.
                """
        except:
             response = f"""
            ## 💬 Genel Bilgi Modülü (Sohbet)
            
            Sistem şu anda genel arama yapamıyor. Lütfen sadece 7. Sınıf konularını (Örn: **Rasyonel**, **Fiil**, **Mitoz**) yazmayı deneyin.
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
* Tam Sayılarla Toplama, Çıkarma, Çarpma ve Bölme İşlemi, Tam Sayıların Kuvveti, Tam Sayı Problemleri

### 2. ÜNİTE: RASYONEL SAYILAR VE İŞLEMLER
* Rasyonel Sayılar (Gösterimi, Sıralaması), Rasyonel Sayılarla İşlemler

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

### 5. ÜNİTE: IŞIĞIN MADDE İLE ETKİLEŞİMİ
* Işığın Soğurulması, Aynalar, Işığın Kırılması ve Mercekler

### 6. ÜNİTE: CANLILARDA ÜREME, BÜYÜME VE GELİŞME
* İnsanda Ürüme, Büyüme ve Gelişme, Bitki ve Hayvanlarda Üreme, Büyüme ve Gelişme

### 7. ÜNİTE: ELEKTRİK DEVRELERİ
* Ampullerin Bağlanma Şekilleri
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
