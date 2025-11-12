# --- MÜZİK ÇALMA MANTIĞI (Özel Link Kontrolü Burada) ---
if st.session_state['music_enabled'] and st.session_state['music_url']:
    st.audio(
        st.session_state['music_url'], 
        format="audio/mp3", 
        start_time=0, 
        loop=True,
        html_attrs={"autoplay": "autoplay", "volume": st.session_state['music_volume']} 
    )
