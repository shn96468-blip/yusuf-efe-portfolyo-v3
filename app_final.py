import streamlit as st
import random
import time

# --- 1. SÖZLÜK YÜKLEME FONKSİYONU ---
def load_dictionary(file_path="kelime_sozlugu.txt"):
    """Sözlük dosyasını okur ve Türkçe -> İngilizce ve İngilizce -> Türkçe olmak üzere iki sözlük oluşturur."""
    tr_en_dict = {}
    en_tr_dict = {}
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    # Satırı türkçe:ingilizce formatında ayır
                    if ':' in line:
                        tr_word, en_word = line.split(':', 1)
                        tr_word = tr_word.strip().lower()
                        en_word = en_word.strip().lower()
                        
                        if tr_word and en_word:
                            # Türkçe -> İngilizce
                            tr_en_dict[tr_word] = en_word
                            # İngilizce -> Türkçe
                            en_tr_dict[en_word] = tr_word
                    
        if not tr_en_dict:
            st.warning("⚠️ Sözlük dosyası boş veya format hatası içeriyor. Lütfen 'türkçe:ingilizce' formatını kontrol edin.")
            return None, None
            
        return tr_en_dict, en_tr_dict

    except FileNotFoundError:
        st.error(f"❌ Hata: Sözlük dosyası '{file_path}' bulunamadı! Sözlük dosyası bulunamadı hatası almışsınız. Uygulama demo kelimelerle çalıştırılacaktır.")
        
        # --- Demo kelimeler (Hata durumunda) ---
        demo_tr_en = {"merhaba": "hello", "kitap": "book", "başarı": "success", "koşmak": "run"}
        demo_en_tr = {"hello": "merhaba", "book": "kitap", "success": "başarı", "run": "koşmak"}
        return demo_tr_en, demo_en_tr
    except Exception as e:
        st.error(f"❌ Sözlük yüklenirken beklenmedik bir hata oluştu: {e}")
        return None, None

# --- SÖZLÜĞÜ YÜKLE ---
TR_EN_DICT, EN_TR_DICT = load_dictionary()
ALL_WORDS = list(TR_EN_DICT.keys()) # Kelime Kartları için Türkçe kelimeler listesi

# --- SABİT METİNLER VE İÇERİK ---
MATH_CONTENT = """
## 📘 Matematik - Konu Anlatımı ve Özet
<div style='background-color: #26292e; padding: 10px; border-radius: 5px;'>
    <p>🔑 Konu: 7. Sınıf Matematik Tüm Üniteler</p>
</div>

### 📄 Detaylı Konu Özeti
7. Sınıf Matematik dersi 6 ana üniteden oluşmaktadır.

#### Tam Sayılarda Dört İşlem (Detaylı Anlatım)
1. **Toplama İşlemi:**
    * **Aynı İşaretliler:** Değerler toplanır, ortak işaret sonuca konur.
        * Örnek 1: $+5 + (+3) = +8$
        * Örnek 2: $-5 + (-3) = -8$
    * **Farklı İşaretliler:** Mutlak değeri büyük olandan küçük olan çıkarılır ve mutlak değeri büyük olanın işareti sonuca konur.
        * Örnek 1: $+8 + (-3) = +5$
        * Örnek 2: $-8 + (+3) = -5$

2. **Çıkarma İşlemi:**
    * Çıkarma işlemi, çıkan sayının **ters işaretlisini** eklemeye dönüştürülür (Toplama kuralına dönüştürülür).
        * Örnek: $10 - (-3)$ işlemi $10 + (+3) = 13$ olur.
        * Örnek: $-10 - (+3)$ işlemi $-10 + (-3) = -13$ olur.

3. **Çarpma/Bölme İşlemi:**
    * **Aynı İşaretliler:** Sonuç her zaman **pozitiftir (+)**.
        * Örnek: $(+5) \times (+3) = +15$
        * Örnek: $(-5) \times (-3) = +15$
    * **Farklı İşaretliler:** Sonuç her zaman **negatiftir (-)**.
        * Örnek: $(+10) \div (-2) = -5$
        * Örnek: $(-10) \div (+2) = -5$
"""
TURKISH_CONTENT = """
## 📖 Türkçe - Konu Anlatımı ve Özet
<div style='background-color: #26292e; padding: 10px; border-radius: 5px;'>
    <p>🔑 Konu: 7. Sınıf Türkçe Tüm Konular</p>
</div>

### 📄 Detaylı Konu Anlatımı
7. Sınıf Türkçe dersi, dil bilgisi, anlam bilgisi ve yazma becerileri üzerine odaklanır.

#### 1. Anlam Bilgisi (Sözcük, Cümle ve Paragrafta Anlam)
* **Sözcükte Anlam:** Gerçek, mecaz ve terim anlam. (Örn: 'Sıcak' ev (Gerçek), 'Sıcak' karşılama (Mecaz)).
* **Cümlede Anlam:** Öznel (kişisel görüş) ve Nesnel (kanıtlanabilir) yargılar. Neden-Sonuç, Amaç-Sonuç cümleleri.
* **Paragrafta Anlam:** Ana fikir, yardımcı fikirler, başlık ve konunun belirlenmesi.

#### 2. Dil Bilgisi (Fiiller ve Ekler)
* **Fiiller (Eylemler):** İş, oluş, durum bildirirler.
* **Kip ve Kişi Ekleri:**
    * **Haber Kipleri (Zaman Bildirir):** Görülen Geçmiş (-di), Duyulan Geçmiş (-miş), Şimdiki (-yor), Gelecek (-ecek), Geniş (-r).
    * **Dilek Kipleri (Dilek/Şart Bildirir):** Gereklilik (-meli), Şart (-sa), İstek (-e), Emir (Eki yoktur).
"""

# --- 2. STREAMLIT SAYFA AYARLARI ---
st.set_page_config(layout="wide", page_title="Yusuf Efe Şahin | 7. Sınıf Eğitim Portalı")

# --- 3. BAŞLIK VE SEKME YAPISI ---
st.title("👨‍🎓 Yusuf Efe Şahin | 7. Sınıf Eğitim Portalı")
st.markdown("---")

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "💡 Koç Modülü", 
    "🔢 Matematik İçerikleri", 
    "📝 Türkçe İçerikleri", 
    "🗣️ Kelime Çevirisi (Hızlı Sözlük)", 
    "🧠 Kelime Kartları (Test Modülü)"
])

# --- 4. TAB 1: KOÇ MODÜLÜ ---
with tab1:
    st.header("💡 Koç Modülü (Cebirsel İfadeler)")
    
    # Koç Cevap Bloğu
    st.markdown(
        """
        <div style='background-color: #38761d; padding: 15px; border-radius: 8px;'>
            <p style='color: white; margin: 0;'>Koç Cevabı: 'tam sayılarda toplama nedir'</p>
            <p style='color: #e0e0e0; font-size: 14px; margin-top: 10px;'>'konusuyla ilgili sana özel olarak hazırladığım ekstra alıştırmalar ve 7. sınıf müfredatındaki en kritik 3 bilgi notunu içeren bir özet hazırlıyorum. Unutma, pratik yapmak başarıyı getirir!'</p>
        </div>
        """, unsafe_allow_html=True
    )

    st.markdown("---")
    
    # Koç Açıklama Bloğu
    st.markdown(
        """
        <div style='background-color: #8fbc94; padding: 10px; border-radius: 5px;'>
            <p style='color: #1a1a1a; margin: 0;'>**Koç Açıklaması - Konu: Cebirsel İfadeler **</p>
        </div>
        """, unsafe_allow_html=True
    )
    st.markdown(MATH_CONTENT.replace("## 📘 Matematik", "## Matematik").replace("### 📄 Detaylı Konu Özeti", ""), unsafe_allow_html=True) # Cebirsel ifadeler konu başlığı görselde var

    # Sesli Çıktı Simülasyonu
    st.markdown("---")
    st.subheader("🔊 Sesli Robot Çıktısı (Simülasyon)")
    st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3", start_time=182) 
    st.caption("(Yukarıdaki ses bileşeni, konunun sesli olarak okunduğunu simüle eder.)")

# --- 5. TAB 2: MATEMATİK İÇERİKLERİ ---
with tab2:
    st.header("🔢 Matematik Dersi İçerikleri")
    col_math_btn1, col_math_btn2, col_math_btn3 = st.columns(3)
    
    with col_math_btn1:
        st.button("📄 Konu Anlatımı", type="primary")
    with col_math_btn2:
        st.button("♦️ PDF Sonuç Kontrol", type="secondary")
    with col_math_btn3:
        st.button("🔥 Deneme Sınavı", type="secondary")
    
    st.markdown("---")
    st.markdown(MATH_CONTENT, unsafe_allow_html=True)


# --- 6. TAB 3: TÜRKÇE İÇERİKLERİ ---
with tab3:
    st.header("📝 Türkçe Dersi İçerikleri")
    col_tr_btn1, col_tr_btn2, col_tr_btn3 = st.columns(3)

    with col_tr_btn1:
        st.button("📄 Konu Anlatımı ve Özet", type="primary")
    with col_tr_btn2:
        st.button("♦️ Hikaye Analizi", type="secondary")
    with col_tr_btn3:
        st.button("🔥 Yazım Kılavuzu", type="secondary")

    st.markdown("---")
    st.markdown(TURKISH_CONTENT, unsafe_allow_html=True)

# --- 7. TAB 4: KELİME ÇEVİRİSİ (HIZLI SÖZLÜK) ---
with tab4:
    st.header("🗣️ Kelime Çevirisi (Hızlı Sözlük)")
    st.info("Tek bir kelime girin. Sözlüğümüzde varsa hızlıca Türkçe ↔ İngilizce çevirisini görün.")

    col1, col2 = st.columns(2)

    with col1:
        kelime_input = st.text_input("Çevrilecek Kelimeyi Girin:", placeholder="Örn: başarı veya one").strip().lower()

    with col2:
        cevir_yonu = st.selectbox("Çeviri Yönü:", 
                                   ["Türkçe -> İngilizce", "İngilizce -> Türkçe"])
    
    if st.button("Kelimeyi Çevir", type="primary"):
        st.markdown("---")
        st.subheader("💡 Çeviri Sonucu")

        if not kelime_input:
            st.error("Lütfen çevrilecek bir kelime girin.")
        else:
            sonuc = None
            if cevir_yonu == "Türkçe -> İngilizce":
                if kelime_input in TR_EN_DICT:
                    sonuc = TR_EN_DICT[kelime_input]
                    st.success(f"**{kelime_input.capitalize()}** kelimesinin İngilizce karşılığı: **{sonuc.capitalize()}**")
                else:
                    # Kullanıcının önceki hatasına benzer uyarı
                    st.warning(f"**{kelime_input.capitalize()}** kelimesinin İngilizce karşılığı sözlüğümüzde bulunamadı. (Sözlüğünüzü genişletin!)")
            
            elif cevir_yonu == "İngilizce -> Türkçe":
                if kelime_input in EN_TR_DICT:
                    sonuc = EN_TR_DICT[kelime_input]
                    st.success(f"**{kelime_input.capitalize()}** kelimesinin Türkçe karşılığı: **{sonuc.capitalize()}**")
                else:
                    # Kullanıcının önceki hatasına benzer uyarı
                    st.warning(f"**{kelime_input.capitalize()}** kelimesinin Türkçe karşılığı sözlüğümüzde bulunamadı. (Sözlüğünüzü genişletin!)")
            
            # Sesli robot simülasyonu
            if sonuc:
                st.markdown("---")
                st.subheader("🔊 Sesli Okunuş (Simülasyon)")
                st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3", start_time=60)
                st.caption("(Yukarıdaki ses bileşeni, çevrilen kelimenin sesli okunuşunu simüle eder.)")

# --- 8. TAB 5: KELİME KARTLARI (TEST MODÜLÜ) ---
with tab5:
    st.header("🧠 Kelime Kartları (Test Modülü)")
    
    # Kelime listesi boşsa uyarı ver
    if not ALL_WORDS:
        st.error("Kelime Kartları modülünü kullanmak için sözlüğünüzde kelime bulunmalıdır.")
    else:
        # Session State Yönetimi
        if 'test_words' not in st.session_state:
            st.session_state.test_words = random.sample(ALL_WORDS, min(5, len(ALL_WORDS)))
            st.session_state.current_index = 0
            st.session_state.show_translation = False

        current_tr_word = st.session_state.test_words[st.session_state.current_index]
        current_en_word = TR_EN_DICT.get(current_tr_word, "ÇEVİRİ BULUNAMADI")

        st.subheader(f"Kelime {st.session_state.current_index + 1} / {len(st.session_state.test_words)}")
        st.markdown(f"## 🇹🇷 {current_tr_word.capitalize()}")

        # Çeviriyi Göster/Gizle butonu
        def toggle_translation():
            st.session_state.show_translation = not st.session_state.show_translation

        # Önceki/Sonraki butonları
        def next_word():
            st.session_state.current_index = (st.session_state.current_index + 1) % len(st.session_state.test_words)
            st.session_state.show_translation = False

        def prev_word():
            st.session_state.current_index = (st.session_state.current_index - 1) % len(st.session_state.test_words)
            st.session_state.show_translation = False

        st.markdown("---")

        if st.session_state.show_translation:
            st.info(f"🇬🇧 Anlamı: **{current_en_word.capitalize()}**")
        else:
            st.info("Anlamını görmek için 'Çeviriyi Göster'e tıklayın.")


        col_card1, col_card2, col_card3 = st.columns([1, 1, 1])

        with col_card1:
            st.button("⬅️ Önceki Kelime", on_click=prev_word, disabled=(len(st.session_state.test_words) == 1))

        with col_card2:
            button_label = "Çeviriyi Gizle" if st.session_state.show_translation else "Çeviriyi Göster"
            st.button(f"👁️ {button_label}", on_click=toggle_translation, type="primary")

        with col_card3:
            st.button("➡️ Sonraki Kelime", on_click=next_word, type="secondary")
            
        st.markdown("---")
        
        # Testi Yenile butonu
        if st.button("🔄 Yeni Bir Test Başlat (5 Kelime)", help="Sözlükten rastgele 5 yeni kelime seçer"):
             st.session_state.test_words = random.sample(ALL_WORDS, min(5, len(ALL_WORDS)))
             st.session_state.current_index = 0
             st.session_state.show_translation = False
             st.experimental_rerun()
