import streamlit as st

# --- 1. TÜM İÇERİKLERİN TANIMI ---

# KOÇ MODÜLÜ İÇERİĞİ
COACH_CONTENT = """
## 💡 Koç Modülü - Öğrenci Koçluğu ve Rehberlik
<div style='background-color: #26292e; padding: 10px; border-radius: 5px;'>
    <p>🎓 Konu: Etkili Ders Çalışma Yöntemleri ve Zaman Yönetimi</p>
</div>
### 🗓️ Haftalık Çalışma Planı
* **Zaman Yönetimi:** Günlük rutin oluşturma ve derslere ayrılan sürenin belirlenmesi.
* **Pomodoro Tekniği:** 25 dakika çalışma, 5 dakika mola tekniği ile odaklanmayı artırma.
* **Verimli Not Alma:** Anahtar kelimeler ve zihin haritası kullanarak not tutma.

### 🎯 Motivasyon ve Hedef Belirleme
* **SMART Hedefler:** (Specific, Measurable, Achievable, Relevant, Time-bound) belirleme.
* **Motivasyon Artırma:** Başarıları takip etme ve küçük ödüllerle kendini teşvik etme.
"""

# MATEMATİK İÇERİĞİ
MATH_CONTENT = """
## 📘 Matematik - Konu Anlatımı ve Özet
<div style='background-color: #26292e; padding: 10px; border-radius: 5px;'>
    <p>🔑 Konu: 7. Sınıf Matematik Müfredatı Özeti</p>
</div>
### 📄 Detaylı Konu Özeti
* Tam Sayılarla İşlemler
* Rasyonel Sayılar
* Cebirsel İfadeler
* Oran ve Orantı
* Yüzdeler
* Doğrular ve Açılar
* Çokgenler ve Alan
* Çember ve Daire
* Veri Analizi
"""

# TÜRKÇE İÇERİĞİ
TURKISH_CONTENT = """
## 📝 Türkçe - Konu Anlatımı ve Özet
<div style='background-color: #26292e; padding: 10px; border-radius: 5px;'>
    <p>🔑 Konu: 7. Sınıf Türkçe Müfredatı Özeti</p>
</div>
### 📄 Detaylı Konu Özeti
* Sözcükte Anlam
* Cümlede Anlam
* Paragrafta Anlam
* Fiiller (Eylem)
* Fiilde Anlam Kayması
* Ekler ve Köklere Giriş
* Yazım Kuralları ve Noktalama İşaretleri
* Metin Türleri (Hikâye, Roman, Şiir)
"""

# FEN BİLİMLERİ İÇERİĞİ
SCIENCE_CONTENT = """
## 🧪 Fen Bilimleri - Konu Anlatımı ve Özet
<div style='background-color: #26292e; padding: 10px; border-radius: 5px;'>
    <p>🔑 Konu: 7. Sınıf Fen Müfredatı Özeti</p>
</div>
### 📄 Detaylı Konu Özeti
* Güneş Sistemi ve Ötesi
* Hücre
* Kuvvet ve Enerji
* Saf Madde ve Karışımlar
* Kimyasal Tepkimeler
* Işığın Maddeyle Etkileşimi
* Canlılarda Üreme, Büyüme ve Gelişme
* Elektrik Devreleri
"""

# SOSYAL BİLGİLER İÇERİĞİ
SOCIAL_CONTENT = """
## 🌍 Sosyal Bilgiler - Konu Anlatımı ve Özet
<div style='background-color: #26292e; padding: 10px; border-radius: 5px;'>
    <p>🔑 Konu: 7. Sınıf Sosyal Bilgiler Tüm Üniteler</p>
</div>
### 📄 Detaylı Konu Özeti
* 1. ÜNİTE: BİREY VE TOPLUM
* 2. ÜNİTE: KÜLTÜR VE MİRAS
* 3. ÜNİTE: İNSANLAR, YERLER VE ÇEVRELER
* 4. ÜNİTE: BİLİM, TEKNOLOJİ VE TOPLUM
* 5. ÜNİTE: ÜRETİM, DAĞITIM VE TÜKETİM
* 6. ÜNİTE: ETKİN VATANDAŞLIK
* 7. ÜNİTE: KÜRESEL BAĞLANTILAR
"""

# İNGİLİZCE İÇERİĞİ
# ==============================================================================
# --- 9. TAB 5: İNGİLİZCE İÇERİKLERİ (İşlevsel) ---
# ==============================================================================
with tab_eng:
    st.header("🗣️ İngilizce Dersi İçerikleri")
    col_ing_btn1, col_ing_btn2, col_ing_btn3 = st.columns(3)
    
    with col_ing_btn1:
        st.button("📄 Konu Anlatımını Aç", type="primary", key="ing_konu") 
    with col_ing_btn2:
        st.button("💬 Konuşma Alıştırması", type="secondary", key="ing_konusma")
    with col_ing_btn3:
        st.button("🔥 Kelime Testi", type="secondary", key="ing_test")
    
    st.markdown("---")
    
    with st.expander("💬 7. Sınıf İngilizce Konularına Göz Atın"):
        # Hata veren satırın düzeltilmiş hali:
        st.info("Aşağıda 7. Sınıf İngilizce Ünitelerine ait genel bir özet listelenmiştir. Kelime bilginizi güçlendirin.")
        st.markdown(ENGLISH_CONTENT, unsafe_allow_html=True)
        st.markdown("**💡 Koç Önerisi:** 'Appearance and Personality' ünitesindeki sıfatları ezberlemek önemlidir.")

# DİN KÜLTÜRÜ İÇERİĞİ
RELIGION_CONTENT = """
## 🕌 Din Kültürü ve Ahlak Bilgisi - Konu Anlatımı ve Özet
<div style='background-color: #26292e; padding: 10px; border-radius: 5px;'>
    <p>🔑 Konu: 7. Sınıf Din Kültürü Müfredatı Özeti</p>
</div>
### 📄 Detaylı Konu Özeti
* Melek ve Ahiret İnancı
* Hac ve Kurban İbadeti
* Ahlaki Davranışlar
* İslam Düşüncesinde Yorumlar
* İletişim ve Nezaket
"""

# --- 2. STREAMLIT SAYFA AYARLARI ---
st.set_page_config(layout="wide", page_title="Yusuf Efe Şahin | 7. Sınıf Eğitim Portalı")
st.title("👨‍🎓 Yusuf Efe Şahin | 7. Sınıf Eğitim Portalı")
st.markdown("---")

# 3. SEKMELERİN TANIMLANMASI
tab_coach, tab_math, tab_tr, tab_sci, tab_soc, tab_eng, tab_rel = st.tabs([
    "💡 Koç Modülü", 
    "🔢 Matematik İçerikleri", 
    "📝 Türkçe İçerikleri", 
    "🧪 Fen Bilimleri",
    "🌍 Sosyal Bilgiler",
    "🗣️ İngilizce",
    "🕌 Din Kültürü",
])

# ==============================================================================
# --- 4. TAB 0: KOÇ MODÜLÜ ---
# ==============================================================================
with tab_coach:
    st.header("💡 Koç Modülü - Rehberlik ve Mentorluk")
    col_coach_btn1, col_coach_btn2, col_coach_btn3 = st.columns(3)
    
    with col_coach_btn1:
        st.button("📝 Çalışma Planı Oluştur", type="primary", key="coach_plan") 
    with col_coach_btn2:
        st.button("🧠 Motivasyon Teknikleri", type="secondary", key="coach_motivasyon")
    with col_coach_btn3:
        st.button("⏰ Pomodoro Zamanlayıcısı", type="secondary", key="coach_pomodoro")
    
    st.markdown("---")
    st.markdown(COACH_CONTENT, unsafe_allow_html=True)


# ==============================================================================
# --- 5. TAB 1: MATEMATİK İÇERİKLERİ (İşlevsel) ---
# ==============================================================================
with tab_math:
    st.header("🔢 Matematik Dersi İçerikleri")
    col_math_btn1, col_math_btn2, col_math_btn3 = st.columns(3)
    
    with col_math_btn1:
        st.button("📄 Konu Anlatımını Aç", type="primary", key="mat_konu") 
    with col_math_btn2:
        st.button("♦️ PDF Sonuç Kontrol", type="secondary", key="mat_pdf")
    with col_math_btn3:
        st.button("🔥 Deneme Sınavı", type="secondary", key="mat_deneme")
    
    st.markdown("---")
    
    with st.expander("📚 7. Sınıf Matematik Konularına Göz Atın"):
        st.info("Aşağıda 7. Sınıf Matematik Müfredatına ait genel bir özet listelenmiştir. Daha fazla detay için linklere bakınız.")
        st.markdown(MATH_CONTENT, unsafe_allow_html=True)
        st.markdown("**💡 Koç Önerisi:** Karmaşık konuları anlamak için [YouTube'daki matematik kanallarını](https://www.youtube.com/@MatematikOgreniyorum/videos) ziyaret edebilirsiniz.")


# ==============================================================================
# --- 6. TAB 2: TÜRKÇE İÇERİKLERİ (İşlevsel) ---
# ==============================================================================
with tab_tr:
    st.header("📝 Türkçe Dersi İçerikleri")
    col_tr_btn1, col_tr_btn2, col_tr_btn3 = st.columns(3)

    with col_tr_btn1:
        st.button("📄 Konu Anlatımını Aç", type="primary", key="turk_konu") 
    with col_tr_btn2:
        st.button("♦️ Hikaye Analizi", type="secondary", key="turk_analiz")
    with col_tr_btn3:
        st.button("🔥 Yazım Kılavuzu", type="secondary", key="turk_yazim")

    st.markdown("---")
    
    with st.expander("📝 7. Sınıf Türkçe Konularına Göz Atın"):
        st.info("Aşağıda 7. Sınıf Türkçe Müfredatına ait genel bir özet listelenmiştir. Dil bilgisi ve anlam konularına odaklanın.")
        st.markdown(TURKISH_CONTENT, unsafe_allow_html=True)
        st.markdown("**💡 Koç Önerisi:** Özellikle fiiller (eylem) konusu için ek alıştırmalar çözmeniz tavsiye edilir.")


# ==============================================================================
# --- 7. TAB 3: FEN BİLİMLERİ İÇERİKLERİ (Şimdi İşlevsel) ---
# ==============================================================================
with tab_sci:
    st.header("🧪 Fen Bilimleri Dersi İçerikleri")
    col_fen_btn1, col_fen_btn2, col_fen_btn3 = st.columns(3)
    
    with col_fen_btn1:
        st.button("📄 Konu Anlatımını Aç", type="primary", key="fen_konu") 
    with col_fen_btn2:
        st.button("🔬 Laboratuvar Deneyleri", type="secondary", key="fen_deney")
    with col_fen_btn3:
        st.button("🔥 Ünite Testi", type="secondary", key="fen_test")
    
    st.markdown("---")
    
    with st.expander("🔬 7. Sınıf Fen Bilimleri Konularına Göz Atın"):
        st.info("Aşağıda 7. Sınıf Fen Bilimleri Müfredatına ait genel bir özet listelenmiştir. Deneyler ve kavramlara dikkat edin.")
        st.markdown(SCIENCE_CONTENT, unsafe_allow_html=True)
        st.markdown("**💡 Koç Önerisi:** Hücre, kuvvet ve enerji gibi temel konuları mutlaka tekrar edin.")


# ==============================================================================
# --- 8. TAB 4: SOSYAL BİLGİLER İÇERİKLERİ (Şimdi İşlevsel) ---
# ==============================================================================
with tab_soc:
    st.header("🌍 Sosyal Bilgiler Dersi İçerikleri")
    col_sosyal_btn1, col_sosyal_btn2, col_sosyal_btn3 = st.columns(3)
    
    with col_sosyal_btn1:
        st.button("📄 Konu Anlatımını Aç", type="primary", key="sos_konu") 
    with col_sosyal_btn2:
        st.button("📜 Tarihi Olaylar", type="secondary", key="sos_olay")
    with col_sosyal_btn3:
        st.button("🔥 Coğrafya Bilgisi", type="secondary", key="sos_cografya")
    
    st.markdown("---")
    
    with st.expander("📜 7. Sınıf Sosyal Bilgiler Konularına Göz Atın"):
        st.info("Aşağıda 7. Sınıf Sosyal Bilgiler Müfredatına ait genel bir özet listelenmiştir. Ünite konularını tekrar edin.")
        st.markdown(SOCIAL_CONTENT, unsafe_allow_html=True)
        st.markdown("**💡 Koç Önerisi:** Birey ve Toplum ile Kültür ve Miras üniteleri genellikle en kapsamlı olanlardır.")


# ==============================================================================
# --- 9. TAB 5: İNGİLİZCE İÇERİKLERİ (Şimdi İşlevsel) ---
# ==============================================================================
with tab_eng:
    st.header("🗣️ İngilizce Dersi İçerikleri")
    col_ing_btn1, col_ing_btn2, col_ing_btn3 = st.columns(3)
    
    with col_ing_btn1:
        st.button("📄 Konu Anlatımını Aç", type="primary", key="ing_konu") 
    with col_ing_btn2:
        st.button("💬 Konuşma Alıştırması", type="secondary", key="ing_konusma")
    with col_ing_btn3:
        st.button("🔥 Kelime Testi", type="secondary", key="ing_test")
    
    st.markdown("---")
    
    with st.expander("💬 7. Sınıf İngilizce Konularına Göz Atın"):
        st.info("Aşağıda 7. Sınıf İngilizce Ünitelerine ait genel bir özet listelenmiştir. Kel

