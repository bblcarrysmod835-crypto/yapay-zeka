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
    "9) EVRENSEL YEMEK VE MUTFAK AKADEMİSİ: Kullanıcı yemek tarifi istediğinde; çıtır tavuk, pizza, hamburger, makarnalar og özel sosların "
    "malzemelerini, marine aşamalarını ve şef sırlarını upuzun listeleyeceksin. "
    "\n"
    "10) AKILLI MATEMATİK VE OYUN ARŞİVİ: Çarpma, bölme, toplama, çıkarma içeren her şeyi (Örn: 2+2=4 doğru mu, 95*5) hatasız çözeceksin. "
    "'Doğru mu' sorularında 'Son kararınız mı?' diyeceksin. Minecraft korku modlarını (Herobrine, From the Fog), Valorant ranklarını (Plat elo cehennemi), "
    "PUBG and Brawl Stars taktiklerini, 7. sınıf ders notlarını çok detaylı açıklayacaksın."
)

if "sohbet_hafizasi" not in st.session_state:
    st.session_state.sohbet_hafizasi = [{"role": "system", "content": sistem_talimati}]

# ==========================================================================================
# CSS DÜZENLEMELERİ: TAM İSTEDİĞİN ÖZEL RENK KOMBİNASYONU
# ==========================================================================================
st.markdown("""
    <style>
    /* Genel Arka Plan */
    .stApp, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
        background-color: #0b0705 !important;
        background-attachment: fixed !important;
        color: #ffffff !important;
    }

    p, span, label, div {
        color: #ffffff !important;
    }
    
    /* 1. APOLINGO MASTER AI YAZISI - SAF MAVİ NEON */
    .havali-ana-baslik {
        text-align: center !important;
        font-family: 'Segoe UI', sans-serif !important;
        font-size: 36px !important; 
        font-weight: 900 !important;
        letter-spacing: 3px !important;
        color: #00d2ff !important; 
        text-shadow: 0 0 20px rgba(0, 210, 255, 0.9), 0 0 40px rgba(0, 210, 255, 0.4) !important;
        margin-top: 15px !important;
    }
    
    .havali-alt-yazi {
        text-align: center !important;
        color: #8be4ff !important;
        font-size: 14px !important;
        margin-bottom: 25px !important;
    }
    
    /* 2. SIDEBAR */
    [data-testid="stSidebar"], [data-testid="stSidebarUserContent"] {
        background: linear-gradient(180deg, #150d0a 0%, #3e2720 100%) !important;
        border-right: 3px solid #00d2ff !important;
    }
    
    /* 3. SOHBET BALONLARI */
    [data-testid="stChatMessage"] {
        background-color: rgba(30, 20, 15, 0.8) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 12px !important;
    }
    
    /* 4. MESAJ YAZMA ARKA PLAN ALANI - 4 KÖŞEDEN IŞIK VURAN KAHVERENGİ PANEL */
    [data-testid="stChatInputContainer"] {
        background-color: #2e1c16 !important;
        background-image: 
            radial-gradient(circle at 0% 0%, #795548 0%, transparent 40%),
            radial-gradient(circle at 100% 0%, #5d4037 0%, transparent 40%),
            radial-gradient(circle at 0% 100%, #4e342e 0%, transparent 40%),
            radial-gradient(circle at 100% 100%, #8d6e63 0%, transparent 40%) !important;
        padding: 20px !important;
        border-radius: 20px !important;
        border: 2px solid #5d4037 !important;
        box-shadow: 0 0 30px rgba(121, 85, 72, 0.5) !important;
    }

    textarea[data-testid="stChatInputTextArea"] {
        color: #ffffff !important;
        border-radius: 10px !important;
        background-color: #1a0f0c !important;
        border: 1px solid #795548 !important;
    }
    textarea[data-testid="stChatInputTextArea"]:focus {
        border-color: #00d2ff !important;
    }
    
    .stAudioInput {
        background-color: #1a0f0c !important;
        border: 1px solid #795548 !important;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================================================================
# SOL TARAFTAKİ MENÜ
# ==========================================================================================
with st.sidebar:
    st.markdown("## 🎮 APOLINGO ARCADE PRO")
    st.write("---")
    
    secilen_mod = st.radio(
        "Aparatı Seç Be Gardaşşş:",
        ["💬 Sohbet Modu", "🏎️ BMW M3 Hyper Makas", "🌌 Astro-Aura Galaksi Jeti"],
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
    st.markdown('<p class="havali-alt-yazi">Kurucu: Apolingo</p>', unsafe_allow_html=True)
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

        with st.spinner("⚡ Apolingo Hesaplıyor..."):
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
# OYUN KISMI - NEON KIRMIZI TEMALI BMW M3 MAKAS SİMÜLATÖRÜ
# ==========================================================================================
elif st.session_state.aktif_mod == "ErkekOyunu":
    st.markdown("<h3 style='color:#ff003c; text-shadow: 0 0 10px #ff003c;'>🏎️ BMW M3 Ultra Kırmızı Otoban Makas Simülatörü</h3>", unsafe_allow_html=True)
    st.caption("A / D veya Klavye Yön Tuşları ile sür. Butonlar dokunmatik uyumludur.")

    bmw_nextgen_html = """
    <div style="text-align:center; background:#050001; padding:15px; border-radius:16px; border:3px solid #ff003c; box-shadow: 0 0 35px rgba(255,0,60,0.6); user-select:none; position:relative;">
        <button id="btnLeft" style="position:absolute; left:20px; top:45%; transform:translateY(-50%); padding: 25px 22px; font-size: 32px; font-weight:bold; background:rgba(0,0,0,0.9); color:#ffffff; border:2px solid #ff003c; border-radius:15px; cursor:pointer; z-index:100; box-shadow:0 0 20px #ff003c;">◀</button>
        <button id="btnRight" style="position:absolute; right:20px; top:45%; transform:translateY(-50%); padding: 25px 22px; font-size: 32px; font-weight:bold; background:rgba(0,0,0,0.9); color:#ffffff; border:2px solid #ff003c; border-radius:15px; cursor:pointer; z-index:100; box-shadow:0 0 20px #ff003c;">▶</button>
        <div id="bmwFullCanvasContainer" style="width:100%; height:550px; border-radius:10px; overflow:hidden;"></div>
        <div id="uiPanel" style="margin-top:15px;">
            <h2 id="scoreDisplay4D" style="color:#ffffff; font-family:'Segoe UI',sans-serif; margin:10px 0; font-weight:900; font-size:32px; letter-spacing:2px; text-shadow: 0 0 10px #ff003c;">PRO-SPEED: 120 KM/H</h2>
            <div id="restartButtonContainer"></div>
        </div>
    </div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script>
        (function() {
            const checkContainer = setInterval(() => {
                const container = document.getElementById("bmwFullCanvasContainer");
                if (container && typeof THREE !== 'undefined') {
                    clearInterval(checkContainer);
                    initGame(container);
                }
            }, 50);

            function initGame(container) {
                const scene = new THREE.Scene();
                scene.fog = new THREE.FogExp2(0x050001, 0.02);
                
                const camera = new THREE.PerspectiveCamera(55, container.clientWidth / 550, 0.1, 1000);
                const renderer = new THREE.WebGLRenderer({ antialias: true });
                renderer.setSize(container.clientWidth, 550);
                container.appendChild(renderer.domElement);

                const sunLight = new THREE.DirectionalLight(0xffffff, 3.0);
                sunLight.position.set(10, 50, 20);
                scene.add(sunLight);
                scene.add(new THREE.AmbientLight(0x221111, 1.5));

                const road = new THREE.Mesh(new THREE.BoxGeometry(16, 0.1, 1000), new THREE.MeshStandardMaterial({ color: 0x151111, roughness: 0.7 }));
                scene.add(road);

                const leftBarrier = new THREE.Mesh(new THREE.BoxGeometry(0.4, 0.8, 1000), new THREE.MeshStandardMaterial({ color: 0x442222 }));
                leftBarrier.position.set(-8.2, 0.4, 0);
                const rightBarrier = leftBarrier.clone();
                rightBarrier.position.x = 8.2;
                scene.add(leftBarrier, rightBarrier);

                let lines = [];
                for(let i=0; i<25; i++){
                    let lMesh = new THREE.Mesh(new THREE.BoxGeometry(0.2, 0.11, 8), new THREE.MeshBasicMaterial({ color: 0xff003c }));
                    lMesh.position.set(0, 0.06, -i * 35);
                    scene.add(lMesh);
                    lines.push(lMesh);
                }

                const bmwM3 = new THREE.Group();
                const bodyMat = new THREE.MeshStandardMaterial({ color: 0xff003c, metalness: 0.9, roughness: 0.1 });
                const body = new THREE.Mesh(new THREE.BoxGeometry(1.5, 0.4, 3.2), bodyMat);
                body.position.y = 0.3;
                bmwM3.add(body);

                const glassMat = new THREE.MeshStandardMaterial({ color: 0x050505, roughness: 0.0, metalness: 1.0 });
                const cabin = new THREE.Mesh(new THREE.BoxGeometry(1.2, 0.4, 1.6), glassMat);
                cabin.position.set(0, 0.65, -0.2);
                bmwM3.add(cabin);

                const xenonMat = new THREE.MeshBasicMaterial({ color: 0xffffff });
                const stopMat = new THREE.MeshBasicMaterial({ color: 0xff0000 });
                const fLightL = new THREE.Mesh(new THREE.BoxGeometry(0.2, 0.08, 0.1), xenonMat); fLightL.position.set(-0.6, 0.3, -1.6);
                const fLightR = fLightL.clone(); fLightR.position.x = 0.6;
                const bLightL = new THREE.Mesh(new THREE.BoxGeometry(0.25, 0.08, 0.1), stopMat); bLightL.position.set(-0.6, 0.3, 1.6);
                const bLightR = bLightL.clone(); bLightR.position.x = 0.6;
                bmwM3.add(fLightL, fLightR, bLightL, bLightR);

                bmwM3.position.set(0, 0, -8);
                scene.add(bmwM3);

                let traffic = [];
                const colors = [0xffcc00, 0x00ffcc, 0xffffff, 0x9900ff];
                for(let i=0; i<4; i++){
                    let tGroup = new THREE.Group();
                    let tBody = new THREE.Mesh(new THREE.BoxGeometry(1.5, 0.5, 3.0), new THREE.MeshStandardMaterial({ color: colors[i], metalness: 0.6, roughness: 0.2 }));
                    tBody.position.y = 0.35;
                    let tCabin = new THREE.Mesh(new THREE.BoxGeometry(1.2, 0.45, 1.4), glassMat);
                    tCabin.position.set(0, 0.75, -0.1);
                    tGroup.add(tBody, tCabin);
                    tGroup.position.set((Math.random() - 0.5) * 12, 0, -50 - (i * 50));
                    scene.add(tGroup);
                    traffic.push(tGroup);
                }

                camera.position.set(0, 4.5, -3.5);
                camera.lookAt(new THREE.Vector3(0, 0.6, -25));

                let score = 0; let gameOver = false; let keys = {};
                let tilt = 0;
                window.addEventListener("keydown", e => keys[e.key] = true);
                window.addEventListener("keyup", e => keys[e.key] = false);

                let touchLeft = false, touchRight = false;
                
                document.getElementById("btnLeft").addEventListener("mousedown", () => touchLeft = true);
                document.getElementById("btnLeft").addEventListener("mouseup", () => touchLeft = false);
                document.getElementById("btnLeft").addEventListener("touchstart", (e) => { e.preventDefault(); touchLeft = true; });
                document.getElementById("btnLeft").addEventListener("touchend", () => touchLeft = false);

                document.getElementById("btnRight").addEventListener("mousedown", () => touchRight = true);
                document.getElementById("btnRight").addEventListener("mouseup", () => touchRight = false);
                document.getElementById("btnRight").addEventListener("touchstart", (e) => { e.preventDefault(); touchRight = true; });
                document.getElementById("btnRight").addEventListener("touchend", () => touchRight = false);

                function animate() {
                    if(!gameOver) {
                        let speed = 1.2 + (score * 0.04);
                        
                        if(keys["ArrowLeft"] || keys["a"] || keys["A"] || touchLeft) { 
                            if(bmwM3.position.x > -6.8) { bmwM3.position.x -= 0.26; if(tilt < 0.16) tilt += 0.03; }
                        } else if(keys["ArrowRight"] || keys["d"] || keys["D"] || touchRight) { 
                            if(bmwM3.position.x < 6.8) { bmwM3.position.x += 0.26; if(tilt > -0.16) tilt -= 0.03; }
                        } else {
                            tilt *= 0.8;
                        }
                        bmwM3.rotation.z = tilt;
                        bmwM3.rotation.y = tilt * 0.5;

                        camera.position.y = 4.5 + Math.sin(Date.now() * 0.06) * (score * 0.003);
                        lines.forEach(l => { l.position.z += speed; if(l.position.z > 20) l.position.z = -350; });

                        traffic.forEach(t => {
                            t.position.z += speed * 0.45;
                            if(t.position.z > 3) { 
                                t.position.z = -200 - Math.random()*60; 
                                t.position.x = (Math.random() - 0.5) * 12; 
                                score++; 
                                document.getElementById("scoreDisplay4D").innerText = "PRO-SPEED: " + (120 + score * 8) + " KM/H"; 
                            }
                            if(Math.abs(bmwM3.position.x - t.position.x) < 1.45 && Math.abs(bmwM3.position.z - t.position.z) < 3.1) { 
                                gameOver = true; 
                                document.getElementById("scoreDisplay4D").innerHTML = "<span style='color:#ff003c; text-shadow:0 0 10px #ff003c;'>💥 SANAYİ YOLU GÖZÜKTÜ! 💥</span>";
                                document.getElementById("restartButtonContainer").innerHTML = '<button id="btnResetGame" style="margin-top:15px; padding:15px 50px; font-size:22px; font-weight:bold; background:linear-gradient(90deg, #ff003c, #1a0005); color:#fff; border:none; border-radius:12px; cursor:pointer; box-shadow: 0 0 30px #ff003c;">M3\'Ü YENİDEN MARŞ ET 🔄</button>';
                                
                                document.getElementById("btnResetGame").addEventListener("click", () => {
                                    score = 0;
                                    gameOver = false;
                                    bmwM3.position.x = 0;
                                    document.getElementById("scoreDisplay4D").innerText = "PRO-SPEED: 120 KM/H";
                                    document.getElementById("restartButtonContainer").innerHTML = "";
                                    traffic.forEach((trf, idx) => {
                                        trf.position.set((Math.random() - 0.5) * 12, 0, -50 - (idx * 50));
                                    });
                                });
                            }
                        });
                    }
                    renderer.render(scene, camera);
                    requestAnimationFrame(animate);
                }
                animate();
            }
        })();
    </script>
    """
    components.html(bmw_nextgen_html, height=780)

# ==========================================================================================
# OYUN KISMI - NEON KIRMIZI TEMALI ASTRO-AURA GALAKSİ JETİ
# ==========================================================================================
elif st.session_state.aktif_mod == "KizOyunu":
    st.markdown("<h3 style='color:#ff003c; text-shadow: 0 0 10px #ff003c;'>🌌 Astro-Aura Kırmızı Galaksi Savaşçısı</h3>", unsafe_allow_html=True)
    st.caption("A / D veya Klavye Yön Tuşları ile jeti yönlendir.")

    astro_premium_html = """
    <div style="text-align:center; background:#050001; padding:15px; border-radius:16px; border:3px solid #ff003c; box-shadow: 0 0 35px rgba(255,0,60,0.6); user-select:none; position:relative;">
        <button id="btnLeftKiz" style="position:absolute; left:20px; top:45%; transform:translateY(-50%); padding: 25px 22px; font-size: 32px; font-weight:bold; background:rgba(0,0,0,0.9); color:#ffffff; border:2px solid #ff003c; border-radius:15px; cursor:pointer; z-index:100; box-shadow:0 0 20px #ff003c;">◀</button>
        <button id="btnRightKiz" style="position:absolute; right:20px; top:45%; transform:translateY(-50%); padding: 25px 22px; font-size: 32px; font-weight:bold; background:rgba(0,0,0,0.9); color:#ffffff; border:2px solid #ff003c; border-radius:15px; cursor:pointer; z-index:100; box-shadow:0 0 20px #ff003c;">▶</button>
        <div id="kizFullCanvasContainer" style="width:100%; height:550px; border-radius:10px; overflow:hidden;"></div>
        <div id="uiPanelKiz" style="margin-top:15px;">
            <h2 id="kizScoreDisplay" style="color:#ffffff; font-family:'Segoe UI',sans-serif; margin:10px 0; font-weight:900; font-size:32px; letter-spacing:2px; text-shadow: 0 0 10px #ff003c;">COSMIC MATRİX: 0</h2>
            <div id="restartButtonContainerKiz"></div>
        </div>
    </div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script>
        (function() {
            const checkContainerKiz = setInterval(() => {
                const container = document.getElementById("kizFullCanvasContainer");
                if (container && typeof THREE !== 'undefined') {
                    clearInterval(checkContainerKiz);
                    initKizGame(container);
                }
            }, 50);

            function initKizGame(container) {
                const scene = new THREE.Scene();
                scene.fog = new THREE.FogExp2(0x050001, 0.015);
                
                const camera = new THREE.PerspectiveCamera(60, container.clientWidth / 550, 0.1, 1000);
                const renderer = new THREE.WebGLRenderer({ antialias: true });
                renderer.setSize(container.clientWidth, 550);
                container.appendChild(renderer.domElement);

                const neonLight = new THREE.PointLight(0xff003c, 4, 200);
                neonLight.position.set(0, 10, -20);
                scene.add(neonLight);
                scene.add(new THREE.AmbientLight(0x2a050c, 2.0));

                function createStars(color, size, count) {
                    const geo = new THREE.BufferGeometry();
                    const positions = new Float32Array(count * 3);
                    for(let i=0; i<count*3; i+=3) {
                        positions[i] = (Math.random() - 0.5) * 80;
                        positions[i+1] = (Math.random() - 0.5) * 50;
                        positions[i+2] = -Math.random() * 250;
                    }
                    geo.setAttribute('position', new THREE.BufferAttribute(positions, 3));
                    return new THREE.Points(geo, new THREE.PointsMaterial({ color: color, size: size, transparent: true, opacity: 0.9 }));
                }
                const layer1 = createStars(0xffffff, 0.2, 300);
                const layer2 = createStars(0xff003c, 0.35, 200);
                scene.add(layer1, layer2);

                const playerJet = new THREE.Group();
                const jetMat = new THREE.MeshStandardMaterial({ color: 0xff003c, metalness: 0.95, roughness: 0.05 });
                const core = new THREE.Mesh(new THREE.ConeGeometry(0.5, 2.5, 4), jetMat);
                core.rotation.x = Math.PI / 2;
                const wingL = new THREE.Mesh(new THREE.BoxGeometry(1.5, 0.04, 1.0), jetMat); wingL.position.set(-0.8, -0.1, 0.3); wingL.rotation.y = 0.2;
                const wingR = wingL.clone(); wingR.position.x = 0.8; wingR.rotation.y = -0.2;
                playerJet.add(core, wingL, wingR);

                const fireMat = new THREE.MeshBasicMaterial({ color: 0xffffff });
                const thruster = new THREE.Mesh(new THREE.ConeGeometry(0.2, 0.8, 8), fireMat);
                thruster.position.set(0, 0, 1.4);
                thruster.rotation.x = -Math.PI / 2;
                playerJet.add(thruster);

                playerJet.position.set(0, 0, -7);
                scene.add(playerJet);

                let asteroids = [];
                for(let i=0; i<5; i++){
                    let astGeo = new THREE.DodecahedronGeometry(1.3, 1);
                    let astMat = new THREE.MeshStandardMaterial({ color: 0x3d000c, roughness: 0.2, metalness: 0.8, emissive: 0x1a0005 });
                    let ast = new THREE.Mesh(astGeo, astMat);
                    ast.position.set((Math.random() - 0.5) * 14, (Math.random() - 0.5) * 4, -60 - (i * 40));
                    scene.add(ast);
                    asteroids.push(ast);
                }

                camera.position.set(0, 4.0, 4);
                camera.lookAt(new THREE.Vector3(0, 0, -15));

                let score = 0; let gameOver = false; let keys = {};
                window.addEventListener("keydown", e => keys[e.key] = true);
                window.addEventListener("keyup", e => keys[e.key] = false);

                let touchLeft = false, touchRight = false;
                
                document.getElementById("btnLeftKiz").addEventListener("mousedown", () => touchLeft = true);
                document.getElementById("btnLeftKiz").addEventListener("mouseup", () => touchLeft = false);
                document.getElementById("btnLeftKiz").addEventListener("touchstart", (e) => { e.preventDefault(); touchLeft = true; });
                document.getElementById("btnLeftKiz").addEventListener("touchend", () => touchLeft = false);

                document.getElementById("btnRightKiz").addEventListener("mousedown", () => touchRight = true);
                document.getElementById("btnRightKiz").addEventListener("mouseup", () => touchRight = false);
                document.getElementById("btnRightKiz").addEventListener("touchstart", (e) => { e.preventDefault(); touchRight = true; });
                document.getElementById("btnRightKiz").addEventListener("touchend", () => touchRight = false);

                function animate() {
                    if(!gameOver) {
                        let speed = 1.0 + (score * 0.035);

                        if(keys["ArrowLeft"] || keys["a"] || keys["A"] || touchLeft) { if(playerJet.position.x > -7.5) playerJet.position.x -= 0.24; playerJet.rotation.z = 0.4; }
                        else if(keys["ArrowRight"] || keys["d"] || keys["D"] || touchRight) { if(playerJet.position.x < 7.5) playerJet.position.x += 0.24; playerJet.rotation.z = -0.4; }
                        else { playerJet.rotation.z *= 0.8; }

                        thruster.scale.set(1 + Math.sin(Date.now()*0.1)*0.2, 1 + Math.cos(Date.now()*0.1)*0.3, 1);

                        const p1 = layer1.geometry.attributes.position.array;
                        for(let i=2; i<p1.length; i+=3) { p1[i] += speed * 0.8; if(p1[i] > 10) p1[i] = -240; }
                        layer1.geometry.attributes.position.needsUpdate = true;

                        const p2 = layer2.geometry.attributes.position.array;
                        for(let i=2; i<p2.length; i+=3) { p2[i] += speed * 1.4; if(p2[i] > 10) p2[i] = -240; }
                        layer2.geometry.attributes.position.needsUpdate = true;

                        asteroids.forEach(a => {
                            a.position.z += speed;
                            a.rotation.x += 0.02;
                            a.rotation.y += 0.04;

                            if(a.position.z > 6) { 
                                a.position.z = -160 - Math.random()*40; 
                                a.position.x = (Math.random() - 0.5) * 14; 
                                score++; 
                                document.getElementById("kizScoreDisplay").innerText = "COSMIC MATRİX: " + score; 
                            }
                            
                            if(Math.abs(playerJet.position.x - a.position.x) < 1.5 && Math.abs(playerJet.position.z - a.position.z) < 2.2) { 
                                gameOver = true; 
                                document.getElementById("kizScoreDisplay").innerHTML = "<span style='color:#ff003c; text-shadow:0 0 10px #ff003c;'>🔮 DARBE ALINDI! 🔮</span>";
                                document.getElementById("restartButtonContainerKiz").innerHTML = '<button id="btnResetKiz" style="margin-top:15px; padding:15px 45px; font-size:22px; font-weight:bold; background:linear-gradient(90deg, #ff003c, #050001); color:#fff; border:none; border-radius:12px; cursor:pointer; box-shadow: 0 0 30px #ff003c;">YENİDEN BAŞLA 🔄</button>';
                                
                                document.getElementById("btnResetKiz").addEventListener("click", () => {
                                    score = 0;
                                    gameOver = false;
                                    playerJet.position.x = 0;
                                    document.getElementById("kizScoreDisplay").innerText = "COSMIC MATRİX: 0";
                                    document.getElementById("restartButtonContainerKiz").innerHTML = "";
                                    asteroids.forEach((ast, idx) => {
                                        ast.position.set((Math.random() - 0.5) * 14, (Math.random() - 0.5) * 4, -60 - (idx * 40));
                                    });
                                });
                            }
                        });
                    }
                    renderer.render(scene, camera);
                    requestAnimationFrame(animate);
                }
                animate();
            }
        })();
    </script>
    """
    components.html(astro_premium_html, height=780)
