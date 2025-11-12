# ==============================================================================
# --- 5. TAB 1: MATEMATİK İÇERİKLERİ ---
# ==============================================================================
with tab_math:
    st.header("🔢 Matematik Dersi İçerikleri")
    col_math_btn1, col_math_btn2, col_math_btn3 = st.columns(3)
    
    with col_math_btn1:
        # BUTONA İŞLEV EKLEDİK: TIKLANDIĞINDA İÇERİĞİ GÖSTER
        konu_anlatimi_clicked = st.button("📄 Konu Anlatımı", type="primary", key="mat_konu") 
    with col_math_btn2:
        st.button("♦️ PDF Sonuç Kontrol", type="secondary", key="mat_pdf")
    with col_math_btn3:
        st.button("🔥 Deneme Sınavı", type="secondary", key="mat_deneme")
    
    # EĞER (IF) KONU ANLATIMI BUTONUNA TIKLANIRSA:
    if konu_anlatimi_clicked:
        st.subheader("📝 Matematik Konu Anlatımı")
        st.markdown(MATH_CONTENT, unsafe_allow_html=True)
        st.markdown("---") # İçeriği ayırmak için çizgi
    else:
        # Butona tıklanmazsa, ana içeriği göstermeye devam et (isteğe bağlı, kaldırılabilir)
        st.markdown(MATH_CONTENT, unsafe_allow_html=True)
