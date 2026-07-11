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
# CSS DÜZENLEMELERİ: KAHVERENGİ IŞIKLAR TAMAMEN SİLİNDİ, SAF GECE SİYAHI VE BEYAZ KUTU GELDİ
# ==========================================================================================
st.markdown("""
    <style>
    /* 1. Genel Arka Plan - Pürüzsüz Net Gece Siyahı (Gölgesiz, Iışıksız) */
    .stApp, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
        background-color: #050505 !important;
        background-image: none !important;
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
        color: #aaaaaa !important;
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
        background-color: #111111 !important;
        border: 1px solid #222222 !important;
        border-radius: 12px !important;
        margin-bottom: 15px !important;
    }
    
    /* 5. MESAJ GİRİŞ KUTUSU - LEKESİZ SAF BEYAZ */
    textarea[data-testid="stChatInputTextArea"] {
        color: #000000 !important;
        border-radius: 12px !important;
        background-color: #ffffff !important;
        border: 2px solid #cccccc !important;
        box-shadow: 0 4px 15px rgba(0,0,0,0.5) !important;
    }
    textarea[data-testid="stChatInputTextArea"]:focus {
        border-color: #ff0000 !important;
        background-color: #ffffff !important;
    }
    textarea[data-testid="stChatInputTextArea"]::placeholder {
        color: #555555 !important;
    }
    .stAudioInput {
        background-color: #ffffff !important;
        border: 2px solid #cccccc !important;
        box-shadow: 0 4px 15px rgba(0,0,0,0.5) !important;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================================================================
# SOL TARAFTAKİ MENÜ
# ==========================================================================================
with st.sidebar:
    st.markdown("## 🎮 APOLINGO ARCADE 4K")
    st.markdown("**Hyper-Engine Grafik Motoru Aktif**")
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
    st.markdown('<p class="havali-alt-yazi">Kurucu: Apolingo | Göz Yormayan Net Gece Sürümü</p>', unsafe_allow_html=True)
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

        with st.spinner("⚡ Apolingo Panellerde Hesaplıyor..."):
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
# AAA KALİTE HYPER BMW M3 MAKAS SİMÜLATÖRÜ
# ==========================================================================================
elif st.session_state.aktif_mod == "ErkekOyunu":
    st.markdown("### 🏎️ BMW M3 Ultra 4K Otoban Makas Simülatörü")
    st.caption("A / D veya Klavye Yön Tuşları aktiftir. Skor yükseldikçe hız ve kamera aksiyonu artar!")

    bmw_nextgen_html = """
    <div style="text-align:center; background:#020202; padding:15px; border-radius:16px; border:3px solid #ff0000; box-shadow: 0 0 35px rgba(255,0,0,0.6); user-select:none; position:relative;">
        <button id="btnLeft" style="position:absolute; left:20px; top:45%; transform:translateY(-50%); padding: 25px 22px; font-size: 32px; font-weight:bold; background:rgba(0,0,0,0.9); color:#ffffff; border:2px solid #ff0000; border-radius:15px; cursor:pointer; z-index:10; box-shadow:0 0 20px #ff0000;">◀</button>
        <button id="btnRight" style="position:absolute; right:20px; top:45%; transform:translateY(-50%); padding: 25px 22px; font-size: 32px; font-weight:bold; background:rgba(0,0,0,0.9); color:#ffffff; border:2px solid #ff0000; border-radius:15px; cursor:pointer; z-index:10; box-shadow:0 0 20px #ff0000;">▶</button>
        <div id="bmwFullCanvasContainer" style="width:100%; height:550px; border-radius:10px; overflow:hidden;"></div>
        <div id="uiPanel" style="margin-top:15px;">
            <h2 id="scoreDisplay4D" style="color:#ffffff; font-family:'Segoe UI',sans-serif; margin:10px 0; font-weight:900; font-size:32px; letter-spacing:2px; text-shadow: 0 0 10px #ff0000;">PRO-SPEED: 0 KM/H</h2>
            <div id="restartButtonContainer"></div>
        </div>
    </div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script>
        const container = document.getElementById("bmwFullCanvasContainer");
        const scene = new THREE.Scene();
        scene.fog = new THREE.FogExp2(0x020202, 0.02);
        
        const camera = new THREE.PerspectiveCamera(55, container.clientWidth / 550, 0.1, 1000);
        const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: false });
        renderer.setSize(container.clientWidth, 550);
        container.appendChild(renderer.domElement);

        // Sinematik Işıklar
        const sunLight = new THREE.DirectionalLight(0xffffff, 3.0);
        sunLight.position.set(10, 50, 20);
        scene.add(sunLight);
        scene.add(new THREE.AmbientLight(0x111111, 1.5));

        // Gerçekçi Asfalt Otoban Çift Şeritli
        const road = new THREE.Mesh(new THREE.BoxGeometry(16, 0.1, 1000), new THREE.MeshStandardMaterial({ color: 0x151515, roughness: 0.7 }));
        scene.add(road);

        // Yan Bariyerler
        const leftBarrier = new THREE.Mesh(new THREE.BoxGeometry(0.4, 0.8, 1000), new THREE.MeshStandardMaterial({ color: 0x333333 }));
        leftBarrier.position.set(-8.2, 0.4, 0);
        const rightBarrier = leftBarrier.clone();
        rightBarrier.position.x = 8.2;
        scene.add(leftBarrier, rightBarrier);

        // Kesikli Yol Şeritleri (Yüksek Çözünürlüklü Keskin Yapı)
        let lines = [];
        for(let i=0; i<25; i++){
            let lMesh = new THREE.Mesh(new THREE.BoxGeometry(0.2, 0.11, 8), new THREE.MeshBasicMaterial({ color: 0xffffff }));
            lMesh.position.set(0, 0.06, -i * 35);
            scene.add(lMesh);
            lines.push(lMesh);
        }

        // Tasarım Harikası BMW M3 (Gelişmiş Aerodinamik)
        const bmwM3 = new THREE.Group();
        const bodyMat = new THREE.MeshStandardMaterial({ color: 0xf0f0f0, metalness: 0.9, roughness: 0.1 });
        const body = new THREE.Mesh(new THREE.BoxGeometry(1.5, 0.4, 3.2), bodyMat);
        body.position.y = 0.3;
        bmwM3.add(body);

        // Karartılmış Spor Camlar
        const glassMat = new THREE.MeshStandardMaterial({ color: 0x050505, roughness: 0.0, metalness: 1.0 });
        const cabin = new THREE.Mesh(new THREE.BoxGeometry(1.2, 0.4, 1.6), glassMat);
        cabin.position.set(0, 0.65, -0.2);
        bmwM3.add(cabin);

        // Ön Xenon Farlar ve Arka Stop Lambaları
        const xenonMat = new THREE.MeshBasicMaterial({ color: 0xffffff });
        const stopMat = new THREE.MeshBasicMaterial({ color: 0xff0000 });
        
        const fLightL = new THREE.Mesh(new THREE.BoxGeometry(0.2, 0.08, 0.1), xenonMat); fLightL.position.set(-0.6, 0.3, -1.6);
        const fLightR = fLightL.clone(); fLightR.position.x = 0.6;
        const bLightL = new THREE.Mesh(new THREE.BoxGeometry(0.25, 0.08, 0.1), stopMat); bLightL.position.set(-0.6, 0.3, 1.6);
        const bLightR = bLightL.clone(); bLightR.position.x = 0.6;
        bmwM3.add(fLightL, fLightR, bLightL, bLightR);

        bmwM3.position.set(0, 0, -8);
        scene.add(bmwM3);

        // Rakip Spor Arabalar (Trafik)
        let traffic = [];
        const colors = [0xff1155, 0x00ffcc, 0xffcc00, 0x6600ff];
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
        document.getElementById("btnLeft").addEventListener("pointerdown", () => touchLeft = true);
        document.getElementById("btnLeft").addEventListener("pointerup", () => touchLeft = false);
        document.getElementById("btnRight").addEventListener("pointerdown", () => touchRight = true);
        document.getElementById("btnRight").addEventListener("pointerup", () => touchRight = false);

        function animate() {
            if(!gameOver) {
                let speed = 1.0 + (score * 0.03);
                
                // Gelişmiş Yumuşak Sürüş Fiziği
                if(keys["ArrowLeft"] || keys["a"] || keys["A"] || touchLeft) { 
                    if(bmwM3.position.x > -6.8) { bmwM3.position.x -= 0.24; if(tilt < 0.15) tilt += 0.025; }
                } else if(keys["ArrowRight"] || keys["d"] || keys["D"] || touchRight) { 
                    if(bmwM3.position.x < 6.8) { bmwM3.position.x += 0.24; if(tilt > -0.15) tilt -= 0.025; }
                } else {
                    tilt *= 0.8;
                }
                bmwM3.rotation.z = tilt; // Sağa sola yatış esnemesi
                bmwM3.rotation.y = tilt * 0.5; // Direksiyon açısı efekti

                // Dinamik Kamera Titremesi (Hız Hissi)
                camera.position.y = 4.5 + Math.sin(Date.now() * 0.05) * (score * 0.002);

                lines.forEach(l => { l.position.z += speed; if(l.position.z > 20) l.position.z = -350; });

                traffic.forEach(t => {
                    t.position.z += speed * 0.4;
                    if(t.position.z > 3) { 
                        t.position.z = -200 - Math.random()*60; 
                        t.position.x = (Math.random() - 0.5) * 12; 
                        score++; 
                        document.getElementById("scoreDisplay4D").innerText = "PRO-SPEED: " + (120 + score * 8) + " KM/H"; 
                    }
                    if(Math.abs(bmwM3.position.x - t.position.x) < 1.45 && Math.abs(bmwM3.position.z - t.position.z) < 3.1) { 
                        gameOver = true; 
                        document.getElementById("scoreDisplay4D").innerHTML = "<span style='color:#ff0000; text-shadow:0 0 10px #ff0000;'>💥 KAZA YAPILDI! OTOBAN KİLİT! 💥</span>";
                        document.getElementById("restartButtonContainer").innerHTML = '<button onclick="location.reload()" style="margin-top:15px; padding:15px 50px; font-size:22px; font-weight:bold; background:linear-gradient(90deg, #ff0000, #440000); color:#fff; border:none; border-radius:12px; cursor:pointer; box-shadow: 0 0 30px #ff0000;">M3\'Ü SANAYİDEN ÇIKAR 🔄</button>';
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
# AAA KALİTE ASTRO-AURA GALAKSİ JETİ OYUNU
# ==========================================================================================
elif st.session_state.aktif_mod == "KizOyunu":
    st.markdown("### 🌌 Astro-Aura 3-Layer Derin Uzay Savaşçısı")
    st.caption("A / D veya Klavye Yön Tuşları ile jeti yönlendir. Katmanlı derin uzay motoru devrede!")

    astro_premium_html = """
    <div style="text-align:center; background:#010103; padding:15px; border-radius:16px; border:3px solid #ff0000; box-shadow: 0 0 35px rgba(255,0,0,0.6); user-select:none; position:relative;">
        <button id="btnLeftKiz" style="position:absolute; left:20px; top:45%; transform:translateY(-50%); padding: 25px 22px; font-size: 32px; font-weight:bold; background:rgba(0,0,0,0.9); color:#ffffff; border:2px solid #ff0000; border-radius:15px; cursor:pointer; z-index:10; box-shadow:0 0 20px #ff0000;">◀</button>
        <button id="btnRightKiz" style="position:absolute; right:20px; top:45%; transform:translateY(-50%); padding: 25px 22px; font-size: 32px; font-weight:bold; background:rgba(0,0,0,0.9); color:#ffffff; border:2px solid #ff0000; border-radius:15px; cursor:pointer; z-index:10; box-shadow:0 0 20px #ff0000;">▶</button>
        <div id="kizFullCanvasContainer" style="width:100%; height:550px; border-radius:10px; overflow:hidden;"></div>
        <div id="uiPanelKiz" style="margin-top:15px;">
            <h2 id="kizScoreDisplay" style="color:#ffffff; font-family:'Segoe UI',sans-serif; margin:10px 0; font-weight:900; font-size:32px; letter-spacing:2px; text-shadow: 0 0 10px #ff3366;">COSMIC MATRİX: 0</h2>
            <div id="restartButtonContainerKiz"></div>
        </div>
    </div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script>
        const container = document.getElementById("kizFullCanvasContainer");
        const scene = new THREE.Scene();
        scene.fog = new THREE.FogExp2(0x010103, 0.015);
        
        const camera = new THREE.PerspectiveCamera(60, container.clientWidth / 550, 0.1, 1000);
        const renderer = new THREE.WebGLRenderer({ antialias: true });
        renderer.setSize(container.clientWidth, 550);
        container.appendChild(renderer.domElement);

        // Kuantum Plazma Işıkları
        const neonLight = new THREE.PointLight(0xff0055, 4, 200);
        neonLight.position.set(0, 10, -20);
        scene.add(neonLight);
        scene.add(new THREE.AmbientLight(0x0f051d, 2.0));

        // Katmanlı (Parallax) Yıldız Alanı - 3 Farklı Derinlik Katmanı
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
        const layer2 = createStars(0xff33aa, 0.35, 200);
        scene.add(layer1, layer2);

        # Fütüristik Delta-Wing Jet
        const playerJet = new THREE.Group();
        const jetMat = new THREE.MeshStandardMaterial({ color: 0xff1144, metalness: 0.95, roughness: 0.05 });
        
        const core = new THREE.Mesh(new THREE.ConeGeometry(0.5, 2.5, 4), jetMat);
        core.rotation.x = Math.PI / 2;
        
        const wingL = new THREE.Mesh(new THREE.BoxGeometry(1.5, 0.04, 1.0), jetMat); wingL.position.set(-0.8, -0.1, 0.3); wingL.rotation.y = 0.2;
        const wingR = wingL.clone(); wingR.position.x = 0.8; wingR.rotation.y = -0.2;
        playerJet.add(core, wingL, wingR);

        // Dinamik İyon Ateşi (Sürekli Titreyen Yapı)
        const fireMat = new THREE.MeshBasicMaterial({ color: 0xffffff });
        const thruster = new THREE.Mesh(new THREE.ConeGeometry(0.2, 0.8, 8), fireMat);
        thruster.position.set(0, 0, 1.4);
        thruster.rotation.x = -Math.PI / 2;
        playerJet.add(thruster);

        playerJet.position.set(0, 0, -7);
        scene.add(playerJet);

        // Metalik Işıltılı Geometrik Meteorit Kuşağı
        let asteroids = [];
        for(let i=0; i<5; i++){
            let astGeo = new THREE.DodecahedronGeometry(1.3, 1);
            let astMat = new THREE.MeshStandardMaterial({ color: 0x4a0e2e, roughness: 0.2, metalness: 0.8, emissive: 0x220211 });
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
        document.getElementById("btnLeftKiz").addEventListener("pointerdown", () => touchLeft = true);
        document.getElementById("btnLeftKiz").addEventListener("pointerup", () => touchLeft = false);
        document.getElementById("btnRightKiz").addEventListener("pointerdown", () => touchRight = true);
        document.getElementById("btnRightKiz").addEventListener("pointerup", () => touchRight = false);

        function animate() {
            if(!gameOver) {
                let speed = 0.8 + (score * 0.03);

                if(keys["ArrowLeft"] || keys["a"] || keys["A"] || touchLeft) { if(playerJet.position.x > -7.5) playerJet.position.x -= 0.22; playerJet.rotation.z = 0.4; }
                else if(keys["ArrowRight"] || keys["d"] || keys["D"] || touchRight) { if(playerJet.position.x < 7.5) playerJet.position.x += 0.22; playerJet.rotation.z = -0.4; }
                else { playerJet.rotation.z *= 0.8; }

                // Motor Ateşinin Titreme Simülatörü
                thruster.scale.set(1 + Math.sin(Date.now()*0.1)*0.2, 1 + Math.cos(Date.now()*0.1)*0.3, 1);

                // Katmanlı Yıldız Akışı (Parallax Derinlik)
                const p1 = layer1.geometry.attributes.position.array;
                for(let i=2; i<p1.length; i+=3) { p1[i] += speed * 0.8; if(p1[i] > 10) p1[i] = -240; }
                layer1.geometry.attributes.position.needsUpdate = true;

                const p2 = layer2.geometry.attributes.position.array;
                for(let i=2; i<p2.length; i+=3) { p2[i] += speed * 1.4; if(p2[i] > 10) p2[i] = -240; }
                layer2.geometry.attributes.position.needsUpdate = true;

                // Asteroitlerin Rotasyonu ve Hareketi
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
                        document.getElementById("kizScoreDisplay").innerHTML = "<span style='color:#ff0055; text-shadow:0 0 10px #ff0055;'>🔮 GRAVİTASYONEL DARBE ALINDI! 🔮</span>";
                        document.getElementById("restartButtonContainerKiz").innerHTML = '<button onclick="location.reload()" style="margin-top:15px; padding:15px 45px; font-size:22px; font-weight:bold; background:linear-gradient(90deg, #ff0055, #220011); color:#fff; border:none; border-radius:12px; cursor:pointer; box-shadow: 0 0 30px #ff0055;">KARA DELİKTEN ÇIK 🔄</button>';
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
