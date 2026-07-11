# ==========================================================================================
# APOLINGO ARCADE HIGH-END UI DESIGN (YENİLENMİŞ ARAYÜZ CSS)
# ==========================================================================================
st.markdown("""
    <style>
    /* Genel Arka Plan ve Metin Renkleri */
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #020617 100%) !important;
        color: #f8fafc !important;
    }
    
    /* Üst Başlık ve Efektler */
    .main-title {
        font-family: 'Segoe UI', Roboto, Helvetica, sans-serif;
        font-size: 3rem !important;
        font-weight: 800 !important;
        background: linear-gradient(90deg, #3b82f6, #8b5cf6, #ec4899);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 5px;
        letter-spacing: 2px;
        filter: drop-shadow(0px 4px 12px rgba(139, 92, 246, 0.3));
    }
    
    .sub-title {
        text-align: center;
        font-size: 1.1rem;
        color: #94a3b8 !important;
        margin-bottom: 25px;
    }
    
    /* Bilgi Kartları (Dashboard Havası) */
    .info-container {
        display: flex;
        gap: 15px;
        justify-content: center;
        margin-bottom: 30px;
    }
    
    .info-card {
        background: rgba(30, 41, 59, 0.4);
        border: 1px solid rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        padding: 15px 25px;
        border-radius: 12px;
        text-align: center;
        min-width: 200px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
        transition: transform 0.3s ease;
    }
    
    .info-card:hover {
        transform: translateY(-3px);
        border-color: #8b5cf6;
    }

    /* Mikrofon ve Input Hizalamaları */
    .stAudioInput {
        margin-top: 5px !important;
    }
    
    /* Muazzam Arcade Buton Tasarımları */
    div[data-testid="stButton"] > button {
        margin-top: 5px !important;
        background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%) !important;
        border: 2px solid #4b5563 !important;
        color: #e2e8f0 !important;
        border-radius: 12px !important;
        height: 46px !important;
        width: 100% !important;
        font-size: 18px !important;
        font-weight: bold !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1) !important;
    }
    
    /* Buton Hover Efektleri (Renk Koduna Göre Parlama) */
    div[data-testid="stButton"] > button:hover {
        border-color: #3b82f6 !important;
        box-shadow: 0 0 15px rgba(59, 130, 246, 0.6) !important;
        transform: scale(1.03);
    }
    
    /* Özel Çıkış Butonu Stili */
    .exit-btn div[data-testid="stButton"] > button {
        background: linear-gradient(135deg, #ef4444 0%, #991b1b 100%) !important;
        border: 1px solid #f87171 !important;
    }
    .exit-btn div[data-testid="stButton"] > button:hover {
        box-shadow: 0 0 15px rgba(239, 68, 68, 0.6) !important;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================================================================
# GÖRÜNÜM KONTROLÜ VE YENİ ARAYÜZ ELEMANLARI
# ==========================================================================================
if st.session_state.aktif_oyun is None:
    # Süslü HTML Başlık Alanı
    st.markdown('<h1 class="main-title">🚀 APOLINGO MASTER ARCADE AI</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">🤖 Evrenin En Detaylı Yapay Zekası & Sınırsız Eğlence Paneli | <b>By Abdurrahim İriş</b></p>', unsafe_allow_html=True)
    
    # İstatistik/Bilgi Kartları (Dashboard Görünümü)
    st.markdown("""
        <div class="info-container">
            <div class="info-card">
                <span style="color: #94a3b8; font-size: 12px; display:block;">BAŞ MÜHENDİS</span>
                <span style="color: #3b82f6; font-size: 18px; font-weight:bold;">APOLINGO</span>
            </div>
            <div class="info-card">
                <span style="color: #94a3b8; font-size: 12px; display:block;">SİSTEM DURUMU</span>
                <span style="color: #10b981; font-size: 18px; font-weight:bold;">● ÇEVRİMİÇİ</span>
            </div>
            <div class="info-card">
                <span style="color: #94a3b8; font-size: 12px; display:block;">SESLİ DİNLEME</span>
                <span style="color: #ec4899; font-size: 18px; font-weight:bold;">AKTİF 🎙️</span>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    st.write("---")

    # Mesaj geçmişi ekrana yazılıyor
    for mesaj in st.session_state.sohbet_hafizasi:
        if mesaj["role"] == "user":
            with st.chat_message("user"):
                st.write(mesaj["content"])
        elif mesaj["role"] == "assistant":
            with st.chat_message("assistant"):
                st.write(mesaj["content"])

    gelen_soru = None

    # ELEMAN DİZİLİMİ
    c_mic, c_text, c_game1, c_game2 = st.columns([0.10, 0.74, 0.08, 0.08])
    
    with c_mic:
        ses_dosyasi = st.audio_input("🎙️", label_visibility="collapsed", key=f"mic_{len(st.session_state.sohbet_hafizasi)}")
        
    with c_text:
        yazi_soru = st.chat_input("Buraya yaz be gardaşşşşş...")
        if yazi_soru:
            gelen_soru = yazi_soru
            
    with c_game1:
        if st.button("🏎️ M3", help="Erkek Oyunu (BMW M3) Başlat!"):
            st.session_state.aktif_oyun = "erkek"
            st.rerun()
            
    with c_game2:
        if st.button("🌌 Aura", help="Kız Oyunu (Astro-Aura) Başlat!"):
            st.session_state.aktif_oyun = "kiz"
            st.rerun()

    # (Buradan sonrası mevcut ses işleme ve yanıt mekanizmanla birebir devam ediyor...)
