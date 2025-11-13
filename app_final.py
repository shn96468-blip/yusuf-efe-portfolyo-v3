# Yapay Zeka (Akıl) Butonu için
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
        
        **Yapılarına Göre Fiiller:** Basit, Türemiş ve Birleşik Fiiller olarak incelenir.
        * **Örnek:** 'okudu' (Basit), 'gözetledi' (Türemiş), 'fark etti' (Birleşik).
        """
    elif "ek fiil" in topic_lower:
        response = """
        ## 🧠 Akıl Konu Anlatımı: Ek Fiil (Ek Eylem)
        
        **Tanım:** Ek fiil, iki temel görevi olan 'imek' fiilidir (im, isen, idir, idi, imiş, ise).
        
        **Görevleri:**
        1.  **İsimleri yüklem yapar:** 'Hava çok **sıcak-tı**.'
        2.  **Basit zamanlı fiilleri birleşik zamanlı yapar:** 'Çocuklar bahçede **oynuyor-du**.'
        """
    elif "zarflar" in topic_lower:
        response = """
        ## 🧠 Akıl Konu Anlatımı: Zarflar (Belirteçler)
        
        **Tanım:** Zarflar, fiilleri, fiilimsileri, sıfatları ve bazen de başka zarfları **zaman, durum, miktar, yer-yön** ve **soru** bakımından belirten kelimelerdir.
        
        **Türleri:** Durum Zarfı ('Nasıl?' sorusuna cevap verir: **hızlı** koşuyor), Zaman Zarfı ('Ne zaman?' sorusuna cevap verir: **yarın** gelecek).
        """
        
    # --- DİĞER TÜM KONULAR REDDEDİLİR ---
    else:
        # Sohbeti reddeden ve sadece bilinen konulara odaklanmayı isteyen kısım
        response = f"""
        ## ⚠️ Akıl Asistan Uyarısı
        
        **'{topic[:20].upper() + ('...' if len(topic) > 20 else '')}'** şu an için anlatabileceğim konular arasında değildir. 
        
        Ben sadece 7. Sınıf **Matematik ve Dil Bilgisi** ana konularını anlatmak üzere programlanmış bir öğrenci asistanıyım ve **sohbet özelliğim kapalıdır.**
        """
        
    st.session_state.ai_response = response
    st.session_state.last_topic = topic
