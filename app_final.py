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
    
    /* Özel Buton Stili */
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
        
* **1. Ünite (Tam Sayılar):** Pozitif ve negatif tam sayılarla toplama, çıkarma, çarpma ve bölme işlemleri, üslü ifadeler.
* **2. Ünite (Rasyonel Sayılar):** Rasyonel sayı kavramı, rasyonel sayılarla dört işlem.
* **3. Ünite (Cebirsel İfadeler):** Cebirsel ifadelerin anlamı, değerini hesaplama, eşitlik ve denklem çözümü.
* **4. Ünite (Oran ve Orantı):** Oran, orantı, doğru ve ters orantı, yüzdeler.
* **5. Ünite (Geometri):** Doğrular ve Açılar, Çokgenler (alan/çevre), Çember ve Daire.
* **6. Ünite (Veri İşleme):** Veri analizi, çizgi ve sütun grafikleri, daire grafiği, cisimlerin farklı yönlerden görünümleri.

Bu konular, lise matematiği için sağlam bir temel oluşturur.""", # Anlatım detaylandırıldı
        "sorular": [
            {"q": " $(-5) + (+8)$ işleminin sonucu kaçtır?", "a": ["$-13$", "$+3$", "$-3$", "$+13$"], "c": "$+3$"},
            {"q": " $(-4) \\cdot (-2)$ işleminin sonucu kaçtır?", "a": ["$-8$", "$+8$", "$0$", "$+2$"], "c": "$+8$"},
            {"q": " $20 \\div (-5)$ işleminin sonucu kaçtır?", "a": ["$4$", "$-4$", "$25$", "$-25$"], "c": "$-4$"},
        ]
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
        ]
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
        ]
    },
    "Din Kültürü ve Ahlak Bilgisi": { 
        "konu": "7. Sınıf Din Kültürü Tüm Üniteler", 
        "anlatim": """7. Sınıf Din Kültürü ve Ahlak Bilgisi dersi 5 ana üniteden oluşmaktadır:
        
* **1. Ünite (Melekler ve Ahiret İnancı):** İmanın şartlarından biri olan ahiret inancının önemi. Ahiret hayatının aşamaları (kıyamet, haşir, mizan) ve görevli melekler (Cebrail-vahiy, Mikail-tabiat, İsrafil-sûr, Azrail-ölüm). Nâs Suresi'nin anlamı.
* **2. Ünite (Hac ve Kurban):** İslam'ın beş şartından biri olan Hac ibadeti, Umre ve Kurban ibadetinin anlamı ve yapılışı. Hz. İsmail'in hayatı.
* **3. Ünite (Ahlaki Davranışlar):** Doğruluk, dürüstlük, adalet gibi güzel ahlaki tutumlar. Hz. Salih'in hayatından örnekler. Fel
