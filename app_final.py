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
        2.  **Katsayı:** Değişkenin önünd
