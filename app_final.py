# app_final.py dosyasındaki mevcut render_subject_tab fonksiyonunu bu kodla DEĞİŞTİRİN

# --- 8. DERS SEKMELERİ İÇİN GENEL FONKSİYON ---
def render_subject_tab(tab_context, subject_title, key_prefix):
    konu_key = f"{key_prefix}_konu"
    pdf_key = f"{key_prefix}_pdf"; deneme_key = f"{key_prefix}_deneme"
    
    # Her ders için konuları burada tanımlayın (Örn: Türkçe konuları)
    if key_prefix == "tr":
        konu_listesi = ["Fiil (Eylem)", "Ek Fiil", "Zarf", "Söz Sanatları", "Yazım ve Noktalama"]
    elif key_prefix == "mat":
        konu_listesi = ["Tam Sayılar", "Rasyonel Sayılar", "Cebirsel İfadeler", "Oran-Orantı", "Çokgenler"]
    elif key_prefix == "sci":
        konu_listesi = ["Güneş Sistemi", "Hücre Bölünmesi (Mitoz-Mayoz)", "Kuvvet ve Enerji", "Işık", "Elektrik"]
    elif key_prefix == "soc":
        konu_listesi = ["Birey ve Toplum", "Kültür ve Miras", "İnsanlar ve Çevreler", "Üretim ve Tüketim"]
    else:
        konu_listesi = ["Konu Listesi Henüz Eklenmedi."]

    
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
            st.subheader("📘 Konu Anlatımı Detay (Aşağıdaki Metin content dosyanızdan geliyor)")
            st.markdown(CONTENT_MAP.get(konu_key, "İçerik Bulunamadı. Lütfen ilgili içerik dosyanızı kontrol edin."), unsafe_allow_html=True)
            st.markdown("---")
            
        else:
            st.info(f"Yukarıdaki butona tıklayarak {subject_title} dersi içeriğini görebilirsiniz.")
