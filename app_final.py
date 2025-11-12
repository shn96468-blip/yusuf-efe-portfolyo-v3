# --- CHAT BOT MANTIĞI (BASİT SİMÜLASYON) ---
def general_chat_portfolyo(mesaj):
    mesaj_lower = mesaj.lower().strip()
    basit_cevaplar = {"merhaba": "Selam, Portfolyo sitesine hoş geldin!", "nasılsın": "Çok iyi çalışıyorum, teşekkürler!", "proje": "Projelerim sayfasına göz atmak ister misin?", "hata": "Hata bildirimleri için Yorum alanını kullanabilirsin."}
    
    for kelime, cevap in basit_cevaplar.items():
        if kelime in mesaj_lower:
            return f"🤖 (Kanka): {cevap}"
    # Düzeltilen Satır (Tırnak işareti eklendi)
    return f"🤖 (Kanka): Anladım. Ben Yusuf Efe Şahin'in AI asistanıyım. Projeleri merak ediyorsan, kartlardan birini seçebilirsin."
