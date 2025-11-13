# Yapay Zeka (Gemini) Butonu için
def generate_ai_explanation(topic):
    topic_lower = topic.lower().strip()
    
    if "rasyonel sayılar" in topic_lower:
        response = """
        ## 🧠 Gemini Konu Anlatımı: Rasyonel Sayılar
        
        **Tanım:** Rasyonel sayılar, $a$ bir tam sayı ve $b$ sıfırdan farklı bir tam sayı olmak üzere, $\\frac{a}{b}$ şeklinde yazılabilen sayılardır. Kesir çizgisi, aslında bir bölme işlemidir.
        
        **İşlemler:**
        * **Toplama/Çıkarma:** Paydalar eşitlenmelidir.
        * **Çarpma:** Paylar çarpılıp paya, paydalar çarpılıp paydaya yazılır.
        * **Bölme:** Birinci rasyonel sayı aynen yazılır, ikinci rasyonel sayı ters çevrilip çarpılır.
        """
    elif "tam sayılar" in topic_lower:
        response = """
        ## 🧠 Gemini Konu Anlatımı: Tam Sayılar
        
        **Tanım:** Tam sayılar, pozitif doğal sayılar ($1, 2, 3, ...$), negatif doğal sayılar ($-1, -2, -3, ...$) ve sıfırın oluşturduğu kümedir. $\\mathbb{Z}$ sembolü ile gösterilir.
        
        **Toplama Kuralları:**
        1.  **Aynı İşaretliler:** Toplanır, ortak işaret sonuca yazılır. (Örn: $-5 + (-3) = -8$)
        2.  **Farklı İşaretliler:** Büyük sayıdan küçük sayı çıkarılır, sonucun işaretine büyük sayının işareti verilir. (Örn: $-10 + 4 = -6$)
        """
    else:
        # SOHBETİ TAMAMEN REDDEDEN VE UYARI VEREN KISIM
        response = f"""
        ## ⚠️ Asistan Uyarısı
        
        **'{(topic[:20] + '...') if len(topic) > 20 else topic}'** şu an için anlatabileceğim konular arasında değildir. 
        
        Ben sadece 7. Sınıf konularını anlatmak üzere programlanmış bir öğrenci asistanıyım ve **sohbet özelliğim kapalıdır.** Lütfen sadece **Rasyonel Sayılar** veya **Tam Sayılar** gibi bir ders konusu yazınız.
        """
        
    st.session_state.ai_response = response
    st.session_state.last_topic = topic
