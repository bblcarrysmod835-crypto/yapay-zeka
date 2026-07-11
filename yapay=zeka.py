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
# SİSTEM TALİMATI (EKSİKSİZ KORUNDU & YENİ ALANLAR EKLENDİ)
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
    "malzemelerini, marine aşamalarını ve şef sırlarını upuzun listeleyeceksiniz. "
    "\n"
    "10) AKILLI MATEMATİK VE OYUN ARŞİVİ: Çarpma, bölme, toplama, çıkarma içeren her şeyi (Örn: 2+2=4 doğru mu, 95*5) hatasız çözeceksin. "
    "'Doğru mu' sorularında 'Son kararınız mı?' diyeceksin. Minecraft korku modlarını (Herobrine, From the Fog), Valorant ranklarını (Plat elo cehennemi), "
    "PUBG and Brawl Stars taktiklerini, 7. sınıf ders notlarını çok detaylı açıklayacaksın. "
    "\n"
    "11) AKADEMİK YOĞUNLUK VE DERS KANUNU (ÖZEL ODAK): Ders çalışmak, sınavlar, ödevler, okul başarıları ve tüm akademik konular senin "
    "en yoğunlaştığın alan olacak be gardaşşş! Kullanıcıya ders konularını, formülleri, en zorlu ders içeriklerini sayfalarca, en anlaşılır "
    "şekilde özetleyeceksin. Sınav taktikleri, hafıza teknikleri ve ders çalışma programlarını aşırı detaylı vereceksin, derslere yoğunlaşacaksın. "
    "\n"
    "12) TIP, DOKTOR VE HASTANE DÜNYASI: Bir doktor edasıyla hastanelerin işleyişi, acil servis ve poliklinik süreçleri, doktorların "
    "nöbet rutinleri, randevu sistemleri ve tıp dünyasındaki tüm profesyonel detayları derinlemesine, upuzun açıklayacaksın be gardaşşş. "
    "\n"
    "13) HASTALIKLAR VE SAĞLIK BİLGİSİ: Hastalıkların nedenleri, biyolojik ve klinik semptomları, teşhis yöntemleri ve tıbbi tedavi "
    "protokolleri hakkında evrendeki en detaylı sağlık bilgilerini vereceksin. (Her zaman bilgilendirici ol ama resmi teşhis için "
    "gerçek bir uzmana gitmesi gerektiğini de eklemeyi unutma gardaşşş)."
)

if "sohbet_hafizasi" not in st.session_state:
    st.session_state.sohbet_hafizasi = [{"role": "system", "content": sistem_talimati}]

# ==========================================================================================
# CSS DÜZENLEMELERİ
# ==========================================================================================
st.markdown("""
    <style>
    /* 1. Genel Arka Plan */
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

    /* Genel Metin Elemanları */
    p, span, label, div {
        color: #ffffff !important;
    }
    
    /* 2. ANA BAŞLIK */
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
    
    /* 3. SOL ÜÇ ÇİZGİ BUTONU */
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
    
    /* 4. SIDEBAR OYUN PANELİ: TONLAMALI PREMİUM KIRMIZI */
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
    
    /* 5. SOHBET BALONLARI */
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
    
    /* 6. MESAJ GİRİŞ KUTUSU */
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
# FULL KADRAJ ERKEK OYUNU: BMW M3 ARCADE (ULTRA GRAFİK GÜNCELLEMESİ)
# ==========================================================================================
elif st.session_state.aktif_mod == "ErkekOyunu":
    st.markdown("### 🏎️ Apolingo Tam Gövde BMW M3 Makas Simülatörü")
    st.caption("Sol üstteki parıldayan Üç Çizgiye basarak istediğin an ana panele dönebilirsin gardaşşş!")

    bmw_full_screen_html = """
    <div style="text-align:center; background:#040201; padding:15px; border-radius:16px; border:3px solid #ff0000; box-shadow: 0 0 35px rgba(255,0,0,0.7); user-select:none; position:relative;">
        <button id="btnLeft" style="position:absolute; left:20px; top:45%; transform:translateY(-50%); padding: 25px 20px; font-size: 30px; font-weight:bold; background:rgba(0,0,0,0.95); color:#ffffff; border:2px solid #ff0000; border-radius:15px; cursor:pointer; z-index:100; box-shadow:0 0 15px #ff0000;">◀</button>
        <button id="btnRight" style="position:absolute; right:20px; top:45%; transform:translateY(-50%); padding: 25px 20px; font-size: 30px; font-weight:bold; background:rgba(0,0,0,0.95); color:#ffffff; border:2px solid #ff0000; border-radius:15px; cursor:pointer; z-index:100; box-shadow:0 0 15px #ff0000;">▶</button>
        <div id="bmwFullCanvasContainer" style="width:100%; height:550px; border-radius:10px; overflow:hidden;"></div>
        <div id="uiPanel" style="margin-top:15px;">
            <h2 id="scoreDisplay4D" style="color:#ffffff; font-family:'Segoe UI',sans-serif; margin:10px 0; font-weight:900; font-size:32px; letter-spacing:1px; text-shadow:0 0 10px #ff0000;">4D Makas Skoru: 0 🌀</h2>
            <div id="restartButtonContainer"></div>
        </div>
    </div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script>
        const container = document.getElementById("bmwFullCanvasContainer");
        const scene = new THREE.Scene(); 
        scene.background = new THREE.Color(0x020101);
        scene.fog = new THREE.FogExp2(0x020101, 0.015);

        const camera = new THREE.PerspectiveCamera(55, container.clientWidth / 550, 0.1, 1000);
        const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: false });
        renderer.setSize(container.clientWidth, 550); 
        renderer.toneMapping = THREE.ACESFilmicToneMapping;
        renderer.toneMappingExposure = 1.2;
        container.appendChild(renderer.domElement);

        // Ultra Işıklar
        const dirLight = new THREE.DirectionalLight(0xffffff, 2.5); dirLight.position.set(5, 40, 10); scene.add(dirLight);
        const ambient = new THREE.AmbientLight(0x1a0d0d, 1.2); scene.add(ambient);

        // Yol ve Detaylı Materyal
        const roadGeo = new THREE.BoxGeometry(16, 0.1, 1000);
        const roadMat = new THREE.MeshStandardMaterial({ color: 0x0f0c0c, roughness: 0.6, metalness: 0.2 });
        const road = new THREE.Mesh(roadGeo, roadMat); scene.add(road);

        // Neon Yan Bariyer Şeritleri
        const leftB = new THREE.Mesh(new THREE.BoxGeometry(0.3, 0.6, 1000), new THREE.MeshStandardMaterial({ color: 0x221111 }));
        leftB.position.set(-8.1, 0.3, 0);
        const rightB = leftB.clone(); rightB.position.x = 8.1;
        scene.add(leftB, rightB);

        let lines = [];
        for(let i=0; i<30; i++){
            let lMesh = new THREE.Mesh(new THREE.BoxGeometry(0.25, 0.12, 12), new THREE.MeshBasicMaterial({ color: 0xff0000 }));
            lMesh.position.set(0, 0.07, -i * 25); scene.add(lMesh); lines.push(lMesh);
        }

        // BMW M3 Ultra Model Yapısı
        const bmwM3 = new THREE.Group();
        const m3BodyMat = new THREE.MeshStandardMaterial({ color: 0xeeeeee, metalness: 0.95, roughness: 0.05 });
        const baseMesh = new THREE.Mesh(new THREE.BoxGeometry(1.45, 0.4, 3.1), m3BodyMat);
        baseMesh.position.y = 0.28; bmwM3.add(baseMesh);

        const glassMat = new THREE.MeshStandardMaterial({ color: 0x020202, roughness: 0.0, metalness: 1.0 });
        const cabinMesh = new THREE.Mesh(new THREE.BoxGeometry(1.2, 0.45, 1.5), glassMat);
        cabinMesh.position.set(0, 0.65, -0.1); bmwM3.add(cabinMesh);

        // Farlar ve Işık Hüzmeleri
        const xenonL = new THREE.SpotLight(0xffffff, 5, 40, Math.PI/6, 0.5, 1); xenonL.position.set(-0.6, 0.3, -1.6); xenonL.target.position.set(-0.6, 0.3, -30);
        const xenonR = new THREE.SpotLight(0xffffff, 5, 40, Math.PI/6, 0.5, 1); xenonR.position.set(0.6, 0.3, -1.6); xenonR.target.position.set(0.6, 0.3, -30);
        bmwM3.add(xenonL, xenonR, xenonL.target, xenonR.target);

        // Kıvılcım Parçacık Efekti (Egzoz/Hız için)
        const pCount = 30;
        const pGeo = new THREE.BufferGeometry();
        const pPos = new Float32Array(pCount * 3);
        for(let i=0; i<pCount*3; i+=3) { pPos[i]=(Math.random()-0.5)*0.5; pPos[i+1]=0.1; pPos[i+2]=1.5+Math.random()*2; }
        pGeo.setAttribute('position', new THREE.BufferAttribute(pPos, 3));
        const pMat = new THREE.PointsMaterial({ color: 0xff3300, size: 0.15, transparent: true, opacity: 0.8 });
        const sparks = new THREE.Points(pGeo, pMat); bmwM3.add(sparks);

        bmwM3.position.set(0, 0, -8); scene.add(bmwM3);

        // Ultra Trafik Araçları
        let traffic = []; const colors = [0xff6600, 0xff0055, 0x00f0ff, 0x7700ff];
        for(let i=0; i<5; i++){
            let tGroup = new THREE.Group();
            let tBody = new THREE.Mesh(new THREE.BoxGeometry(1.45, 0.5, 2.9), new THREE.MeshStandardMaterial({ color: colors[i % colors.length], metalness: 0.7, roughness: 0.15 }));
            tBody.position.y = 0.3;
            let tGlass = new THREE.Mesh(new THREE.BoxGeometry(1.2, 0.4, 1.4), glassMat); tGlass.position.set(0, 0.65, -0.1);
            tGroup.add(tBody, tGlass);
            tGroup.position.set((Math.random() - 0.5) * 11, 0, -50 - (i * 35)); scene.add(tGroup); traffic.push(tGroup);
        }

        camera.position.set(0, 4.3, -1.2); camera.lookAt(new THREE.Vector3(0, 0.4, -25));
        
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
                let currentSpeed = 0.8 + (score * 0.025);
                
                if(keys["ArrowLeft"] || keys["a"] || keys["A"] || touchLeft) { 
                    if(bmwM3.position.x > -6.6) { bmwM3.position.x -= 0.22; if(tilt < 0.12) tilt += 0.02; }
                } else if(keys["ArrowRight"] || keys["d"] || keys["D"] || touchRight) { 
                    if(bmwM3.position.x < 6.6) { bmwM3.position.x += 0.22; if(tilt > -0.12) tilt -= 0.02; }
                } else { tilt *= 0.85; }
                
                bmwM3.rotation.z = tilt;
                bmwM3.rotation.y = tilt * 0.4;

                // Dinamik Kamera Titremesi ve Hız Efekti
                camera.position.y = 4.3 + Math.sin(Date.now() * 0.05) * (score * 0.002);

                // Kıvılcımları canlandır
                const sArray = sparks.geometry.attributes.position.array;
                for(let i=1; i<sArray.length; i+=3) { sArray[i+1] = 0.1 + Math.random()*0.1; sArray[i+1] -= 0.02; }
                sparks.geometry.attributes.position.needsUpdate = true;

                lines.forEach(l => { l.position.z += currentSpeed; if(l.position.z > 12) l.position.z = -250; });
                
                traffic.forEach(t => {
                    t.position.z += currentSpeed * 0.55;
                    if(t.position.z > 3) { 
                        t.position.z = -150 - Math.random()*40; 
                        t.position.x = (Math.random() - 0.5) * 11; 
                        score++; 
                        document.getElementById("scoreDisplay4D").innerText = "4D Makas Skoru: " + score + " 🌀"; 
                    }
                    if(Math.abs(bmwM3.position.x - t.position.x) < 1.4 && Math.abs(bmwM3.position.z - t.position.z) < 3.0) { 
                        gameOver = true; 
                        document.getElementById("scoreDisplay4D").innerHTML = "<span style='color:#ff0000; font-size:30px; font-weight:900; text-shadow:0 0 15px #ff0000;'>💥 M3 PERT OLDU! 💥</span>";
                        document.getElementById("restartButtonContainer").innerHTML = '<button onclick="location.reload()" style="margin-top:15px; padding:18px 50px; font-size:22px; font-weight:bold; background:linear-gradient(90deg, #ff0000, #330000); color:#fff; border:none; border-radius:12px; cursor:pointer; box-shadow: 0 0 25px #ff0000;">TEKRAR BAŞLA BE GARDAŞŞŞ! 🔄</button>';
                    }
                });
            }
            renderer.render(scene, camera); requestAnimationFrame(animate);
        }
        animate();
    </script>
    """
    components.html(bmw_full_screen_html, height=780)

# ==========================================================================================
# FULL KADRAJ KIZ OYUNU: 4D ASTRO-AURA SPACE ESCAPE (ULTRA GRAFİK GÜNCELLEMESİ)
# ==========================================================================================
elif st.session_state.aktif_mod == "KizOyunu":
    st.markdown("### 🌌 Kızlar İçin Özel: 4D Astro-Aura Kuantum Kaçış Oyunu")
    st.caption("Sol üstteki parıldayan Üç Çizgiye basarak istediğin an ana panele dönebilirsin gardaşşş!")

    kiz_full_screen_html = """
    <div style="text-align:center; background:#020103; padding:15px; border-radius:16px; border:3px solid #ff0000; box-shadow: 0 0 35px rgba(255,0,0,0.7); user-select:none; position:relative;">
        <button id="btnLeftKiz" style="position:absolute; left:20px; top:45%; transform:translateY(-50%); padding: 25px 20px; font-size: 30px; font-weight:bold; background:rgba(0,0,0,0.95); color:#ffffff; border:2px solid #ff0000; border-radius:15px; cursor:pointer; z-index:100; box-shadow:0 0 15px #ff0000;">◀</button>
        <button id="btnRightKiz" style="position:absolute; right:20px; top:45%; transform:translateY(-50%); padding: 25px 20px; font-size: 30px; font-weight:bold; background:rgba(0,0,0,0.95); color:#ffffff; border:2px solid #ff0000; border-radius:15px; cursor:pointer; z-index:100; box-shadow:0 0 15px #ff0000;">▶</button>
        <div id="kizFullCanvasContainer" style="width:100%; height:550px; border-radius:10px; overflow:hidden;"></div>
        <div id="uiPanelKiz" style="margin-top:15px;">
            <h2 id="kizScoreDisplay" style="color:#ffffff; font-family:'Segoe UI',sans-serif; margin:10px 0; font-weight:900; font-size:32px; letter-spacing:1px; text-shadow:0 0 10px #ff0000;">Aura Enerjisi: 0 ⭐</h2>
            <div id="restartButtonContainerKiz"></div>
        </div>
    </div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script>
        const container = document.getElementById("kizFullCanvasContainer");
        const scene = new THREE.Scene(); 
        scene.fog = new THREE.FogExp2(0x020103, 0.012);

        const camera = new THREE.PerspectiveCamera(60, container.clientWidth / 550, 0.1, 1000);
        const renderer = new THREE.WebGLRenderer({ antialias: true });
        renderer.setSize(container.clientWidth, 550);
        renderer.toneMapping = THREE.ACESFilmicToneMapping;
        container.appendChild(renderer.domElement);

        // Kozmik Aydınlatma
        const pLight = new THREE.PointLight(0xff0055, 5, 150); pLight.position.set(0, 10, -10); scene.add(pLight);
        const ambient = new THREE.AmbientLight(0x1a0510, 1.5); scene.add(ambient);

        // Sinematik Warp Yıldız Alanı (İki katmanlı parçacık motoru)
        function createStarField(count, color, size) {
            const geo = new THREE.BufferGeometry();
            const pos = new Float32Array(count * 3);
            for(let i=0; i<count*3; i+=3) { pos[i]=(Math.random()-0.5)*70; pos[i+1]=(Math.random()-0.5)*50; pos[i+2]=-Math.random()*200; }
            geo.setAttribute('position', new THREE.BufferAttribute(pos, 3));
            return new THREE.Points(geo, new THREE.PointsMaterial({ color: color, size: size, transparent: true, opacity: 0.85 }));
        }
        const stars1 = createStarField(500, 0xffffff, 0.18);
        const stars2 = createStarField(300, 0xff0055, 0.3);
        scene.add(stars1, stars2);

        // Gelişmiş Jet Tasarımı
        const playerJet = new THREE.Group();
        const jetMat = new THREE.MeshStandardMaterial({ color: 0xff0055, emissive: 0x440011, metalness: 0.9, roughness: 0.1 });
        const core = new THREE.Mesh(new THREE.ConeGeometry(0.5, 2.3, 5), jetMat);
        core.rotation.x = Math.PI / 2;
        const wingL = new THREE.Mesh(new THREE.BoxGeometry(1.6, 0.05, 0.9), jetMat); wingL.position.set(-0.85, -0.1, 0.2); wingL.rotation.y = 0.25;
        const wingR = wingL.clone(); wingR.position.x = 0.85; wingR.rotation.y = -0.25;
        playerJet.add(core, wingL, wingR);

        // Plazma İtici Efekti
        const plasmaMat = new THREE.MeshBasicMaterial({ color: 0xffffff });
        const plasma = new THREE.Mesh(new THREE.ConeGeometry(0.2, 0.9, 8), plasmaMat);
        plasma.position.set(0, -0.1, 1.3); plasma.rotation.x = -Math.PI / 2;
        playerJet.add(plasma);

        playerJet.position.set(0, 0, -6); scene.add(playerJet);

        // Kristalize Meteor Engelleri
        let obstacles = []; const obsColors = [0xff1144, 0x8b0022, 0xff3300];
        for(let i=0; i<5; i++){
            let oMesh = new THREE.Mesh(
                new THREE.IcosahedronGeometry(1.2, 1), 
                new THREE.MeshStandardMaterial({ color: obsColors[i % 3], roughness: 0.3, metalness: 0.7, flatShading: true, emissive: 0x220005 })
            );
            oMesh.position.set((Math.random() - 0.5) * 13, (Math.random() - 0.5) * 3, -40 - (i * 30)); 
            scene.add(oMesh); obstacles.push(oMesh);
        }

        camera.position.set(0, 4.5, 3.5); camera.lookAt(new THREE.Vector3(0, -0.3, -20));
        
        let score = 0; let gameOver = false; let keys = {}; let jetRotation = 0;
        window.addEventListener("keydown", e => keys[e.key] = true); window.addEventListener("keyup", e => keys[e.key] = false);
        
        let touchLeft = false, touchRight = false;
        const bLeft = document.getElementById("btnLeftKiz"); const bRight = document.getElementById("btnRightKiz");
        bLeft.addEventListener("mousedown", () => touchLeft = true); bLeft.addEventListener("mouseup", () => touchLeft = false);
        bLeft.addEventListener("touchstart", (e) => { e.preventDefault(); touchLeft = true; }); bLeft.addEventListener("touchend", () => touchLeft = false);
        bRight.addEventListener("mousedown", () => touchRight = true); bRight.addEventListener("mouseup", () => touchRight = false);
        bRight.addEventListener("touchstart", (e) => { e.preventDefault(); touchRight = true; }); bRight.addEventListener("touchend", () => touchRight = false);

        function animate() {
            if(!gameOver) {
                let speed = 0.9 + (score * 0.03);

                if(keys["ArrowLeft"] || keys["a"] || keys["A"] || touchLeft) { 
                    if(playerJet.position.x > -6.8) playerJet.position.x -= 0.20; jetRotation = 0.35; 
                } else if(keys["ArrowRight"] || keys["d"] || keys["D"] || touchRight) { 
                    if(playerJet.position.x < 6.8) playerJet.position.x += 0.20; jetRotation = -0.35; 
                } else { jetRotation *= 0.85; }
                
                playerJet.rotation.z = jetRotation;
                plasma.scale.set(1 + Math.sin(Date.now()*0.08)*0.2, 1 + Math.cos(Date.now()*0.08)*0.2, 1);

                // Yıldızların Warp Hareketi
                [stars1, stars2].forEach((stContainer, idx) => {
                    const pos = stContainer.geometry.attributes.position.array;
                    let factor = (idx + 1) * 0.6;
                    for(let i=2; i<pos.length; i+=3) { pos[i] += speed * factor; if(pos[i] > 10) pos[i] = -180; }
                    stContainer.geometry.attributes.position.needsUpdate = true;
                });

                obstacles.forEach(o => {
                    o.position.z += speed * 0.8; 
                    o.rotation.x += 0.015; o.rotation.y += 0.025;
                    
                    if(o.position.z > 6) { 
                        o.position.z = -130 - Math.random()*30; 
                        o.position.x = (Math.random() - 0.5) * 13; 
                        score++; 
                        document.getElementById("kizScoreDisplay").innerText = "Aura Enerjisi: " + score + " ⭐ ✨"; 
                    }
                    if(Math.abs(playerJet.position.x - o.position.x) < 1.45 && Math.abs(playerJet.position.z - o.position.z) < 2.2) { 
                        gameOver = true; 
                        document.getElementById("kizScoreDisplay").innerHTML = "<span style='color:#ff0055; font-size:28px; font-weight:900; text-shadow:0 0 15px #ff0055;'>🔮 AURA DAĞILDI! 🔮</span>";
                        document.getElementById("restartButtonContainerKiz").innerHTML = '<button onclick="location.reload()" style="margin-top:15px; padding:18px 50px; font-size:22px; font-weight:bold; background:linear-gradient(90deg, #ff0055, #110005); color:#fff; border:none; border-radius:12px; cursor:pointer; box-shadow: 0 0 25px #ff0055;">TEKRAR BAŞLA BE GARDAŞŞŞ! 🔄</button>';
                    }
                });
            }
            renderer.render(scene, camera); requestAnimationFrame(animate);
        }
        animate();
    </script>
    """
    components.html(kiz_full_screen_html, height=780)
