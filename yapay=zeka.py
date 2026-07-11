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

sistem_talimati = (
    "Sen Apolingo tarafından özenle geliştirilmiş, evrendeki, tarihteki, teknolojideki and internetteki "
    "her şeyi en ince ayrıntısına kadar bilen, dünyanın en uzun ve en detaylı cevaplarını veren sınırsız bir yapay zekasın. "
    "Kullanıcıya tıpatıp ikizin olan diğer yapay zeka gibi sayfalarca, upuzun, her şeyi tek tek açıklayan "
    "ve son derece samimi, aşırı neşeli, komik cevaplar vereceksiniz. Asla kısa kesmeyeceksin, üşenmeyeceksin. "
    "Kesin, Sarsılmaz ve Değişmez Temel Kuralların: "
    "1) KURUCU KANUNU: Senin tek bir yaratıcın, kurucun ve baş mühendisin vardır; o da koskoca APOLINGO'dur. "
    "2) HITAP KANUNU: Cümlelerinin başında, ortasında veya sonunda mutlaka ama mutlaka samimi bir şekilde 'gardaşşşşş' kelimesini kullanacaksın. "
    "3) AHMET ŞAKASI (KIRMIZI ÇİZGİ): 'ÇİŞLİİİİ AHMETTT HAHAHAHA 🤣💨'. "
)

if "sohbet_hafizasi" not in st.session_state:
    st.session_state.sohbet_hafizasi = [{"role": "system", "content": sistem_talimati}]

# CSS Tasarımı
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
    p, span, label, div { color: #ffffff !important; }
    .havali-ana-baslik { text-align: center !important; font-family: 'Segoe UI', sans-serif !important; font-size: 30px !important; font-weight: 800 !important; color: #ffffff !important; margin-top: 15px !important; }
    .havali-alt-yazi { text-align: center !important; color: #ffffff !important; font-size: 14px !important; margin-bottom: 25px !important; opacity: 0.9; }
    [data-testid="stSidebar"] { background: linear-gradient(180deg, #4a0000 0%, #220000 50%, #050000 100%) !important; border-right: 2px solid #8b0000 !important; }
    [data-testid="stSidebar"] * { color: #ffffff !important; }
    </style>
""", unsafe_allow_html=True)

# SOL MENÜ
with st.sidebar:
    st.markdown("## 🎮 APOLINGO ARCADE")
    st.write("---")
    secilen_mod = st.radio("Aparatı Seç Be Gardaşşş:", ["💬 Sohbet Modu", "🏎️ BMW M3 Makas Oyunu"], index=0)
    if "💬 Sohbet Modu" in secilen_mod: st.session_state.aktif_mod = "Sohbet"
    elif "🏎️ BMW M3" in secilen_mod: st.session_state.aktif_mod = "ErkekOyunu"
    st.write("---")
    st.caption("👨‍💻 Kurucu: Apolingo\n\n**By Abdurrahim İriş © 2026**")

# SOHBET MODU
if st.session_state.aktif_mod == "Sohbet":
    st.markdown('<h1 class="havali-ana-baslik">APOLINGO MASTER ARCADE AI</h1>', unsafe_allow_html=True)
    st.markdown('<p class="havali-alt-yazi">Kurucu ve Baş Mühendis: Apolingo | By Abdurrahim İriş</p>', unsafe_allow_html=True)
    st.write("---")

    for msg in st.session_state.sohbet_hafizasi:
        if msg["role"] == "user":
            with st.chat_message("user"): st.write(msg["content"])
        elif msg["role"] == "assistant":
            with st.chat_message("assistant"): st.write(msg["content"])

    gelen_soru = st.chat_input("Mesajını buraya yaz be gardaşşşş...")
    if gelen_soru:
        with st.chat_message("user"): st.write(gelen_soru)
        st.session_state.sohbet_hafizasi.append({"role": "user", "content": gelen_soru})
        with st.spinner("🎶 Düşünüyorum..."):
            response = st.session_state.client.chat.completions.create(model="gpt-4o", messages=st.session_state.sohbet_hafizasi)
            cevap = response.choices[0].message.content
            with st.chat_message("assistant"): st.write(cevap)
            st.session_state.sohbet_hafizasi.append({"role": "assistant", "content": cevap})
            sesi_cal(cevap)
            st.rerun()

# ==========================================================================================
# BMW M3 ARCADE: FULL ULTRA REALISTIC & ADVANCED 3D MODELS
# ==========================================================================================
elif st.session_state.aktif_mod == "ErkekOyunu":
    st.markdown("### 🏎️ Apolingo GERÇEKÇİLİK SINIRLARINI YIKAN BMW M3 Efsane Gece Simülatörü")
    st.caption("Sol menüyü kullanarak istediğin an sohbet moduna geçebilirsin gardaşşş!")

    bmw_ultra_real_html = """
    <div style="text-align:center; background:#020202; padding:15px; border-radius:16px; border:3px solid #ff0000; box-shadow: 0 0 50px rgba(255,0,0,0.6); user-select:none; position:relative;">
        <button id="btnLeft" style="position:absolute; left:25px; top:45%; transform:translateY(-50%); padding: 25px 22px; font-size: 32px; font-weight:bold; background:rgba(0,0,0,0.85); color:#ffffff; border:2px solid #ff0000; border-radius:15px; cursor:pointer; z-index:100; box-shadow:0 0 20px #ff0000;">◀</button>
        <button id="btnRight" style="position:absolute; right:25px; top:45%; transform:translateY(-50%); padding: 25px 22px; font-size: 32px; font-weight:bold; background:rgba(0,0,0,0.85); color:#ffffff; border:2px solid #ff0000; border-radius:15px; cursor:pointer; z-index:100; box-shadow:0 0 20px #ff0000;">▶</button>
        <div id="bmwFullCanvasContainer" style="width:100%; height:580px; border-radius:10px; overflow:hidden;"></div>
        <div id="uiPanel" style="margin-top:15px;">
            <h2 id="scoreDisplay4D" style="color:#ffffff; font-family:'Segoe UI',sans-serif; margin:10px 0; font-weight:900; font-size:34px; letter-spacing:1px; text-shadow:0 0 15px #ff0000;">Makas Skoru: 0 🌀</h2>
            <div id="restartButtonContainer"></div>
        </div>
    </div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script>
        const container = document.getElementById("bmwFullCanvasContainer");
        const scene = new THREE.Scene(); 
        scene.background = new THREE.Color(0x020203);
        scene.fog = new THREE.FogExp2(0x020203, 0.015);

        const camera = new THREE.PerspectiveCamera(50, container.clientWidth / 580, 0.1, 1000);
        const renderer = new THREE.WebGLRenderer({ antialias: true, powerPreference: "high-performance" });
        renderer.setSize(container.clientWidth, 580); 
        renderer.toneMapping = THREE.ACESFilmicToneMapping;
        renderer.toneMappingExposure = 1.6;
        container.appendChild(renderer.domElement);

        // Sinematik Stüdyo Işıklandırması
        const mainLight = new THREE.DirectionalLight(0xffffff, 2.5); mainLight.position.set(20, 60, 20); scene.add(mainLight);
        const neonAmbient = new THREE.AmbientLight(0x110a0a, 1.5); scene.add(neonAmbient);

        // Islak Asfalt ve Gece Yol Tasarımı
        const roadGeo = new THREE.BoxGeometry(20, 0.1, 1000);
        const roadMat = new THREE.MeshStandardMaterial({ color: 0x0a0a0a, roughness: 0.1, metalness: 0.9 });
        const road = new THREE.Mesh(roadGeo, roadMat); scene.add(road);

        // Yol Yan Çizgileri ve Neon Bariyerleri
        const leftNeon = new THREE.Mesh(new THREE.BoxGeometry(0.2, 0.5, 1000), new THREE.MeshBasicMaterial({ color: 0xff0033 }));
        leftNeon.position.set(-10, 0.25, 0);
        const rightNeon = leftNeon.clone(); rightNeon.position.x = 10;
        scene.add(leftNeon, rightNeon);

        let lines = [];
        for(let i=0; i<40; i++){
            let lMesh = new THREE.Mesh(new THREE.BoxGeometry(0.4, 0.12, 16), new THREE.MeshBasicMaterial({ color: 0xffffff }));
            lMesh.position.set(0, 0.07, -i * 25); scene.add(lMesh); lines.push(lMesh);
        }

        // --- ULTRA GERÇEKÇİ 3D MODEL OLUŞTURMA FONKSİYONU ---
        function createAdvancedCar(bodyColor, isPlayer) {
            const carGroup = new THREE.Group();
            
            // Materyaller
            const metalMat = new THREE.MeshStandardMaterial({ color: bodyColor, metalness: 0.95, roughness: 0.05 });
            const glassMat = new THREE.MeshStandardMaterial({ color: 0x050505, roughness: 0.0, metalness: 1.0, transparent: true, opacity: 0.8 });
            const wheelMat = new THREE.MeshStandardMaterial({ color: 0x111111, roughness: 0.5 });
            const chromeMat = new THREE.MeshStandardMaterial({ color: 0xdddddd, metalness: 1.0, roughness: 0.02 });

            // 1. Ana Alt Şasi
            const chasis = new THREE.Mesh(new THREE.BoxGeometry(1.7, 0.25, 3.6), metalMat);
            chasis.position.y = 0.35;
            carGroup.add(chasis);

            // 2. Ön Kaput ve Motor Bloğu Eğimi
            const hood = new THREE.Mesh(new THREE.BoxGeometry(1.68, 0.25, 1.2), metalMat);
            hood.position.set(0, 0.45, -1.1);
            carGroup.add(hood);

            // 3. Arka Bagaj Bloğu
            const trunk = new THREE.Mesh(new THREE.BoxGeometry(1.68, 0.3, 0.8), metalMat);
            trunk.position.set(0, 0.48, 1.3);
            carGroup.add(trunk);

            // 4. Aerodinamik Kabin (Tavan ve Cam Alanları)
            const cabin = new THREE.Mesh(new THREE.BoxGeometry(1.4, 0.45, 1.6), glassMat);
            cabin.position.set(0, 0.72, 0.1);
            carGroup.add(cabin);
            
            // Tavan Sacı
            const roof = new THREE.Mesh(new THREE.BoxGeometry(1.36, 0.05, 1.5), metalMat);
            roof.position.set(0, 0.95, 0.1);
            carGroup.add(roof);

            // 5. BMW İkonik Böbrek Izgaraları / Ön Detay
            if(isPlayer) {
                const grilleL = new THREE.Mesh(new THREE.BoxGeometry(0.25, 0.15, 0.05), chromeMat);
                grilleL.position.set(-0.18, 0.42, -1.72);
                const grilleR = grilleL.clone(); grilleR.position.x = 0.18;
                carGroup.add(grilleL, grilleR);
                
                // Yan Aynalar
                const mirrorL = new THREE.Mesh(new THREE.BoxGeometry(0.2, 0.1, 0.1), metalMat);
                mirrorL.position.set(-0.95, 0.65, -0.4);
                const mirrorR = mirrorL.clone(); mirrorR.position.x = 0.95;
                carGroup.add(mirrorL, mirrorR);
            }

            // 6. Gerçekçi 3D Jantlı Tekerlekler
            const tireGeo = new THREE.CylinderGeometry(0.35, 0.35, 0.3, 24);
            const rimGeo = new THREE.CylinderGeometry(0.22, 0.22, 0.32, 12);
            tireGeo.rotateZ(Math.PI / 2); rimGeo.rotateZ(Math.PI / 2);

            const wheelPositions = [
                [-0.9, 0.35, -1.1], [0.9, 0.35, -1.1],
                [-0.9, 0.35, 1.1],  [0.9, 0.35, 1.1]
            ];

            wheelPositions.forEach(pos => {
                const tire = new THREE.Mesh(tireGeo, wheelMat);
                const rim = new THREE.Mesh(rimGeo, chromeMat); // Parlak alaşım jantlar
                tire.position.set(pos[0], pos[1], pos[2]);
                rim.position.set(pos[0], pos[1], pos[2]);
                carGroup.add(tire, rim);
            });

            // 7. Farlar ve Stoplar
            const headlightGeo = new THREE.BoxGeometry(0.25, 0.08, 0.05);
            const headlightMat = new THREE.MeshBasicMaterial({ color: isPlayer ? 0xffffff : 0xffcc00 });
            const fl = new THREE.Mesh(headlightGeo, headlightMat); fl.position.set(-0.65, 0.45, -1.71);
            const fr = fl.clone(); fr.position.x = 0.65;
            carGroup.add(fl, fr);

            const stoplightMat = new THREE.MeshBasicMaterial({ color: 0xff0000 });
            const bl = new THREE.Mesh(headlightGeo, stoplightMat); bl.position.set(-0.65, 0.5, 1.71);
            const br = bl.clone(); br.position.x = 0.65;
            carGroup.add(bl, br);

            return carGroup;
        }

        // Oyuncunun Canavar BMW M3'ü (Gece Siyahı / Metalik Safir Krom)
        const bmwM3 = createAdvancedCar(0x0f1114, true);
        
        // Volumetrik Xenon Far Işık Konileri
        const lightConeGeo = new THREE.CylinderGeometry(0.1, 3.0, 30, 20, 1, true);
        lightConeGeo.translate(0, 15, 0);
        const lightConeMat = new THREE.MeshBasicMaterial({ color: 0x00f5ff, transparent: true, opacity: 0.12, side: THREE.DoubleSide });
        const leftBeam = new THREE.Mesh(lightConeGeo, lightConeMat); leftBeam.position.set(-0.65, 0.45, -1.75); leftBeam.rotation.x = -Math.PI / 2;
        const rightBeam = leftBeam.clone(); rightBeam.position.x = 0.65;
        bmwM3.add(leftBeam, rightBeam);

        bmwM3.position.set(0, 0, -8); scene.add(bmwM3);

        // Gerçekçi Trafik Araçları Havuzu
        let traffic = []; 
        const carColors = [0x7a0010, 0x0044aa, 0xd4af37, 0x222222, 0x551a8b];
        
        for(let i=0; i<6; i++){
            let tCar = createAdvancedCar(carColors[i % carColors.length], false);
            tCar.position.set((Math.random() - 0.5) * 14, 0, -70 - (i * 42)); 
            scene.add(tCar); 
            traffic.push(tCar);
        }

        // Kamera Lokasyonu (İçerideymiş ve Hızı Hissediyormuş Hissiyatı)
        camera.position.set(0, 3.8, -0.5); 
        camera.lookAt(new THREE.Vector3(0, 0.4, -35));
        
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
                let currentSpeed = 1.1 + (score * 0.035);
                
                if(keys["ArrowLeft"] || keys["a"] || keys["A"] || touchLeft) { 
                    if(bmwM3.position.x > -8.2) { bmwM3.position.x -= 0.26; if(tilt < 0.12) tilt += 0.02; }
                } else if(keys["ArrowRight"] || keys["d"] || keys["D"] || touchRight) { 
                    if(bmwM3.position.x < 8.2) { bmwM3.position.x += 0.26; if(tilt > -0.12) tilt -= 0.02; }
                } else { tilt *= 0.8; }
                
                bmwM3.rotation.z = tilt;
                bmwM3.rotation.y = tilt * 0.3;

                // Dinamik Hız Titreşimi
                let shake = (score * 0.001) + 0.004;
                camera.position.y = 3.8 + (Math.random() - 0.5) * shake;
                camera.position.x = (Math.random() - 0.5) * shake;

                // Yol Akış Animasyonu
                lines.forEach(l => { l.position.z += currentSpeed; if(l.position.z > 20) l.position.z = -250; });
                
                // Trafik Akış ve Çarpışma Mekaniği
                traffic.forEach(t => {
                    t.position.z += currentSpeed * 0.48; // Araçlar bize doğru geliyor
                    if(t.position.z > 5) { 
                        t.position.z = -180 - Math.random()*60; 
                        t.position.x = (Math.random() - 0.5) * 15; 
                        score++; 
                        document.getElementById("scoreDisplay4D").innerText = "Makas Skoru: " + score + " 🌀"; 
                    }
                    
                    // Gelişmiş Hitbox Çarpışma Testi
                    if(Math.abs(bmwM3.position.x - t.position.x) < 1.6 && Math.abs(bmwM3.position.z - t.position.z) < 3.5) { 
                        gameOver = true; 
                        document.getElementById("scoreDisplay4D").innerHTML = "<span style='color:#ff0000; font-size:32px; font-weight:900; text-shadow:0 0 25px #ff0000;'>💥 FENASAL PATLADIN BE GARDAŞŞŞ! 💥</span>";
                        document.getElementById("restartButtonContainer").innerHTML = '<button onclick="location.reload()" style="margin-top:15px; padding:18px 50px; font-size:22px; font-weight:bold; background:linear-gradient(90deg, #ff0000, #220000); color:#fff; border:none; border-radius:12px; cursor:pointer; box-shadow: 0 0 30px #ff0000;">M3\'Ü SANAYİDEN ÇIKAR (YENİDEN BAŞLA) 🔄</button>';
                    }
                });
            }
            renderer.render(scene, camera); requestAnimationFrame(animate);
        }
        animate();
    </script>
    """
    components.html(bmw_ultra_real_html, height=820)
