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
# BMW M3 ARCADE: TAVANI DÜMDÜZ JİLET GİBİ VE FULL SEVİYE GÖVDE TASARIMI
# ==========================================================================================
elif st.session_state.aktif_mod == "ErkekOyunu":
    st.markdown("### 🏎️ Apolingo Next-Gen Assetto Sürüm: Full Donanım Pürüzsüz BMW M3")
    st.caption("Arabanın üzerindeki tüm spoyler ve çıkıntılar sıfırlandı, tavan jilet gibi pürüzsüz yapıldı ve araba fulllendi be gardaşş!")

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
        scene.background = new THREE.Color(0x010102);
        scene.fog = new THREE.FogExp2(0x010102, 0.001); 

        const camera = new THREE.PerspectiveCamera(46, container.clientWidth / 570, 0.1, 1000);
        const renderer = new THREE.WebGLRenderer({ antialias: true, powerPreference: "high-performance" });
        renderer.setSize(container.clientWidth, 570); 
        renderer.toneMapping = THREE.ACESFilmicToneMapping;
        renderer.toneMappingExposure = 1.9;
        container.appendChild(renderer.domElement);

        // Canlı Stüdyo Işıkları
        const sunLight = new THREE.DirectionalLight(0xffffff, 3.8); sunLight.position.set(10, 60, 15); scene.add(sunLight);
        const ambient = new THREE.AmbientLight(0x221c1c, 2.0); scene.add(ambient);

        // Parlak Islak Otoban
        const roadGeo = new THREE.BoxGeometry(18, 0.1, 1000);
        const roadMat = new THREE.MeshStandardMaterial({ color: 0x070707, roughness: 0.02, metalness: 0.99 });
        const road = new THREE.Mesh(roadGeo, roadMat); scene.add(road);

        const leftNeon = new THREE.Mesh(new THREE.BoxGeometry(0.15, 0.3, 1000), new THREE.MeshBasicMaterial({ color: 0xff0033 }));
        leftNeon.position.set(-9, 0.15, 0);
        const rightNeon = leftNeon.clone(); rightNeon.position.x = 9;
        scene.add(leftNeon, rightNeon);

        let lines = [];
        for(let i=0; i<35; i++){
            let lMesh = new THREE.Mesh(new THREE.BoxGeometry(0.25, 0.11, 16), new THREE.MeshBasicMaterial({ color: 0xffffff }));
            lMesh.position.set(0, 0.06, -i * 24); scene.add(lMesh); lines.push(lMesh);
        }

        // --- EN FULL VE ÜSTÜ %100 PÜRÜZSÜZ TAVANLI M3 YAPIM MOTORU ---
        function createFullyLoadedM3(bodyColor, isPlayer) {
            const m3Group = new THREE.Group();
            
            // Üst Düzey Kaplamalar
            const paintMat = new THREE.MeshStandardMaterial({ color: bodyColor, metalness: 0.99, roughness: 0.01 });
            const smoothRoofMat = new THREE.MeshStandardMaterial({ color: 0x111111, metalness: 0.95, roughness: 0.05 }); 
            const glassMat = new THREE.MeshStandardMaterial({ color: 0x05080c, roughness: 0, metalness: 1, transparent: true, opacity: 0.88 });
            const tyreMat = new THREE.MeshStandardMaterial({ color: 0x080808, roughness: 0.7 });
            const chromeMat = new THREE.MeshStandardMaterial({ color: 0xf5f5f5, metalness: 1.0, roughness: 0.01 });
            const brakeMat = new THREE.MeshStandardMaterial({ color: 0xdd0000, metalness: 0.9 }); 
            const diskMat = new THREE.MeshStandardMaterial({ color: 0x888888, metalness: 0.95, roughness: 0.15 }); 

            // 1. Ana Alt Alt Şasi (Dolu Duruş)
            const base = new THREE.Mesh(new THREE.BoxGeometry(1.74, 0.26, 3.75), paintMat);
            base.position.y = 0.28;
            m3Group.add(base);

            // 2. Ön Spor M Tampon Splitter
            const frontBumper = new THREE.Mesh(new THREE.BoxGeometry(1.72, 0.20, 0.12), new THREE.MeshStandardMaterial({ color: 0x020202, roughness: 0.5 }));
            frontBumper.position.set(0, 0.20, -1.9);
            m3Group.add(frontBumper);

            // 3. Ön Kaput ve Aerodinamik Çizgiler
            const hood = new THREE.Mesh(new THREE.BoxGeometry(1.70, 0.18, 1.30), paintMat);
            hood.position.set(0, 0.40, -1.18);
            m3Group.add(hood);

            // 4. Arka Düz Bagaj Kapağı (Tepesinde veya arkasında hiçbir ekstra çıkıntı/spoyler yok, JİLET gibi!)
            const trunk = new THREE.Mesh(new THREE.BoxGeometry(1.70, 0.24, 0.75), paintMat);
            trunk.position.set(0, 0.42, 1.38);
            m3Group.add(trunk);

            // 5. Tamamen Akıcı Coupe Kabin Tasarımı
            const cabin = new THREE.Mesh(new THREE.BoxGeometry(1.40, 0.42, 1.72), glassMat);
            cabin.position.set(0, 0.65, 0.05);
            m3Group.add(cabin);

            // Jilet gibi Dümdüz Karbon Pürüzsüz Tavan (Üstünde hiçbir anten, çıkıntı veya fazlalık asla yok!)
            const flatRoof = new THREE.Mesh(new THREE.BoxGeometry(1.36, 0.03, 1.48), smoothRoofMat);
            flatRoof.position.set(0, 0.86, 0.05);
            m3Group.add(flatRoof);

            // İç Dikiz Aynası
            const mirrorInside = new THREE.Mesh(new THREE.BoxGeometry(0.18, 0.04, 0.03), chromeMat);
            mirrorInside.position.set(0, 0.78, -0.65);
            m3Group.add(mirrorInside);

            // 6. Krom Böbrek Izgaraları ve Aynalar
            const kL = new THREE.Mesh(new THREE.BoxGeometry(0.20, 0.16, 0.03), chromeMat);
            kL.position.set(-0.14, 0.36, -1.91);
            const kR = kL.clone(); kR.position.x = 0.14;
            m3Group.add(kL, kR);

            const mirrorL = new THREE.Mesh(new THREE.BoxGeometry(0.16, 0.08, 0.10), paintMat);
            mirrorL.position.set(-0.96, 0.60, -0.30);
            const mirrorR = mirrorL.clone(); mirrorR.position.x = 0.96;
            m3Group.add(mirrorL, mirrorR);

            // 7. Full Performans Tekerlek Sistemi (Dönen Jantlar + Diskler + Kırmızı Brembolar)
            const tG = new THREE.CylinderGeometry(0.35, 0.35, 0.28, 36);
            const rG = new THREE.CylinderGeometry(0.26, 0.26, 0.29, 20);
            const dG = new THREE.CylinderGeometry(0.21, 0.21, 0.04, 16);
            const cG = new THREE.BoxGeometry(0.05, 0.14, 0.08);
            
            tG.rotateZ(Math.PI / 2); rG.rotateZ(Math.PI / 2); dG.rotateZ(Math.PI / 2);

            const wPositions = [
                [-0.92, 0.35, -1.15], [0.92, 0.35, -1.15],
                [-0.92, 0.35, 1.30],  [0.92, 0.35, 1.30]
            ];

            wPositions.forEach(pos => {
                const tire = new THREE.Mesh(tG, tyreMat);
                const rim = new THREE.Mesh(rG, chromeMat);
                const disk = new THREE.Mesh(dG, diskMat);
                const caliper = new THREE.Mesh(cG, brakeMat);
                
                tire.position.set(pos[0], pos[1], pos[2]);
                rim.position.set(pos[0], pos[1], pos[2]);
                disk.position.set(pos[0] + (pos[0] > 0 ? -0.03 : 0.03), pos[1], pos[2]);
                caliper.position.set(pos[0] + (pos[0] > 0 ? -0.05 : 0.05), pos[1] + 0.10, pos[2] - 0.04);
                
                m3Group.add(tire, rim, disk, caliper);
            });

            // 8. Lazer Xenon Farlar & Çift Yuvarlak Egzozlar
            const fGeo = new THREE.BoxGeometry(0.22, 0.06, 0.03);
            const fMat = new THREE.MeshBasicMaterial({ color: isPlayer ? 0xffffff : 0xffbb00 });
            const headL = new THREE.Mesh(fGeo, fMat); headL.position.set(-0.65, 0.40, -1.89);
            const headR = headL.clone(); headR.position.x = 0.65;
            m3Group.add(headL, headR);

            const sMat = new THREE.MeshBasicMaterial({ color: 0xff0011 });
            const stopL = new THREE.Mesh(fGeo, sMat); stopL.position.set(-0.65, 0.44, 1.76);
            const stopR = stopL.clone(); stopR.position.x = 0.65;
            m3Group.add(stopL, stopR);

            // Arka Çift Çıkış Krom Egzozlar
            const exGeo = new THREE.CylinderGeometry(0.05, 0.05, 0.2, 12); exGeo.rotateX(Math.PI/2);
            const exL = new THREE.Mesh(exGeo, chromeMat); exL.position.set(-0.4, 0.15, 1.76);
            const exR = exL.clone(); exR.position.x = 0.4;
            m3Group.add(exL, exR);

            return m3Group;
        }

        // Sürdüğün Oyuncu Arabası (Efsanevi Estoril Metalik M Mavi - Full Modifiyeli, Kusursuz Üst Yüzey)
        const bmwM3 = createFullyLoadedM3(0x0a2244, true);

        // Lazer Xenon Far Aydınlatması
        const beamCone = new THREE.CylinderGeometry(0.05, 3.8, 42, 16, 1, true);
        beamCone.translate(0, 21, 0);
        const beamMat = new THREE.MeshBasicMaterial({ color: 0x00faff, transparent: true, opacity: 0.15, side: THREE.DoubleSide });
        const leftBeam = new THREE.Mesh(beamCone, beamMat); leftBeam.position.set(-0.65, 0.40, -1.9); leftBeam.rotation.x = -Math.PI / 2;
        const rightBeam = leftBeam.clone(); rightBeam.position.x = 0.65;
        bmwM3.add(leftBeam, rightBeam);

        // Egzoz Patlama Kıvılcımları
        const sparkCount = 40;
        const sparkGeo = new THREE.BufferGeometry();
        const sparkPos = new Float32Array(sparkCount * 3);
        for(let i=0; i<sparkCount*3; i+=3) { sparkPos[i]=(Math.random()-0.5)*0.5; sparkPos[i+1]=0.15; sparkPos[i+2]=1.78+Math.random()*2; }
        sparkGeo.setAttribute('position', new THREE.BufferAttribute(sparkPos, 3));
        const sparks = new THREE.Points(sparkGeo, new THREE.PointsMaterial({ color: 0xff5500, size: 0.16, transparent: true, opacity: 0.85 }));
        bmwM3.add(sparks);

        bmwM3.position.set(0, 0, -8); scene.add(bmwM3);

        // Trafik Araçları Havuzu
        let traffic = []; const colors = [0xaa0011, 0x11aa22, 0x222222, 0xccaa00, 0x5511aa];
        for(let i=0; i<5; i++){
            let tCar = createFullyLoadedM3(colors[i % colors.length], false);
            tCar.position.set((Math.random() - 0.5) * 12, 0, -75 - (i * 45)); 
            scene.add(tCar); 
            traffic.push(tCar);
        }

        camera.position.set(0, 3.5, -0.2); camera.lookAt(new THREE.Vector3(0, 0.3, -35));
        
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
                let currentSpeed = 1.15 + (score * 0.045);
                
                if(keys["ArrowLeft"] || keys["a"] || keys["A"] || touchLeft) { 
                    if(bmwM3.position.x > -7.4) { bmwM3.position.x -= 0.28; if(tilt < 0.12) tilt += 0.022; }
                } else if(keys["ArrowRight"] || keys["d"] || keys["D"] || touchRight) { 
                    if(bmwM3.position.x < 7.4) { bmwM3.position.x += 0.28; if(tilt > -0.12) tilt -= 0.022; }
                } else { tilt *= 0.75; }
                
                bmwM3.rotation.z = tilt;
                bmwM3.rotation.y = tilt * 0.25;

                // Dinamik Hız Sarsıntısı
                let shakeFactor = (score * 0.001) + 0.002;
                camera.position.y = 3.5 + (Math.random() - 0.5) * shakeFactor;

                // Kıvılcım Devirdaimi
                const sArray = sparks.geometry.attributes.position.array;
                for(let i=2; i<sArray.length; i+=3) { sArray[i] += 0.22; if(sArray[i] > 4) sArray[i] = 1.78; }
                sparks.geometry.attributes.position.needsUpdate = true;

                lines.forEach(l => { l.position.z += currentSpeed; if(l.position.z > 15) l.position.z = -250; });
                
                traffic.forEach(t => {
                    t.position.z += currentSpeed * 0.50;
                    if(t.position.z > 4) { 
                        t.position.z = -180 - Math.random()*60; 
                        t.position.x = (Math.random() - 0.5) * 12; 
                        score++; 
                        document.getElementById("scoreDisplay4D").innerText = "Otoban Makas Skoru: " + score + " 🌀"; 
                    }
                    if(Math.abs(bmwM3.position.x - t.position.x) < 1.62 && Math.abs(bmwM3.position.z - t.position.z) < 3.6) { 
                        gameOver = true; 
                        document.getElementById("scoreDisplay4D").innerHTML = "<span style='color:#ff0000; font-size:32px; font-weight:900; text-shadow:0 0 20px #ff0000;'>💥 AMBANS FIRLADI! M3 PERT! 💥</span>";
                        document.getElementById("restartButtonContainer").innerHTML = '<button onclick="location.reload()" style="margin-top:15px; padding:18px 50px; font-size:22px; font-weight:bold; background:linear-gradient(90deg, #ff0000, #220000); color:#fff; border:none; border-radius:12px; cursor:pointer; box-shadow: 0 0 30px #ff0000;">SANAYİYE ÇEK (YENIDEN BAŞLA) 🔄</button>';
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
