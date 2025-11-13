# generate_ai_explanation fonksiyonunun tamamen güncellenmiş hali
def generate_ai_explanation(topic):
    topic_lower = topic.lower().strip()
    response = ""
    
    # 1. TÜRKÇE (DİL BİLGİSİ VE ANLAM)
    if any(k in topic_lower for k in ["fiil", "ek fiil", "zarf", "anlatım bozukluğu", 
                                     "yazım", "noktalama", "sözcükte anlam", "cümlede anlam", 
                                     "parçada anlam", "metin türü", "söz sanatı"]):
        response = f"## 💻 Akıl Konu Anlatımı: {topic.upper()} (TÜRKÇE) 🎉"
        
    # 2. MATEMATİK
    elif any(k in topic_lower for k in ["tam sayı", "rasyonel", "cebirsel", "denklem", 
                                        "oran", "orantı", "yüzde", "doğrular", "açılar", 
                                        "çokgen", "çember", "daire", "veri analiz", "cisim"]):
        response = f"## 🧠 Akıl Konu Anlatımı: {topic.upper()} (MATEMATİK) 🎉"

    # 3. FEN BİLİMLERİ
    elif any(k in topic_lower for k in ["güneş sistemi", "uzay", "hücre", "mitoz", "mayoz", 
                                        "kütle", "ağırlık", "kuvvet", "enerji", "saf madde", 
                                        "karışım", "ışık", "ayna", "mercek", "üreme", 
                                        "elektrik devresi", "ampul"]):
        response = f"## 🧪 Akıl Konu Anlatımı: {topic.upper()} (FEN BİLİMLERİ) 🎉"

    # 4. SOSYAL BİLGİLER
    elif any(k in topic_lower for k in ["birey ve toplum", "kültür ve miras", "insanlar yerler çevreler", 
                                        "bilim teknoloji toplum", "üretim dağıtım tüketim", 
                                        "etkin vatandaşlık", "küresel bağlantı", "atatürk"]):
        response = f"## 🌍 Akıl Konu Anlatımı: {topic.upper()} (SOSYAL BİLGİLER) 🎉"

    # 5. İNGİLİZCE
    elif any(k in topic_lower for k in ["appearance", "personality", "sports", "wild animals", 
                                        "television", "celebrations", "dreams", "public buildings", 
                                        "environment", "planets"]):
        response = f"## 🗣️ Akıl Konu Anlatımı: {topic.upper()} (İNGİLİZCE) 🎉"

    # 6. DİN KÜLTÜRÜ
    elif any(k in topic_lower for k in ["melek", "ahiret", "nas suresi", "hac", "kurban", "umre", 
                                        "en'âm suresi", "ahlak", "hz. isa", "hz. ismail", "hz. salih",
                                        "felak suresi", "hz. muhammed", "kâfirun suresi", "yorum"]):
        response = f"## 🕌 Akıl Konu Anlatımı: {topic.upper()} (DİN KÜLTÜRÜ) 🎉"
    
    else:
        # Konu tanınamazsa bu uyarı verilir.
        response = f"""## ⚠️ Akıl Asistanı Uyarısı: '{topic.upper()}' şu an için anlatabileceğim ana ders konuları arasında değildir."""
        
    st.session_state.ai_response = response
    st.session_state.last_topic = topic
