# app_final.py dosyasındaki mevcut render_subject_tab fonksiyonunu bu kodla DEĞİŞTİRİN

# --- 8. DERS SEKMELERİ İÇİN GENEL FONKSİYON ---
def render_subject_tab(tab_context, subject_title, key_prefix):
    konu_key = f"{key_prefix}_konu"
    pdf_key = f"{key_prefix}_pdf"; deneme_key = f"{key_prefix}_deneme"
    
    # Kalan 4 ders için detaylı konu listeleri buraya eklenmiştir
    if key_prefix == "tr":
        konu_listesi = [
            "Sözcükte Anlam", "Cümlede Anlam", "Parçada Anlam", "Tablo, Grafik, Görsel Yorumlama",
            "Metin Türleri", "Söz Sanatları", "Fiiller", "Ek Fiil", "Zarflar", 
            "Anlatım Bozuklukları", "Yazım Kuralları", "Noktalama İşaretleri"
        ]
    elif key_prefix == "mat":
        konu_listesi = [
            "Tam Sayılarla İşlemler (1. Ünite)", "Rasyonel Sayılar ve İşlemleri (2. Ünite)", 
            "Cebirsel İfadelerden Eşitlik ve Denklemlere (3. Ünite)", 
            "Oran Orantıdan Yüzdelere (4. Ünite)", "Doğrular ve Açılar, Çokgenler, Çember ve Daire (5. Ünite)",
            "Veri Analizinden Cisimlerin Farklı Yönlerden Görünümlerine (6. Ünite)"
        ]
    elif key_prefix == "sci":
        konu_listesi = [
            "Güneş Sistemi ve Ötesi (1. Ünite)", "Hücre ve Bölünmeler (2. Ünite)", 
            "Kuvvet ve Enerji (3. Ünite)", "Saf Madde ve Karışımlar (4. Ünite)", 
            "Işığın Madde ile Etkileşimi (5. Ünite)", "Canlılarda Üreme, Büyüme ve Gelişme (6. Ünite)", 
            "Elektrik Devreleri (7. Ünite)"
        ]
    elif key_prefix == "soc":
        konu_listesi = [
            "Birey ve Toplum (1. Ünite)", "Kültür ve Miras (2. Ünite)", 
            "İnsanlar, Yerler ve Çevreler (3. Ünite)", "Bilim, Teknoloji ve Toplum (4. Ünite)", 
            "Üretim, Dağıtım ve Tüketim (5. Ünite)", "Etkin Vatandaşlık (6. Ünite)", 
            "Küresel Bağlantılar (7. Ünite)"
        ]
    else:
        konu_listesi = ["Bu derse ait Konu Listesi Henüz Eklenmedi."]

    
    with tab_context:
        st.header(f"{subject_title} Dersi İçerikleri")
        
        # SADECE 3 BUTON KALDI
        col_btn1, col_btn2, col_btn3 = st.columns(3) 
        
        with col_btn1:
            button_label = "⬆️ Konuyu Gizle" if st.session_state.content_key == konu_key else "📄 Konu Anlatımı"
            st.button(button_label, type="primary", key=konu_key, on_click=toggle_content, args=(konu_key,)) 
                      
        with col_btn2: st.button("♦️ PDF Sonuç Kontrol", type="secondary", key=pdf_key)
        with col_btn3: st.button("🔥 Deneme Sınavı", type="secondary", key=deneme_key)
        
        st.markdown("---")
        
        if st.session_state.content_key == konu_key:
            st.subheader(f"✨ {subject_title} Dersi Konu Listesi") 
            
            # YENİ EKLENEN KISIM: KONU LİSTESİNİ GÖSTER
            for konu in konu_listesi:
                st.markdown(f"* **{konu}**")
            
            st.markdown("---")

            # KONU ANLATIMI DETAY METNİNİ GÖSTER
            st.subheader("📘 Konu Anlatımı Detay")
            st.markdown(CONTENT_MAP.get(konu_key, "İçerik Bulunamadı. Lütfen ilgili içerik dosyanızı kontrol edin."), unsafe_allow_html=True)
            st.markdown("---")
            
        else:
            st.info(f"Yukarıdaki butona tıklayarak {subject_title} dersi içeriğini görebilirsiniz.")
