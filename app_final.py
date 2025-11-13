# render_subject_tab FONKSİYONUNUN TAMAMINI AŞAĞIDAKİ KODLA DEĞİŞTİRİN

def render_subject_tab(tab_context, subject_title, key_prefix):
    konu_key = f"{key_prefix}_konu"
    pdf_key = f"{key_prefix}_pdf"; deneme_key = f"{key_prefix}_deneme"
    
    with tab_context:
        st.header(f"{subject_title} Dersi İçerikleri")
        
        # 4 buton yerine, sadece 3 buton (Konu Anlatımı, PDF, Deneme) kullanılıyor.
        col_btn1, col_btn3, col_btn4 = st.columns(3) 
        
        with col_btn1:
            button_label = "⬆️ Konuyu Gizle" if st.session_state.content_key == konu_key else "📄 Konu Anlatımı"
            st.button(button_label, type="primary", key=konu_key, on_click=toggle_content, args=(konu_key,)) 
            
        # Sabit Video İzle butonu SİLİNDİ (col_btn2 atlandı)
                      
        with col_btn3: st.button("♦️ PDF Sonuç Kontrol", type="secondary", key=pdf_key)
        with col_btn4: st.button("🔥 Deneme Sınavı", type="secondary", key=deneme_key)
        
        st.markdown("---")
        
        if st.session_state.content_key == konu_key:
            st.subheader(f"✨ {subject_title} Konu Anlatımı Detay") 
            st.markdown(CONTENT_MAP.get(konu_key, "İçerik Bulunamadı. Lütfen ilgili içerik dosyanızı kontrol edin."), unsafe_allow_html=True)
            st.markdown("---")
            
        else:
            st.info(f"Yukarıdaki butona tıklayarak {subject_title} dersi içeriğini görebilirsiniz.")
