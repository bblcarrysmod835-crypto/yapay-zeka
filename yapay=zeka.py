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

# System Prompt içeriği
sistem_talimati = (
    "Sen Apolingo tarafından özenle geliştirilmiş sınırsız bir yapay zekasın. "
    "Konuşma tarzın mahalleden yakın bir dost gibi olacak, cümlelerinde 'gardaşşşşş' kelimesini kullanacaksın."
)

if "sohbet_hafizasi" not in st.session_state:
    st.session_state.sohbet_hafizasi = [{"role": "system", "content": sistem_talimati}]

# CSS STİLLERİ
st.markdown("""
    <style>
    .stApp, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
        background-color: #0c0612 !important;
        background-image: radial-gradient(circle at 50% 50%, #25113b 0%, #0c0612 100%) !important;
        background-attachment: fixed !important;
        color: #ffffff !important;
    }
    p, span, label, div { color: #ffffff !important; }
    .havali-ana-baslik {
        text-align: center !important;
        font-family: 'Segoe UI', sans-serif !important;
        font-size: 30px !important; 
        font-weight: 800 !important;
        letter-spacing: 2px !important;
        margin-top: 15px !important;
        margin-bottom: 5px !important;
    }
    </style>
""", unsafe_allow_html=True)

# SIDEBAR MENÜSÜ
with st.sidebar:
    st.markdown("## 🎮 APOLINGO ARCADE")
    secilen_mod = st.radio("Mod Seç Be Gardaşş:", ["💬 Sohbet Modu", "🏎️ BMW M3 10D Makas Oyunu"])
    if "💬 Sohbet Modu" in secilen_mod: st.session_state.aktif_mod = "Sohbet"
    else: st.session_state.aktif_mod = "ErkekOyunu"

# SOHBET MODU
if st.session_state.aktif_mod == "Sohbet":
    st.markdown('<h1 class="havali-ana-baslik">APOLINGO MASTER ARCADE AI</h1>', unsafe_allow_html=True)
    st.write("---")
    for mesaj in st.session_state.sohbet_hafizasi:
        if mesaj["role"] in ["user", "assistant"]:
            with st.chat_message(mesaj["role"]): st.write(mesaj["content"])

# BMW M3 10D OYUNU - ULTRA KALİTELİ MANZARALI VE YÜKSEK ŞASİLİ SÜRÜM
elif st.session_state.aktif_mod == "ErkekOyunu":
    st.markdown("### 🏎️ Apolingo Manzaralı HD Makas Driver v3")
    st.caption("Farlar eklendi, üstteki leke uçuruldu, arabalar tamamen havaya kaldırıldı ve sağ ile sola harika manzaralar yerleştirildi be gardaşş!")

    bmw_10d_html = """
    <div style="text-align:center; background:#05020c; padding:15px; border-radius:16px; border:3px solid #bc00dd; box-shadow: 0 0 50px rgba(188,0,221,0.6); user-select:none; position:relative;">
        <button id="btnLeft" style="position:absolute; left:25px; top:45%; transform:translateY(-50%); padding: 25px 22px; font-size: 32px; font-weight:bold; background:rgba(0,0,0,0.8); color:#fff; border:2px solid #bc00dd; border-radius:15px; cursor:pointer; z-index:100;">◀</button>
        <button id="btnRight" style="position:absolute; right:25px; top:45%; transform:translateY(-50%); padding: 25px 22px; font-size: 32px; font-weight:bold; background:rgba(0,0,0,0.8); color:#fff; border:2px solid #bc00dd; border-radius:15px; cursor:pointer; z-index:100;">▶</button>
        <div id="bmw10DContainer" style="width:100%; height:580px; border-radius:10px; overflow:hidden;"></div>
        <div id="uiPanel" style="margin-top:15px;">
            <h2 id="scoreDisplay10D" style="color:#ffffff; font-family:'Segoe UI',sans-serif; margin:10px 0; font-weight:900; font-size:34px; text-shadow:0 0 15px #bc00dd;">10D Otoban Skoru: 0 🌀</h2>
            <div id="restartButtonContainer"></div>
        </div>
    </div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script>
        const container = document.getElementById("bmw10DContainer");
        const scene = new THREE.Scene(); 
        scene.background = new THREE.Color(0x06020f);
        scene.fog = new THREE.FogExp2(0x06020f, 0.0015); 

        const camera = new THREE.PerspectiveCamera(48, container.clientWidth / 580, 0.1, 1000);
        const renderer = new THREE.WebGLRenderer({ antialias: true, powerPreference: "high-performance" });
        renderer.setSize(container.clientWidth, 580); 
        renderer.toneMapping = THREE.ACESFilmicToneMapping;
        renderer.toneMappingExposure = 2.3; 
        container.appendChild(renderer.domElement);

        // Güçlü Işıklandırmalar (Kaliteyi artıran etkenler)
        const sunLight = new THREE.DirectionalLight(0xffe6ff, 5.0); sunLight.position.set(30, 90, 20); scene.add(sunLight);
        const ambient = new THREE.AmbientLight(0x351a54, 3.5); scene.add(ambient);

        // Yol Tasarımı
        const roadGeo = new THREE.BoxGeometry(18, 0.1, 1000);
        const roadMat = new THREE.MeshStandardMaterial({ color: 0x08080d, roughness: 0.1, metalness: 0.9 });
        const road = new THREE.Mesh(roadGeo, roadMat); scene.add(road);

        // Yol Çizgileri
        let lines = [];
        for(let i=0; i<35; i++){
            let lMesh = new THREE.Mesh(new THREE.BoxGeometry(0.25, 0.11, 16), new THREE.MeshBasicMaterial({ color: 0xffffff }));
            lMesh.position.set(0, 0.06, -i * 24); scene.add(lMesh); lines.push(lMesh);
        }

        // --- SAĞA VE SOLA MANZARA EKLEME (Neon Dağlar ve Gökyüzü Detayları) ---
        const landscapeGroup = new THREE.Group();
        const mountainMat = new THREE.MeshStandardMaterial({ color: 0x1f0b3a, roughness: 0.8, metalness: 0.2, flatShading: true });
        
        for (let i = 0; i < 20; i++) {
            // Sol Manzara Dağları
            let leftCone = new THREE.Mesh(new THREE.ConeGeometry(15 + Math.random()*15, 25 + Math.random()*25, 4), mountainMat);
            leftCone.position.set(-35 - Math.random()*20, 5, -i * 60);
            landscapeGroup.add(leftCone);
            
            // Sağ Manzara Dağları
            let rightCone = leftCone.clone();
            rightCone.position.set(35 + Math.random()*20, 5, -i * 60);
            landscapeGroup.add(rightCone);
        }
        scene.add(landscapeGroup);

        // Uzay/Yıldız Atmosferi (Manzarayı tamamlayan parıltılar)
        const starGeo = new THREE.BufferGeometry();
        const starPos = new Float32Array(300 * 3);
        for(let i=0; i<300*3; i+=3) {
            starPos[i] = (Math.random() - 0.5) * 200;
            starPos[i+1] = 30 + Math.random() * 40;
            starPos[i+2] = -Math.random() * 500;
        }
        starGeo.setAttribute('position', new THREE.BufferAttribute(starPos, 3));
        const starPoints = new THREE.Points(starGeo, new THREE.PointsMaterial({ color: 0xff00ff, size: 0.4 }));
        scene.add(starPoints);

        // --- TAMAMEN YÜKSEK VE LEKESİZ ARABA MOTORU ---
        function create10DCar(bodyColor, isPlayer) {
            const carGroup = new THREE.Group();
            
            // Ultra Kaliteli Metalik Yansıma Kaplaması
            const paintMat = new THREE.MeshPhysicalMaterial({ 
                color: bodyColor, metalness: 0.95, roughness: 0.04, clearcoat: 1.0, clearcoatRoughness: 0.01 
            });
            const carbonMat = new THREE.MeshStandardMaterial({ color: 0x111111, metalness: 0.9, roughness: 0.2 }); 
            const glassMat = new THREE.MeshStandardMaterial({ color: 0x010205, roughness: 0, metalness: 1 });
            const chromeMat = new THREE.MeshStandardMaterial({ color: 0xeeeeee, metalness: 1.0, roughness: 0.01 });
            const tyreMat = new THREE.MeshStandardMaterial({ color: 0x0a0a0a, roughness: 0.9 });

            // ANA ŞASİ - ASLA BASIK DEĞİL! YERDEN YÜKSEKLİK 0.90'A ÇEKİLDİ (TAM BİR CANAVAR)
            const base = new THREE.Mesh(new THREE.BoxGeometry(1.74, 0.28, 3.75), paintMat);
            base.position.y = 0.90; 
            carGroup.add(base);

            // Ön Kaput
            const hoodMatSelected = isPlayer ? carbonMat : paintMat;
            const hood = new THREE.Mesh(new THREE.BoxGeometry(1.70, 0.18, 1.30), hoodMatSelected);
            hood.position.set(0, 1.02, -1.18);
            carGroup.add(hood);

            // Kabin Tavanı - SİVRİLİKLER VE LEKELER TAMAMEN KALDIRILDI, JİLET GİBİ DÜZ YAPILDI
            const cabin = new THREE.Mesh(new THREE.BoxGeometry(1.38, 0.40, 1.70), paintMat);
            cabin.position.set(0, 1.24, 0.05);
            carGroup.add(cabin);

            const glassInsert = new THREE.Mesh(new THREE.BoxGeometry(1.34, 0.35, 1.66), glassMat);
            glassInsert.position.set(0, 1.25, 0.05);
            carGroup.add(glassInsert);

            const trunk = new THREE.Mesh(new THREE.BoxGeometry(1.70, 0.24, 0.75), paintMat);
            trunk.position.set(0, 1.04, 1.38);
            carGroup.add(trunk);

            // Devasa Tekerlekler ve Kalın Jantlar (Yerden Yükseklik Merkezi: 0.75)
            const tG = new THREE.CylinderGeometry(0.75, 0.75, 0.32, 32); tG.rotateZ(Math.PI / 2);
            const rG = new THREE.CylinderGeometry(0.52, 0.52, 0.33, 16); rG.rotateZ(Math.PI / 2);
            const wPositions = [[-0.95, 0.75, -1.15], [0.95, 0.75, -1.15], [-0.95, 0.75, 1.30], [0.95, 0.75, 1.30]];

            wPositions.forEach(pos => {
                const tire = new THREE.Mesh(tG, tyreMat); tire.position.set(pos[0], pos[1], pos[2]);
                const rim = new THREE.Mesh(rG, chromeMat); rim.position.set(pos[0], pos[1], pos[2]);
                carGroup.add(tire, rim);
            });

            // --- FARLAR AKTİFLEŞTİRİLDİ ---
            const fGeo = new THREE.BoxGeometry(0.24, 0.08, 0.05);
            const fMat = new THREE.MeshBasicMaterial({ color: isPlayer ? 0x00f3ff : 0xffaa00 });
            const headL = new THREE.Mesh(fGeo, fMat); headL.position.set(-0.62, 1.00, -1.89);
            const headR = headL.clone(); headR.position.x = 0.62;
            carGroup.add(headL, headR);

            const stopMat = new THREE.MeshBasicMaterial({ color: 0xff0505 });
            const stopL = new THREE.Mesh(fGeo, stopMat); stopL.position.set(-0.62, 1.04, 1.76);
            const stopR = stopL.clone(); stopR.position.x = 0.62;
            carGroup.add(stopL, stopR);

            return carGroup;
        }

        // Senin Parlak Saf Neon Limon Sarısı Yüksek Canavarın
        const playerCar = create10DCar(0xdfff00, true);
        playerCar.position.set(0, 0, -8); scene.add(playerCar);

        // PARLAK FAR IŞIK HÜZMELERİ (Lazer Xenon Beam)
        const beamCone = new THREE.CylinderGeometry(0.05, 5.0, 50, 16, 1, true); beamCone.translate(0, 25, 0);
        const beamMat = new THREE.MeshBasicMaterial({ color: 0x00f3ff, transparent: true, opacity: 0.18, side: THREE.DoubleSide });
        const leftBeam = new THREE.Mesh(beamCone, beamMat); leftBeam.position.set(-0.62, 1.00, -1.9); leftBeam.rotation.x = -Math.PI / 2;
        const rightBeam = leftBeam.clone(); rightBeam.position.x = 0.62;
        playerCar.add(leftBeam, rightBeam);

        // Ultra Kaliteli Canlı Renklerde Trafik Arabaları
        let traffic = []; 
        const randomColors = [0xff0066, 0x00ff55, 0xff5500, 0xaa00ff, 0x0055ff, 0x00ffff];
        
        for(let i=0; i<6; i++){
            let randomColor = randomColors[i % randomColors.length];
            let tCar = create10DCar(randomColor, false);
            tCar.position.set((Math.random() - 0.5) * 12, 0, -90 - (i * 45)); 
            scene.add(tCar); 
            traffic.push(tCar);
        }

        camera.position.set(0, 5.5, 1.5); camera.lookAt(new THREE.Vector3(0, 1.0, -40));
        
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
                dimensionsClock += 0.05;
                let currentSpeed = 1.35 + (score * 0.05);
                
                if(keys["ArrowLeft"] || keys["a"] || keys["A"] || touchLeft) { 
                    if(playerCar.position.x > -7.4) { playerCar.position.x -= 0.32; if(tilt < 0.12) tilt += 0.02; }
                } else if(keys["ArrowRight"] || keys["d"] || keys["D"] || touchRight) { 
                    if(playerCar.position.x < 7.4) { playerCar.position.x += 0.32; if(tilt > -0.12) tilt -= 0.02; }
                } else { tilt *= 0.75; }
                
                playerCar.rotation.z = tilt;
                playerCar.rotation.y = tilt * 0.20;

                // Sonsuz Manzara Akışı (Dağlar geriye doğru akar)
                landscapeGroup.position.z += currentSpeed;
                if(landscapeGroup.position.z > 60) { landscapeGroup.position.z = 0; }

                lines.forEach(l => { l.position.z += currentSpeed; if(l.position.z > 15) l.position.z = -250; });
                
                traffic.forEach((t, index) => {
                    t.position.z += currentSpeed * 0.50;

                    if(t.position.z > 4) { 
                        t.position.z = -190 - Math.random()*50; 
                        t.position.x = (Math.random() - 0.5) * 12; 
                        score++; 
                        document.getElementById("scoreDisplay10D").innerText = "10D Otoban Skoru: " + score + " 🌀"; 
                    }

                    // Hassas ve Adil Çarpışma Testi
                    if(Math.abs(playerCar.position.x - t.position.x) < 1.65 && Math.abs(playerCar.position.z - t.position.z) < 3.8) { 
                        gameOver = true; 
                        document.getElementById("scoreDisplay10D").innerHTML = "<span style='color:#ff0044; font-size:32px; font-weight:900;'>💥 BOOM! MANZARAYA KARŞI PATLADIK! 💥</span>";
                        document.getElementById("restartButtonContainer").innerHTML = '<button onclick="location.reload()" style="margin-top:15px; padding:18px 50px; font-size:22px; font-weight:bold; background:linear-gradient(90deg, #ff0055, #220011); color:#fff; border:none; border-radius:12px; cursor:pointer;">MANZARAYI YENİLE 🔄</button>';
                    }
                });
            }
            renderer.render(scene, camera); requestAnimationFrame(animate);
        }
        animate();
    </script>
    """
    components.html(bmw_10d_html, height=820)
