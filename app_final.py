# --- CHAT BOT MANTIĞI (Genişletilmiş SİMÜLASYON) ---
def general_chat_portfolyo(mesaj):
    mesaj_lower = mesaj.lower().strip()
    
    # Yeni Ders Cevapları
    ders_cevaplari = {
        "fonksiyon nedir": "Matematikte bir fonksiyon, her girdiyi tam olarak bir çıktıya eşleyen bir kuraldır.",
        "pythonda değişken": "Python'da değişkenler, bilgileri depolamak için kullanılan bellek konumlarıdır.",
        "osmanlı": "Osmanlı İmparatorluğu, 1299'dan 1922'ye kadar var olmuş büyük bir devlettir.",
        "merhaba": "Selam, Portfolyo sitesine hoş geldin! Dersler hakkında veya projelerim hakkında soru sorabilirsin.",
        "proje": "Projelerim sayfasına göz atmak ister misin?",
        "hata": "Hata bildirimleri için Yorum alanını kullanabilirsin."
    }

    for kelime, cevap in ders_cevaplari.items():
        if kelime in mesaj_lower:
            return f"🤖 (Kanka): {cevap}"
            
    return f"🤖 (Kanka): Anladım. Ben Yusuf Efe Şahin'in AI asistanıyım. Hangi ders içeriğiyle ilgili bilgi almak istiyorsun? (Örn: 'Pythonda değişken nedir?' gibi.)"
