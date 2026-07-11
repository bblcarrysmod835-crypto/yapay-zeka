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
st.set_page_config(page_title="Apolingo 10D Master Full Arcade", page_icon="🏎️", layout="wide")

# Yapay zekanın beynini ve hafızasını başlatıyoruz
if "client" not in st.session_state:
    st.session_state.client = Client()

# Sürekli dinleme için ses kontrol tetikleyicisi
if "ses_isleme_aktif" not in st.session_state:
    st.session_state.ses_isleme_aktif = True

# Menü ve Oyun Seçim Durumu
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
# CSS STİLLERİ
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
    
    [data-testid="stSidebar"], [data-testid="stSidebarUserContent"] {
        background: linear-gradient(180deg, #4a0000 0%, #220000 50%, #050000 100%) !important;
        border-right: 2px solid #8b0000 !important;
    }
    
    [data-testid="stSidebar"] * {
        color: #ffffff !important;
    }

    [data-testid="stChatMessage"] {
        background-color: rgba(20, 10, 5, 0.7) !important;
        border: 1px solid rgba(255, 255, 255, 0.15) !important;
        border-radius: 16px !important;
    }
    </style>
""", unsafe_allow_html=True)

# SIDEBAR MENÜSÜ
with st.sidebar:
    st.markdown("## 🎮 APOLINGO ARCADE")
    st.markdown("10D Boyutlu Özel Mod")
    st.write("---")
    
    secilen_mod = st.radio(
        "Aparatı Seç Be Gardaşş:",
        ["💬 Sohbet Modu", "🏎️ BMW M3 10D Makas Oyunu", "🌌 Astro-Aura Kuantum Oyunu"],
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
    st.markdown('<p class="havali-alt-yazi">Kurucu ve Baş Mühendis: Apolingo | By Abdurrahim İriş</p>', unsafe_allow_html=True)
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
# BMW M3 10D HİPER OYUNU: SIFIR ÇIKINTILI TAVAN, ÖZEL KAPUT VE RENKLİ TRAFİK
# ==========================================================================================
elif st.session_state.aktif_mod == "ErkekOyunu":
    st.markdown("### 🏎️ Apolingo 10D Hiper Realizm: Özel Kaputlu Sarı Canavar")
    st.caption("Senin araban efsanevi Neon Sarısı ve Karbon Kaputlu yapıldı! Diğer arabalar rengarenk, tavan ise jilet gibi pürüzsüz be gardaşş!")

    bmw_10d_html = """
    <div style="text-align:center; background:#000000; padding:15px; border-radius:16px; border:3px solid #ff0000; box-shadow: 0 0 50px rgba(255,0,0,0.9); user-select:none; position:relative;">
        <button id="btnLeft" style="position:absolute; left:25px; top:45%; transform:translateY(-50%); padding: 25px 22px; font-size: 32px; font-weight:bold; background:rgba(0,0,0,0.9); color:#ffffff; border:2px solid #ff0000; border-radius:15px; cursor:pointer; z-index:100; box-shadow:0 0 20px #ff0000;">◀</button>
        <button id="btnRight" style="position:absolute; right:25px; top:45%; transform:translateY(-50%); padding: 25px 22px; font-size: 32px; font-weight:bold; background:rgba(0,0,0,0.9); color:#ffffff; border:2px solid #ff0000; border-radius:15px; cursor:pointer; z-index:100; box-shadow:0 0 20px #ff0000;">▶</button>
        <div id="bmw10DContainer" style="width:100%; height:570px; border-radius:10px; overflow:hidden;"></div>
        <div id="uiPanel" style="margin-top:15px;">
            <h2 id="scoreDisplay10D" style="color:#ffffff; font-family:'Segoe UI',sans-serif; margin:10px 0; font-weight:900; font-size:34px; letter-spacing:1px; text-shadow:0 0 15px #ff0000;">10D Otoban Skoru: 0 🌀</h2>
            <div id="restartButtonContainer"></div>
        </div>
    </div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script>
        const container = document.getElementById("bmw10DContainer");
        const scene = new THREE.Scene(); 
        scene.background = new THREE.Color(0x010103);
        scene.fog = new THREE.FogExp2(0x010103, 0.0012); 

        const camera = new THREE.PerspectiveCamera(46, container.clientWidth / 570, 0.1, 1000);
        const renderer = new THREE.WebGLRenderer({ antialias: true, powerPreference: "high-performance" });
        renderer.setSize(container.clientWidth, 570); 
        renderer.toneMapping = THREE.ACESFilmicToneMapping;
        renderer.toneMappingExposure = 2.0;
        container.appendChild(renderer.domElement);

        const sunLight = new THREE.DirectionalLight(0xffffff, 4.0); sunLight.position.set(10, 60, 15); scene.add(sunLight);
        const ambient = new THREE.AmbientLight(0x221c1c, 2.5); scene.add(ambient);

        // Parlak Islak Otoban
        const roadGeo = new THREE.BoxGeometry(18, 0.1, 1000);
        const roadMat = new THREE.MeshStandardMaterial({ color: 0x050505, roughness: 0.01, metalness: 0.99 });
        const road = new THREE.Mesh(roadGeo, roadMat); scene.add(road);

        let lines = [];
        for(let i=0; i<35; i++){
            let lMesh = new THREE.Mesh(new THREE.BoxGeometry(0.25, 0.11, 16), new THREE.MeshBasicMaterial({ color: 0xffffff }));
            lMesh.position.set(0, 0.06, -i * 24); scene.add(lMesh); lines.push(lMesh);
        }

        // --- 10D ÖZEL JİLET TAVANLI ARABA ÜRETİM MOTORU ---
        function create10DCar(bodyColor, isPlayer) {
            const carGroup = new THREE.Group();
            
            const paintMat = new THREE.MeshStandardMaterial({ color: bodyColor, metalness: 0.98, roughness: 0.02 });
            const carbonMat = new THREE.MeshStandardMaterial({ color: 0x111111, metalness: 0.90, roughness: 0.15 }); 
            const glassMat = new THREE.MeshStandardMaterial({ color: 0x02050a, roughness: 0, metalness: 1 });
            const chromeMat = new THREE.MeshStandardMaterial({ color: 0xeeeeee, metalness: 1.0, roughness: 0.01 });
            const tyreMat = new THREE.MeshStandardMaterial({ color: 0x060606, roughness: 0.8 });
            const brakeMat = new THREE.MeshStandardMaterial({ color: 0xee0000, metalness: 0.9 });

            // Ana Alt Şasi
            const base = new THREE.Mesh(new THREE.BoxGeometry(1.74, 0.26, 3.75), paintMat);
            base.position.y = 0.28;
            carGroup.add(base);

            // ÖN KAPUT (Oyuncuya Özel Agresif Karbon Kaput, Diğerlerine Normal Gövde Rengi Kaput)
            const hoodMatSelected = isPlayer ? carbonMat : paintMat;
            const hood = new THREE.Mesh(new THREE.BoxGeometry(1.70, 0.18, 1.30), hoodMatSelected);
            hood.position.set(0, 0.40, -1.18);
            carGroup.add(hood);

            // JİLET GİBİ %100 PÜRÜZSÜZ TEK PARÇA ÜST KABİN (Çıkıntılar, Çizgiler Tamamen Sıfırlandı!)
            const cabinGeo = new THREE.BoxGeometry(1.38, 0.42, 1.70);
            const cabin = new THREE.Mesh(cabinGeo, paintMat);
            cabin.position.set(0, 0.62, 0.05);
            carGroup.add(cabin);

            // Cam Alanı (Kabin İçine Gömülü Kusursuz İllüzyon)
            const glassInsert = new THREE.Mesh(new THREE.BoxGeometry(1.34, 0.36, 1.66), glassMat);
            glassInsert.position.set(0, 0.63, 0.05);
            carGroup.add(glassInsert);

            // Arka Bagaj Kapağı (Sıfır Spoyler, Dümdüz)
            const trunk = new THREE.Mesh(new THREE.BoxGeometry(1.70, 0.24, 0.75), paintMat);
            trunk.position.set(0, 0.42, 1.38);
            carGroup.add(trunk);

            // Tekerlekler & Kaliperler
            const tG = new THREE.CylinderGeometry(0.35, 0.35, 0.28, 32); tG.rotateZ(Math.PI / 2);
            const rG = new THREE.CylinderGeometry(0.25, 0.25, 0.29, 16); rG.rotateZ(Math.PI / 2);
            const wPositions = [[-0.92, 0.35, -1.15], [0.92, 0.35, -1.15], [-0.92, 0.35, 1.30], [0.92, 0.35, 1.30]];

            wPositions.forEach(pos => {
                const tire = new THREE.Mesh(tG, tyreMat); tire.position.set(pos[0], pos[1], pos[2]);
                const rim = new THREE.Mesh(rG, chromeMat); rim.position.set(pos[0], pos[1], pos[2]);
                const caliper = new THREE.Mesh(new THREE.BoxGeometry(0.04, 0.12, 0.08), brakeMat);
                caliper.position.set(pos[0] + (pos[0] > 0 ? -0.04 : 0.04), pos[1] + 0.08, pos[2]);
                carGroup.add(tire, rim, caliper);
            });

            // LAZER FARLAR VE STOPLAR
            const fGeo = new THREE.BoxGeometry(0.24, 0.07, 0.04);
            const fMat = new THREE.MeshBasicMaterial({ color: isPlayer ? 0x00f3ff : 0xffaa00 }); // Oyuncuya Buz Mavisi Far
            const headL = new THREE.Mesh(fGeo, fMat); headL.position.set(-0.62, 0.38, -1.89);
            const headR = headL.clone(); headR.position.x = 0.62;
            carGroup.add(headL, headR);

            const stopMat = new THREE.MeshBasicMaterial({ color: 0xff0505 });
            const stopL = new THREE.Mesh(fGeo, stopMat); stopL.position.set(-0.62, 0.42, 1.76);
            const stopR = stopL.clone(); stopR.position.x = 0.62;
            carGroup.add(stopL, stopR);

            return carGroup;
        }

        // SENİN ARABAN: Göz Alıcı Neon Limon Sarısı (0xdfff00) ve Karbon Kaputlu
        const playerCar = create10DCar(0xdfff00, true);
        playerCar.position.set(0, 0, -8); scene.add(playerCar);

        // Buz Mavisi Far Işıkları Konisi
        const beamCone = new THREE.CylinderGeometry(0.05, 4.0, 45, 16, 1, true); beamCone.translate(0, 22.5, 0);
        const beamMat = new THREE.MeshBasicMaterial({ color: 0x00f0ff, transparent: true, opacity: 0.14, side: THREE.DoubleSide });
        const leftBeam = new THREE.Mesh(beamCone, beamMat); leftBeam.position.set(-0.62, 0.38, -1.9); leftBeam.rotation.x = -Math.PI / 2;
        const rightBeam = leftBeam.clone(); rightBeam.position.x = 0.62;
        playerCar.add(leftBeam, rightBeam);

        // RENKLİ TRAFİK HAVUZU (Sürekli Farklı Canlı Renkler Alan Akıllı Sistem)
        let traffic = []; 
        const randomColors = [0xff007f, 0x00ff66, 0xff6600, 0x9900ff, 0x0033ff, 0x00ffff, 0xff00ff];
        
        for(let i=0; i<6; i++){
            let randomColor = randomColors[i % randomColors.length];
            let tCar = create10DCar(randomColor, false);
            tCar.position.set((Math.random() - 0.5) * 12, 0, -80 - (i * 40)); 
            scene.add(tCar); 
            traffic.push(tCar);
        }

        camera.position.set(0, 3.6, -0.1); camera.lookAt(new THREE.Vector3(0, 0.3, -40));
        
        let score = 0; let gameOver = false; let keys = {}; let tilt = 0; let dimensionsClock = 0;
        window.addEventListener("keydown", e => keys[e.key] = true); window.addEventListener("keyup", e => keys[e.key] = false);
        
        let touchLeft = false, touchRight = false;
        const bLeft = document.getElementById("btnLeft"); const bRight = document.getElementById("btnRight");
        bLeft.addEventListener("mousedown", () => touchLeft = true); bLeft.addEventListener("mouseup", () => touchLeft = false);
        bLeft.addEventListener("touchstart", (e) => { e.preventDefault(); touchLeft = true; }); bLeft.addEventListener("touchend", () => touchLeft = false);
        bRight.addEventListener("mousedown", () => touchRight = true); bRight.addEventListener("mouseup", () => touchRight = false);
        bRight.addEventListener("touchstart", (e) => { e.preventDefault(); touchRight = true; }); bRight.addEventListener("touchend", () => touchRight = false);

        function animate() {
            if(!gameOver) {
                dimensionsClock += 0.05; // 10D Zaman ve Titreşim Matrisi
                let currentSpeed = 1.25 + (score * 0.05);
                
                if(keys["ArrowLeft"] || keys["a"] || keys["A"] || touchLeft) { 
                    if(playerCar.position.x > -7.4) { playerCar.position.x -= 0.30; if(tilt < 0.14) tilt += 0.025; }
                } else if(keys["ArrowRight"] || keys["d"] || keys["D"] || touchRight) { 
                    if(playerCar.position.x < 7.4) { playerCar.position.x += 0.30; if(tilt > -0.14) tilt -= 0.025; }
                } else { tilt *= 0.72; }
                
                // 10D Süpriz Fizik Esnemesi: Şasi makas yönüne ve motor devrine göre hafifçe yaylanır
                playerCar.rotation.z = tilt;
                playerCar.rotation.y = tilt * 0.22;
                playerCar.position.y = 0.01 * Math.sin(dimensionsClock * 4); // Motor Sarsıntısı Boyutu

                // Dinamik Yol Kamerası Titreşimi
                camera.position.y = 3.6 + (Math.random() - 0.5) * ((score * 0.001) + 0.003);

                lines.forEach(l => { l.position.z += currentSpeed; if(l.position.z > 15) l.position.z = -250; });
                
                traffic.forEach((t, index) => {
                    t.position.z += currentSpeed * 0.52;
                    
                    // Diğer arabalara 10D dalgalanma efekti
                    t.position.y = 0.015 * Math.cos(dimensionsClock * 3 + index);

                    if(t.position.z > 4) { 
                        t.position.z = -180 - Math.random()*50; 
                        t.position.x = (Math.random() - 0.5) * 12; 
                        
                        // Her canlandığında yeni bomba gibi rastgele bir renk ata!
                        let nextColor = randomColors[Math.floor(Math.random() * randomColors.length)];
                        t.children.forEach(child => {
                            if(child.material && child.material.color && child.geometry.type === "BoxGeometry" && child.position.y === 0.28) {
                                child.material.color.setHex(nextColor);
                            }
                        });

                        score++; 
                        document.getElementById("scoreDisplay10D").innerText = "10D Otoban Skoru: " + score + " 🌀"; 
                    }

                    // Hassas Çarpışma Kutusu
                    if(Math.abs(playerCar.position.x - t.position.x) < 1.62 && Math.abs(playerCar.position.z - t.position.z) < 3.6) { 
                        gameOver = true; 
                        document.getElementById("scoreDisplay10D").innerHTML = "<span style='color:#ff0000; font-size:32px; font-weight:900; text-shadow:0 0 20px #ff0000;'>💥 10. BOYUTTA PERT OLDUK! 💥</span>";
                        document.getElementById("restartButtonContainer").innerHTML = '<button onclick="location.reload()" style="margin-top:15px; padding:18px 50px; font-size:22px; font-weight:bold; background:linear-gradient(90deg, #ff0000, #220000); color:#fff; border:none; border-radius:12px; cursor:pointer; box-shadow: 0 0 30px #ff0000;">YENİ BOYUTTA DOĞ 🔄</button>';
                    }
                });
            }
            renderer.render(scene, camera); requestAnimationFrame(animate);
        }
        animate();
    </script>
    """
    components.html(bmw_10d_html, height=800)

# ==========================================================================================
# ASTRO-AURA SPACE ESCAPE: EKSİKSİZ KORUNDU
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
        container.appendChild(renderer.domElement);

        const neonLight = new THREE.PointLight(0xff00bb, 8, 250); neonLight.position.set(0, 15, -20); scene.add(neonLight);
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
        scene.add(createStars(800, 0xffffff, 0.18), createStars(500, 0xff00bb, 0.32));

        const playerJet = new THREE.Group();
        const chromePink = new THREE.MeshStandardMaterial({ color: 0xff0066, metalness: 0.95, roughness: 0.02 });
        const core = new THREE.Mesh(new THREE.CylinderGeometry(0.12, 0.48, 2.8, 12), chromePink); core.rotation.x = Math.PI / 2;
        const cockpit = new THREE.Mesh(new THREE.SphereGeometry(0.3, 24, 24), new THREE.MeshStandardMaterial({ color: 0x00faff }));
        cockpit.position.set(0, 0.22, -0.5); cockpit.scale.set(1, 1, 2.0);
        const leftWing = new THREE.Mesh(new THREE.BoxGeometry(2.0, 0.05, 0.9), chromePink); leftWing.position.set(-1.1, -0.05, 0.4);
        const rightWing = leftWing.clone(); rightWing.position.x = 1.1;
        playerJet.add(core, cockpit, leftWing, rightWing);

        playerJet.position.set(0, 0, -6); scene.add(playerJet);

        let obstacles = []; const oColors = [0xff0066, 0xb300ff, 0xff4400];
        for(let i=0; i<5; i++){
            let oMesh = new THREE.Mesh(new THREE.IcosahedronGeometry(1.4, 1), new THREE.MeshStandardMaterial({ color: oColors[i % 3], roughness: 0.3, flatShading: true }));
            oMesh.position.set((Math.random() - 0.5) * 14, (Math.random() - 0.5) * 4, -60 - (i * 35)); 
            scene.add(oMesh); obstacles.push(oMesh);
        }

        camera.position.set(0, 4.2, 4.5); camera.lookAt(new THREE.Vector3(0, -0.2, -25));
        let score = 0; let gameOver = false; let keys = {}; let jetRot = 0;
        window.addEventListener("keydown", e => keys[e.key] = true); window.addEventListener("keyup", e => keys[e.key] = false);

        let touchLeft = false, touchRight = false;
        const bLeft = document.getElementById("btnLeftKiz"); const bRight = document.getElementById("btnRightKiz");
        bLeft.addEventListener("mousedown", () => touchLeft = true); bLeft.addEventListener("mouseup", () => touchLeft = false);
        bRight.addEventListener("mousedown", () => touchRight = true); bRight.addEventListener("mouseup", () => touchRight = false);

        function animate() {
            if(!gameOver) {
                let speed = 1.1 + (score * 0.04);
                if(keys["ArrowLeft"] || keys["a"] || keys["A"] || touchLeft) { if(playerJet.position.x > -7.5) playerJet.position.x -= 0.24; jetRot = 0.42; }
                else if(keys["ArrowRight"] || keys["d"] || keys["D"] || touchRight) { if(playerJet.position.x < 7.5) playerJet.position.x += 0.24; jetRot = -0.42; }
                else { jetRot *= 0.80; }
                playerJet.rotation.z = jetRot;
                nebula.rotation.y += 0.0015;

                obstacles.forEach(o => {
                    o.position.z += speed; o.rotation.x += 0.02;
                    if(o.position.z > 5) { o.position.z = -160 - Math.random()*50; o.position.x = (Math.random() - 0.5) * 14; score++; document.getElementById("kizScoreDisplay").innerText = "Aura Enerjisi: " + score + " ⭐"; }
                    if(Math.abs(playerJet.position.x - o.position.x) < 1.45 && Math.abs(playerJet.position.z - o.position.z) < 2.2) {
                        gameOver = true;
                        document.getElementById("kizScoreDisplay").innerHTML = "<span style='color:#ff00bb; font-size:30px; font-weight:900;'>🔮 AURANIZ SIFIRLANDI! 🔮</span>";
                        document.getElementById("restartButtonContainerKiz").innerHTML = '<button onclick="location.reload()" style="margin-top:15px; padding:18px 50px; font-size:22px; background:linear-gradient(90deg, #ff00bb, #330022); color:#fff; border:none; border-radius:12px; cursor:pointer;">KOZMİK BAĞLANTIYI YENİLE 🔄</button>';
                    }
                });
            }
            renderer.render(scene, camera); requestAnimationFrame(animate);
        }
        animate();
    </script>
    """
    components.html(kiz_ultra_real_html, height=800)
