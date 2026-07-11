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
# CSS DÜZENLEMELERİ (KIRMIZI SIDEBAR VE SAF BEYAZ METİN ALANLARI)
# ==========================================================================================
st.markdown("""
    <style>
    /* 1. Genel Arka Plan */
    .stApp, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
        background-color: #0b0705 !important;
        background-image: 
            radial-gradient(circle at 100% 0%, #3a1c11 0%, transparent 50%),
            radial-gradient(circle at 0% 100%, #220e08 0%, transparent 50%) !important;
        background-attachment: fixed !important;
        color: #ffffff !important;
    }

    p, span, label, div {
        color: #ffffff !important;
    }
    
    /* 2. ANA BAŞLIK */
    .havali-ana-baslik {
        text-align: center !important;
        font-family: 'Segoe UI', sans-serif !important;
        font-size: 32px !important; 
        font-weight: 900 !important;
        letter-spacing: 3px !important;
        color: #ffffff !important; 
        margin-top: 15px !important;
    }
    
    .havali-alt-yazi {
        text-align: center !important;
        color: #cccccc !important;
        font-size: 14px !important;
        margin-bottom: 25px !important;
    }
    
    /* 3. SIDEBAR: TONLAMALI PREMİUM KIRMIZI */
    [data-testid="stSidebar"], [data-testid="stSidebarUserContent"] {
        background: linear-gradient(180deg, #5a0000 0%, #2a0000 50%, #0d0000 100%) !important;
        border-right: 3px solid #b30000 !important;
        box-shadow: 8px 0 30px rgba(179, 0, 0, 0.25) !important;
    }
    
    [data-testid="stSidebar"] * {
        color: #ffffff !important;
    }
    
    /* 4. SOHBET BALONLARI */
    [data-testid="stChatMessage"] {
        background-color: rgba(25, 15, 10, 0.6) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 12px !important;
        margin-bottom: 15px !important;
    }
    
    /* 5. MESAJ GİRİŞ KUTUSU - SAF BEYAZ */
    textarea[data-testid="stChatInputTextArea"] {
        color: #111111 !important;
        border-radius: 12px !important;
        background-color: #ffffff !important;
        border: 2px solid #dddddd !important;
    }
    textarea[data-testid="stChatInputTextArea"]:focus {
        border-color: #8b0000 !important;
    }
    textarea[data-testid="stChatInputTextArea"]::placeholder {
        color: #777777 !important;
    }
    .stAudioInput {
        background-color: #ffffff !important;
        border: 2px solid #dddddd !important;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================================================================
# SOL TARAFTAKİ MENÜ
# ==========================================================================================
with st.sidebar:
    st.markdown("## 🎮 APOLINGO ARCADE ULTRA")
    st.markdown("**Premium Next-Gen Grafik Güncellemesi**")
    st.write("---")
    
    secilen_mod = st.radio(
        "Aparatı Seç Be Gardaşşş:",
        ["💬 Sohbet Modu", "🏎️ BMW M3 Ultra Makas", "🌌 Astro-Aura Kuantum Jet"],
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
# SOHBET MODU
# ==========================================================================================
if st.session_state.aktif_mod == "Sohbet":
    st.markdown('<h1 class="havali-ana-baslik">APOLINGO MASTER AI</h1>', unsafe_allow_html=True)
    st.markdown('<p class="havali-alt-yazi">Kurucu: Apolingo | Premium Engine</p>', unsafe_allow_html=True)
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
        except:
            pass

    if gelen_soru:
        with st.chat_message("user"):
            st.write(gelen_soru)
        st.session_state.sohbet_hafizasi.append({"role": "user", "content": gelen_soru})
        soru_lower = gelen_soru.lower().strip()

        with st.spinner("⚡ Hesaplamalar Yapılıyor..."):
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
            except:
                st.session_state.ses_isleme_aktif = True

# ==========================================================================================
# NEXT-GEN ULTRA BMW M3 MAKAS SİMÜLATÖRÜ
# ==========================================================================================
elif st.session_state.aktif_mod == "ErkekOyunu":
    st.markdown("### 🏎️ BMW M3 Ultra-Quality Next-Gen Makas Simülatörü")
    st.caption("A, D veya Yön Tuşları ile kontrol et. Kaliteli şeritler ve gövde fizikleri aktif!")

    bmw_nextgen_html = """
    <div style="text-align:center; background:#050201; padding:15px; border-radius:16px; border:3px solid #ff0000; box-shadow: 0 0 30px rgba(255,0,0,0.4); user-select:none; position:relative;">
        <button id="btnLeft" style="position:absolute; left:20px; top:45%; transform:translateY(-50%); padding: 25px 22px; font-size: 32px; font-weight:bold; background:rgba(20,0,0,0.85); color:#ffffff; border:2px solid #ff3333; border-radius:15px; cursor:pointer; z-index:10; box-shadow:0 0 15px #ff0000;">◀</button>
        <button id="btnRight" style="position:absolute; right:20px; top:45%; transform:translateY(-50%); padding: 25px 22px; font-size: 32px; font-weight:bold; background:rgba(20,0,0,0.85); color:#ffffff; border:2px solid #ff3333; border-radius:15px; cursor:pointer; z-index:10; box-shadow:0 0 15px #ff0000;">▶</button>
        <div id="bmwFullCanvasContainer" style="width:100%; height:550px; border-radius:10px; overflow:hidden;"></div>
        <div id="uiPanel" style="margin-top:15px;">
            <h2 id="scoreDisplay4D" style="color:#ffffff; font-family:'Segoe UI',sans-serif; margin:10px 0; font-weight:900; font-size:30px; letter-spacing:1px;">HIGH-RES MAKAS: 0 🔥</h2>
            <div id="restartButtonContainer"></div>
        </div>
    </div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script>
        const container = document.getElementById("bmwFullCanvasContainer");
        const scene = new THREE.Scene();
        scene.fog = new THREE.FogExp2(0x050201, 0.015);
        
        const camera = new THREE.PerspectiveCamera(50, container.clientWidth / 550, 0.1, 1000);
        const renderer = new THREE.WebGLRenderer({ antialias: true, powerPreference: "high-performance" });
        renderer.setSize(container.clientWidth, 550);
        renderer.shadowMap.enabled = true;
        container.appendChild(renderer.domElement);

        // Kaliteli Işıklandırma
        const mainLight = new THREE.DirectionalLight(0xffffff, 2.5);
        mainLight.position.set(5, 40, 20);
        scene.add(mainLight);
        
        const ambientLight = new THREE.AmbientLight(0x221111, 1.2);
        scene.add(ambientLight);

        // Ultra Asfalt Pist
        const roadGeo = new THREE.BoxGeometry(18, 0.1, 1000);
        const roadMat = new THREE.MeshStandardMaterial({ color: 0x110d0c, roughness: 0.6, metalness: 0.1 });
        const road = new THREE.Mesh(roadGeo, roadMat);
        scene.add(road);

        // Parlayan Neon Şerit Çizgileri
        let lines = [];
        for(let i=0; i<30; i++){
            let lMesh = new THREE.Mesh(new THREE.BoxGeometry(0.3, 0.12, 12), new THREE.MeshBasicMaterial({ color: 0xff1111 }));
            lMesh.position.set(0, 0.08, -i * 25);
            scene.add(lMesh);
            lines.push(lMesh);
        }

        // Gelişmiş BMW M3 Tasarımı (Gölgeli ve Detaylı)
        const bmwM3 = new THREE.Group();
        
        // Karoseri
        const bodyMat = new THREE.MeshStandardMaterial({ color: 0xe6e6e6, metalness: 0.8, roughness: 0.15 });
        const body = new THREE.Mesh(new THREE.BoxGeometry(1.6, 0.45, 3.4), bodyMat);
        body.position.y = 0.35;
        bmwM3.add(body);

        // Kabin / Camlar
        const glassMat = new THREE.MeshStandardMaterial({ color: 0x0a0a0a, roughness: 0.0, metalness: 1.0 });
        const cabin = new THREE.Mesh(new THREE.BoxGeometry(1.3, 0.45, 1.7), glassMat);
        cabin.position.set(0, 0.75, -0.1);
        bmwM3.add(cabin);

        // Kırmızı LED Arka Lambalar (Stop Lambaları)
        const taillightMat = new THREE.MeshBasicMaterial({ color: 0xff0000 });
        const leftLight = new THREE.Mesh(new THREE.BoxGeometry(0.3, 0.1, 0.1), taillightMat);
        leftLight.position.set(-0.6, 0.45, 1.7);
        const rightLight = leftLight.clone();
        rightLight.position.x = 0.6;
        bmwM3.add(leftLight, rightLight);

        bmwM3.position.set(0, 0, -10);
        scene.add(bmwM3);

        // Yüksek Kaliteli Trafik Araçları
        let traffic = [];
        const carColors = [0xffcc00, 0x11ff11, 0x00ccff, 0xcc00ff];
        for(let i=0; i<5; i++){
            let tGroup = new THREE.Group();
            let tBody = new THREE.Mesh(new THREE.BoxGeometry(1.5, 0.6, 3.0), new THREE.MeshStandardMaterial({ color: carColors[i%4], roughness: 0.2 }));
            tBody.position.y = 0.4;
            let tCabin = new THREE.Mesh(new THREE.BoxGeometry(1.2, 0.5, 1.4), glassMat);
            tCabin.position.set(0, 0.85, -0.1);
            tGroup.add(tBody, tCabin);
            tGroup.position.set((Math.random() - 0.5) * 13, 0, -60 - (i * 45));
            scene.add(tGroup);
            traffic.push(tGroup);
        }

        camera.position.set(0, 5.0, -2.5);
        camera.lookAt(new THREE.Vector3(0, 0.8, -30));

        let score = 0; let gameOver = false; let keys = {};
        let rollAngle = 0; // Dönüş esneme açısı
        window.addEventListener("keydown", e => keys[e.key] = true);
        window.addEventListener("keyup", e => keys[e.key] = false);

        let touchLeft = false, touchRight = false;
        document.getElementById("btnLeft").addEventListener("pointerdown", () => touchLeft = true);
        document.getElementById("btnLeft").addEventListener("pointerup", () => touchLeft = false);
        document.getElementById("btnRight").addEventListener("pointerdown", () => touchRight = true);
        document.getElementById("btnRight").addEventListener("pointerup", () => touchRight = false);

        function animate() {
            if(!gameOver) {
                let currentSpeed = 0.85 + (score * 0.02);
                
                // Fiziksel gövde esneme ve kontrol mekanizması
                if(keys["ArrowLeft"] || keys["a"] || keys["A"] || touchLeft) { 
                    if(bmwM3.position.x > -7.5) {
                        bmwM3.position.x -= 0.22;
                        if(rollAngle < 0.12) rollAngle += 0.02;
                    }
                } else if(keys["ArrowRight"] || keys["d"] || keys["D"] || touchRight) { 
                    if(bmwM3.position.x < 7.5) {
                        bmwM3.position.x += 0.22;
                        if(rollAngle > -0.12) rollAngle -= 0.02;
                    }
                } else {
                    rollAngle *= 0.85; // Düzlüğe geri dönme
                }
                bmwM3.rotation.z = rollAngle; // Sağa sola yatma efekti

                // Yol akışı
                lines.forEach(l => { 
                    l.position.z += currentSpeed; 
                    if(l.position.z > 15) l.position.z = -300; 
                });

                // Trafik Yapay Zekası ve Çarpışma Algılama
                traffic.forEach(t => {
                    t.position.z += currentSpeed * 0.45;
                    if(t.position.z > 2) { 
                        t.position.z = -180 - Math.random()*50; 
                        t.position.x = (Math.random() - 0.5) * 13; 
                        score++; 
                        document.getElementById("scoreDisplay4D").innerText = "HIGH-RES MAKAS: " + score + " 🔥"; 
                    }
                    
                    // Hassas çarpışma kutusu kontrolü
                    if(Math.abs(bmwM3.position.x - t.position.x) < 1.45 && Math.abs(bmwM3.position.z - t.position.z) < 3.2) { 
                        gameOver = true; 
                        document.getElementById("scoreDisplay4D").innerHTML = "<span style='color:#ff3333; font-size:28px;'>💥 MAKAS PATLADI! BMW PERT! 💥</span>";
                        document.getElementById("restartButtonContainer").innerHTML = '<button onclick="location.reload()" style="margin-top:15px; padding:15px 45px; font-size:22px; font-weight:bold; background:linear-gradient(90deg, #ff0000, #8b0000); color:#fff; border:none; border-radius:12px; cursor:pointer; box-shadow: 0 0 25px #ff0000; transition: 0.2s;">YENİ M3 ÇEK BE GARDAŞŞŞ! 🔄</button>';
                    }
                });
            }
            renderer.render(scene, camera);
            requestAnimationFrame(animate);
        }
        animate();
    </script>
    """
    components.html(bmw_nextgen_html, height=780)

# ==========================================================================================
# NEXT-GEN ULTRA ASTRO-AURA KUANTUM JET OYUNU
# ==========================================================================================
elif st.session_state.aktif_mod == "KizOyunu":
    st.markdown("### 🌌 Astro-Aura Premium 4D Space Escape")
    st.caption("A, D veya Yön Tuşları ile fütüristik jetini kozmik fırtınadan koru be gardaş!")

    astro_premium_html = """
    <div style="text-align:center; background:#030105; padding:15px; border-radius:16px; border:3px solid #ff0000; box-shadow: 0 0 30px rgba(255,0,0,0.4); user-select:none; position:relative;">
        <button id="btnLeftKiz" style="position:absolute; left:20px; top:45%; transform:translateY(-50%); padding: 25px 22px; font-size: 32px; font-weight:bold; background:rgba(15,0,25,0.85); color:#ffffff; border:2px solid #ff3333; border-radius:15px; cursor:pointer; z-index:10; box-shadow:0 0 15px #ff0000;">◀</button>
        <button id="btnRightKiz" style="position:absolute; right:20px; top:45%; transform:translateY(-50%); padding: 25px 22px; font-size: 32px; font-weight:bold; background:rgba(15,0,25,0.85); color:#ffffff; border:2px solid #ff3333; border-radius:15px; cursor:pointer; z-index:10; box-shadow:0 0 15px #ff0000;">▶</button>
        <div id="kizFullCanvasContainer" style="width:100%; height:550px; border-radius:10px; overflow:hidden;"></div>
        <div id="uiPanelKiz" style="margin-top:15px;">
            <h2 id="kizScoreDisplay" style="color:#ffffff; font-family:'Segoe UI',sans-serif; margin:10px 0; font-weight:900; font-size:30px; letter-spacing:1px;">AURA MATRİSİ: 0 ⭐</h2>
            <div id="restartButtonContainerKiz"></div>
        </div>
    </div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script>
        const container = document.getElementById("kizFullCanvasContainer");
        const scene = new THREE.Scene();
        scene.fog = new THREE.FogExp2(0x030105, 0.012);
        
        const camera = new THREE.PerspectiveCamera(55, container.clientWidth / 550, 0.1, 1000);
        const renderer = new THREE.WebGLRenderer({ antialias: true });
        renderer.setSize(container.clientWidth, 550);
        container.appendChild(renderer.domElement);

        // Işık Efektleri (Mor ve Kırmızı Kozmik Işıklar)
        const spaceLight = new THREE.PointLight(0xff33aa, 3, 150);
        spaceLight.position.set(0, 15, -10);
        scene.add(spaceLight);
        scene.add(new THREE.AmbientLight(0x1a0a2a, 1.5));

        // Kaliteli Kuantum Tozu / Yıldız Alanı
        const starGeo = new THREE.BufferGeometry();
        const starCount = 600;
        const starPositions = new Float32Array(starCount * 3);
        for(let i=0; i<starCount*3; i+=3) {
            starPositions[i] = (Math.random() - 0.5) * 70;
            starPositions[i+1] = (Math.random() - 0.5) * 45;
            starPositions[i+2] = -Math.random() * 200;
        }
        starGeo.setAttribute('position', new THREE.BufferAttribute(starPositions, 3));
        const starMat = new THREE.PointsMaterial({ color: 0xff66cc, size: 0.35, transparent: true, opacity: 0.8 });
        const starField = new THREE.Points(starGeo, starMat);
        scene.add(starField);

        // Premium Kuantum Stealth Jet Tasarımı
        const playerJet = new THREE.Group();
        const jetMat = new THREE.MeshStandardMaterial({ color: 0xff3333, metalness: 0.9, roughness: 0.1 });
        
        // Ana Gövde
        const coreGeo = new THREE.ConeGeometry(0.6, 2.4, 4);
        const core = new THREE.Mesh(coreGeo, jetMat);
        core.rotation.x = Math.PI / 2;
        playerJet.add(core);

        // Kanatlar
        const wingGeo = new THREE.BoxGeometry(2.2, 0.05, 0.8);
        const wings = new THREE.Mesh(wingGeo, jetMat);
        wings.position.set(0, -0.1, 0.2);
        playerJet.add(wings);

        // Plazma İtici Motor Ateşi (Arka Işık)
        const engineLight = new THREE.Mesh(new THREE.SphereGeometry(0.25, 8, 8), new THREE.MeshBasicMaterial({ color: 0xffffff }));
        engineLight.position.set(0, 0, 1.2);
        playerJet.add(engineLight);

        playerJet.position.set(0, 0, -8);
        scene.add(playerJet);

        // Geometrik Kuantum Kristalleri (Engeller)
        let crystals = [];
        for(let i=0; i<5; i++){
            let cGeo = new THREE.IcosahedronGeometry(1.2, 0); // Kristalize köşeli yapı
            let cMat = new THREE.MeshStandardMaterial({ color: 0x990033, emissive: 0x4a0011, roughness: 0.3, metalness: 0.7 });
            let crystal = new THREE.Mesh(cGeo, cMat);
            crystal.position.set((Math.random() - 0.5) * 14, (Math.random() - 0.5) * 4, -50 - (i * 35));
            scene.add(crystal);
            crystals.push(crystal);
        }

        camera.position.set(0, 4.5, 3);
        camera.lookAt(new THREE.Vector3(0, 0, -18));

        let score = 0; let gameOver = false; let keys = {};
        window.addEventListener("keydown", e => keys[e.key] = true);
        window.addEventListener("keyup", e => keys[e.key] = false);

        let touchLeft = false, touchRight = false;
        document.getElementById("btnLeftKiz").addEventListener("pointerdown", () => touchLeft = true);
        document.getElementById("btnLeftKiz").addEventListener("pointerup", () => touchLeft = false);
        document.getElementById("btnRightKiz").addEventListener("pointerdown", () => touchLeft = true);
        document.getElementById("btnRightKiz").addEventListener("pointerup", () => touchLeft = false);

        function animate() {
            if(!gameOver) {
                let gameSpeed = 0.65 + (score * 0.025);

                if(keys["ArrowLeft"] || keys["a"] || keys["A"] || touchLeft) { if(playerJet.position.x > -7.5) playerJet.position.x -= 0.20; playerJet.rotation.z = 0.3; }
                else if(keys["ArrowRight"] || keys["d"] || keys["D"] || touchRight) { if(playerJet.position.x < 7.5) playerJet.position.x += 0.20; playerJet.rotation.z = -0.3; }
                else { playerJet.rotation.z *= 0.85; }

                // Uzay tozu akışı
                const positions = starField.geometry.attributes.position.array;
                for(let i=2; i<positions.length; i+=3) { 
                    positions[i] += gameSpeed * 1.5; 
                    if(positions[i] > 10) positions[i] = -180; 
                }
                starField.geometry.attributes.position.needsUpdate = true;

                // Kristallerin Hareketi ve Çarpışma
                crystals.forEach(c => {
                    c.position.z += gameSpeed;
                    c.rotation.x += 0.03;
                    c.rotation.y += 0.02;

                    if(c.position.z > 5) { 
                        c.position.z = -140 - Math.random()*30; 
                        c.position.x = (Math.random() - 0.5) * 14; 
                        score++; 
                        document.getElementById("kizScoreDisplay").innerText = "AURA MATRİSİ: " + score + " ⭐"; 
                    }
                    
                    if(Math.abs(playerJet.position.x - c.position.x) < 1.5 && Math.abs(playerJet.position.z - c.position.z) < 2.2) { 
                        gameOver = true; 
                        document.getElementById("kizScoreDisplay").innerHTML = "<span style='color:#ff3366; font-size:26px;'>🔮 KUANTUM KALKANLARI ÇÖKTÜ! 🔮</span>";
                        document.getElementById("restartButtonContainerKiz").innerHTML = '<button onclick="location.reload()" style="margin-top:15px; padding:15px 45px; font-size:22px; font-weight:bold; background:linear-gradient(90deg, #ff0055, #4a0011); color:#fff; border:none; border-radius:12px; cursor:pointer; box-shadow: 0 0 25px #ff0055;">KAZANI YENİDEN TETİKLE! 🔄</button>';
                    }
                });
            }
            renderer.render(scene, camera);
            requestAnimationFrame(animate);
        }
        animate();
    </script>
    """
    components.html(astro_premium_html, height=780)
