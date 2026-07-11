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
# BMW M3 ARCADE: SİSSİZ, ULTRA NET RAY-TRACING & PRO DETAYLI 3D MODEL SÜRÜMÜ
# ==========================================================================================
elif st.session_state.aktif_mod == "ErkekOyunu":
    st.markdown("### 🏎️ Apolingo HD Kristal Netliğinde BMW M3 Gece Makas Simülatörü V2 Pro")
    st.caption("Sis kaldırıldı, görüş netleştirildi ve BMW M3 profesyonel detaylarla donatıldı be gardaşşş!")

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
        scene.background = new THREE.Color(0x020104);
        
        // SİS ETKİSİ TAMAMEN KALDIRILDI VEYA ULTRA ŞEFFAF YAPILDI (Görüş mesafesi artık sonsuz netlikte!)
        scene.fog = new THREE.FogExp2(0x020104, 0.002); 

        const camera = new THREE.PerspectiveCamera(50, container.clientWidth / 570, 0.1, 1000);
        const renderer = new THREE.WebGLRenderer({ antialias: true, powerPreference: "high-performance" });
        renderer.setSize(container.clientWidth, 570); 
        renderer.toneMapping = THREE.ACESFilmicToneMapping;
        renderer.toneMappingExposure = 1.7;
        container.appendChild(renderer.domElement);

        // Sinematik Işık Şeması - Arabanın parlaması için güçlendirildi
        const sunLight = new THREE.DirectionalLight(0xffffff, 2.8); sunLight.position.set(15, 60, 25); scene.add(sunLight);
        const ambient = new THREE.AmbientLight(0x1a1313, 1.5); scene.add(ambient);

        // Islak ve Kusursuz Yansımalı Asfalt
        const roadGeo = new THREE.BoxGeometry(18, 0.1, 1000);
        const roadMat = new THREE.MeshStandardMaterial({ color: 0x0a0a0a, roughness: 0.05, metalness: 0.95 });
        const road = new THREE.Mesh(roadGeo, roadMat); scene.add(road);

        // Neon Bariyer Işıkları (Yolu aydınlatıyor)
        const leftNeon = new THREE.Mesh(new THREE.BoxGeometry(0.2, 0.4, 1000), new THREE.MeshBasicMaterial({ color: 0xff0033 }));
        leftNeon.position.set(-9, 0.2, 0);
        const rightNeon = leftNeon.clone(); rightNeon.position.x = 9;
        scene.add(leftNeon, rightNeon);

        let lines = [];
        for(let i=0; i<35; i++){
            let lMesh = new THREE.Mesh(new THREE.BoxGeometry(0.3, 0.11, 14), new THREE.MeshBasicMaterial({ color: 0xffffff }));
            lMesh.position.set(0, 0.06, -i * 24); scene.add(lMesh); lines.push(lMesh);
        }

        // --- PROFESYONEL GEOMETRİK ARABA MODELLEME FONKSİYONU ---
        function createRealisticCar(bodyColor, isPlayer) {
            const carGroup = new THREE.Group();
            
            // Üst Düzey Malzeme Kaplamaları
            const metalMat = new THREE.MeshStandardMaterial({ color: bodyColor, metalness: 0.98, roughness: 0.02 });
            const glassMat = new THREE.MeshStandardMaterial({ color: 0x050505, roughness: 0.0, metalness: 1.0, transparent: true, opacity: 0.90 });
            const tyreMat = new THREE.MeshStandardMaterial({ color: 0x111111, roughness: 0.7 });
            const chromeMat = new THREE.MeshStandardMaterial({ color: 0xffffff, metalness: 1.0, roughness: 0.01 });
            const brakeMat = new THREE.MeshStandardMaterial({ color: 0xff0000, metalness: 0.8 }); // Kırmızı Kaliperler

            // 1. Ana Alt Şasi ve Tamponlar
            const base = new THREE.Mesh(new THREE.BoxGeometry(1.68, 0.32, 3.6), metalMat);
            base.position.y = 0.32;
            carGroup.add(base);

            // Agresif Ön Tampon Hava Girişleri (M Serisi Özel Tasarım)
            const bumper = new THREE.Mesh(new THREE.BoxGeometry(1.66, 0.2, 0.2), new THREE.MeshStandardMaterial({ color: 0x000000, roughness: 0.5 }));
            bumper.position.set(0, 0.22, -1.8);
            carGroup.add(bumper);

            // 2. Ön Motor Kaputu (Eğimli Kas Çizgileri Dahil)
            const hood = new THREE.Mesh(new THREE.BoxGeometry(1.64, 0.24, 1.2), metalMat);
            hood.position.set(0, 0.44, -1.1);
            carGroup.add(hood);

            // 3. Arka Bagaj Çıkıntısı ve M3 İnce Spoyler (Spoiler)
            const trunk = new THREE.Mesh(new THREE.BoxGeometry(1.64, 0.28, 0.8), metalMat);
            trunk.position.set(0, 0.46, 1.3);
            carGroup.add(trunk);
            
            const spoiler = new THREE.Mesh(new THREE.BoxGeometry(1.58, 0.04, 0.15), new THREE.MeshStandardMaterial({ color: 0x000000, metalness: 0.9 }));
            spoiler.position.set(0, 0.61, 1.6);
            carGroup.add(spoiler);

            // 4. Aerodinamik Kabin Gövdesi, Direkler ve Camlar
            const cabinMesh = new THREE.Mesh(new THREE.BoxGeometry(1.36, 0.46, 1.65), glassMat);
            cabinMesh.position.set(0, 0.70, 0.05);
            carGroup.add(cabinMesh);

            // Tavan Sacı
            const roof = new THREE.Mesh(new THREE.BoxGeometry(1.33, 0.04, 1.48), metalMat);
            roof.position.set(0, 0.93, 0.05);
            carGroup.add(roof);

            // 5. BMW Karakteristik Böbrek Izgaraları, Logosu ve Yan Aynalar
            const bobrekL = new THREE.Mesh(new THREE.BoxGeometry(0.24, 0.16, 0.06), chromeMat);
            bobrekL.position.set(-0.16, 0.42, -1.71);
            const bobrekR = bobrekL.clone(); bobrekR.position.x = 0.16;
            carGroup.add(bobrekL, bobrekR);

            const aynaL = new THREE.Mesh(new THREE.BoxGeometry(0.2, 0.07, 0.12), metalMat);
            aynaL.position.set(-0.94, 0.64, -0.35);
            const aynaR = aynaL.clone(); aynaR.position.x = 0.94;
            carGroup.add(aynaL, aynaR);

            // 6. Jantlı, Kaliperli ve Detaylı Tekerlek Setleri
            const tGeo = new THREE.CylinderGeometry(0.35, 0.35, 0.28, 32);
            const jGeo = new THREE.CylinderGeometry(0.24, 0.24, 0.29, 16);
            const calGeo = new THREE.BoxGeometry(0.08, 0.14, 0.08); // Spor Kaliper
            tGeo.rotateZ(Math.PI / 2); jGeo.rotateZ(Math.PI / 2);

            const wPositions = [
                [-0.89, 0.35, -1.05], [0.89, 0.35, -1.05],
                [-0.89, 0.35, 1.2],   [0.89, 0.35, 1.2]
            ];

            wPositions.forEach(pos => {
                const tire = new THREE.Mesh(tGeo, tyreMat);
                const rim = new THREE.Mesh(jGeo, chromeMat);
                const caliper = new THREE.Mesh(calGeo, brakeMat);
                
                tire.position.set(pos[0], pos[1], pos[2]);
                rim.position.set(pos[0], pos[1], pos[2]);
                caliper.position.set(pos[0] + (pos[0] > 0 ? -0.12 : 0.12), pos[1] + 0.1, pos[2]);
                
                carGroup.add(tire, rim, caliper);
            });

            // 7. Led Xenon Mercek Farlar
            const lightGeo = new THREE.BoxGeometry(0.26, 0.08, 0.05);
            const headlightMat = new THREE.MeshBasicMaterial({ color: isPlayer ? 0xffffff : 0xffaa00 });
            const fl = new THREE.Mesh(lightGeo, headlightMat); fl.position.set(-0.62, 0.44, -1.71);
            const fr = fl.clone(); fr.position.x = 0.62;
            carGroup.add(fl, fr);

            // Arka Stop Lambaları
            const stopMat = new THREE.MeshBasicMaterial({ color: 0xff0022 });
            const bl = new THREE.Mesh(lightGeo, stopMat); bl.position.set(-0.62, 0.48, 1.71);
            const br = bl.clone(); br.position.x = 0.62;
            carGroup.add(bl, br);

            return carGroup;
        }

        // Oyuncunun Canavar BMW M3'ü (Gece Siyahı / Derin Safir Saf Metalik Renk)
        const bmwM3 = createRealisticCar(0x0a101d, true);

        // Volumetrik Güçlü Xenon Hüzmeleri
        const lightConeGeo = new THREE.CylinderGeometry(0.1, 3.2, 35, 16, 1, true);
        lightConeGeo.translate(0, 17.5, 0);
        const lightConeMat = new THREE.MeshBasicMaterial({ color: 0x00d8ff, transparent: true, opacity: 0.18, side: THREE.DoubleSide });
        const leftHüzme = new THREE.Mesh(lightConeGeo, lightConeMat); leftHüzme.position.set(-0.62, 0.44, -1.75); leftHüzme.rotation.x = -Math.PI / 2;
        const rightHüzme = leftHüzme.clone(); rightHüzme.position.x = 0.62;
        bmwM3.add(leftHüzme, rightHüzme);

        // Egzoz Alev Patlama Efekti
        const sparkCount = 45;
        const sparkGeo = new THREE.BufferGeometry();
        const sparkPos = new Float32Array(sparkCount * 3);
        for(let i=0; i<sparkCount*3; i+=3) { sparkPos[i]=(Math.random()-0.5)*0.4; sparkPos[i+1]=0.15; sparkPos[i+2]=1.7+Math.random()*2.5; }
        sparkGeo.setAttribute('position', new THREE.BufferAttribute(sparkPos, 3));
        const sparks = new THREE.Points(sparkGeo, new THREE.PointsMaterial({ color: 0xff7700, size: 0.2, transparent: true, opacity: 0.95 }));
        bmwM3.add(sparks);

        bmwM3.position.set(0, 0, -8); scene.add(bmwM3);

        // Profesyonel Trafik Araç Havuzu
        let traffic = []; const colors = [0xd6001c, 0x0044cc, 0xe6b800, 0x262626, 0x5e35b1];
        for(let i=0; i<5; i++){
            let tCar = createRealisticCar(colors[i % colors.length], false);
            tCar.position.set((Math.random() - 0.5) * 12, 0, -70 - (i * 42)); 
            scene.add(tCar); 
            traffic.push(tCar);
        }

        camera.position.set(0, 3.8, -0.6); camera.lookAt(new THREE.Vector3(0, 0.3, -35));
        
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
                let currentSpeed = 1.05 + (score * 0.035);
                
                if(keys["ArrowLeft"] || keys["a"] || keys["A"] || touchLeft) { 
                    if(bmwM3.position.x > -7.4) { bmwM3.position.x -= 0.26; if(tilt < 0.15) tilt += 0.026; }
                } else if(keys["ArrowRight"] || keys["d"] || keys["D"] || touchRight) { 
                    if(bmwM3.position.x < 7.4) { bmwM3.position.x += 0.26; if(tilt > -0.15) tilt -= 0.026; }
                } else { tilt *= 0.80; }
                
                bmwM3.rotation.z = tilt;
                bmwM3.rotation.y = tilt * 0.35;

                // Dinamik Titreşim Kamerası
                let shakeFactor = (score * 0.0012) + 0.004;
                camera.position.y = 3.8 + (Math.random() - 0.5) * shakeFactor;

                // Egzoz Kıvılcımları
                const sArray = sparks.geometry.attributes.position.array;
                for(let i=2; i<sArray.length; i+=3) { sArray[i] += 0.18; if(sArray[i] > 4.5) sArray[i] = 1.7; }
                sparks.geometry.attributes.position.needsUpdate = true;

                lines.forEach(l => { l.position.z += currentSpeed; if(l.position.z > 15) l.position.z = -250; });
                
                traffic.forEach(t => {
                    t.position.z += currentSpeed * 0.55;
                    if(t.position.z > 4) { 
                        t.position.z = -180 - Math.random()*60; 
                        t.position.x = (Math.random() - 0.5) * 12; 
                        score++; 
                        document.getElementById("scoreDisplay4D").innerText = "4D Makas Skoru: " + score + " 🌀"; 
                    }
                    if(Math.abs(bmwM3.position.x - t.position.x) < 1.60 && Math.abs(bmwM3.position.z - t.position.z) < 3.5) { 
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
# ASTRO-AURA SPACE ESCAPE: ULTRA KALİTELİ VE AKICI HD SÜRÜMÜ
# ==========================================================================================
elif st.session_state.aktif_mod == "KizOyunu":
    st.markdown("### 🌌 Kızlar İçin Özel: 4D Astro-Aura Kozmik Kuantum Simülatörü HD Pro")
    st.caption("Uzay mekiği reaktör çekirdeği, hareketli meteorlar ve gökada partikülleri zenginleştirildi be gardaşşş!")

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

        // Kuantum Işıkları
        const neonLight = new THREE.PointLight(0xff00bb, 8, 250); neonLight.position.set(0, 15, -20); scene.add(neonLight);
        const blueLight = new THREE.PointLight(0x00f0ff, 6, 200); blueLight.position.set(0, -10, -10); scene.add(blueLight);
        scene.add(new THREE.AmbientLight(0x130624, 1.4));

        // 3D Dönen Dev Kuantum Nebula
        const nebulaGeo = new THREE.SphereGeometry(95, 32, 32);
        const nebulaMat = new THREE.MeshBasicMaterial({ color: 0x3d005c, wireframe: true, transparent: true, opacity: 0.18 });
        const nebula = new THREE.Mesh(nebulaGeo, nebulaMat); scene.add(nebula);

        // Sinematik Warp Yıldız Parçacıkları
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

        // YÜKSEK KALİTELİ KUANTUM JETİ MODELİ
        const playerJet = new THREE.Group();
        const chromePink = new THREE.MeshStandardMaterial({ color: 0xff0066, metalness: 0.95, roughness: 0.02, emissive: 0x44001c });
        
        const core = new THREE.Mesh(new THREE.CylinderGeometry(0.12, 0.48, 2.8, 12), chromePink); core.rotation.x = Math.PI / 2;
        const cockpit = new THREE.Mesh(new THREE.SphereGeometry(0.3, 24, 24), new THREE.MeshStandardMaterial({ color: 0x00faff, roughness: 0, metalness: 1 }));
        cockpit.position.set(0, 0.22, -0.5); cockpit.scale.set(1, 1, 2.0);
        
        // Plazma Kanatlar ve İticiler
        const leftWing = new THREE.Mesh(new THREE.BoxGeometry(2.0, 0.05, 0.9), chromePink); leftWing.position.set(-1.1, -0.05, 0.4); leftWing.rotation.y = 0.25;
        const rightWing = leftWing.clone(); rightWing.position.x = 1.1; rightWing.rotation.y = -0.25;
        
        // Kanat Ucu Işıkları
        const lLight = new THREE.Mesh(new THREE.SphereGeometry(0.08), new THREE.MeshBasicMaterial({ color: 0x00ffff })); lLight.position.set(-2.1, 0, 0.4);
        const rLight = lLight.clone(); rLight.position.x = 2.1;
        playerJet.add(core, cockpit, leftWing, rightWing, lLight, rLight);

        // Plazma Egzoz İzi Parçacık Motoru
        const trailCount = 40;
        const trailGeo = new THREE.BufferGeometry();
        const trailPos = new Float32Array(trailCount * 3);
        for(let i=0; i<trailCount*3; i+=3) { trailPos[i]=0; trailPos[i+1]=-0.1; trailPos[i+2]=1.4+Math.random(); }
        trailGeo.setAttribute('position', new THREE.BufferAttribute(trailPos, 3));
        const trailSparks = new THREE.Points(trailGeo, new THREE.PointsMaterial({ color: 0x00ffcc, size: 0.28, transparent: true, opacity: 0.85 }));
        playerJet.add(trailSparks);

        playerJet.position.set(0, 0, -6); scene.add(playerJet);

        // Kristalize Asteroit Engelleri
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

                // Plazma İzi Animasyonu
                const tArr = trailSparks.geometry.attributes.position.array;
                for(let i=2; i<tArr.length; i+=3) { tArr[i] += 0.15; if(tArr[i] > 3.8) tArr[i] = 1.4; }
                trailSparks.geometry.attributes.position.needsUpdate = true;

                // Meteor Döngüsü
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
