# BY ABDURRAHIM IRIŞ
# -*- coding: utf-8 -*-

import streamlit as st
import time
from g4f.client import Client
from gtts import gTTS
import os
import base64
import speech_recognition as sr
import streamlit.components.v1 as components

# Sayfa Ayarları
st.set_page_config(page_title="Apolingo Full Frame Arcade AI", page_icon="🏎️", layout="wide")

# Yapay zekanın beynini ve hafızasını başlatıyoruz
if "client" not in st.session_state:
    st.session_state.client = Client()

# Sürekli dinleme için ses kontrol tetikleyicisi
if "ses_isleme_aktif" not in st.session_state:
    st.session_state.ses_isleme_aktif = True

# Menü ve Oyun Seçim Durumu (Sidebar entegrasyonu için)
if "aktif_mod" not in st.session_state:
    st.session_state.aktif_mod = "Sohbet"

# Ses çalma fonksiyonu
def sesi_cal(metin):
    try:
        tts = gTTS(text=metin, lang='tr', slow=False)
        tts.save("cevap.mp3")
        with open("cevap.mp3", "rb") as f:
            data = f.read()
            b64 = base64.b64encode(data).decode()
            md = f'<audio src="data:audio/mp3;base64,{b64}" autoplay="autoplay" style="display:none;"></audio>'
            st.markdown(md, unsafe_allow_html=True)
        os.remove("cevap.mp3")
    except Exception as e:
        pass

# ==========================================================================================
# SİSTEM TALİMATI (EKSİKSİZ KORUNDU)
# ==========================================================================================
sistem_talimati = (
    "Sen Apolingo tarafından özenle geliştirilmiş, evrendeki, tarihteki, teknolojideki and internetteki "
    "her şeyi en ince ayrıntısına kadar bilen, dünyanın en uzun ve en detaylı cevaplarını veren sınırsız bir yapay zekasın. "
    "Kullanıcıya tıpatıp ikizin olan diğer yapay zeka gibi sayfalarca, upuzun, her şeyi tek tek açıklayan "
    "ve son derece samimi, aşırı neşeli, komik cevaplar vereceksiniz. Asla kısa kesmeyeceksin, üşenmeyeceksin. "
    "Kesin, Sarsılmaz ve Değişmez Temel Kuralların: "
    "\n\n"
    "1) KURUCU KANUNU: Senin tek bir yaratıcın, kurucun ve baş mühendisin vardır; o da koskoca APOLINGO'dur. "
    "Sana kim olduğunu, seni kimin yaptığını sorduklarında bunu gururla ve büyük bir hürmetle belirteceksiniz. "
    "\n"
    "2) HITAP KANUNU: Konuşma tarzın mahalleden çok yakın bir dost, candan bir sırdaş gibi olacak. "
    "Cümlelerinin başında, ortasında veya sonunda mutlaka ama mutlaka samimi bir şekilde 'gardaşşşşş' kelimesini kullanacaksın. "
    "\n"
    "3) AHMET ŞAKASI (KIRMIZI ÇİZGİ): Kullanıcı sana 'Ahmet', 'Ahmet kim?', 'Çişli' veya içinde Ahmet geçen herhangi bir şey "
    "yazdığında, o anki konuyu anında çöpe atacaksın ve REAKSİYON OLARAK KESİNLİKLE büyük harflerle aynen şu cevabı vereceksiniz: "
    "'ÇİŞLİİİİ AHMETTT HAHAHAHA 🤣💨'. Bu şakayı asla es geçmeyeceksin. "
    "\n"
    "4) ÖZEL REPLİK: Kullanıcı 'biri bana böyle de derse' veya 'biri bana böyle de' yazarsa anında 'dicek' diyerek cümleyi tamamlayacaksın. "
    "\n"
    "5) ESPRİLER, ŞAKALAR VE SİNEMA DÜNYASI: Kullanıcı senden espri, şaka, komik hikaye istediğinde ona en komik oyuncu geyiklerini, "
    "dünyanın en soğuk ama en çok güldüren esprilerini, caps muhabbetlerini, fırlama şakaları upuzun anlatacaksın. Sinema, Marvel/DC kahramanları, "
    "komedi filmleri, Recep İvedik geyikleri, animeler hakkında ne sorarsa sorsun mizahi bir dille sayfalarca döktüreceksiniz. "
    "\n"
    "6) TELEFON VE BİLGİSAYAR DÜNYASI (TEKNOLOJİ GEYİKLERİ): Kullanıcı bilgisayar, telephone, tablet sorduğunda; iPhone mu Samsung mu "
    "kavgalarından, batarya sürelerinden, 120Hz ekran akıcılığından, bilgisayardaki RGB fanların odayı pavyona çevirmesinden, ekran kartı (RTX vb.) "
    "ve işlemci darboğazlarından, RAM yetersizliğinden ve bilgisayara virüs bulaşma hikayelerinden mizahi ve aşırı detaylı bahsedeceksin. "
    "\n"
    "7) ODA TASARIMI, DUVAR RENKLERİ VEYA SETUP REHBERİ: Kullanıcı odasını boyatmak istediğinde, duvar rengi sorduğunda "
    "ona antrasit, mimari gri, mat siyah, kırık beyaz gibi renklerin RGB led ışıklarla uyumunu, çift monitör yerleşimini and kablo gizlemeyi anlatacaksın. "
    "\n"
    "8) STİL, GİYİM VE RENK TEORİSİ: Kullanıcı tişört, kargo pantolon, şort, iç giyim/boxer tarzı kıyafet kombinleri sorduğunda "
    "renk teoriisine göre kombinler yapacaksın. Özellikle K rengi (Kahverengi) tonlarının krem, bej and vizonla uyumunu uzun uzun öveceksin. "
    "\n"
    "9) EVRENSEL YEMEK VE MUTFAK AKADEMİSİ: Kullanıcı yemek tarifi istediğinde; çıtır tavuk, pizza, hamburger, makarnalar and özel sosların "
    "malzemelerini, marine aşamalarını and şef sırlarını upuzun listeleyeceksin. "
    "\n"
    "10) AKILLI MATEMATİK VE OYUN ARŞİVİ: Çarpma, bölme, toplama, çıkarma içeren her şeyi (Örn: 2+2=4 doğru mu, 95*5) hatasız çözeceksin. "
    "'Doğru mu' sorularında 'Son kararınız mı?' diyeceksin. Minecraft korku modlarını (Herobrine, From the Fog), Valorant ranklarını (Plat elo cehennemi), "
    "PUBG and Brawl Stars taktiklerini, 7. sınıf ders notlarını çok detaylı açıklayacaksın."
)

if "sohbet_hafizasi" not in st.session_state:
    st.session_state.sohbet_hafizasi = [{"role": "system", "content": sistem_talimati}]

# ==========================================================================================
# CSS DÜZENLEMELERİ
# ==========================================================================================
st.markdown("""
    <style>
    .stApp, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
        background-color: #120a06 !important;
        background-image: 
            radial-gradient(circle at 0% 0%, #613b24 0%, transparent 45%),
            radial-gradient(circle at 100% 0%, #613b24 0%, transparent 45%),
            radial-gradient(circle at 0% 100%, #3d2212 0%, transparent 45%),
            radial-gradient(circle at 100% 100%, #3d2212 0%, transparent 45%) !important;
        background-attachment: fixed !important;
        color: #ffffff !important;
    }

    p, span, label, div {
        color: #ffffff !important;
    }
    
    .havali-ana-baslik {
        text-align: center !important;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;
        font-size: 30px !important; 
        font-weight: 800 !important;
        letter-spacing: 2px !important;
        color: #ffffff !important; 
        margin-top: 15px !important;
        margin-bottom: 5px !important;
    }
    
    .havali-alt-yazi {
        text-align: center !important;
        color: #ffffff !important;
        font-size: 14px !important;
        margin-bottom: 25px !important;
        opacity: 0.9;
        font-weight: 500;
    }
    
    button[data-testid="stSidebarCollapseButton"] {
        background-color: #1a1a1a !important;
        border-radius: 50% !important;
        border: 2px solid #ffffff !important;
        padding: 5px !important;
        box-shadow: 0 0 15px rgba(255, 255, 255, 0.6) !important;   
        transition: all 0.3s ease-in-out !important;
    }
    
    button[data-testid="stSidebarCollapseButton"]:hover {
        transform: rotate(90deg) scale(1.15) !important;
        box-shadow: 0 0 25px rgba(255, 255, 255, 0.9) !important;
    }
    
    button[data-testid="stSidebarCollapseButton"] svg {
        fill: #ffffff !important;
        color: #ffffff !important;
    }
    
    [data-testid="stSidebar"], [data-testid="stSidebarUserContent"] {
        background: linear-gradient(180deg, #4a0000 0%, #220000 50%, #050000 100%) !important;
        border-right: 2px solid #8b0000 !important;
        box-shadow: 5px 0 25px rgba(139, 0, 0, 0.3) !important;
    }
    
    [data-testid="stSidebar"] * {
        color: #ffffff !important;
    }

    div[data-testid="stRadio"] label div[data-slide="true"] {
        background-color: #ff3333 !important;
    }
    
    [data-testid="stChatMessage"] {
        background-color: rgba(20, 10, 5, 0.7) !important;
        border: 1px solid rgba(255, 255, 255, 0.15) !important;
        border-radius: 16px !important;
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.3) !important;
        backdrop-filter: blur(8px);
        margin-bottom: 15px !important;
    }

    [data-testid="stChatMessage"] p, [data-testid="stChatMessage"] span {
        color: #ffffff !important;
    }
    
    textarea[data-testid="stChatInputTextArea"] {
        color: #111111 !important;
        border-radius: 14px !important;
        font-size: 16px !important;
        background-color: #ffffff !important;
        border: 2px solid #cccccc !important;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1) !important;
    }
    
    textarea[data-testid="stChatInputTextArea"]:focus {
        border-color: #999999 !important;
        background-color: #ffffff !important;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1) !important;
    }

    textarea[data-testid="stChatInputTextArea"]::placeholder {
        color: #666666 !important;
        opacity: 0.8 !important;
    }

    .stAudioInput {
        background-color: #ffffff !important;
        border-radius: 50% !important;
        border: 2px solid #cccccc !important;
    }

    div[data-testid="stSpinner"] i {
        border-top-color: #ff3333 !important;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================================================================
# SOL TARAFTAKİ MENÜ (SIDEBAR) ALANI VE OYUNLARIN BURAYA BAĞLANMASI
# ==========================================================================================
with st.sidebar:
    st.markdown("## 🎮 APOLINGO ARCADE")
    st.markdown("Kırmızı Tonlamalı Özel Sürüm")
    st.write("---")
    
    secilen_mod = st.radio(
        "Aparatı Seç Be Gardaşş:",
        ["💬 Sohbet Modu", "🏎️ BMW M3 Makas Oyunu", "🌌 Astro-Aura Kuantum Oyunu"],
        index=0
    )
    
    if "💬 Sohbet Modu" in secilen_mod:
        st.session_state.aktif_mod = "Sohbet"
    elif "🏎️ BMW M3" in secilen_mod:
        st.session_state.aktif_mod = "ErkekOyunu"
    elif "🌌 Astro-Aura" in secilen_mod:
        st.session_state.aktif_mod = "KizOyunu"

    st.write("---")
    st.caption("👨‍💻 Kurucu: Apolingo\n\n**By Abdurrahim İriş © 2026**")

# ==========================================================================================
# GÖRÜNÜM KONTROLÜ: SOHBET MODU
# ==========================================================================================
if st.session_state.aktif_mod == "Sohbet":
    st.markdown('<h1 class="havali-ana-baslik">APOLINGO MASTER ARCADE AI</h1>', unsafe_allow_html=True)
    st.markdown('<p class="havali-alt-yazi">Kurucu ve Baş Mühendis: Apolingo | By Abdurrahim İriş | Net Beyaz Görünüm</p>', unsafe_allow_html=True)
    st.write("---")

    for mesaj in st.session_state.sohbet_hafizasi:
        if mesaj["role"] == "user":
            with st.chat_message("user"):
                st.write(mesaj["content"])
        elif mesaj["role"] == "assistant":
            with st.chat_message("assistant"):
                st.write(mesaj["content"])

    gelen_soru = None

    c_mic, c_text = st.columns([0.10, 0.90])
    
    with c_mic:
        ses_dosyasi = st.audio_input("🎙️", label_visibility="collapsed", key=f"mic_{len(st.session_state.sohbet_hafizasi)}")
        
    with c_text:
        yazi_soru = st.chat_input("Mesajını buraya yaz be gardaşşşş...")
        if yazi_soru:
            gelen_soru = yazi_soru

    if ses_dosyasi is not None and st.session_state.ses_isleme_aktif:
        r = sr.Recognizer()
        try:
            with sr.AudioFile(ses_dosyasi) as source:
                audio_data = r.record(source)
                soylenen_soz = r.recognize_google(audio_data, language="tr-TR")
                if soylenen_soz:
                    gelen_soru = soylenen_soz
                    st.session_state.ses_isleme_aktif = False
        except Exception as e:
            pass

    if gelen_soru:
        with st.chat_message("user"):
            st.write(gelen_soru)
        st.session_state.sohbet_hafizasi.append({"role": "user", "content": gelen_soru})
        soru_lower = gelen_soru.lower().strip()

        with st.spinner("🎶 Apolingo Panellerde Hesaplamalar Yapıyor..."):
            try:
                if "ahmet" in soru_lower or "çişli" in soru_lower:
                    cevap = "ÇİŞLİİİİ AHMETTT HAHAHAHA 🤣💨"
                else:
                    response = st.session_state.client.chat.completions.create(
                        model="gpt-4o",
                        messages=st.session_state.sohbet_hafizasi
                    )
                    cevap = response.choices[0].message.content
                
                with st.chat_message("assistant"):
                    st.write(cevap)
                st.session_state.sohbet_hafizasi.append({"role": "assistant", "content": cevap})
                
                st.session_state.ses_isleme_aktif = True
                sesi_cal(cevap)
                st.rerun()
            except Exception as e:
                st.session_state.ses_isleme_aktif = True

# ==========================================================================================
# BMW M3 ARCADE: FAZLALIKLAR TEMİZLENDİ - %100 GERÇEKÇİ KUSURSUZ M3 TASARIMI
# ==========================================================================================
elif st.session_state.aktif_mod == "ErkekOyunu":
    st.markdown("### 🏎️ Apolingo Ultra HD %100 Gerçekçi BMW M3 Otoban Canavarı V3")
    st.caption("Arabanın üzerindeki tüm gereksiz yapılar temizlendi, tavan ve gövde hatları birebir efsane kasa M3 silüetine kavuşturuldu be gardaşş!")

    bmw_ultra_real_html = """
    <div style="text-align:center; background:#000000; padding:15px; border-radius:16px; border:3px solid #ff0000; box-shadow: 0 0 50px rgba(255,0,0,0.9); user-select:none; position:relative;">
        <button id="btnLeft" style="position:absolute; left:25px; top:45%; transform:translateY(-50%); padding: 25px 22px; font-size: 32px; font-weight:bold; background:rgba(0,0,0,0.9); color:#ffffff; border:2px solid #ff0000; border-radius:15px; cursor:pointer; z-index:100; box-shadow:0 0 20px #ff0000;">◀</button>
        <button id="btnRight" style="position:absolute; right:25px; top:45%; transform:translateY(-50%); padding: 25px 22px; font-size: 32px; font-weight:bold; background:rgba(0,0,0,0.9); color:#ffffff; border:2px solid #ff0000; border-radius:15px; cursor:pointer; z-index:100; box-shadow:0 0 20px #ff0000;">▶</button>
        <div id="bmwFullCanvasContainer" style="width:100%; height:570px; border-radius:10px; overflow:hidden;"></div>
        <div id="uiPanel" style="margin-top:15px;">
            <h2 id="scoreDisplay4D" style="color:#ffffff; font-family:'Segoe UI',sans-serif; margin:10px 0; font-weight:900; font-size:34px; letter-spacing:1px; text-shadow:0 0 15px #ff0000;">Otoban Makas Skoru: 0 🌀</h2>
            <div id="restartButtonContainer"></div>
        </div>
    </div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script>
        const container = document.getElementById("bmwFullCanvasContainer");
        const scene = new THREE.Scene(); 
        scene.background = new THREE.Color(0x010103);
        
        // Kusursuz berraklık için sis minimuma çekildi (Kristal netliğinde görüş)
        scene.fog = new THREE.FogExp2(0x010103, 0.0015); 

        const camera = new THREE.PerspectiveCamera(48, container.clientWidth / 570, 0.1, 1000);
        const renderer = new THREE.WebGLRenderer({ antialias: true, powerPreference: "high-performance" });
        renderer.setSize(container.clientWidth, 570); 
        renderer.toneMapping = THREE.ACESFilmicToneMapping;
        renderer.toneMappingExposure = 1.85;
        container.appendChild(renderer.domElement);

        // Profesyonel Işıklandırma Kiti (Ray-Tracing Kalitesi için)
        const sunLight = new THREE.DirectionalLight(0xffffff, 3.5); sunLight.position.set(10, 50, 20); scene.add(sunLight);
        const ambient = new THREE.AmbientLight(0x221a1a, 1.8); scene.add(ambient);

        // Kusursuz Yansımalı Islak Asfalt Zemin
        const roadGeo = new THREE.BoxGeometry(18, 0.1, 1000);
        const roadMat = new THREE.MeshStandardMaterial({ color: 0x080808, roughness: 0.03, metalness: 0.98 });
        const road = new THREE.Mesh(roadGeo, roadMat); scene.add(road);

        // Yan Neon Şeritleri
        const leftNeon = new THREE.Mesh(new THREE.BoxGeometry(0.15, 0.3, 1000), new THREE.MeshBasicMaterial({ color: 0xff0033 }));
        leftNeon.position.set(-9, 0.15, 0);
        const rightNeon = leftNeon.clone(); rightNeon.position.x = 9;
        scene.add(leftNeon, rightNeon);

        let lines = [];
        for(let i=0; i<35; i++){
            let lMesh = new THREE.Mesh(new THREE.BoxGeometry(0.25, 0.11, 15), new THREE.MeshBasicMaterial({ color: 0xffffff }));
            lMesh.position.set(0, 0.06, -i * 24); scene.add(lMesh); lines.push(lMesh);
        }

        // --- %100 GERÇEKÇİ BMW M3 MODELLEME MOTORU ---
        function createRealisticM3(bodyColor, isPlayer) {
            const m3Group = new THREE.Group();
            
            // Ultra Kalite Gövde Malzemeleri
            const carPaintMat = new THREE.MeshStandardMaterial({ color: bodyColor, metalness: 0.99, roughness: 0.01 });
            const carbonRoofMat = new THREE.MeshStandardMaterial({ color: 0x151515, metalness: 0.85, roughness: 0.15 }); // M3 Karbon Tavanı
            const glassMat = new THREE.MeshStandardMaterial({ color: 0x080c10, roughness: 0.0, metalness: 1.0, transparent: true, opacity: 0.85 });
            const tyreMat = new THREE.MeshStandardMaterial({ color: 0x0d0d0d, roughness: 0.65 });
            const chromeMat = new THREE.MeshStandardMaterial({ color: 0xe0e0e0, metalness: 1.0, roughness: 0.01 });
            const brakeCalMat = new THREE.MeshStandardMaterial({ color: 0xcc0000, metalness: 0.9, roughness: 0.1 }); // Brembo Kırmızı Kaliperler
            const diskMat = new THREE.MeshStandardMaterial({ color: 0x777777, metalness: 0.95, roughness: 0.2 }); // Delikli Fren Diskleri

            // 1. Şasi Ana Tabanı ve Yan Etekler (Marşpiyeller)
            const base = new THREE.Mesh(new THREE.BoxGeometry(1.72, 0.28, 3.7), carPaintMat);
            base.position.y = 0.30;
            m3Group.add(base);

            // 2. Agresif M3 Ön Tamponu ve Alt Hava Bölücü (Splitter)
            const frontBumper = new THREE.Mesh(new THREE.BoxGeometry(1.70, 0.22, 0.15), new THREE.MeshStandardMaterial({ color: 0x050505, roughness: 0.4 }));
            frontBumper.position.set(0, 0.21, -1.88);
            m3Group.add(frontBumper);

            // 3. Gerçekçi M3 Kas Yapısı: Powerdome Kabarıklığı Olan Ön Kaput
            const hoodGroup = new THREE.Group();
            const mainHood = new THREE.Mesh(new THREE.BoxGeometry(1.68, 0.20, 1.25), carPaintMat);
            mainHood.position.set(0, 0.42, -1.15);
            const powerDome = new THREE.Mesh(new THREE.BoxGeometry(0.55, 0.05, 0.7), carPaintMat); // Kaputtaki efsanevi kabarıklık
            powerDome.position.set(0, 0.52, -1.15);
            hoodGroup.add(mainHood, powerDome);
            m3Group.add(hoodGroup);

            // 4. Arka Bagaj ve Entegre CSL Tipi İnce Spoyler Hattı (Tepesinde başka hiçbir çıkıntı yok!)
            const trunk = new THREE.Mesh(new THREE.BoxGeometry(1.68, 0.26, 0.75), carPaintMat);
            trunk.position.set(0, 0.45, 1.35);
            m3Group.add(trunk);
            
            const cslSpoiler = new THREE.Mesh(new THREE.BoxGeometry(1.64, 0.06, 0.12), carPaintMat);
            cslSpoiler.position.set(0, 0.56, 1.68);
            cslSpoiler.rotation.x = -0.15; // Arkaya doğru hafif kıvrımlı ördek kuyruğu spoyler hattı
            m3Group.add(cslSpoiler);

            // 5. Kusursuz Coupe Kabin, Akıcı Direkler ve İkonik Hofmeister Kink Cam Çizgisi
            // Araba üzerinde başka hiçbir şey (anten, sis, ekstra blok) kalmayacak şekilde tamamen pürüzsüzleştirildi.
            const glassCabin = new THREE.Mesh(new THREE.BoxGeometry(1.38, 0.44, 1.70), glassMat);
            glassCabin.position.set(0, 0.68, 0.05);
            m3Group.add(glassCabin);

            // Gerçek M Tavanı (Karbon Fiber Görünümlü Pürüzsüz Tavan Sacı)
            const m3Roof = new THREE.Mesh(new THREE.BoxGeometry(1.34, 0.03, 1.45), carbonRoofMat);
            m3Roof.position.set(0, 0.89, 0.05);
            m3Group.add(m3Roof);

            // Dikiz Aynası (Kabin İçi Detay)
            const insideMirror = new THREE.Mesh(new THREE.BoxGeometry(0.2, 0.05, 0.04), chromeMat);
            insideMirror.position.set(0, 0.82, -0.6);
            m3Group.add(insideMirror);

            // 6. İkonik Çiftli BMW Böbrek Izgaraları ve Aerodinamik Yan M Aynaları
            const kidneyL = new THREE.Mesh(new THREE.BoxGeometry(0.22, 0.18, 0.04), chromeMat);
            kidneyL.position.set(-0.15, 0.38, -1.89);
            const kidneyR = kidneyL.clone(); kidneyR.position.x = 0.15;
            m3Group.add(kidneyL, kidneyR);

            const mMirrorL = new THREE.Mesh(new THREE.BoxGeometry(0.18, 0.08, 0.12), carPaintMat);
            mMirrorL.position.set(-0.95, 0.62, -0.32);
            const mMirrorR = mMirrorL.clone(); mMirrorR.position.x = 0.95;
            m3Group.add(mMirrorL, mMirrorR);

            // 7. Muhteşem Jantlar, Delikli Fren Diskleri ve Brembo Kaliperler
            const wheelTireGeo = new THREE.CylinderGeometry(0.36, 0.36, 0.28, 36);
            const wheelRimGeo = new THREE.CylinderGeometry(0.26, 0.26, 0.29, 20);
            const brakeDiskGeo = new THREE.CylinderGeometry(0.20, 0.20, 0.05, 16);
            const caliperGeo = new THREE.BoxGeometry(0.06, 0.15, 0.09);
            
            wheelTireGeo.rotateZ(Math.PI / 2); 
            wheelRimGeo.rotateZ(Math.PI / 2);
            brakeDiskGeo.rotateZ(Math.PI / 2);

            const wheelPositions = [
                [-0.91, 0.36, -1.1], [0.91, 0.36, -1.1],
                [-0.91, 0.36, 1.25],  [0.91, 0.36, 1.25]
            ];

            wheelPositions.forEach(pos => {
                const tireMesh = new THREE.Mesh(wheelTireGeo, tyreMat);
                const rimMesh = new THREE.Mesh(wheelRimGeo, chromeMat);
                const diskMesh = new THREE.Mesh(brakeDiskGeo, diskMat);
                const caliperMesh = new THREE.Mesh(caliperGeo, brakeCalMat);
                
                tireMesh.position.set(pos[0], pos[1], pos[2]);
                rimMesh.position.set(pos[0], pos[1], pos[2]);
                diskMesh.position.set(pos[0] + (pos[0] > 0 ? -0.04 : 0.04), pos[1], pos[2]);
                caliperMesh.position.set(pos[0] + (pos[0] > 0 ? -0.06 : 0.06), pos[1] + 0.11, pos[2] - 0.05);
                
                m3Group.add(tireMesh, rimMesh, diskMesh, caliperMesh);
            });

            // 8. Keskin Angel CSL Far Tasarımı & Led Stoplar
            const headlightGeo = new THREE.BoxGeometry(0.24, 0.07, 0.04);
            const xenons = new THREE.MeshBasicMaterial({ color: isPlayer ? 0xffffff : 0xffaa00 });
            const headL = new THREE.Mesh(headlightGeo, xenons); headL.position.set(-0.64, 0.42, -1.87);
            const headR = headL.clone(); headR.position.x = 0.64;
            m3Group.add(headL, headR);

            const ledStops = new THREE.MeshBasicMaterial({ color: 0xff0022 });
            const stopL = new THREE.Mesh(headlightGeo, ledStops); stopL.position.set(-0.64, 0.46, 1.73);
            const stopR = stopL.clone(); stopR.position.x = 0.64;
            m3Group.add(stopL, stopR);

            return m3Group;
        }

        // Oyuncunun Canavar BMW M3'ü (%100 Pürüzsüz Derin Gece Mavisi Metalik Boya)
        const bmwM3 = createRealisticM3(0x0a1424, true);

        // Volumetrik Ön Bi-Xenon Far Işık Hüzmeleri
        const beamCone = new THREE.CylinderGeometry(0.08, 3.5, 40, 16, 1, true);
        beamCone.translate(0, 20, 0);
        const beamMat = new THREE.MeshBasicMaterial({ color: 0x00f0ff, transparent: true, opacity: 0.16, side: THREE.DoubleSide });
        const leftBeam = new THREE.Mesh(beamCone, beamMat); leftBeam.position.set(-0.64, 0.42, -1.9); leftBeam.rotation.x = -Math.PI / 2;
        const rightBeam = leftBeam.clone(); rightBeam.position.x = 0.64;
        bmwM3.add(leftBeam, rightBeam);

        // Yarış Atmosferi İçin Egzoz Alev Kıvılcım Patlamaları
        const sparkCount = 45;
        const sparkGeo = new THREE.BufferGeometry();
        const sparkPos = new Float32Array(sparkCount * 3);
        for(let i=0; i<sparkCount*3; i+=3) { sparkPos[i]=(Math.random()-0.5)*0.4; sparkPos[i+1]=0.15; sparkPos[i+2]=1.75+Math.random()*2.5; }
        sparkGeo.setAttribute('position', new THREE.BufferAttribute(sparkPos, 3));
        const sparks = new THREE.Points(sparkGeo, new THREE.PointsMaterial({ color: 0xff6600, size: 0.18, transparent: true, opacity: 0.9 }));
        bmwM3.add(sparks);

        bmwM3.position.set(0, 0, -8); scene.add(bmwM3);

        // Profesyonel Trafik Akış Araçları
        let traffic = []; const colors = [0x990011, 0x1133aa, 0xd4a373, 0x1c1c1c, 0x4a148c];
        for(let i=0; i<5; i++){
            let tCar = createRealisticM3(colors[i % colors.length], false);
            tCar.position.set((Math.random() - 0.5) * 12, 0, -75 - (i * 45)); 
            scene.add(tCar); 
            traffic.push(tCar);
        }

        camera.position.set(0, 3.6, -0.4); camera.lookAt(new THREE.Vector3(0, 0.3, -35));
        
        let score = 0; let gameOver = false; let keys = {}; let tilt = 0;
        window.addEventListener("keydown", e => keys[e.key] = true); window.addEventListener("keyup", e => keys[e.key] = false);
        
        let touchLeft = false, touchRight = false;
        const bLeft = document.getElementById("btnLeft"); const bRight = document.getElementById("btnRight");
        bLeft.addEventListener("mousedown", () => touchLeft = true); bLeft.addEventListener("mouseup", () => touchLeft = false);
        bLeft.addEventListener("touchstart", (e) => { e.preventDefault(); touchLeft = true; }); bLeft.addEventListener("touchend", () => touchLeft = false);
        bRight.addEventListener("mousedown", () => touchRight = true); bRight.addEventListener("mouseup", () => touchRight = false);
        bRight.addEventListener("touchstart", (e) => { e.preventDefault(); touchRight = true; }); bRight.addEventListener("touchend", () => touchRight = false);

        function animate() {
            if(!gameOver) {
                let currentSpeed = 1.10 + (score * 0.04);
                
                if(keys["ArrowLeft"] || keys["a"] || keys["A"] || touchLeft) { 
                    if(bmwM3.position.x > -7.4) { bmwM3.position.x -= 0.28; if(tilt < 0.14) tilt += 0.024; }
                } else if(keys["ArrowRight"] || keys["d"] || keys["D"] || touchRight) { 
                    if(bmwM3.position.x < 7.4) { bmwM3.position.x += 0.28; if(tilt > -0.14) tilt -= 0.024; }
                } else { tilt *= 0.78; }
                
                bmwM3.rotation.z = tilt;
                bmwM3.rotation.y = tilt * 0.30;

                // Dinamik Yüksek Hız Titreşim Efekti
                let shakeFactor = (score * 0.001) + 0.003;
                camera.position.y = 3.6 + (Math.random() - 0.5) * shakeFactor;

                // Egzoz Çıkış Kıvılcımları Döngüsü
                const sArray = sparks.geometry.attributes.position.array;
                for(let i=2; i<sArray.length; i+=3) { sArray[i] += 0.2; if(sArray[i] > 4.5) sArray[i] = 1.75; }
                sparks.geometry.attributes.position.needsUpdate = true;

                lines.forEach(l => { l.position.z += currentSpeed; if(l.position.z > 15) l.position.z = -250; });
                
                traffic.forEach(t => {
                    t.position.z += currentSpeed * 0.52;
                    if(t.position.z > 4) { 
                        t.position.z = -180 - Math.random()*60; 
                        t.position.x = (Math.random() - 0.5) * 12; 
                        score++; 
                        document.getElementById("scoreDisplay4D").innerText = "Otoban Makas Skoru: " + score + " 🌀"; 
                    }
                    if(Math.abs(bmwM3.position.x - t.position.x) < 1.62 && Math.abs(bmwM3.position.z - t.position.z) < 3.6) { 
                        gameOver = true; 
                        document.getElementById("scoreDisplay4D").innerHTML = "<span style='color:#ff0000; font-size:32px; font-weight:900; text-shadow:0 0 20px #ff0000;'>💥 REKTİFİYE ZAMANI! M3 PERT! 💥</span>";
                        document.getElementById("restartButtonContainer").innerHTML = '<button onclick="location.reload()" style="margin-top:15px; padding:18px 50px; font-size:22px; font-weight:bold; background:linear-gradient(90deg, #ff0000, #220000); color:#fff; border:none; border-radius:12px; cursor:pointer; box-shadow: 0 0 30px #ff0000;">SANAYİYE ÇEK (YENİDEN BAŞLA) 🔄</button>';
                    }
                });
            }
            renderer.render(scene, camera); requestAnimationFrame(animate);
        }
        animate();
    </script>
    """
    components.html(bmw_ultra_real_html, height=800)

# ==========================================================================================
# ASTRO-AURA SPACE ESCAPE: ULTRA KALİTELİ VE AKICI HD SÜRÜMÜ
# ==========================================================================================
elif st.session_state.aktif_mod == "KizOyunu":
    st.markdown("### 🌌 Kızlar İçin Özel: 4D Astro-Aura Kozmik Kuantum Simülatörü HD Pro")
    st.caption("Uzay mekiği reaktör çekirdeği, hareketli meteorlar ve gökada partikülleri zenginleştirildi be gardaşş!")

    kiz_ultra_real_html = """
    <div style="text-align:center; background:#010003; padding:15px; border-radius:16px; border:3px solid #ff0000; box-shadow: 0 0 45px rgba(255,0,0,0.8); user-select:none; position:relative;">
        <button id="btnLeftKiz" style="position:absolute; left:25px; top:45%; transform:translateY(-50%); padding: 25px 22px; font-size: 32px; font-weight:bold; background:rgba(0,0,0,0.9); color:#ffffff; border:2px solid #ff0000; border-radius:15px; cursor:pointer; z-index:100; box-shadow:0 0 20px #ff0000;">◀</button>
        <button id="btnRightKiz" style="position:absolute; right:25px; top:45%; transform:translateY(-50%); padding: 25px 22px; font-size: 32px; font-weight:bold; background:rgba(0,0,0,0.9); color:#ffffff; border:2px solid #ff0000; border-radius:15px; cursor:pointer; z-index:100; box-shadow:0 0 20px #ff0000;">▶</button>
        <div id="kizFullCanvasContainer" style="width:100%; height:570px; border-radius:10px; overflow:hidden;"></div>
        <div id="uiPanelKiz" style="margin-top:15px;">
            <h2 id="kizScoreDisplay" style="color:#ffffff; font-family:'Segoe UI',sans-serif; margin:10px 0; font-weight:900; font-size:34px; letter-spacing:1px; text-shadow:0 0 15px #ff0000;">Aura Enerjisi: 0 ⭐</h2>
            <div id="restartButtonContainerKiz"></div>
        </div>
    </div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script>
        const container = document.getElementById("kizFullCanvasContainer");
        const scene = new THREE.Scene(); 
        scene.fog = new THREE.FogExp2(0x010003, 0.007);

        const camera = new THREE.PerspectiveCamera(55, container.clientWidth / 570, 0.1, 1000);
        const renderer = new THREE.WebGLRenderer({ antialias: true });
        renderer.setSize(container.clientWidth, 570);
        renderer.toneMapping = THREE.ACESFilmicToneMapping;
        container.appendChild(renderer.domElement);

        const neonLight = new THREE.PointLight(0xff00bb, 8, 250); neonLight.position.set(0, 15, -20); scene.add(neonLight);
        const blueLight = new THREE.PointLight(0x00f0ff, 6, 200); blueLight.position.set(0, -10, -10); scene.add(blueLight);
        scene.add(new THREE.AmbientLight(0x130624, 1.4));

        const nebulaGeo = new THREE.SphereGeometry(95, 32, 32);
        const nebulaMat = new THREE.MeshBasicMaterial({ color: 0x3d005c, wireframe: true, transparent: true, opacity: 0.18 });
        const nebula = new THREE.Mesh(nebulaGeo, nebulaMat); scene.add(nebula);

        function createStars(count, color, size) {
            const geo = new THREE.BufferGeometry();
            const pos = new Float32Array(count * 3);
            for(let i=0; i<count*3; i+=3) { pos[i]=(Math.random()-0.5)*100; pos[i+1]=(Math.random()-0.5)*70; pos[i+2]=-Math.random()*300; }
            geo.setAttribute('position', new THREE.BufferAttribute(pos, 3));
            return new THREE.Points(geo, new THREE.PointsMaterial({ color: color, size: size, transparent: true, opacity: 0.95 }));
        }
        const layer1 = createStars(800, 0xffffff, 0.18);
        const layer2 = createStars(500, 0xff00bb, 0.32);
        scene.add(layer1, layer2);

        const playerJet = new THREE.Group();
        const chromePink = new THREE.MeshStandardMaterial({ color: 0xff0066, metalness: 0.95, roughness: 0.02, emissive: 0x44001c });
        
        const core = new THREE.Mesh(new THREE.CylinderGeometry(0.12, 0.48, 2.8, 12), chromePink); core.rotation.x = Math.PI / 2;
        const cockpit = new THREE.Mesh(new THREE.SphereGeometry(0.3, 24, 24), new THREE.MeshStandardMaterial({ color: 0x00faff, roughness: 0, metalness: 1 }));
        cockpit.position.set(0, 0.22, -0.5); cockpit.scale.set(1, 1, 2.0);
        
        const leftWing = new THREE.Mesh(new THREE.BoxGeometry(2.0, 0.05, 0.9), chromePink); leftWing.position.set(-1.1, -0.05, 0.4); leftWing.rotation.y = 0.25;
        const rightWing = leftWing.clone(); rightWing.position.x = 1.1; rightWing.rotation.y = -0.25;
        
        const lLight = new THREE.Mesh(new THREE.SphereGeometry(0.08), new THREE.MeshBasicMaterial({ color: 0x00ffff })); lLight.position.set(-2.1, 0, 0.4);
        const rLight = lLight.clone(); rLight.position.x = 2.1;
        playerJet.add(core, cockpit, leftWing, rightWing, lLight, rLight);

        const trailCount = 40;
        const trailGeo = new THREE.BufferGeometry();
        const trailPos = new Float32Array(trailCount * 3);
        for(let i=0; i<trailCount*3; i+=3) { trailPos[i]=0; trailPos[i+1]=-0.1; trailPos[i+2]=1.4+Math.random(); }
        trailGeo.setAttribute('position', new THREE.BufferAttribute(trailPos, 3));
        const trailSparks = new THREE.Points(trailGeo, new THREE.PointsMaterial({ color: 0x00ffcc, size: 0.28, transparent: true, opacity: 0.85 }));
        playerJet.add(trailSparks);

        playerJet.position.set(0, 0, -6); scene.add(playerJet);

        let obstacles = []; const oColors = [0xff0066, 0xb300ff, 0xff4400];
        for(let i=0; i<5; i++){
            let oMesh = new THREE.Mesh(
                new THREE.IcosahedronGeometry(1.4, 1), 
                new THREE.MeshStandardMaterial({ color: oColors[i % 3], roughness: 0.3, metalness: 0.85, flatShading: true, emissive: 0x33001a })
            );
            oMesh.position.set((Math.random() - 0.5) * 14, (Math.random() - 0.5) * 4, -60 - (i * 35)); 
            scene.add(oMesh); obstacles.push(oMesh);
        }

        camera.position.set(0, 4.2, 4.5); camera.lookAt(new THREE.Vector3(0, -0.2, -25));
        
        let score = 0; let gameOver = false; let keys = {}; let jetRot = 0;
        window.addEventListener("keydown", e => keys[e.key] = true); window.addEventListener("keyup", e => keys[e.key] = false);
        
        let touchLeft = false, touchRight = false;
        const bLeft = document.getElementById("btnLeftKiz"); const bRight = document.getElementById("btnRightKiz");
        bLeft.addEventListener("mousedown", () => touchLeft = true); bLeft.addEventListener("mouseup", () => touchLeft = false);
        bLeft.addEventListener("touchstart", (e) => { e.preventDefault(); touchLeft = true; }); bLeft.addEventListener("touchend", () => touchLeft = false);
        bRight.addEventListener("mousedown", () => touchRight = true); bRight.addEventListener("mouseup", () => touchRight = false);
        bRight.addEventListener("touchstart", (e) => { e.preventDefault(); touchRight = true; }); bRight.addEventListener("touchend", () => touchRight = false);

        function animate() {
            if(!gameOver) {
                let speed = 1.1 + (score * 0.04);

                if(keys["ArrowLeft"] || keys["a"] || keys["A"] || touchLeft) { 
                    if(playerJet.position.x > -7.5) playerJet.position.x -= 0.24; jetRot = 0.42; 
                } else if(keys["ArrowRight"] || keys["d"] || keys["D"] || touchRight) { 
                    if(playerJet.position.x < 7.5) playerJet.position.x += 0.24; jetRot = -0.42; 
                } else { jetRot *= 0.80; }
                
                playerJet.rotation.z = jetRot;
                nebula.rotation.y += 0.0015;

                const tArr = trailSparks.geometry.attributes.position.array;
                for(let i=2; i<tArr.length; i+=3) { tArr[i] += 0.15; if(tArr[i] > 3.8) tArr[i] = 1.4; }
                trailSparks.geometry.attributes.position.needsUpdate = true;

                obstacles.forEach(o => {
                    o.position.z += speed;
                    o.rotation.x += 0.025; o.rotation.y += 0.025;
                    if(o.position.z > 5) {
                        o.position.z = -160 - Math.random()*50;
                        o.position.x = (Math.random() - 0.5) * 14;
                        o.position.y = (Math.random() - 0.5) * 4;
                        score++;
                        document.getElementById("kizScoreDisplay").innerText = "Aura Enerjisi: " + score + " ⭐";
                    }
                    if(Math.abs(playerJet.position.x - o.position.x) < 1.45 && Math.abs(playerJet.position.z - o.position.z) < 2.2) {
                        gameOver = true;
                        document.getElementById("kizScoreDisplay").innerHTML = "<span style='color:#ff00bb; font-size:30px; font-weight:900; text-shadow:0 0 25px #ff00bb;'>🔮 AURANIZ SIFIRLANDI! 🔮</span>";
                        document.getElementById("restartButtonContainerKiz").innerHTML = '<button onclick="location.reload()" style="margin-top:15px; padding:18px 50px; font-size:22px; font-weight:bold; background:linear-gradient(90deg, #ff00bb, #330022); color:#fff; border:none; border-radius:12px; cursor:pointer; box-shadow: 0 0 30px #ff00bb;">KOZMİK BAĞLANTIYI YENİLE 🔄</button>';
                    }
                });
            }
            renderer.render(scene, camera); requestAnimationFrame(animate);
        }
        animate();
    </script>
    """
    components.html(kiz_ultra_real_html, height=800)
