# Lütfen tüm app_final.py içeriğini bu kodla tamamen değiştirin.
import streamlit as st

# --- 1. STREAMLIT DURUM YÖNETİMİ (Session State) ---
if 'content_key' not in st.session_state:
    st.session_state.content_key = None 

# AI asistanı (Akıl) için durum yönetimi.
if 'ai_response' not in st.session_state:
    st.session_state.ai_response = "Konuyu yazın ve Akıl'dan Konu Anlatmasını isteyin. (Örn: Rasyonel Sayılar, Söz Sanatları, Mitoz)"
    st.session_state.last_topic = ""

# --- BUTON TIKLAMA İŞLEVLERİ ---

def toggle_content(key):
    # Manuel Konu Anlatımı Butonları için
    if st.session_state.content_key == key:
        st.session_state.content_key = None
    else:
        st.session_state.content_key = key

# YAPAY ZEKA (AKIL) FONKSİYONU - ÖĞRETMEN GİBİ DETAYLI VE UZUN METİNLER
def generate_ai_explanation(topic):
    topic_lower = topic.lower().strip()
    response = ""

    # ===============================================
    # 7. SINIF MATEMATİK KONULARI (DAHA DA UZUN VE DETAYLI)
    # ===============================================
    if "rasyonel sayılar" in topic_lower:
        response = """
        ## 🧠 Akıl Konu Anlatımı: Rasyonel Sayılar (Öğretmen Detayında!)
        
        **Tanım ve Kavramlar:** Rasyonel sayılar, $a$ bir tam sayı ve $b$ sıfırdan farklı bir tam sayı olmak üzere, $\\frac{a}{b}$ şeklinde yazılabilen sayılar kümesidir ($\\mathbb{Q}$). Her tam sayı (örneğin 5) paydası 1 olan bir rasyonel sayıdır (5/1). Ondalık gösterim ve devirli ondalık gösterimler de rasyonel sayıları ifade etmenin farklı yollarıdır.

        **Toplama ve Çıkarma İşlemleri:** Rasyonel sayılarda toplama ve çıkarma yapmanın temel kuralı, **paydaların eşit olmasıdır**. Paydalar eşitlendikten sonra, sadece paylar toplanır veya çıkarılır. Payda aynen yazılır.
        * **Örnek 1 (Eşitleme):** $\\frac{1}{2} + \\frac{1}{4}$ işleminde paydalar 4'te eşitlenir. $\\frac{1 \\cdot 2}{2 \\cdot 2} + \\frac{1}{4} = \\frac{2}{4} + \\frac{1}{4} = \\mathbf{\\frac{3}{4}}$
        * **Örnek 2 (Tam Sayılarla):** $3 - \\frac{1}{5}$ işleminde $3 = \\frac{15}{5}$ kabul edilir. $\\frac{15}{5} - \\frac{1}{5} = \\mathbf{\\frac{14}{5}}$

        **Çarpma ve Bölme İşlemleri:**
        * **Çarpma:** Paylar kendi arasında, paydalar kendi arasında çarpılır. **İşaret kuralını unutmayın!** $\\frac{2}{3} \\cdot (-\\frac{5}{7}) = \\mathbf{-\\frac{10}{21}}$
        * **Bölme:** Birinci rasyonel sayı aynen yazılır, ikinci rasyonel sayı ters çevrilir ve çarpma işlemi yapılır. $\\frac{1}{2} : \\frac{3}{4} \\rightarrow \\frac{1}{2} \\cdot \\frac{4}{3} = \\mathbf{\\frac{4}{6}} = \\mathbf{\\frac{2}{3}}$
        """
    elif "tam sayılar" in topic_lower:
        response = """
        ## 🧠 Akıl Konu Anlatımı: Tam Sayılar (Öğretmen Detayında!)
        
        **Kümeler ve Gösterim:** Tam sayılar kümesi ($\\mathbb{Z}$), doğal sayılar kümesini ($\\mathbb{N}$) de içine alan daha geniş bir kümedir. Negatif sayılar ($-1, -2, -3, ...$), pozitif sayılar ($1, 2, 3, ...$) ve nötr olan sıfır (0) tam sayıları oluşturur. Sayı doğrusunun sağ tarafı pozitif, sol tarafı negatiftir.
        
        **Çıkarma İşlemi (Kural):** Çıkarma işlemi toplama işlemine dönüştürülür ve çıkan sayının işareti ters çevrilir.
        * **Örnek:** $(-7) - (-3) \\rightarrow (-7) + (+3) = \\mathbf{-4}$ (Büyük sayıdan küçük sayı çıkarılır, büyüğün işareti alınır).
        
        **Tam Sayıların Kuvveti:**
        * **Kural:** Negatif bir tam sayının **çift kuvvetleri pozitif** olurken, **tek kuvvetleri negatif** olur. Bu kural parantezli kullanımlarda geçerlidir.
        * **Örnek:** $(-5)^2 = +25$, $(-5)^3 = -125$. **DİKKAT:** Parantezsiz durumda $-2^4 = -16$ (çünkü eksi işareti etkilenmez).
        """
    elif "cebirsel ifadeler" in topic_lower:
        response = """
        ## 🧠 Akıl Konu Anlatımı: Cebirsel İfadeler (Öğretmen Detayında!)
        
        **Tanım ve Yapı:** Cebirsel ifadeler, en az bir değişken (bilinmeyen) ve en az bir işlem içeren matematiksel ifadelerdir. Örneğin, 'Bir sayının 3 katının 5 fazlası' ifadesi $\\mathbf{3x + 5}$ şeklinde gösterilir. Toplama ve çıkarma yapılırken sadece **benzer terimler** (değişkeni ve üssü aynı olanlar) toplanıp çıkarılabilir.

        **Temel Kavramların Ayrımı:** Cebirsel ifadeleri anlamak için bu terimleri çok iyi bilmelisiniz:
        1.  **Değişken (Bilinmeyen):** $x, y, a$ gibi harflerle gösterilen ve değeri değişebilen semboldür.
        2.  **Katsayı:** Değişkenin önündeki çarpım durumunda olan sayıdır. ($\mathbf{4}x - 7$'de $x$'in katsayısı $4$'tür.)
        3.  **Sabit Terim:** Yanında değişken bulunmayan sayıdır. ($\mathbf{4x - 7}$'de sabit terim $\mathbf{-7}$'dir.)
        4.  **Terim:** Bir cebirsel ifadede artı (+) veya eksi (-) işaretleriyle ayrılmış her bir kısım bir terimdir. ($4x - 7$ ifadesi iki terimlidir: $4x$ ve $-7$.)
        """
    
    # ===============================================
    # 7. SINIF TÜRKÇE KONULARI (DAHA DA UZUN VE DETAYLI)
    # ===============================================
    elif "fiiller" in topic_lower or "ek fiil" in topic_lower or "zarflar" in topic_lower:
        response = """
        ## 🧠 Akıl Konu Anlatımı: Fiiller, Ek Fiil ve Zarflar (Öğretmen Detayında!)
        
        **Fiiller (Eylemler):** Bir iş, oluş veya durum bildiren kelimelerdir. Fiiller anlamlarına göre:
        1.  **İş (Kılış) Fiilleri:** Öznenin iradesiyle gerçekleşir ve nesne alabilirler. (Neyi, Kimi?) $\rightarrow$ **Okumak** (Kitabı okumak).
        2.  **Oluş Fiilleri:** Öznenin iradesi dışında, kendiliğinden zamanla gerçekleşir. $\rightarrow$ **Büyümek**, **Paslanmak**.
        3.  **Durum Fiilleri:** Öznenin içinde bulunduğu durumu bildirir, nesne almazlar. $\rightarrow$ **Uyumak**, **Gülmek**.
        
        **Ek Fiil (Ek Eylem):** 'İmek' fiilidir. İki hayati görevi vardır:
        1.  **İsimleri Yüklem Yapmak:** 'Burası dünkü maçın **yeriydi**.' (yer-i-idi)
        2.  **Basit Zamanlı Fiili Birleşik Zamanlı Yapmak:** 'Güneş her gün **doğuyormuş**.' (Şimdiki zamanın rivayeti)
        
        **Zarflar (Belirteçler):** Fiilin nasıl, ne zaman, ne kadar ve nereye yapıldığını belirten sözcüklerdir.
        * **Durum (Hal) Zarfları (Nasıl?):** 'Çocuk **hızlı** koşuyor.'
        * **Zaman Zarfları (Ne zaman?):** 'Misafirler **az önce** geldi.'
        * **Yer-Yön Zarfları (Nereye?):** 'Dışarı **çık**.'
        """
    elif "söz sanatları" in topic_lower:
        response = """
        ## 🧠 Akıl Konu Anlatımı: Söz Sanatları (Öğretmen Detayında!)
        
        Anlatıma güzellik, çekicilik ve etki gücü katan sanatlardır.
        
        **1. Benzetme (Teşbih):** Zayıf bir varlığın, ortak özellik bakımından güçlü bir varlığa benzetilmesidir. Dört temel ögesi vardır: benzeyen, benzetilen, benzetme yönü, benzetme edatı.
        * **Örnek:** 'Çocuğun dişleri **inci gibi** parlıyordu.' (Benzeyen: diş, Benzetilen: inci, Benzetme Yönü: parlaklık, Benzetme Edatı: gibi)
        
        **2. Kişileştirme (Teşhis):** İnsan dışındaki varlıklara insan özellikleri yüklenmesidir.
        * **Örnek:** 'Yorgun **bulutlar** şehre gözyaşı **döktü**.' (Ağlamak ve yorgunluk, bulutlara ait özelliklerdir.)
        
        **3. Abartma (Mübalağa):** Bir durumu, inandırıcı olmayacak derecede büyütmek veya küçültmek.
        * **Örnek:** 'Sana dünyalar kadar **ödev** verdim.' (Çokluk abartılmıştır.)
        """

    # ===============================================
    # 7. SINIF FEN BİLİMLERİ KONULARI (DAHA DA UZUN VE DETAYLI)
    # ===============================================
    elif "hücre" in topic_lower or "mitoz" in topic_lower or "mayoz" in topic_lower:
        response = """
        ## 🧠 Akıl Konu Anlatımı: Hücre ve Bölünmeler (Öğretmen Detayında!)
        
        **Hücre:** Canlıların en küçük yapısal ve işlevsel birimidir. Hayvan hücresi ve bitki hücresi arasında organel farkları vardır (Bitkide hücre duvarı, kloroplast, büyük koful bulunur).
        
        **1. Mitoz Bölünme:**
        * **Amaç:** Büyüme, gelişme, yıpranan doku ve organların onarımı. Tek hücrelilerde üremeyi sağlar.
        * **Sonuç:** Ana hücre ile **aynı** kromozom sayısına ve genetik yapıya sahip **2 yeni hücre** oluşur ($2n \\rightarrow 2n$).
        
        **2. Mayoz Bölünme:**
        * **Amaç:** Eşeyli üreme için **üreme hücrelerini (gamet)** oluşturmak.
        * **Sonuç:** Kromozom sayısı **yarıya iner** ve genetik yapısı farklı **4 yeni hücre** oluşur ($2n \\rightarrow n$). Mayoz, krossing over (parça değişimi) ile **tür içi çeşitliliği** sağlar.
        """
    elif "kütle ve ağırlık" in topic_lower:
        response = """
        ## 🧠 Akıl Konu Anlatımı: Kütle ve Ağırlık İlişkisi (Öğretmen Detayında!)
        
        Bu iki fiziksel kavram arasındaki ayrımı netleştirelim. Aralarındaki fark, kütlenin değişmez, ağırlığın ise kuvvete bağlı olarak değişir olmasıdır.
        
        * **Kütle (m):** Bir cisimdeki madde miktarıdır. Evrenin neresine giderseniz gidin **değişmez**. Ölçüm aracı **eşit kollu terazi**dir. Birimi kilogramdır (kg).
        * **Ağırlık (G):** Kütleye etki eden **yer çekimi kuvvetidir**. Bu kuvvet, gezegenlere göre değişir. Ölçüm aracı **dinamometre**dir. Birimi Newton (N)'dur.
        
        **Örnek:** Kütlesi 70 kg olan bir öğrencinin Dünya'daki kütlesi de 70 kg, Ay'daki kütlesi de 70 kg'dır. Ancak Dünya'daki ağırlığı $\\approx 700$ N iken, Ay'daki ağırlığı $\\approx 117$ N'dur (çünkü Ay'ın çekimi Dünya'nın $\\frac{1}{6}$'sı kadardır).
        """
        
    # ===============================================
    # 7. SINIF SOSYAL BİLGİLER KONULARI (DAHA DA UZUN VE DETAYLI)
    # ===============================================
    elif "kültür ve miras" in topic_lower:
        response = """
        ## 🧠 Akıl Konu Anlatımı: Kültür ve Miras (Öğretmen Detayında!)
        
        **Kültür:** Bir toplumun tarih boyunca ürettiği maddi (somut) ve manevi (soyut) tüm değerlerin bütünüdür. Bir toplumun yaşam tarzını, inançlarını, sanatını ve geleneklerini kapsar.
        
        **Kültürel Mirasın Unsurları:**
        1.  **Somut Miras (Maddi):** Gözle görülebilen, elle tutulabilen eserlerdir. Mimari yapılar (cami, saray), kıyafetler, yemekler, aletler ve tarihi eserler bu gruba girer. **Örnek:** Ayasofya Cami, Türk kahvesi.
        2.  **Soyut Miras (Manevi):** Gelenekler, sözlü anlatımlar, dil, inançlar, halk oyunları ve törenlerdir. **Örnek:** Hacivat ve Karagöz gölge oyunu, Alevi-Bektaşi semahı.
        
        Bu mirasları korumak, bir milleti millet yapan değerleri geleceğe taşımaktır.
        """
    elif "birey ve toplum" in topic_lower:
        response = """
        ## 🧠 Akıl Konu Anlatımı: Birey ve Toplum (Rol ve Statü)
        
        Bireyler, toplum içinde doğar ve toplumun bir parçası olur. Toplum içindeki yerimizi ve görevlerimizi **Statü** ve **Rol** kavramları belirler.
        
        **Statü:** Bireyin toplum içindeki pozisyonudur. Statü, kazanılmış (çalışarak elde edilen, Örn: Doktor) veya doğuştan (cinsiyet, ırk, Örn: Evlat) olabilir.
        
        **Rol:** Bireyin sahip olduğu statü gereği sergilemesi beklenen davranışlardır. Her statünün bir rolü vardır.
        * **Örnek:** Yusuf Efe'nin Statüsü: **Öğrenci** $\\rightarrow$ Rolü: **Ders çalışmak, okula gitmek, saygılı olmak.**
        * **Örnek:** Annenizin/Babanızın Statüsü: **Ebeveyn** $\\rightarrow$ Rolü: **Çocuğuna bakmak, eğitim vermek, rehberlik etmek.**
        
        Rollerinizi doğru oynamak, toplumun düzenini sağlamak için önemlidir.
        """
        
    # ===============================================
    # DİĞER TÜM KONULAR REDDEDİLİR (Sohbet Yasağı)
    # ===============================================
    else:
        response = f"""
        ## ⚠️ Akıl Asistan Uyarısı
        
        **'{topic[:20].upper() + ('...' if len(topic) > 20 else '')}'** şu an için anlatabileceğim konular arasında değildir. 
        
        Ben sadece 7. Sınıf **Matematik, Türkçe Dil Bilgisi, Fen ve Sosyal Bilgiler** ana konularını **detaylı** anlatmak üzere programlanmış bir öğrenci asistanıyım ve **sohbet özelliğim kapalıdır.** Lütfen bu derslerin konularından birini yazınız.
        """
        
    st.session_state.ai_response = response
    st.session_state.last_topic = topic

# --- 2. TÜM İÇERİKLERİN YENİ VE DETAYLI TANIMI (Önceki Adımdan) ---
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
        "Konu Adını Yazınız (Örn: Rasyonel Sayılar, Söz Sanatları, Mitoz)", 
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
