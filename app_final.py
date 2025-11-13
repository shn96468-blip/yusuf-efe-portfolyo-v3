# ... render_subject_tab fonksiyonu içinde ...

    with col_btn1:
        # 1. Butona tıklandığında set_content_and_show çalışır.
        st.button("📄 Konu Anlatımı", type="primary", key=f"{subject_key}_konu",
                  on_click=set_content_and_show, args=(content_key,)) 
    # ... diğer butonlar ...
    
    st.markdown("---")
    
    # 2. Eğer o ders seçiliyse, içerik gösterilir.
    if st.session_state.page_selected == content_key and st.session_state.content_show:
        st.subheader(f"✨ {subject_title} Konu Anlatımı Detay")
        st.markdown(CONTENT_MAP[content_key], unsafe_allow_html=True)
        
        # İçeriği gizleme butonu da hemen altında görünür.
        if st.button("⬆️ Konu Anlatımını Gizle", key=f"{subject_key}_hide"):
            st.session_state.content_show = False
            st.session_state.page_selected = 'coach' 
    else:
        # Butona tıklanmadıysa, varsayılan özet gösterilir.
        st.info(f"Yukarıdaki '📄 Konu Anlatımı' butonuna tıklayarak {subject_title} dersi içeriğini görebilirsiniz.")
        st.markdown(CONTENT_MAP[content_key], unsafe_allow_html=True)
