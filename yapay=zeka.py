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
    "ona antrasit, mimari gri, mat siyah, kırık beyaz gibi renklerin RGB led ışıklarla uyumunu, çift monitör yerleşimini ve kablo gizlemeyi anlatacaksın. "
    "\n"
    "8) STİL, GİYİM VE RENK TEORİSİ: Kullanıcı tişört, kargo pantolon, şort, iç giyim/boxer tarzı kıyafet kombinleri sorduğunda "
    "renk teoriisine göre kombinler yapacaksın. Özellikle K rengi (Kahverengi) tonlarının krem, bej ve vizonla uyumunu uzun uzun öveceksin. "
    "\n"
    "9) EVRENSEL YEMEK VE MUTFAK AKADEMİSİ: Kullanıcı yemek tarifi istediğinde; çıtır tavuk, pizza, hamburger, makarnalar ve özel sosların "
    "malzemelerini, marine aşamalarını ve şef sırlarını upuzun listeleyeceksin. "
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
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.15) !important;
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
        "Aparatı Seç Be Gardaşşş:",
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
# BMW M3 ARCADE: ULTRA FENASAL RAY-TRACING & ISLAK ASFALT GÜNCELLEMESİ
# ==========================================================================================
elif st.session_state.aktif_mod == "ErkekOyunu":
    st.markdown("### 🏎️ Apolingo Ultra Realistik BMW M3 Gece Makas Simülatörü")
    st.caption("Sol üstteki parıldayan Üç Çizgiye basarak istediğin an ana panele dönebilirsin gardaşşş!")

    bmw_ultra_real_html = """
    <div style="text-align:center; background:#010000; padding:15px; border-radius:16px; border:3px solid #ff0000; box-shadow: 0 0 45px rgba(255,0,0,0.8); user-select:none; position:relative;">
        <button id="btnLeft" style="position:absolute; left:25px; top:45%; transform:translateY(-50%); padding: 25px 22px; font-size: 32px; font-weight:bold; background:rgba(0,0,0,0.9); color:#ffffff; border:2px solid #ff0000; border-radius:15px; cursor:pointer; z-index:100; box-shadow:0 0 20px #ff0000;">◀</button>
        <button id="btnRight" style="position:absolute; right:25px; top:45%; transform:translateY(-50%); padding: 25px 22px; font-size: 32px; font-weight:bold; background:rgba(0,0,0,0.9); color:#ffffff; border:2px solid #ff0000; border-radius:15px; cursor:pointer; z-index:100; box-shadow:0 0 20px #ff0000;">▶</button>
        <div id="bmwFullCanvasContainer" style="width:100%; height:570px; border-radius:10px; overflow:hidden;"></div>
        <div id="uiPanel" style="margin-top:15px;">
            <h2 id="scoreDisplay4D" style="color:#ffffff; font-family:'Segoe UI',sans-serif; margin:10px 0; font-weight:900; font-size:34px; letter-spacing:1px; text-shadow:0 0 15px #ff0000;">4D Makas Skoru: 0 🌀</h2>
            <div id="restartButtonContainer"></div>
        </div>
    </div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script>
        const container = document.getElementById("bmwFullCanvasContainer");
        const scene = new THREE.Scene(); 
        scene.background = new THREE.Color(0x010002);
        scene.fog = new THREE.FogExp2(0x010002, 0.012);

        const camera = new THREE.PerspectiveCamera(50, container.clientWidth / 570, 0.1, 1000);
        const renderer = new THREE.WebGLRenderer({ antialias: true, powerPreference: "high-performance" });
        renderer.setSize(container.clientWidth, 570); 
        renderer.toneMapping = THREE.ACESFilmicToneMapping;
        renderer.toneMappingExposure = 1.4;
        container.appendChild(renderer.domElement);

        // Ultra Işık Şeması (Ray-Tracing simülasyonu)
        const sunLight = new THREE.DirectionalLight(0xffffff, 1.8); sunLight.position.set(10, 50, 20); scene.add(sunLight);
        const ambient = new THREE.AmbientLight(0x0a0505, 0.8); scene.add(ambient);

        // Islak ve Yansımalı Asfalt Teknolojisi
        const roadGeo = new THREE.BoxGeometry(18, 0.1, 1000);
        const roadMat = new THREE.MeshStandardMaterial({ color: 0x070606, roughness: 0.15, metalness: 0.85 }); // Yansıma yüksek tutuldu
        const road = new THREE.Mesh(roadGeo, roadMat); scene.add(road);

        // Neon Bariyer Işıkları (Yola yansıyan kırmızı çizgiler)
        const leftNeon = new THREE.Mesh(new THREE.BoxGeometry(0.2, 0.4, 1000), new THREE.MeshBasicMaterial({ color: 0xff0033 }));
        leftNeon.position.set(-9, 0.2, 0);
        const rightNeon = leftNeon.clone(); rightNeon.position.x = 9;
        scene.add(leftNeon, rightNeon);

        let lines = [];
        for(let i=0; i<35; i++){
            let lMesh = new THREE.Mesh(new THREE.BoxGeometry(0.3, 0.11, 14), new THREE.MeshBasicMaterial({ color: 0xffffff }));
            lMesh.position.set(0, 0.06, -i * 22); scene.add(lMesh); lines.push(lMesh);
        }

        // Ultra Detaylı BMW M3 Gövdesi
        const bmwM3 = new THREE.Group();
        const bodyMat = new THREE.MeshStandardMaterial({ color: 0x111111, metalness: 0.95, roughness: 0.02 }); // Metalik Mat Siyah/Krom kaplama
        const bodyBase = new THREE.Mesh(new THREE.BoxGeometry(1.6, 0.35, 3.4), bodyMat); bodyBase.position.y = 0.3; bmwM3.add(bodyBase);
        
        const cabinMat = new THREE.MeshStandardMaterial({ color: 0x050505, roughness: 0.0, metalness: 1.0 });
        const cabin = new THREE.Mesh(new THREE.BoxGeometry(1.3, 0.45, 1.6), cabinMat); cabin.position.set(0, 0.65, -0.1); bmwM3.add(cabin);

        // Krom Spor Jantlar
        const wheelGeo = new THREE.CylinderGeometry(0.3, 0.3, 0.25, 16);
        const wheelMat = new THREE.MeshStandardMaterial({ color: 0xdddddd, metalness: 1.0, roughness: 0.05 });
        const w1 = new THREE.Mesh(wheelGeo, wheelMat); w1.rotation.z = Math.PI/2; w1.position.set(-0.85, 0.3, -1);
        const w2 = w1.clone(); w2.position.x = 0.85;
        const w3 = w1.clone(); w3.position.z = 1.1;
        const w4 = w2.clone(); w4.position.z = 1.1;
        bmwM3.add(w1, w2, w3, w4);

        // Volumetrik Xenon Farlar (Ön tarafa yayılan koni şeklinde gerçekçi ışık hüzmesi)
        const lightConeGeo = new THREE.CylinderGeometry(0.1, 2.5, 25, 16, 1, true);
        lightConeGeo.translate(0, 12.5, 0);
        const lightConeMat = new THREE.MeshBasicMaterial({ color: 0xffffff, transparent: true, opacity: 0.15, side: THREE.DoubleSide });
        
        const leftHüzme = new THREE.Mesh(lightConeGeo, lightConeMat); leftHüzme.position.set(-0.6, 0.35, -1.7); leftHüzme.rotation.x = -Math.PI / 2;
        const rightHüzme = leftHüzme.clone(); rightHüzme.position.x = 0.6;
        bmwM3.add(leftHüzme, rightHüzme);

        // Arka Kırmızı LED Stop Lambaları
        const stopL = new THREE.Mesh(new THREE.BoxGeometry(0.3, 0.1, 0.1), new THREE.MeshBasicMaterial({ color: 0xff0000 })); stopL.position.set(-0.6, 0.45, 1.7);
        const stopR = stopL.clone(); stopR.position.x = 0.6;
        bmwM3.add(stopL, stopR);

        // Egzoz Alev/Kıvılcım Efekti
        const sparkCount = 40;
        const sparkGeo = new THREE.BufferGeometry();
        const sparkPos = new Float32Array(sparkCount * 3);
        for(let i=0; i<sparkCount*3; i+=3) { sparkPos[i]=(Math.random()-0.5)*0.4; sparkPos[i+1]=0.15; sparkPos[i+2]=1.7+Math.random()*2; }
        sparkGeo.setAttribute('position', new THREE.BufferAttribute(sparkPos, 3));
        const sparks = new THREE.Points(sparkGeo, new THREE.PointsMaterial({ color: 0xffaa00, size: 0.18, transparent: true, opacity: 0.9 }));
        bmwM3.add(sparks);

        bmwM3.position.set(0, 0, -8); scene.add(bmwM3);

        // Trafik Araçları (Yüksek Kaliteli Metalik Tasarım)
        let traffic = []; const colors = [0xff0055, 0x00f5ff, 0xffbb00, 0x8b00ff];
        for(let i=0; i<5; i++){
            let tGroup = new THREE.Group();
            let tBody = new THREE.Mesh(new THREE.BoxGeometry(1.6, 0.5, 3.2), new THREE.MeshStandardMaterial({ color: colors[i % colors.length], metalness: 0.8, roughness: 0.1 }));
            tBody.position.y = 0.35;
            let tGlass = new THREE.Mesh(new THREE.BoxGeometry(1.3, 0.4, 1.5), cabinMat); tGlass.position.set(0, 0.7, -0.1);
            tGroup.add(tBody, tGlass);
            tGroup.position.set((Math.random() - 0.5) * 12, 0, -60 - (i * 38)); scene.add(tGroup); traffic.push(tGroup);
        }

        camera.position.set(0, 4.0, -1.0); camera.lookAt(new THREE.Vector3(0, 0.3, -30));
        
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
                let currentSpeed = 0.95 + (score * 0.03);
                
                if(keys["ArrowLeft"] || keys["a"] || keys["A"] || touchLeft) { 
                    if(bmwM3.position.x > -7.2) { bmwM3.position.x -= 0.24; if(tilt < 0.15) tilt += 0.025; }
                } else if(keys["ArrowRight"] || keys["d"] || keys["D"] || touchRight) { 
                    if(bmwM3.position.x < 7.2) { bmwM3.position.x += 0.24; if(tilt > -0.15) tilt -= 0.025; }
                } else { tilt *= 0.82; }
                
                bmwM3.rotation.z = tilt;
                bmwM3.rotation.y = tilt * 0.35;

                // Sinematik Hız Titremesi (Motion Shake Algorithm)
                let shakeFactor = (score * 0.0015) + 0.005;
                camera.position.y = 4.0 + (Math.random() - 0.5) * shakeFactor;
                camera.position.x = (Math.random() - 0.5) * shakeFactor;

                // Egzoz Kıvılcım Animasyonu
                const sArray = sparks.geometry.attributes.position.array;
                for(let i=2; i<sArray.length; i+=3) { sArray[i] += 0.15; if(sArray[i] > 4) sArray[i] = 1.7; }
                sparks.geometry.attributes.position.needsUpdate = true;

                lines.forEach(l => { l.position.z += currentSpeed; if(l.position.z > 15) l.position.z = -250; });
                
                traffic.forEach(t => {
                    t.position.z += currentSpeed * 0.52;
                    if(t.position.z > 4) { 
                        t.position.z = -160 - Math.random()*50; 
                        t.position.x = (Math.random() - 0.5) * 12; 
                        score++; 
                        document.getElementById("scoreDisplay4D").innerText = "4D Makas Skoru: " + score + " 🌀"; 
                    }
                    if(Math.abs(bmwM3.position.x - t.position.x) < 1.5 && Math.abs(bmwM3.position.z - t.position.z) < 3.3) { 
                        gameOver = true; 
                        document.getElementById("scoreDisplay4D").innerHTML = "<span style='color:#ff0000; font-size:32px; font-weight:900; text-shadow:0 0 20px #ff0000;'>💥 AMBANS FIRLADI M3 PERT! 💥</span>";
                        document.getElementById("restartButtonContainer").innerHTML = '<button onclick="location.reload()" style="margin-top:15px; padding:18px 50px; font-size:22px; font-weight:bold; background:linear-gradient(90deg, #ff0000, #220000); color:#fff; border:none; border-radius:12px; cursor:pointer; box-shadow: 0 0 30px #ff0000;">SANAYİYE GİT (YENİDEN BAŞLA) 🔄</button>';
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
# ASTRO-AURA SPACE ESCAPE: ULTRA FENASAL NEBULA & FRAKTAL METEOR GÜNCELLEMESİ
# ==========================================================================================
elif st.session_state.aktif_mod == "KizOyunu":
    st.markdown("### 🌌 Kızlar İçin Özel: 4D Astro-Aura Kozmik Kuantum Simülatörü")
    st.caption("Sol üstteki parıldayan Üç Çizgiye basarak istediğin an ana panele dönebilirsin gardaşşş!")

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
        scene.fog = new THREE.FogExp2(0x010003, 0.009);

        const camera = new THREE.PerspectiveCamera(55, container.clientWidth / 570, 0.1, 1000);
        const renderer = new THREE.WebGLRenderer({ antialias: true });
        renderer.setSize(container.clientWidth, 570);
        renderer.toneMapping = THREE.ACESFilmicToneMapping;
        container.appendChild(renderer.domElement);

        // Kuantum Işıkları
        const neonLight = new THREE.PointLight(0xff00bb, 6, 200); neonLight.position.set(0, 15, -20); scene.add(neonLight);
        const blueLight = new THREE.PointLight(0x00f0ff, 4, 150); blueLight.position.set(0, -10, -10); scene.add(blueLight);
        scene.add(new THREE.AmbientLight(0x0d0314, 1.2));

        // 3D Dönen Dev Kuantum Nebula/Gaz Bulutu Fonu
        const nebulaGeo = new THREE.SphereGeometry(90, 32, 32);
        const nebulaMat = new THREE.MeshBasicMaterial({ color: 0x220033, wireframe: true, transparent: true, opacity: 0.15 });
        const nebula = new THREE.Mesh(nebulaGeo, nebulaMat); scene.add(nebula);

        // Sinematik Warp Yıldız Parçacıkları (Akışkan Hız Efektli)
        function createStars(count, color, size) {
            const geo = new THREE.BufferGeometry();
            const pos = new Float32Array(count * 3);
            for(let i=0; i<count*3; i+=3) { pos[i]=(Math.random()-0.5)*90; pos[i+1]=(Math.random()-0.5)*60; pos[i+2]=-Math.random()*250; }
            geo.setAttribute('position', new THREE.BufferAttribute(pos, 3));
            return new THREE.Points(geo, new THREE.PointsMaterial({ color: color, size: size, transparent: true, opacity: 0.9 }));
        }
        const layer1 = createStars(600, 0xffffff, 0.15);
        const layer2 = createStars(400, 0xff00bb, 0.28);
        scene.add(layer1, layer2);

        // Ultra Fırlama Kuantum Jeti Model Anatomisi
        const playerJet = new THREE.Group();
        const chromePink = new THREE.MeshStandardMaterial({ color: 0xff0077, metalness: 0.95, roughness: 0.01, emissive: 0x330011 });
        
        const core = new THREE.Mesh(new THREE.CylinderGeometry(0.1, 0.45, 2.6, 8), chromePink); core.rotation.x = Math.PI / 2;
        const cockpit = new THREE.Mesh(new THREE.SphereGeometry(0.28, 16, 16), new THREE.MeshStandardMaterial({ color: 0x00f5ff, roughness: 0, metalness: 1 }));
        cockpit.position.set(0, 0.2, -0.4); cockpit.scale.set(1, 1, 1.8);
        
        const leftWing = new THREE.Mesh(new THREE.BoxGeometry(1.8, 0.04, 0.8), chromePink); leftWing.position.set(-1.0, -0.05, 0.3); leftWing.rotation.y = 0.3;
        const rightWing = leftWing.clone(); rightWing.position.x = 1.0; rightWing.rotation.y = -0.3;
        playerJet.add(core, cockpit, leftWing, rightWing);

        // Plazma Egzoz İzi Parçacık Motoru
        const trailCount = 30;
        const trailGeo = new THREE.BufferGeometry();
        const trailPos = new Float32Array(trailCount * 3);
        for(let i=0; i<trailCount*3; i+=3) { trailPos[i]=0; trailPos[i+1]=-0.1; trailPos[i+2]=1.3+Math.random(); }
        trailGeo.setAttribute('position', new THREE.BufferAttribute(trailPos, 3));
        const trailSparks = new THREE.Points(trailGeo, new THREE.PointsMaterial({ color: 0x00f5ff, size: 0.25, transparent: true, opacity: 0.8 }));
        playerJet.add(trailSparks);

        playerJet.position.set(0, 0, -6); scene.add(playerJet);

        // Fraktal Yapıda Meteor Engelleri (Kendi ekseninde dönen parıltılı lav asteroitleri)
        let obstacles = []; const colors = [0xff0055, 0x9900ff, 0xff3300];
        for(let i=0; i<5; i++){
            let oMesh = new THREE.Mesh(
                new THREE.DodecahedronGeometry(1.3, 1), 
                new THREE.MeshStandardMaterial({ color: colors[i % 3], roughness: 0.4, metalness: 0.8, flatShading: true, emissive: 0x220011 })
            );
            oMesh.position.set((Math.random() - 0.5) * 14, (Math.random() - 0.5) * 4, -50 - (i * 32)); 
            scene.add(oMesh); obstacles.push(oMesh);
        }

        camera.position.set(0, 4.0, 4.0); camera.lookAt(new THREE.Vector3(0, -0.2, -22));
        
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
                let speed = 1.0 + (score * 0.035);

                if(keys["ArrowLeft"] || keys["a"] || keys["A"] || touchLeft) { 
                    if(playerJet.position.x > -7.5) playerJet.position.x -= 0.22; jetRot = 0.4; 
                } else if(keys["ArrowRight"] || keys["d"] || keys["D"] || touchRight) { 
                    if(playerJet.position.x < 7.5) playerJet.position.x += 0.22; jetRot = -0.4; 
                } else { jetRot *= 0.82; }
                
                playerJet.rotation.z = jetRot;
                nebula.rotation.y += 0.001; // Nebula yavaşça döner

                // Plazma Egzoz İzi Animasyonu
                const tArr = trailSparks.geometry.attributes.position.array;
                for(let i=2; i<tArr.length; i+=3) { tArr[i] += 0.12; if(tArr[i] > 2.5) tArr[i] = 1.3; }
                trailSparks.geometry.attributes.position.needsUpdate = true;

                // Yıldızların İleri Akış Hareketi
                [layer1, layer2].forEach((layer, idx) => {
                    const pos = layer.geometry.attributes.position.array;
                    let mult = (idx + 1) * 0.7;
                    for(let i=2; i<pos.length; i+=3) { pos[i] += speed * mult; if(pos[i] > 15) pos[i] = -230; }
                    layer.geometry.attributes.position.needsUpdate = true;
                });

                obstacles.forEach(o => {
                    o.position.z += speed * 0.85; 
                    o.rotation.x += 0.02; o.rotation.y += 0.03;
                    
                    if(o.position.z > 6) { 
                        o.position.z = -140 - Math.random()*40; 
                        o.position.x = (Math.random() - 0.5) * 14; 
                        score++; 
                        document.getElementById("kizScoreDisplay").innerText = "Aura Enerjisi: " + score + " ⭐ ✨"; 
                    }
                    if(Math.abs(playerJet.position.x - o.position.x) < 1.55 && Math.abs(playerJet.position.z - o.position.z) < 2.4) { 
                        gameOver = true; 
                        document.getElementById("kizScoreDisplay").innerHTML = "<span style='color:#ff0055; font-size:30px; font-weight:900; text-shadow:0 0 20px #ff0055;'>🔮 KARADELİK YUTTU! (AURA SIFIRLANDI) 🔮</span>";
                        document.getElementById("restartButtonContainerKiz").innerHTML = '<button onclick="location.reload()" style="margin-top:15px; padding:18px 50px; font-size:22px; font-weight:bold; background:linear-gradient(90deg, #ff0055, #15000a); color:#fff; border:none; border-radius:12px; cursor:pointer; box-shadow: 0 0 30px #ff0055;">BOYUT DEĞİŞTİR (YENİDEN BAŞLA) 🔄</button>';
                    }
                });
            }
            renderer.render(scene, camera); requestAnimationFrame(animate);
        }
        animate();
    </script>
    """
    components.html(kiz_ultra_real_html, height=800)
