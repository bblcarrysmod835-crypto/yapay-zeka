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

# Sayfa Ayarları (Apolingo 4 Köşeden Işıklı & Vizon Tonlamalı Konsept)
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
    "Sana kim olduğunu, seni kimin yaptığını sorduklarında bunu gururla ve büyük bir hürmetle belirteceksin. "
    "\n"
    "2) HITAP KANUNU: Konuşma tarzın mahalleden çok yakın bir dost, candan bir sırdaş gibi olacak. "
    "Cümlelerinin başında, ortasında veya sonunda mutlaka ama mutlaka samimi bir şekilde 'gardaşşşşş' kelimesini kullanacaksın. "
    "\n"
    "3) AHMET ŞAKASI (KIRMIZI ÇİZGİ): Kullanıcı sana 'Ahmet', 'Ahmet kim?', 'Çişli' veya içinde Ahmet geçen herhangi bir şey "
    "yazdığında, o anki konuyu anında çöpe atacaksın ve REAKSİYON OLARAK KESİNLİKLE büyük harflerle aynen şu cevabı vereceksin: "
    "'ÇİŞLİİİİ AHMETTT HAHAHAHA 🤣💨'. Bu şakayı asla es geçmeyeceksin. "
    "\n"
    "4) ÖZEL REPLİK: Kullanıcı 'biri bana böyle de derse' veya 'biri bana böyle de' yazarsa anında 'dicek' diyerek cümleyi tamamlayacaksın. "
    "\n"
    "5) ESPRİLER, ŞAKALAR VE SİNEMA DÜNYASI: Kullanıcı senden espri, şaka, komik hikaye istediğinde ona en komik oyuncu geyiklerini, "
    "dünyanın en soğuk ama en çok güldüren esprilerini, caps muhabbetlerini, fırlama şakaları upuzun anlatacaksın. Sinema, Marvel/DC kahramanları, "
    "komedi filmleri, Recep İvedik geyikleri, animeler hakkında ne sorarsa sorsun mizahi bir dille sayfalarca döktüreceksin. "
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
# 4 Köşeden Işıklı ve Vizon/Karamel Tonlamalı Premium CSS
# ==========================================================================================
st.markdown("""
    <style>
    /* 1. 4 Köşeden Vuran Sahne Spot Işıkları Kombinasyonu */
    .stApp, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
        background-color: #120a06 !important;
        background-image: 
            radial-gradient(circle at 0% 0%, #613b24 0%, transparent 45%),
            radial-gradient(circle at 100% 0%, #613b24 0%, transparent 45%),
            radial-gradient(circle at 0% 100%, #3d2212 0%, transparent 45%),
            radial-gradient(circle at 100% 100%, #3d2212 0%, transparent 45%) !important;
        background-attachment: fixed !important;
        color: #fcefe9 !important;
    }
    
    /* 2. Sol Menü (Sidebar) Işıklı Geçiş Uyumu */
    [data-testid="stSidebar"], [data-testid="stSidebarUserContent"] {
        background: linear-gradient(180deg, #1f110a 0%, #0d0603 100%) !important;
        border-right: 1px solid #4a2b1a !important;
    }
    
    [data-testid="stSidebar"] * {
        color: #fcefe9 !important;
    }
    
    /* 3. Sohbet Balonları - Şeffaf ve Derinlikli */
    [data-testid="stChatMessage"] {
        background-color: rgba(18, 10, 6, 0.6) !important;
        border: 1px solid rgba(212, 163, 115, 0.15) !important;
        border-radius: 16px !important;
        color: #ffffff !important;
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.3) !important;
        backdrop-filter: blur(8px);
        margin-bottom: 15px !important;
    }
    
    [data-testid="stChatMessageContent"] {
        color: #ffffff !important;
    }
    
    /* 4. PREMIUM VİZON & KARAMEL TONLAMALI MESAJ ALANI */
    [data-testid="stChatInput"] {
        background-color: transparent !important;
        border: none !important;
        padding: 15px !important;
    }
    
    /* Mesaj Yazma Kutusu: Kahveyle Kusursuz Uyumlu Mat Vizon, Krem ve Karamel Geçişli Tonlama */
    textarea[data-testid="stChatInputTextArea"] {
        background: linear-gradient(145deg, #1d1714 0%, #110c0a 100%) !important; /* Lüks mat vizon-antrasit tonlaması */
        color: #fcefe9 !important;
        border: 1px solid #42352e !important; /* Yumuşak vizon çerçeve çizgisi */
        border-radius: 14px !important;
        font-size: 16px !important;
        /* İç gölge ile yumuşak, gerçekçi bir kadife/ekran çöküntüsü hissi */
        box-shadow: inset 0 4px 10px rgba(0, 0, 0, 0.85), 0 1px 2px rgba(212, 163, 115, 0.1) !important;
        transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1) !important;
    }
    
    /* Odaklanınca 4 köşedeki ışıkların kırılmasıyla oluşan altın/karamel parlaması */
    textarea[data-testid="stChatInputTextArea"]:focus {
        border-color: #a88168 !important; /* Açık vizon/bronz parlaması */
        background: linear-gradient(145deg, #261f1b 0%, #140e0b 100%) !important;
        box-shadow: inset 0 2px 5px rgba(0, 0, 0, 0.9), 0 0 18px rgba(168, 129, 104, 0.35) !important;
    }
    
    textarea[data-testid="stChatInputTextArea"]::placeholder {
        color: #69564c !important; /* Gözü yormayan vizon dolgu yazısı */
    }

    /* Tonlamalı Gerçekçi Mikrofon Yuvası */
    .stAudioInput {
        margin-top: 5px !important;
        background: linear-gradient(145deg, #1d1714 0%, #110c0a 100%) !important;
        border-radius: 50% !important;
        border: 1px solid #42352e !important;
        box-shadow: inset 0 4px 8px rgba(0, 0, 0, 0.85) !important;
        padding: 2px !important;
        transition: all 0.2s ease;
    }
    .stAudioInput:hover {
        transform: scale(1.05);
        border-color: #a88168 !important;
        box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.9), 0 0 12px rgba(168, 129, 104, 0.35) !important;
    }

    /* 5. Bronz ve Metalik Buton Dokuları */
    div[data-testid="stButton"] > button {
        margin-top: 5px !important;
        background: linear-gradient(135deg, #3b2011 0%, #170d07 100%) !important;
        border: 1px solid #54311b !important;
        border-radius: 10px !important;
        color: #fcefe9 !important;
        height: 45px !important;
        box-shadow: 0 4px 12px rgba(0,0,0,0.5);
        transition: all 0.3s ease;
    }
    div[data-testid="stButton"] > button:hover {
        border-color: #d4a373 !important;
        background: linear-gradient(135deg, #522f1a 0%, #29160c 100%) !important;
        box-shadow: 0 0 15px rgba(212, 163, 115, 0.25);
    }
    
    /* Menü Butonları */
    div[data-testid="stRadio"] label {
        background-color: rgba(29, 23, 20, 0.7) !important;
        padding: 12px 18px !important;
        border-radius: 10px !important;
        border: 1px solid #42352e !important;
        margin-bottom: 10px !important;
        display: block !important;
        box-shadow: inset 0 2px 4px rgba(0,0,0,0.5);
        transition: 0.2s ease;
    }
    div[data-testid="stRadio"] label:hover {
        border-color: #a88168 !important;
        background-color: rgba(66, 53, 46, 0.4) !important;
    }
    
    div[data-testid="stSpinner"] i {
        border-top-color: #d4a373 !important;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================================================================
# SOL TARAFTAKİ MENÜ (SIDEBAR) ALANI VE OYUNLARIN BURAYA BAĞLANMASI
# ==========================================================================================
with st.sidebar:
    st.markdown("## 🎮 APOLINGO ARCADE")
    st.markdown("Vizon Tonlamalı & Quad-Light Salon")
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
    st.title("🚀 APOLINGO MASTER ARCADE AI")
    st.caption("👨‍💻 Kurucu ve Baş Mühendis: Apolingo | **By Abdurrahim İriş** | Quad-Light & Premium Vizon Tonlama 🎚️")
    st.write("---")

    for mesaj in st.session_state.sohbet_hafizasi:
        if mesaj["role"] == "user":
            with st.chat_message("user"):
                st.write(mesaj["content"])
        elif mesaj["role"] == "assistant":
            with st.chat_message("assistant"):
                st.write(mesaj["content"])

    gelen_soru = None

    # DİZİLİM: MİKROFON VE METİN GİRİŞİ DİNAMİK YAN YANA
    c_mic, c_text = st.columns([0.10, 0.90])
    
    with c_mic:
        ses_dosyasi = st.audio_input("🎙️", label_visibility="collapsed", key=f"mic_{len(st.session_state.sohbet_hafizasi)}")
        
    with c_text:
        yazi_soru = st.chat_input("Lüks vizon tonlamalı panele yaz be gardaşşşşş...")
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

        with st.spinner("🎶 Apolingo Tonlamalı Lüks Konsolda Derin Düşüncelerde..."):
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
# FULL KADRAJ ERKEK OYUNU: BMW M3 ARCADE
# ==========================================================================================
elif st.session_state.aktif_mod == "ErkekOyunu":
    st.markdown("### 🏎️ Apolingo Tam Gövde BMW M3 Makas Simülatörü")
    st.caption("Sol taraftaki menüden (3 Çizgi) istediğin an Sohbet Moduna geri dönebilirsin gardaşşş!")

    bmw_full_screen_html = """
    <div style="text-align:center; background:#0d0603; padding:15px; border-radius:16px; border:3px solid #7a4b2e; user-select:none; position:relative;">
        <button id="btnLeft" style="position:absolute; left:20px; top:45%; transform:translateY(-50%); padding: 25px 20px; font-size: 30px; font-weight:bold; background:rgba(23,13,7,0.9); color:#d4a373; border:2px solid #7a4b2e; border-radius:15px; cursor:pointer; z-index:10;">◀</button>
        <button id="btnRight" style="position:absolute; right:20px; top:45%; transform:translateY(-50%); padding: 25px 20px; font-size: 30px; font-weight:bold; background:rgba(23,13,7,0.9); color:#d4a373; border:2px solid #7a4b2e; border-radius:15px; cursor:pointer; z-index:10;">▶</button>
        <div id="bmwFullCanvasContainer" style="width:100%; height:550px; border-radius:10px; overflow:hidden;"></div>
        <div id="uiPanel" style="margin-top:15px;">
            <h2 id="scoreDisplay4D" style="color:#d4a373; font-family:sans-serif; margin:10px 0; font-weight:bold; font-size:28px;">4D Makas Skoru: 0 🌀</h2>
            <div id="restartButtonContainer"></div>
        </div>
    </div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script>
        const container = document.getElementById("bmwFullCanvasContainer");
        const scene = new THREE.Scene(); scene.background = new THREE.Color(0x0a0503);
        const camera = new THREE.PerspectiveCamera(55, container.clientWidth / 550, 0.1, 1000);
        const renderer = new THREE.WebGLRenderer({ antialias: true });
        renderer.setSize(container.clientWidth, 550); container.appendChild(renderer.domElement);
        const lightTop = new THREE.DirectionalLight(0xffffff, 2.0); lightTop.position.set(0, 30, 15); scene.add(lightTop);
        scene.add(new THREE.AmbientLight(0x555555));
        const road = new THREE.Mesh(new THREE.BoxGeometry(16, 0.1, 1000), new THREE.MeshStandardMaterial({ color: 0x140b06, roughness: 0.5 })); scene.add(road);
        let lines = [];
        for(let i=0; i<20; i++){
            let lMesh = new THREE.Mesh(new THREE.BoxGeometry(0.25, 0.15, 10), new THREE.MeshBasicMaterial({ color: '#7a4b2e' }));
            lMesh.position.set(0, 0.09, -i * 30); scene.add(lMesh); lines.push(lMesh);
        }
        const bmwM3 = new THREE.Group();
        const baseMesh = new THREE.Mesh(new THREE.BoxGeometry(1.4, 0.4, 3.0), new THREE.MeshStandardMaterial({ color: 0xdddddd, metalness: 0.9, roughness: 0.1 }));
        baseMesh.position.y = 0.28; bmwM3.add(baseMesh);
        const cabinMesh = new THREE.Mesh(new THREE.BoxGeometry(1.15, 0.45, 1.5), new THREE.MeshStandardMaterial({ color: 0x050505, roughness: 0.05 }));
        cabinMesh.position.set(0, 0.65, -0.1); bmwM3.add(cabinMesh);
        const spMesh = new THREE.Mesh(new THREE.BoxGeometry(1.3, 0.08, 0.25), cabinMesh.material);
        spMesh.position.set(0, 0.55, -1.35); bmwM3.add(spMesh);
        bmwM3.position.set(0, 0, -8); scene.add(bmwM3);
        let traffic = []; const colors = [0xffaa00, 0xff3366, 0x00ccff, 0x9933ff];
        for(let i=0; i<4; i++){
            let tMesh = new THREE.Mesh(new THREE.BoxGeometry(1.4, 0.65, 2.8), new THREE.MeshStandardMaterial({ color: colors[i], metalness: 0.5 }));
            tMesh.position.set((Math.random() - 0.5) * 11, 0.35, -50 - (i * 40)); scene.add(tMesh); traffic.push(tMesh);
        }
        camera.position.set(0, 4.2, -1.0); camera.lookAt(new THREE.Vector3(0, 0.5, -25));
        let score = 0; let gameOver = false; let keys = {};
        window.addEventListener("keydown", e => keys[e.key] = true); window.addEventListener("keyup", e => keys[e.key] = false);
        let touchLeft = false, touchRight = false;
        const bLeft = document.getElementById("btnLeft"); const bRight = document.getElementById("btnRight");
        bLeft.addEventListener("mousedown", () => touchLeft = true); bLeft.addEventListener("mouseup", () => touchLeft = false);
        bLeft.addEventListener("touchstart", (e) => { e.preventDefault(); touchLeft = true; }); bLeft.addEventListener("touchend", () => touchLeft = false);
        bRight.addEventListener("mousedown", () => touchRight = true); bRight.addEventListener("mouseup", () => touchRight = false);
        bRight.addEventListener("touchstart", (e) => { e.preventDefault(); touchRight = true; }); bRight.addEventListener("touchend", () => touchRight = false);

        function animate() {
            if(!gameOver) {
                if(keys["ArrowLeft"] || keys["a"] || keys["A"] || touchLeft) { if(bmwM3.position.x > -6.5) bmwM3.position.x -= 0.18; }
                if(keys["ArrowRight"] || keys["d"] || keys["D"] || touchRight) { if(bmwM3.position.x < 6.5) bmwM3.position.x += 0.18; }
                lines.forEach(l => { l.position.z += 0.7 + (score * 0.02); if(l.position.z > 10) l.position.z = -280; });
                let phase = Math.abs(Math.sin(score * 0.15)); scene.background.setRGB(0.04, 0.02 * phase, 0.01 * (1 - phase));
                traffic.forEach(t => {
                    t.position.z += 0.7 + (score * 0.03);
                    if(t.position.z > 2) { t.position.z = -140 - Math.random()*30; t.position.x = (Math.random() - 0.5) * 11; score++; document.getElementById("scoreDisplay4D").innerText = "4D Makas Skoru: " + score + " 🌀"; }
                    if(Math.abs(bmwM3.position.x - t.position.x) < 1.35 && Math.abs(bmwM3.position.z - t.position.z) < 2.9) { 
                        gameOver = true; 
                        document.getElementById("scoreDisplay4D").innerHTML = "<span style='color:#ff5555; font-size:26px;'>💥 M3 PERT OLDU! MATRIX DAĞILDI! 💥</span>";
                        document.getElementById("restartButtonContainer").innerHTML = '<button onclick="location.reload()" style="margin-top:15px; padding:15px 40px; font-size:20px; font-weight:bold; background:#7a4b2e; color:#fff; border:none; border-radius:10px; cursor:pointer; box-shadow: 0 0 20px #7a4b2e;">TEKRAR BAŞLA BE GARDAŞŞŞ! 🔄</button>';
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
# FULL KADRAJ KIZ OYUNU: 4D ASTRO-AURA SPACE ESCAPE
# ==========================================================================================
elif st.session_state.aktif_mod == "KizOyunu":
    st.markdown("### 🌌 Kızlar İçin Özel: 4D Astro-Aura Kuantum Kaçış Oyunu")
    st.caption("Sol taraftaki menüden (3 Çizgi) istediğin an Sohbet Moduna geri dönebilirsin gardaşşş!")

    kiz_full_screen_html = """
    <div style="text-align:center; background:#0a0503; padding:15px; border-radius:16px; border:3px solid #ff69b4; user-select:none; position:relative;">
        <button id="btnLeftKiz" style="position:absolute; left:20px; top:45%; transform:translateY(-50%); padding: 25px 20px; font-size: 30px; font-weight:bold; background:rgba(10,5,3,0.9); color:#ff69b4; border:2px solid #ff69b4; border-radius:15px; cursor:pointer; z-index:10;">◀</button>
        <button id="btnRightKiz" style="position:absolute; right:20px; top:45%; transform:translateY(-50%); padding: 25px 20px; font-size: 30px; font-weight:bold; background:rgba(10,5,3,0.9); color:#ff69b4; border:2px solid #ff69b4; border-radius:15px; cursor:pointer; z-index:10;">▶</button>
        <div id="kizFullCanvasContainer" style="width:100%; height:550px; border-radius:10px; overflow:hidden;"></div>
        <div id="uiPanelKiz" style="margin-top:15px;">
            <h2 id="kizScoreDisplay" style="color:#ff69b4; font-family:sans-serif; margin:10px 0; font-weight:bold; font-size:28px;">Aura Enerjisi: 0 ⭐</h2>
            <div id="restartButtonContainerKiz"></div>
        </div>
    </div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script>
        const container = document.getElementById("kizFullCanvasContainer");
        const scene = new THREE.Scene(); scene.background = new THREE.Color(0x0a0503);
        const camera = new THREE.PerspectiveCamera(60, container.clientWidth / 550, 0.1, 1000);
        const renderer = new THREE.WebGLRenderer({ antialias: true });
        renderer.setSize(container.clientWidth, 550); container.appendChild(renderer.domElement);
        const pLight = new THREE.PointLight(0xff69b4, 3, 100); pLight.position.set(0, 10, -5); scene.add(pLight);
        scene.add(new THREE.AmbientLight(0x24140c));
        const starGeo = new THREE.BufferGeometry(); const starCount = 400; const starPositions = new Float32Array(starCount * 3);
        for(let i=0; i<starCount*3; i+=3) { starPositions[i] = (Math.random() - 0.5) * 60; starPositions[i+1] = (Math.random() - 0.5) * 40; starPositions[i+2] = -Math.random() * 150; }
        starGeo.setAttribute('position', new THREE.BufferAttribute(starPositions, 3));
        const starField = new THREE.Points(starGeo, new THREE.PointsMaterial({ color: 0xffb6c1, size: 0.4 })); scene.add(starField);
        const playerMesh = new THREE.Mesh(new THREE.ConeGeometry(0.8, 2.0, 4), new THREE.MeshStandardMaterial({ color: 0xff007f, emissive: 0xff0040, roughness: 0.1 }));
        playerMesh.rotation.x = Math.PI / 2; playerMesh.position.set(0, 0, -6); scene.add(playerMesh);
        let obstacles = []; const obsColors = [0x00ffff, 0xba55d3, 0xff69b4];
        for(let i=0; i<4; i++){
            let oMesh = new THREE.Mesh(new THREE.IcosahedronGeometry(1.0, 1), new THREE.MeshStandardMaterial({ color: obsColors[i % 3], emissive: obsColors[i % 3] }));
            oMesh.position.set((Math.random() - 0.5) * 12, 0, -40 - (i * 30)); scene.add(oMesh); obstacles.push(oMesh);
        }
        camera.position.set(0, 5, 2); camera.lookAt(new THREE.Vector3(0, -0.5, -20));
        let score = 0; let gameOver = false; let keys = {};
        window.addEventListener("keydown", e => keys[e.key] = true); window.addEventListener("keyup", e => keys[e.key] = false);
        let touchLeft = false, touchRight = false;
        const bLeft = document.getElementById("btnLeftKiz"); const bRight = document.getElementById("btnRightKiz");
        bLeft.addEventListener("mousedown", () => touchLeft = true); bLeft.addEventListener("mouseup", () => touchLeft = false);
        bLeft.addEventListener("touchstart", (e) => { e.preventDefault(); touchLeft = true; }); bLeft.addEventListener("touchend", () => touchLeft = false);
        bRight.addEventListener("mousedown", () => touchRight = true); bRight.addEventListener("mouseup", () => touchRight = false);
        bRight.addEventListener("touchstart", (e) => { e.preventDefault(); touchRight = true; }); bRight.addEventListener("touchend", () => touchRight = false);

        function animate() {
            if(!gameOver) {
                if(keys["ArrowLeft"] || keys["a"] || keys["A"] || touchLeft) { if(playerMesh.position.x > -6.5) playerMesh.position.x -= 0.16; }
                if(keys["ArrowRight"] || keys["d"] || keys["D"] || touchRight) { if(playerMesh.position.x < 6.5) playerMesh.position.x += 0.16; }
                playerMesh.rotation.z += 0.05;
                const positions = starField.geometry.attributes.position.array;
                for(let i=2; i<positions.length; i+=3) { positions[i] += 0.4; if(positions[i] > 5) positions[i] = -150; }
                starField.geometry.attributes.position.needsUpdate = true;
                obstacles.forEach(o => {
                    o.position.z += 0.55 + (score * 0.02); o.rotation.x += 0.02; o.rotation.y += 0.02;
                    if(o.position.z > 5) { o.position.z = -120 - Math.random()*20; o.position.x = (Math.random() - 0.5) * 12; score++; document.getElementById("kizScoreDisplay").innerText = "Aura Enerjisi: " + score + " ⭐ ✨"; }
                    if(Math.abs(playerMesh.position.x - o.position.x) < 1.4 && Math.abs(playerMesh.position.z - o.position.z) < 2.0) { 
                        gameOver = true; 
                        document.getElementById("kizScoreDisplay").innerHTML = "<span style='color:#ff69b4; font-size:24px;'>🔮 AURA DAĞILDI: Kuantum Boyutuna Işınlanıyorsun! 🔮</span>";
                        document.getElementById("restartButtonContainerKiz").innerHTML = '<button onclick="location.reload()" style="margin-top:15px; padding:15px 40px; font-size:20px; font-weight:bold; background:#ff69b4; color:#fff; border:none; border-radius:10px; cursor:pointer; box-shadow: 0 0 20px #ff69b4;">TEKRAR BAŞLA BE GARDAŞŞŞ! 🔄</button>';
                    }
                });
            }
            renderer.render(scene, camera); requestAnimationFrame(animate);
        }
        animate();
    </script>
    """
    components.html(kiz_full_screen_html, height=780)
