import streamlit as st
import time

# --- SAYFA VE TEMA AYARLARI ---
st.set_page_config(
    page_title="Yusuf Efe Şahin | Portfolyo",
    layout="wide",
    page_icon="💼",
    initial_sidebar_state="expanded"
)

# Koyu Temayı zorlamak için CSS enjeksiyonu
# Not: Görseldeki butonların turuncu kenarlık ve elmas simgeleri için özel CSS enjeksiyonu gerekiyor,
# ancak Streamlit'in standart yapısını koruyarak sadece metin ve ikonları düzenliyoruz.
st.markdown(
    """
    <style>
    /* Genel koyu arkaplan ve renk ayarları korundu */
    .stApp {
        background-color: #0E1117; 
        color: white;
    }
    .css-1d391kg { 
        background-color: #0E1117;
    }
    h1, h2, h3, h4, h5, h6 {
        color: #FF4B4B; 
    }
    .stTextInput, .stTextArea, .stSelectbox {
        background-color: #262730;
        color: white;
        border: 1px solid #31333F;
    }
    .stButton>button {
        color: white;
        border-color: #FF4B4B;
    }
    
    /* Görseldeki buton kenarlıkları için özel stil ekliyoruz */
    .stButton>button {
        color: white;
        border-color: #FF4B4B; /* Kırmızı/Turuncu ton */
        border-width: 2px;
        font-weight: bold;
    }
    
    /* Özel Buton Stili (Hover/Focus) */
    .stButton>button:focus:not(:active) {
        border-color: #FF4B4B; 
        color: #FF4B4B;
        box-shadow: 0 0 0 0.2rem rgba(255, 75, 75, 0.25);
    }
    
    /* Konu kutusu stili (Görseldeki mavi kutu) */
    .stAlert {
        background-color: #1E3147 !important; /* Mavi-Koyu Ton */
        color: white !important;
        border-left: 5px solid #FF4B4B !important; /* Kırmızı vurgu */
    }
    
    /* Konu kutusunun ikonunu ve başlığını hizalama */
    .css-1f9e236.e1qvo95c1 { /* Streamlit Info/Warning/Success div'inin içindeki metin */
        font-size: 1.1rem;
        font-weight: 600;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- OTURUM DURUMU (SESSION STATE) BAŞLANGIÇ AYARLARI ---
ADMIN_PASSWORD = "123" 

# 7. SINIF DERS VERİLERİ (Konu Anlatımı ve Quiz/Test Soruları)
DEFAULT_DERSLER = {
    "Matematik": {
        "konu": "7. Sınıf Matematik Tüm Üniteler", 
        "anlatim": """7. Sınıf Matematik dersi 6 ana üniteden oluşmaktadır:
        
* **1. Ünite (Tam Sayılar):** Pozitif ve negatif tam sayılarla toplama, çıkarma, çarpma ve bölme işlemleri, üslü ifadeler. **Örnek:** $-5 + 8 = 3$, $4 \cdot (-2) = -8$.
* **2. Ünite (Rasyonel Sayılar):** Rasyonel sayı kavramı, rasyonel sayılarla dört işlem. Kesirlerin ondalık gösterimi.
* **3. Ünite (Cebirsel İfadeler):** Cebirsel ifadelerin anlamı, değerini hesaplama, eşitlik ve denklem çözümü. **Örnek:** $2x + 5 = 15$ denkleminin çözümü.
* **4. Ünite (Oran ve Orantı):** Oran, orantı, doğru ve ters orantı, yüzdeler.
* **5. Ünite (Geometri):** Doğrular ve Açılar, Çokgenler (alan/çevre), Çember ve Daire.
* **6. Ünite (Veri İşleme):** Veri analizi, çizgi ve sütun grafikleri, daire grafiği, cisimlerin farklı yönlerden görünümleri.

Bu konular, lise matematiği için sağlam bir temel oluşturur.""", 
        "sorular": [
            {"q": " $(-5) + (+8)$ işleminin sonucu kaçtır?", "a": ["$-13$", "$+3$", "$-3$", "$+13$"], "c": "$+3$"},
            {"q": " $(-4) \\cdot (-2)$ işleminin sonucu kaçtır?", "a": ["$-8$", "$+8$", "$0$", "$+2$"], "c": "$+8$"},
            {"q": " $20 \\div (-5)$ işleminin sonucu kaçtır?", "a": ["$4$", "$-4$", "$25$", "$-25$"], "c": "$-4$"},
        ],
        "koc_anlatimi": """
**Tam Sayılarda Dört İşlem (Detaylı Anlatım)**

1.  **Toplama İşlemi:**
    * **Aynı İşaretliler:** Değerler toplanır, ortak işaret sonuca konur.
        * **Örnek 1:** $+5 + (+3) = +8$
        * **Örnek 2:** $-5 + (-3) = -8$
    * **Farklı İşaretliler:** Mutlak değeri büyük olandan küçük olan çıkarılır ve mutlak değeri büyük olanın işareti sonuca konur.
        * **Örnek 3:** $+8 + (-3) = +5$ (8'den 3 çıkarıldı, büyük olan 8'in işareti +)
        * **Örnek 4:** $-10 + (+4) = -6$ (10'dan 4 çıkarıldı, büyük olan 10'un işareti -)

2.  **Çıkarma İşlemi:** Çıkarma işlemi, çıkan sayının işaretini değiştirip toplama işlemine dönüştürülür.
    * **Örnek 5:** $7 - (-2)$ işleminde, $-2$ nin işareti $+2$ olur. Sonuç: $7 + 2 = 9$.
    * **Örnek 6:** $-5 - (+3)$ işleminde, $+3$ ün işareti $-3$ olur. Sonuç: $-5 + (-3) = -8$.

3.  **Çarpma ve Bölme İşlemi:** İşaret kuralları çok basittir:
    * **Aynı İşaretliler:** Sonuç her zaman **Pozitiftir** ($+\cdot+=+$, $-\cdot-=+$).
    * **Farklı İşaretliler:** Sonuç her zaman **Negatiftir** ($+\cdot-=-$, $-\cdot+=-$).
    * **Örnek 7 (Çarpma):** $(-6) \cdot (-3) = +18$ (Aynı işaret)
    * **Örnek 8 (Bölme):** $15 \div (-5) = -3$ (Farklı işaret)
"""
    },
    "Türkçe": {
        "konu": "7. Sınıf Türkçe Tüm Konular",
        "anlatim": """7. Sınıf Türkçe dersi temel olarak Anlam Bilgisi ve Dil Bilgisi olmak üzere iki ana başlıkta incelenir:

* **Anlam Bilgisi:** Sözcükte, cümlede ve parçada anlam, tablo/grafik yorumlama, metin türleri ve söz sanatları.
* **Dil Bilgisi:** Fiiller (Eylemler), Ek Fiil, Zarflar, Anlatım Bozuklukları.
* **Yazım ve Noktalama:** Yazım Kuralları ve Noktalama İşaretleri.

Bu konular, öğrencilerin hem okuduğunu anlama hem de doğru ve etkili yazma becerilerini geliştirir.""",
        "sorular": [
            {"q": " 'Zengin' kelimesinin zıt anlamlısı nedir?", "a": ["Varlıklı", "Fakir", "Varlığa", "Cimri"], "c": "Fakir"},
            {"q": " Aşağıdaki kelime çiftlerinden hangisi eş anlamlıdır?", "a": ["Gürültü - Sessiz", "Hürriyet - Özgürlük", "İleri - Geri", "Aç - Tok"], "c": "Hürriyet - Özgürlük"},
            {"q": " Aşağıdaki cümlelerin hangisinde mecaz anlamlı bir sözcük kullanılmıştır?", "a": ["Ağacın dallarını budadı.", "Bütün sınıf ona güldü.", "Dün akşam bize geldi.", "Olayın sıcaklığını koruyor."], "c": "Olayın sıcaklığını koruyor."},
        ],
        "koc_anlatimi": """
**Fiil (Eylem) Nedir ve Yapı Özellikleri:**

Fiiller, cümlede bir işi, oluşu veya hareketi zaman ve kişiye bağlı olarak bildiren kelimelerdir. Fiillerin yapıları üç ana başlıkta incelenir:

1.  **Basit Fiiller:** Yapım eki almamış, sadece çekim eki (kip ve kişi eki) almış fiillerdir.
    * **Örnekler:** *gel-di*, *yaz-ıyor*, *oku-malıyız*. (Burada sadece zaman ve kişi eki var.)

2.  **Türemiş Fiiller:** İsim veya fiil köklerine yapım eki getirilerek oluşturulan fiillerdir.
    * **Örnek 1:** *göz (isim)* + *-le* $\rightarrow$ *gözle-* (gözlemek)
    * **Örnek 2:** *yaz (fiil)* + *-dır* $\rightarrow$ *yazdır-* (yazdırmak)
    * *Örnek Cümle:* Kitaplarını başkasına **yazdırdı**.

3.  **Birleşik Fiiller:** İki veya daha fazla kelimenin birleşmesiyle oluşan fiillerdir. Üç çeşidi vardır:
    * **Kurallı Birleşik Fiiller (Yeterlik, Tezlik, Sürerlik, Yaklaşma):** *gel-ebilmek*, *git-ivermek*, *bak-akalmak*.
    * **Yardımcı Fiille Kurulanlar:** *etmek, olmak, eylemek, kılmak* gibi yardımcı fiillerle kurulur. (*hasta olmak, yardım etmek*)
    * **Anlamca Kaynaşmış (Deyimleşmiş):** Deyimler. (*gözden düşmek, kulak vermek*)
"""
    },
    "Fen Bilimleri": {
        "konu": "7. Sınıf Fen Bilimleri Tüm Üniteler",
        "anlatim": """7. Sınıf Fen Bilimleri dersi, madde, enerji, canlılar ve uzay konularını kapsayan 7 ana üniteden oluşur:

* **1. Ünite:** Güneş Sistemi ve Ötesi (Uzay Araştırmaları, Gök Cisimleri)
* **2. Ünite:** Hücre ve Bölünmeler (Mitoz, Mayoz)
* **3. Ünite:** Kuvvet ve Enerji (Kütle, Ağırlık, İş ve Enerji Dönüşümleri)
* **4. Ünite:** Saf Madde ve Karışımlar (Tanecikli Yapı, Saf Maddeler, Karışımların Ayrılması)
* **5. Ünite:** Işığın Madde İle Etkileşimi (Soğurulma, Aynalar, Kırılma ve Mercekler)
* **6. Ünite:** Canlılarda Üreme, Büyüme ve Gelişme (İnsan, Bitki ve Hayvanlarda)
* **7. Ünite:** Elektrik Devreleri (Ampullerin Bağlanma Şekilleri)

Bu konular, temel bilimsel düşünme becerilerini geliştirir.""",
        "sorular": [
            {"q": " Atomun çekirdeğinde bulunan pozitif yüklü parçacık hangisidir?", "a": ["Elektron", "Nötron", "Proton", "Molekül"], "c": "Proton"},
            {"q": " Periyodik sistemde elementler neye göre sıralanmıştır?", "a": ["Kütle numarası", "Yoğunluk", "Atom numarası", "Atom ağırlığı"], "c": "Atom numarası"},
        ],
        "koc_anlatimi": """
**Mitoz ve Mayoz Bölünme Farkları (Örneklerle)**

Hücre bölünmesi, canlılarda büyüme, üreme ve onarım amaçlı gerçekleşir. İki temel tipi vardır:

1.  **Mitoz Bölünme:**
    * **Görüldüğü Yer:** Vücut (somatik) hücrelerinde (deri, karaciğer vb.).
    * **Amaç:** Büyüme, gelişme ve yaraları onarma. Tek hücrelilerde üreme.
    * **Kromozom Sayısı:** Sabit kalır ($2n \rightarrow 2n$ veya $n \rightarrow n$).
    * **Oluşan Hücre Sayısı:** 2 yeni hücre oluşur.
    * **Kalıtsal Çeşitlilik:** Oluşan hücreler **ana hücreyle aynı** kalıtsal yapıdadır (Çeşitlilik YOK).
    * **Örnek:** Parmağınız kesildiğinde yaranın iyileşmesi.

2.  **Mayoz Bölünme:**
    * **Görüldüğü Yer:** Üreme ana hücrelerinde (erkekte sperm ana hücresi, dişide yumurta ana hücresi).
    * **Amaç:** Eşeyli üremeyi sağlamak.
    * **Kromozom Sayısı:** Yarıya iner ($2n \rightarrow n$).
    * **Oluşan Hücre Sayısı:** 4 yeni hücre oluşur.
    * **Kalıtsal Çeşitlilik:** Oluşan hücreler **farklı** kalıtsal yapıdadır (Kalıtsal Çeşitlilik VAR).
    * **Örnek:** Bir insanın üreme hücrelerinin oluşması.
"""
    },
    "Din Kültürü ve Ahlak Bilgisi": { 
        "konu": "7. Sınıf Din Kültürü Tüm Üniteler", 
        "anlatim": """7. Sınıf Din Kültürü ve Ahlak Bilgisi dersi 5 ana üniteden oluşmaktadır:
        
* **1. Ünite (Melekler ve Ahiret İnancı):** İmanın şartlarından biri olan ahiret inancının önemi. Ahiret hayatının aşamaları (kıyamet, haşir, mizan) ve görevli melekler (Cebrail-vahiy, Mikail-tabiat, İsrafil-sûr, Azrail-ölüm). Nâs Suresi'nin anlamı.
* **2. Ünite (Hac ve Kurban):** İslam'ın beş şartından biri olan Hac ibadeti, Umre ve Kurban ibadetinin anlamı ve yapılışı. Hz. İsmail'in hayatı.
* **3. Ünite (Ahlaki Davranışlar):** Doğruluk, dürüstlük, adalet gibi güzel ahlaki tutumlar. Hz. Salih'in hayatından örnekler. Felak Suresi'nin anlamı.
* **4. Ünite (Hz. Muhammed s.a.v.):** Peygamberimizin örnek şahsiyeti, tevazu ve güvenilirliği. Kâfirun Suresi'nin anlamı.
* **5. Ünite (İslam Düşüncesinde Yorumlar):** Mezheplerin ve tasavvufi yorumların ortaya çıkış sebepleri.

Bu konular, İslam'ın temel inanç, ibadet ve ahlak prensiplerini içerir.""", 
        "sorular": [
            {"q": " Vahiy meleği olarak bilinen ve peygamberlere emirleri ileten melek hangisidir?", "a": ["Mikail", "İsrafil", "Azrail", "Cebrail"], "c": "Cebrail"}, 
            {"q": " Aşağıdakilerden hangisi ahiret hayatının aşamalarından biri değildir?", "a": ["Kıyamet", "Haşir", "Tevhid", "Mizan"], "c": "Tevhid"},
        ],
        "koc_anlatimi": """
**Dört Büyük Melek ve Görevleri (Detaylı)**

Melekler, Allah'ın emirlerini yerine getiren, nurdan yaratılmış, gözle görülmeyen manevi varlıklardır. Dört büyük meleğin temel görevleri şunlardır:

1.  **Cebrail (A.S.):** **Vahiy Meleği** olarak bilinir. Peygamberlere Allah'tan gelen ayetleri ve emirleri iletmekle görevlidir.
    * *Örnek Görev:* Kur'an-ı Kerim'in Hz. Muhammed'e (s.a.v.) parça parça indirilmesi.

2.  **Mikail (A.S.):** **Tabiat Olayları Meleği** olarak bilinir. Yağmurun yağması, rüzgarın esmesi ve bitkilerin yetişmesi gibi doğa ve geçim olaylarını yönetmekle görevlidir.
    * *Örnek Görev:* Dünya üzerindeki rızıkların ve bereketin dağıtımına nezaret etmek.

3.  **İsrafil (A.S.):** **Sûr Meleği** olarak bilinir. İki kere Sûr'a üflemekle görevlidir:
    * *Birinci Üfleme:* Kıyametin kopuşunu ve tüm canlıların yok olmasını sağlar.
    * *İkinci Üfleme:* Yeniden dirilişi (Haşir) başlatır.

4.  **Azrail (A.S.):** **Ölüm Meleği** olarak bilinir. Eceli gelen canlıların ruhunu almakla görevlidir.
    * *Örnek Görev:* Allah'ın emriyle her canlının yaşam süresini sonlandırmak.
"""
    },
    "Sosyal Bilgiler": {
        # Konu adını görseldeki gibi düzeltiyoruz
        "konu": "İletişim ve İnsan İlişkileri", 
        "anlatim": """7. Sınıf Sosyal Bilgiler dersi 7 ana üniteden oluşmaktadır:
        
* **1. Ünite (Birey ve Toplum - İletişim ve İnsan İlişkileri):** İletişim, duygu, düşünce veya bilgilerin akla gelebilecek her türlü yolla bir kişiden diğerine aktarılmasıdır. Etkili iletişimde empati kurmak önemlidir. Etkili iletişim unsurları: 'Ben dili' kullanmak, göz teması kurmak.
* **2. Ünite:** Kültürel Miras (Tarih ve kültür varlıklarımız)
* **3. Ünite:** İnsanlar Yerler ve Çevreler (Coğrafi konum ve yaşam)
* **4. Ünite:** Bilim, Teknoloji ve Toplum (Gelişim ve değişim)
* **5. Ünite:** Üretim, Dağıtım ve Tüketim (Ekonomik faaliyetler)
* **6. Ünite:** Etkin Vatandaşlık (Haklar, sorumluluklar ve yönetim)
* **7. Ünite:** Küresel Bağlantılar (Uluslararası ilişkiler ve sorunlar)
        
Bu ders, bireyin toplumsal hayattaki yerini, yaşadığı çevreyi ve dünyayı anlamasını sağlar.""", 
        "sorular": [
            {"q": " Aşağıdakilerden hangisi etkili iletişimi olumsuz etkiler?", "a": ["Empati kurmak", "Göz teması kurmak", "Yargılayıcı konuşmak", "Açık ve net konuşmak"], "c": "Yargılayıcı konuşmak"},
            {"q": " 'Kızgın olduğumu anlıyorum.' cümlesi hangi iletişim diline örnektir?", "a": ["Sen dili", "Ben dili", "Emir dili", "Vücut dili"], "c": "Ben dili"},
        ],
        "koc_anlatimi": """
**İletişim Türleri ve "Ben Dili" Kullanımı (Örneklerle)**

İletişim, insanların bilgi, duygu ve düşüncelerini aktarma sürecidir. Bu süreçte kullanılan dil, iletişimin kalitesini belirler.

1.  **Sen Dili (Olumsuz İletişim):** Suçlayıcı, yargılayıcı ve karşıdaki kişiyi savunmaya iten bir dildir. Genellikle "sen", "siz" zamirleri veya emir kipleri içerir.
    * **Örnek:** "Her zaman geç kalıyorsun, **sorumsuzsun**!"
    * **Etkisi:** Karşımızdakini kırar, anlaşmazlığa yol açar.

2.  **Ben Dili (Olumlu İletişim):** Kişinin kendi duygularını ve düşüncelerini karşıdakini yargılamadan ifade ettiği dildir. Genellikle "ben", "bana" gibi birinci tekil şahıs zamirleri içerir.
    * **Örnek:** "Geç kaldığında, dersin yarısını kaçırdığım için **endişeleniyorum**."
    * **Etkisi:** Soruna odaklanmayı sağlar, kişinin kendini açıklamasına olanak tanır ve duyguları açıklar.

**Etkili İletişim İçin İpuçları:**

* **Empati Kurmak:** Kendini karşındakinin yerine koymak.
* **Göz Teması Kurmak:** Samimiyeti ve dikkati gösterir.
* **Aktif Dinleme:** Sadece duymak değil, söylenenin anlamını kavramaya çalışmak.
"""
    },
    "İngilizce": {
        "konu": "7. Sınıf İngilizce Tüm Üniteler", 
        "anlatim": """7. Sınıf İngilizce dersi, öğrencilerin günlük hayatta ihtiyaç duyduğu temaları ve dilbilgisi yapılarını içerir:
        
* **1. Dönem Üniteleri:** Appearance and Personality (Görünüş ve Kişilik), Sports (Spor), Biographies (Biyografiler), Wild Animals (Vahşi Hayvanlar), Television (Televizyon).
* **2. Dönem Üniteleri:** Television (Tekrar/Devam), Celebrations (Kutlamalar), Dreams (Rüyalar), Public Buildings (Halk Binaları), Environment (Çevre), Planets (Gezegenler).

**Not:** Bu alan, yalnızca ünite başlıklarını listelemek amaçlıdır. Detaylı konu anlatımı, Konu Anlatımı özelliğimizden hariç tutulmuştur.""",
        "sorular": [
            {"q": " What does 'generous' mean?", "a": ["Cimri", "Cömert", "Yorgun", "Sinirli"], "c": "Cömert"},
            {"q": " 'O çok uzun ve zayıf.' cümlesinin İngilizcesi hangisidir?", "a": ["He is short and plump.", "She is kind and helpful.", "He is tall and slim.", "She is short and handsome."], "c": "He is tall and slim."},
        ],
        "koc_anlatimi": """
**Görünüş ve Kişilik Tanımlamaları (Detaylı Anlatım)**

İngilizcede birini tanımlarken, fiziksel görünüşünü (Appearance) ve karakter özelliklerini (Personality) belirten sıfatları kullanırız.

1.  **Görünüş (Appearance) Sıfatları:**
    * **Boy:** *Tall* (Uzun), *Short* (Kısa), *Medium height* (Orta boylu).
        * **Örnek:** She is **tall** and she has **long hair**.
    * **Kilo:** *Slim* (İnce), *Plump/Overweight* (Toplu/Kilolu), *Thin* (Zayıf).
    * **Saç:** *Long/Short hair*, *Curly/Straight hair*, *Blonde/Dark hair*.

2.  **Kişilik (Personality) Sıfatları:**
    * **Olumlu Özellikler:**
        * *Kind* (Nazik, iyi kalpli) $\rightarrow$ She is **kind** to everyone.
        * *Generous* (Cömert) $\rightarrow$ He is **generous** and shares his toys.
        * *Honest* (Dürüst) $\rightarrow$ They are **honest** people.
    * **Olumsuz Özellikler:**
        * *Selfish* (Bencil) $\rightarrow$ He is **selfish** and never shares.
        * *Rude* (Kaba) $\rightarrow$ Don't be **rude** to your teachers.
        * *Lazy* (Tembel) $\rightarrow$ She is a bit **lazy** sometimes.
"""
    }
} 


# GENEL ARKA PLAN MÜZİĞİ İÇİN ÖRNEK MP3 LİNKİ
GENEL_FON_URL = "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3" 
SESLI_ACIKLAMA_URL = "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-4.mp3" # Simülasyon Ses URL'si

# Session State Tanımlamaları
if 'admin_mode' not in st.session_state:
    st.session_state['admin_mode'] = False
if 'app_color' not in st.session_state:
    st.session_state['app_color'] = '#FF4B4B'
if 'secilen_sayfa' not in st.session_state:
    st.session_state['secilen_sayfa'] = "Hakkımda" 
if 'music_enabled' not in st.session_state:
    st.session_state['music_enabled'] = True 
if 'music_url' not in st.session_state:
    st.session_state['music_url'] = GENEL_FON_URL
if 'music_volume' not in st.session_state:
    st.session_state['music_volume'] = 0.5 
if 'show_admin_login' not in st.session_state:
    st.session_state['show_admin_login'] = False
if 'announcement' not in st.session_state:
    st.session_state['announcement'] = "🚀 Hoş geldiniz! 7. Sınıf Ders içeriklerini ve araçları keşfedin."
if 'announcement_color' not in st.session_state:
    st.session_state['announcement_color'] = 'success'
if 'secilen_modul' not in st.session_state:
    # Varsayılan modül: Konu Anlatımı
    st.session_state['secilen_modul'] = "Konu Anlatımı" 
if 'test_konusu' not in st.session_state:
    st.session_state['test_konusu'] = ""
if 'koc_mesaj' not in st.session_state:
    st.session_state['koc_mesaj'] = ""


# --- PORTFOLYO İÇERİK FONKSİYONU ---
def get_portfolyo_bilgisi(baslik):
    if baslik == "Hakkımda":
        return ("""Merhaba, ben Yusuf Efe Şahin. Bu kişisel portfolyo sayfamda, teknoloji, yazılım ve tasarım alanındaki çalışmalarımı sergiliyorum. Yaratıcı projeler geliştirmeye ve sürekli öğrenmeye odaklıyım.""", "👨‍💻")
    elif baslik == "Projelerim":
        return ("""Yaptığım bazı öne çıkan projeler ve kullandığım teknolojiler aşağıdadır.

* **Portfolyo Sitesi (Streamlit/Python):** Kişisel projelerimi sergilediğim ana alan.
* **Proje 2:** Python ile veri analizi ve görselleştirme çalışması.
* **Proje 3:** Web tabanlı basit bir uygulama geliştirme örneği.""", "💡")
    elif baslik == "İletişim":
        return ("""Sorularınız, iş teklifleri veya geri bildirimleriniz için benimle aşağıdaki yollarla iletişime geçebilirsiniz:
            
* **E-posta:** yusuf_efe_sahin@mail.com
* **LinkedIn:** /yusufeşahin
* **GitHub:** /yusufeşahinprojeler""", "📧")
    elif baslik == "Çeviri Aracı":
        return ("""Hızlı metin çevirisi yapabileceğiniz simülasyon aracıdır.""", "🌍")
    return ("İçerik Bulunamadı.", "❓")


# --- DERS MODÜLLERİ (Konu Anlatımı, Ders Koçlarımız, Çalışma Alanı/PDF/Deneme) ---
def render_ders_modulu(ders_adi, ders_veri, modul):
    # Görseldeki başlığa uyması için başlık etiketini değiştirelim
    st.subheader(f"✅ Seçili Sayfa: {ders_adi}")
    st.markdown(f"## 📚 {ders_adi} Dersi İçerikleri", unsafe_allow_html=True)
    
    # Modül Navigasyonu (Görseldeki buton metinleri ve ikonları düzenleniyor)
    col_konu, col_pdf, col_koc, col_alan = st.columns(4)
    
    with col_konu:
        # Konu Anlatımı (Görselde adı Konu Anlatımı, kodda da aynı)
        if st.button("📖 Konu Anlatımı", key="btn_konu_anlatim_new", use_container_width=True):
            st.session_state['secilen_modul'] = "Konu Anlatımı"
            st.session_state['test_konusu'] = "" 
            st.session_state['koc_mesaj'] = "" # Koç mesajını temizle
    with col_pdf:
        # PDF Sonuç Kontrol (Görselde adı PDF Sonuç Kontrol, kodda da aynı)
        if st.button("🔶 PDF Sonuç Kontrol", key="btn_pdf_kontrol_new", use_container_width=True):
            st.session_state['secilen_modul'] = "PDF Kontrol"
            st.session_state['test_konusu'] = ""
            st.session_state['koc_mesaj'] = ""
    with col_koc:
        # Ders Koçlarımız (Görselde adı Ders Koçlarımız, kodda da aynı)
        if st.button("🔶 Ders Koçlarımız", key="btn_ders_koclari", use_container_width=True):
            st.session_state['secilen_modul'] = "Ders Koçlarımız"
            st.session_state['test_konusu'] = ""
    with col_alan:
        # Çalışma Alanı (Görseldeki adı "Çalışma Alanı", kodda "Deneme Sınavı" yerine bu isim kullanılacak)
        if st.button("🔶 Çalışma Alanı", key="btn_deneme_sinavi_new", use_container_width=True):
            st.session_state['secilen_modul'] = "Deneme Sınavı" # Modül adı içeride sabit kalmalı
            st.session_state['koc_mesaj'] = ""
            
    st.markdown("---")

    # Modül İçeriği
    if modul == "Konu Anlatımı":
        st.header(f"📖 {ders_adi} - Konu Anlatımı ve Özet")
        
        # Konu başlığını gösteren kısım (Görseldeki gibi)
        st.info(f"👉 **Konu:** {ders_veri['konu']}") 
        
        st.markdown("---")
        
        # Başlık Görseldeki gibi "Detaylı Konu Anlatımı" olarak güncellendi
        st.subheader("📝 Detaylı Konu Anlatımı")
        st.markdown(ders_veri['anlatim']) 

    elif modul == "Deneme Sınavı":
        render_dinamik_test_alani(ders_adi, ders_veri['sorular'], "Çalışma Alanı") # Başlık için Çalışma Alanı gönderildi

    elif modul == "PDF Kontrol":
        st.header("📄 PDF Sonuç Kontrol (Simülasyon)")
        st.warning("Bu modül sadece bir gösterimdir. Gerçek bir PDF kontrol fonksiyonu burada yer alacaktır.")
        st.file_uploader("Lütfen Cevap Anahtarını Kontrol Etmek İstediğiniz PDF'i Yükleyin:")

    elif modul == "Ders Koçlarımız":
        st.header("🧑‍🏫 Ders Koçlarımız (Anında Cevap ve Sesli Simülasyon)")
        st.info("Konunuzu yazın, koç size o konuyu **detaylı ve bol örnekli** anlatsın.")
        
        # Kullanıcıdan soruyu al
        koç_mesaj = st.text_area(
            "Koça Sorunuzu Yazın:", 
            placeholder="Örneğin: Tam sayılarla çarpma işlemi nasıl yapılır?", 
            key=f"koc_input_{ders_adi}"
        )
        
        if st.form_submit_button("Koç Cevabını Hazırla"):
             if koç_mesaj:
                # Koçun vereceği açıklayıcı (simüle edilmiş) cevap
                koç_anlatimi = ders_veri.get('koc_anlatimi', f"Üzgünüm, şu an için '{ders_adi}' dersi koçunun özel bir açıklama metni tanımlanmamış. Ancak genel olarak bu ders: {ders_veri['konu']} konularını kapsar.")
                
                # 1. Koç Cevabı Metin Kutusu (Görseldeki gibi kırmızı kenarlıklı)
                # Buradaki başlığı doğrudan kullanıcının sorduğu konu ve sabit metin ile birleştirdik.
                st.markdown(
                    f"""
                    <div style='border-left: 5px solid #FF4B4B; padding: 10px; background-color: #1E3147;'>
                        <p style='color: #FF4B4B; font-weight: bold;'>Koç Cevabı: {koç_mesaj.capitalize()}</p>
                        <p> '{koç_mesaj.capitalize()}' konusuyla ilgili sana özel olarak hazırladığım ekstra alıştırmalar ve 7. sınıf müfredatındaki en kritik 3 bilgi notunu içeren bir özet hazırlıyorum. Unutma, pratik yapmak başarıyı getirir!</p>
                    </div>
                    """, 
                    unsafe_allow_html=True
                )

                st.markdown("---")
                
                # 2. Detaylı Koç Açıklaması (Görseldeki gibi)
                st.markdown(f"**Koç Açıklaması - Konu: {koç_mesaj.capitalize()}**")
                st.markdown(koç_anlatimi)
                
                st.markdown("---")
                
                # 3. Sesli Robot Simülasyonu (Autoplay kaldırıldı)
                st.subheader("🔊 Sesli Robot Çıktısı (Simülasyon)")
                
                # HTML Audio etiketi kullanarak ses çalma. 'autoplay' özelliği kaldırıldı.
                st.markdown(f"""
                    <audio controls loop=false>
                        <source src="{SESLI_ACIKLAMA_URL}" type="audio/mp3">
                        Tarayıcınız ses etiketini desteklemiyor.
                    </audio>
                    <div style='margin-top: 10px; font-style: italic; color: #aaa;'>
                    (Yukarıdaki ses bileşeni, koçun bu konuyu sesli olarak okuduğunu simüle eder. Ses otomatik başlamaz.)
                    </div>
                """, unsafe_allow_html=True)
            else:
                 st.warning("Lütfen Koçunuza açıklanmasını istediğiniz bir konu yazın.")

        else:
            st.info("Lütfen Koçunuza açıklanmasını istediğiniz bir konu yazın.")


# --- DİNAMİK TEST ALANI İŞLEVİ ---
def render_dinamik_test_alani(ders_adi, sorular, modül_başlık):
    st.header(f"🔥 {ders_adi} - {modül_başlık}") # Başlığı "Çalışma Alanı" olarak gösterir
    
    # Konu Adı Girişi
    with st.form(f"test_konusu_form_{ders_adi}", clear_on_submit=False):
        
        # Konu Adı Giriniz Alanı (Görsellerdeki gibi)
        st.markdown("##### Konu Adı Giriniz:")
        test_konusu_input = st.text_input(
            "Test Yapmak İstediğiniz Konu Adını Giriniz (Örn: Tam Sayılar)", 
            key=f"test_konusu_input_{ders_adi}",
            label_visibility="collapsed", 
            value=st.session_state['test_konusu'],
            placeholder="Konu Adını Giriniz" 
        )
        
        if st.form_submit_button("Testi Oluştur"):
            if test_konusu_input:
                st.session_state['test_konusu'] = test_konusu_input
                st.success(f"'{test_konusu_input}' konusuna ait test oluşturuluyor... (Simülasyon)")
                st.rerun()
            else:
                st.error("Lütfen bir konu adı giriniz.")
    
    # Kullanıcı bir konu girdiyse ve test oluşturulduysa (Simülasyon)
    if st.session_state['test_konusu'] and st.session_state['secilen_modul'] == "Deneme Sınavı":
        st.markdown("---")
        st.subheader(f"❓ Konu: **{st.session_state['test_konusu']}** Test Soruları")
        st.info(f"Bu test, **{st.session_state['test_konusu']}** konusuna özel olarak üretilmiş simülasyon sorularıdır.")
        
        # Quiz Formu (Sorular sabit kalsa bile konuya özel olduğu hissini verir)
        with st.form(f"quiz_form_{ders_adi}_soru", clear_on_submit=False): # Key çakışmasını engelle
            kullanici_cevaplari = {}
            
            # Dinamik konu başlığını yansıtmak için soruları yeniden yazarız.
            guncel_sorular = [{"q": q['q'].replace("Sözcükte Anlam İlişkileri", st.session_state['test_konusu']), **q} for q in sorular]
            
            for i, q in enumerate(guncel_sorular):
                q_text = q['q']
                st.markdown(f"**Soru {i+1}:** {q_text}", unsafe_allow_html=True) 
                kullanici_cevaplari[f"q_{i}"] = st.radio(f"Cevabınız:", q['a'], key=f"q_radio_{ders_adi}_{i}", index=None) 
                st.markdown("---")

            if st.form_submit_button("Cevapları Kontrol Et"):
                dogru_sayisi = 0
                yanlis_sayisi = 0
                bos_sayisi = 0
                
                st.subheader("Sonuçlar")
                
                for i, q in enumerate(guncel_sorular):
                    secim = kullanici_cevaplari[f"q_{i}"]
                    
                    if secim is None:
                        bos_sayisi += 1
                        st.warning(f"⚠️ Soru {i+1} Boş bırakıldı. Doğru Cevap: {q['c']}")
                    elif secim == q['c']:
                        dogru_sayisi += 1
                        st.success(f"✅ Soru {i+1} Doğru!")
                    else:
                        yanlis_sayisi += 1
                        st.error(f"❌ Soru {i+1} Yanlış. Doğru Cevap: {q['c']}")
                
                st.markdown("---")
                
                col_d, col_y, col_b = st.columns(3)
                col_d.metric("✅ Doğru Sayısı", dogru_sayisi)
                col_y.metric("❌ Yanlış Sayısı", yanlis_sayisi)
                col_b.metric("❓ Boş Sayısı", bos_sayisi)
                
                if dogru_sayisi > (len(guncel_sorular) / 2):
                    st.balloons()
                
                st.markdown(f"## 🎉 Toplam Sonuç: {dogru_sayisi} Doğru / {len(guncel_sorular)} Soru")

# --- ÇEVİRİ ARACI İŞLEVİ ---
def render_cevirici():
    st.header("🌍 Çeviri Aracı (Simülasyon)")
    st.info("Girdiğiniz metin, burada seçtiğiniz dile çevrilmiş gibi gösterilecektir.")
    
    with st.form("cevirici_form", clear_on_submit=False):
        kaynak_metin = st.text_area("Çevrilecek Metni Giriniz:", height=150)
        
        col_dil1, col_dil2 = st.columns(2)
        with col_dil1:
            kaynak_dil = st.selectbox("Kaynak Dil:", options=["Türkçe", "İngilizce"])
        with col_dil2:
            hedef_dil = st.selectbox("Hedef Dil:", options=["İngilizce", "Türkçe", "Almanca", "İspanyolca"])
        
        if st.form_submit_button("Çevir"):
            if kaynak_metin:
                cevrilmis_metin = f"[{hedef_dil} Çevirisi]: {kaynak_metin.upper()} (Simülasyon Çevirisi Başarılı!)"
                st.success(f"Çeviri Tamamlandı ({kaynak_dil} -> {hedef_dil}):")
                st.code(cevrilmis_metin)
            else:
                st.warning("Lütfen çevrilecek metni giriniz.")

# --- BAŞLIK AYARLARI ---
st.title(f"💼 Yusuf Efe Şahin Portfolyo")

# --- ANA İÇERİK ALANI (Ziyaretçi Modu) ---

if not st.session_state['admin_mode']:
    # --- GENEL FON MÜZİĞİ KONTROLLERİ ---
    col_kapat, col_ac, col_volume_slider = st.columns([1, 1, 6]) 

    if st.session_state['music_enabled']:
        # Müzik çalma kodu
        st.audio(st.session_state['music_url'], format="audio/mp3", loop=True)
        
        with col_kapat:
            # Syntax hatası düzeltilmiş buton
            if st.button("🔊 Müzik Kapat", key="btn_kapat_ses", use_container_width=True):
                st.session_state['music_enabled'] = False
                st.rerun()
        with col_volume_slider:
            new_volume = st.slider("Müzik Ses Seviyesi", 0.0, 1.0, st.session_state['music_volume'], step=0.1, key="music_volume_slider")
            if new_volume != st.session_state['music_volume']:
                st.session_state['music_volume'] = new_volume
                st.rerun() 
    elif st.session_state['music_url']: 
        with col_ac:
            if st.button("🔇 Müzik Aç", key="btn_ac_ses", use_container_width=True):
                st.session_state['music_enabled'] = True
                st.rerun()
    
    st.markdown("---")
    
    # Duyuru Mesajı
    if st.session_state['announcement_color'] == 'success':
        st.success(f"📣 {st.session_state['announcement']}")
    elif st.session_state['announcement_color'] == 'info':
        st.info(f"📣 {st.session_state['announcement']}")
    elif st.session_state['announcement_color'] == 'warning':
        st.warning(f"📣 {st.session_state['announcement']}")
    elif st.session_state['announcement_color'] == 'error':
        st.error(f"📣 {st.session_state['announcement']}")
    
    # --- NAVİGASYON (Portfolyo, Dersler ve Araçlar) ---
    st.header("🌐 Site Bölümleri ve 7. Sınıf Dersleri")

    PORTFOLYO_SAYFALAR = ["Hakkımda", "Projelerim", "İletişim"]
    ARACLAR_SAYFALAR = ["Çeviri Aracı"] 
    DERS_SAYFALAR = list(DEFAULT_DERSLER.keys())
    
    SAYFALAR = PORTFOLYO_SAYFALAR + DERS_SAYFALAR + ARACLAR_SAYFALAR
    
    # Ana Butonlar için dinamik sütun oluşturma
    cols = st.columns(len(SAYFALAR))
    for i, sayfa in enumerate(SAYFALAR):
        with cols[i]:
            if st.button(f"🔹 {sayfa}", key=f"btn_{sayfa}", use_container_width=True):
                st.session_state['secilen_sayfa'] = sayfa
                # Ders sayfasına geçildiğinde modül varsayılana ('Konu Anlatımı') ayarlansın
                if sayfa in DERS_SAYFALAR:
                    st.session_state['secilen_modul'] = "Konu Anlatımı" 
                    st.session_state['test_konusu'] = "" # Konu değişince testi sıfırla
                    st.session_state['koc_mesaj'] = "" # Koç mesajını temizle
                else:
                    st.session_state['secilen_modul'] = "Konu Anlatımı"
                st.rerun()
                
    st.markdown("---")
    secilen_sayfa = st.session_state['secilen_sayfa']

    
    # --- İÇERİK YAZDIRMA VE ÖZELLİK ÇAĞIRMA ---
    
    # 1. DERS SAYFASI İÇERİĞİ (Artık Modül Yapısı Kullanıyor)
    if secilen_sayfa in DERS_SAYFALAR:
        ders_veri = DEFAULT_DERSLER[secilen_sayfa]
        render_ders_modulu(secilen_sayfa, ders_veri, st.session_state['secilen_modul'])
        
    # 2. ÇEVİRİ ARACI
    elif secilen_sayfa == "Çeviri Aracı":
        render_cevirici()
        
    # 3. PORTFOLYO SAYFALARI (Hakkımda, Projelerim, İletişim)
    else:
        icerik, simge = get_portfolyo_bilgisi(secilen_sayfa)
        st.subheader(f"✅ Seçili Sayfa: {secilen_sayfa}")
        st.markdown(f"## {simge} {secilen_sayfa}")
        st.markdown(f"**{icerik}**")
        
    st.markdown("---")

# --- YÖNETİCİ VE YAN PANEL (SIDEBAR) AYARLARI ---
st.sidebar.title("Kullanıcı İşlemleri")

# YÖNETİCİ MODU
if st.session_state['admin_mode']:
    st.sidebar.subheader("⚙️ Yönetici Ayarları") 
    st.sidebar.button("🔒 YÖNETİCİ ÇIKIŞI", on_click=lambda: (st.session_state.update({'admin_mode': False}), st.rerun()))
    
    # TEMA RENGİ AYARI
    new_color = st.sidebar.color_picker(
        "Uygulama Tema Rengini Seçin:", 
        st.session_state['app_color']
    )
    if new_color != st.session_state['app_color']:
        st.session_state['app_color'] = new_color
        st.rerun()
    
    # MÜZİK KONTROLÜ
    st.sidebar.markdown("---")
    st.sidebar.subheader("🎶 Fon Müziği Ayarları")
    
    MUSIC_OPTIONS = {
        "Melodi 1 (Genel Fon)": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3",
        "Piyano Melodisi (Fon)": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3",
        "Özel Şarkı Linki Gir": "CUSTOM_URL",
        "Müzik Kapalı": ""
    }
    
    # Yönetici Ses Düzeyi
    yeni_volume = st.sidebar.slider("Yönetici Ses Seviyesi", 0.0, 1.0, st.session_state['music_volume'], step=0.1, key="admin_music_volume_slider")
    if yeni_volume != st.session_state['music_volume']:
        st.session_state['music_volume'] = yeni_volume
        st.rerun() 

    secilen_sarki_adi = st.sidebar.selectbox("Çalınacak Şarkıyı Seçin:", options=list(MUSIC_OPTIONS.keys()))
    yeni_url = MUSIC_OPTIONS[secilen_sarki_adi]
    
    if secilen_sarki_adi == "Özel Şarkı Linki Gir":
        custom_url_input = st.sidebar.text_input("MP3 Linkini Yapıştırın:", key="custom_music_url_input", value=st.session_state.get('music_url') if st.session_state.get('music_url') not in MUSIC_OPTIONS.values() else "")
        if custom_url_input and custom_url_input.lower().endswith('.mp3'):
             yeni_url = custom_url_input
        else:
             st.sidebar.warning("Lütfen geçerli bir MP3 linki girin. (Örn: ...mp3)")
             yeni_url = st.session_state['music_url'] 
    
    if yeni_url != st.session_state['music_url']:
        st.session_state['music_url'] = yeni_url
        st.session_state['music_enabled'] = bool(yeni_url) 
        st.rerun() 
    
    
    # DUYURU AYARLARI
    st.sidebar.markdown("---")
    st.sidebar.subheader("📢 Site Duyurusu")
    st.session_state['announcement'] = st.sidebar.text_area("Duyuru Metni:", value=st.session_state['announcement'])
    st.session_state['announcement_color'] = st.sidebar.selectbox("Duyuru Kutusu Rengi:", ["success", "info", "warning", "error"], index=["success", "info", "warning", "error"].index(st.session_state['announcement_color']))
    if st.sidebar.button("Duyuruyu Güncelle", key="btn_guncelle_duyuru"):
        st.rerun()

else:
    # YÖNETİCİ GİRİŞ BUTONU
    st.sidebar.button("🔒 Yönetici Girişi", on_click=lambda: st.session_state.update({'show_admin_login': True}))

    # YÖNETİCİ GİRİŞ FORMU
    if st.session_state['show_admin_login']:
        with st.sidebar.form("admin_login_form"):
            admin_pass = st.text_input("Yönetici Şifresi", type="password")
            if st.form_submit_button("Giriş Yap"):
                if admin_pass == ADMIN_PASSWORD:
                    st.session_state['admin_mode'] = True
                    st.session_state['show_admin_login'] = False
                    st.rerun()
                else:
                    st.error("Hatalı yönetici şifresi.") 
    
st.sidebar.markdown("---")
st.sidebar.title("⭐ Yorumlar ve Geri Bildirim")

# Yorum Formu korundu
with st.sidebar.form("geri_bildirim_formu", clear_on_submit=True):
    st.sidebar.write("Site hakkındaki yorumlarınızı buraya yazın.")
    st.selectbox("Konu:", ["Genel Yorum", "Hata Bildirimi", "Tasarım Önerisi", "Teşekkür"])
    st.text_area("Mesajınız:")
    if st.form_submit_button("Yorumu Gönder"):
        st.sidebar.success(f"Yorumunuz başarıyla iletildi!")

st.sidebar.markdown("---")
st.sidebar.caption("Geliştirici: Yusuf Efe Şahin | Portfolyo v2.0")
