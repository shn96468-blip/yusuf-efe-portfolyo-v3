# ==============================================================================
# --- 8. TAB 4: SOSYAL BİLGİLER İÇERİKLERİ ---
# ==============================================================================
with tab_soc:
    st.header("🌍 Sosyal Bilgiler Dersi İçerikleri")
    col_sosyal_btn1, col_sosyal_btn2, col_sosyal_btn3 = st.columns(3)
    
    with col_sosyal_btn1:
        st.button("📄 Konu Anlatımı", type="primary", key="sos_konu") 
    with col_sosyal_btn2:
        st.button("📜 Tarihi Olaylar", type="secondary", key="sos_olay")
    with col_sosyal_btn3:
        st.button("🔥 Coğrafya Bilgisi", type="secondary", key="sos_cografya")
    
    st.markdown("---")  # <--- Hata veren satırın düzeltilmiş hali
    st.markdown(SOCIAL_CONTENT, unsafe_allow_html=True)
