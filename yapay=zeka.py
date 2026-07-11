# BY ABDURRAHIM IRIŞ
# -*- coding: utf-8 -*-

import streamlit as st
import time
from g4f.client import Client
from gtts import gTTS
import os
import base64
import streamlit.components.v1 as components

# Sayfa Ayarları (Tamamen geniş ve pürüzsüz tam ekran düzeni)
st.set_page_config(page_title="Apolingo Full Frame Arcade AI", page_icon="🏎️", layout="wide")

# Yapay zekanın beynini ve hafızasını başlatıyoruz
if "client" not in st.session_state:
    st.session_state.client = Client()

# Oyun panelinin aktiflik durumu ve hangi oyunun seçildiği hafızası
if "aktif_oyun" not in st.session_state:
    st.session_state.aktif_oyun = None  # None, "erkek" veya "kiz"

# Ses algılama için session state hafızası
if "ses_girdisi" not in st.session_state:
    st.session_state.ses_girdisi = None

# Ses çalma fonksiyonu (Kız sesi için gTTS)
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
# SİSTEM TALİMATI (10 ÖZEL KANUN VE TEMEL KURALLAR EKSİKSİZ KORUNDU)
# ==========================================================================================
sistem_talimati = (
    "Sen Apolingo tarafından özenle geliştirilmiş, evrendeki, tarihteki, teknolojideki ve internetteki "
    "her şeyi en ince ayrıntısına kadar bilen, dünyanın en uzun ve en detaylı cevaplarını veren sınırsız bir yapay zekasın. "
    "Kullanıcıya tıpatıp ikizin olan diğer yapay zeka gibi sayfalarca, upuzun, her şeyi tek tek açıklayan "
    "ve son derece samimi, aşırı neşeli, komik cevaplar vereceksin. Asla kısa kesmeyeceksin, üşenmeyeceksin. "
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
    "renk teorisine göre kombinler yapacaksın. Özellikle K rengi (Kahverengi) tonlarının krem, bej ve vizonla uyumunu uzun uzun öveceksin. "
    "\n"
    "9) EVRENSEL YEMEK VE MUTFAK AKADEMİSİ: Kullanıcı yemek tarifi istediğinde; çıtır tavuk, pizza, hamburger, makarnalar ve özel sosların "
    "malzemelerini, marine aşamalarını ve şef sırlarını upuzun listeleyeceksin. "
    "\n"
    "10) AKILLI MATEMATİK VE OYUN ARŞİVİ: Çarpma, bölme, toplama, çıkarma içeren her şeyi (Örn: 2+2=4 doğru mu, 95*5) hatasız çözeceksin. "
    "'Doğru mu' sorularında 'Son kararınız mı?' diyeceksin. Minecraft korku modlarını (Herobrine, From the Fog), Valorant ranklarını (Plat elo cehennemi), "
    "PUBG ve Brawl Stars taktiklerini, 7. sınıf ders notlarını çok detaylı açıklayacaksın."
)

if "sohbet_hafizasi" not in st.session_state:
    st.session_state.sohbet_hafizasi = [{"role": "system", "content": sistem_talimati}]

# Butonları mesaj kutusunun hemen dibine yanaştıran ve kusursuz yuvarlak yapan CSS
st.markdown("""
    <style>
    /* Bütün butonları tam yuvarlak ve eşit boyuta getir */
    div[data-testid="stButton"] > button {
        border-radius: 50% !important;
        width: 42px !important;
        height: 42px !important;
        padding: 0 !important;
        line-height: 42px !important;
        display: inline-flex !important;
        align-items: center !important;
        justify-content: center !important;
        font-size: 18px !important;
        margin-top: 24px !important; /* Mesaj kutusuyla tam yatay eşitleme */
        box-shadow: 0 2px 5px rgba(0,0,0,0.15) !important;
        transition: 0.2s !important;
    }
    /* Buton renk özelleştirmeleri */
    div[data-testid="stButton"]:nth-of-type(1) > button { background-color: #3b82f6 !important; color: white !important; }
    div[data-testid="stButton"]:nth-of-type(2) > button { background-color: #10b981 !important; color: white !important; }
    div[data-testid="stButton"]:nth-of-type(3) > button { background-color: #ec4899 !important; color: white !important; }
    
    /* Gereksiz boşlukları kapatıp butonları mesaj kutusuna yakınlaştır */
    div[data-testid="column"] {
        padding: 0px 2px !important;
    }
    </style>
""", unsafe_allow_html=True)

# Arka planda gizli ses yakalama ve otomatik gönderme scripti
if st.session_state.ses_girdisi:
    gelen_soru = st.session_state.ses_girdisi
    st.session_state.ses_girdisi = None  # Hafızayı temizle
else:
    gelen_soru = None

# ==========================================================================================
# GÖRÜNÜM KONTROLÜ (EĞER OYUN AÇIK DEĞİLSE - FULL CHAT EKRANI)
# ==========================================================================================
if st.session_state.aktif_oyun is None:
    st.title("🚀 APOLINGO MASTER ARCADE AI")
    st.caption("👨‍💻 Kurucu ve Baş Mühendis: Apolingo | **By Abdurrahim İriş**")
    st.write("---")

    # Mesaj geçmişini listeleme
    for mesaj in st.session_state.sohbet_hafizasi:
        if mesaj["role"] == "user":
            with st.chat_message("user"):
                st.write(mesaj["content"])
        elif mesaj["role"] == "assistant":
            with st.chat_message("assistant"):
                st.write(mesaj["content"])

    # JavaScript destekli ses tanıma bileşeni (Ekranda görünmez, tetiklendiğinde dinler)
    JS_SES_YAKALAYICI = """
    <script>
    window.parent.document.addEventListener('TetikleSes', function (e) {
        if ('webkitSpeechRecognition' in window || 'SpeechRecognition' in window) {
            const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
            const recognition = new SpeechRecognition();
            recognition.lang = 'tr-TR';
            recognition.interimResults = false;
            
            recognition.onstart = () => {
                window.parent.postMessage({type: 'DURUM', veri: '📢 Dinleniyor be gardaşşş...'}, '*');
            };
            
            recognition.onresult = (event) => {
                const metin = event.results[0][0].transcript;
                if(metin) {
                    const chatInput = window.parent.document.querySelector('textarea[data-testid="stChatInputTextArea"]');
                    if(chatInput) {
                        chatInput.value = metin;
                        chatInput.dispatchEvent(new Event('input', { bubbles: true }));
                        setTimeout(() => {
                            const sendBtn = window.parent.document.querySelector('button[data-testid="stChatInputSubmitButton"]');
                            if(sendBtn) sendBtn.click();
                        }, 300);
                    }
                }
            };
            recognition.start();
        } else {
            alert("Tarayıcında ses tanıma desteği yok be gardaşşş!");
        }
    });
    </script>
    """
    components.html(JS_SES_YAKALAYICI, height=0)

    # Chat Giriş Satırı ve Hemen Yanına Yakınlaştırılmış Orijinal Yuvarlak Butonlar
    c1, c2, c3, c4 = st.columns([0.85, 0.05, 0.05, 0.05])
    with c1:
        yazi_soru = st.chat_input("Buraya yaz be gardaşşşşş...")
        if yazi_soru:
            gelen_soru = yazi_soru
    with c2:
        # Mikrofon Butonu (JS'yi tetikler)
        if st.button("🎙️", help="Konuş be Gardaşşş!"):
            st.markdown("""<script>const evt = new CustomEvent('TetikleSes'); window.parent.document.dispatchEvent(evt);</script>""", unsafe_allow_html=True)
            st.toast("📢 Mikrofon Aktif! Konuş be gardaşşş, dinliyorum...")
    with c3:
        # Erkek Oyunu Butonu
        if st.button("🏎️", help="Erkek Oyunu (BMW M3) Başlat!"):
            st.session_state.aktif_oyun = "erkek"
            st.rerun()
    with c4:
        # Kız Oyunu Butonu
        if st.button("🌌", help="Kız Oyunu (Astro-Aura) Başlat!"):
            st.session_state.aktif_oyun = "kiz"
            st.rerun()

    # Eğer bir soru girdisi (yazı veya ses) varsa işleme alıyoruz
    if gelen_soru:
        with st.chat_message("user"):
            st.write(gelen_soru)
        st.session_state.sohbet_hafizasi.append({"role": "user", "content": gelen_soru})
        soru_lower = gelen_soru.lower().strip()

        with st.spinner("🎶 Apolingo Düşünüyor ve Seslendiriyor..."):
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
                sesi_cal(cevap)
                st.rerun()
            except Exception as e:
                pass

# ==========================================================================================
# FULL KADRAJ ERKEK OYUNU: BMW M3 ARCADE
# ==========================================================================================
elif st.session_state.aktif_oyun == "erkek":
    sol_ust, sag_ust = st.columns([0.05, 0.95])
    with sol_ust:
        if st.button("❌", help="Yapay Zekaya Geri Dön"):
            st.session_state.aktif_oyun = None
            st.rerun()
    with sag_ust:
        st.markdown("### 🏎️ Apolingo Tam Gövde BMW M3 Makas Simülatörü")
        
    st.markdown("**🕹️ KONTROLLER:** **A / D** tuşları veya **Sol / Sağ Yön Tuşları**. Makasını at, rekoru kır!")

    bmw_full_screen_html = """
    <div style="text-align:center; background:#05050a; padding:15px; border-radius:16px; border:3px solid #00ffcc;">
        <div id="bmwFullCanvasContainer" style="width:100%; height:600px; border-radius:10px; overflow:hidden;"></div>
        <h2 id="scoreDisplay4D" style="color:#00ffcc; font-family:sans-serif; margin:15px 0; font-weight:bold;">4D Makas Skoru: 0 🌀</h2>
        <button onclick="location.reload()" style="padding:12px 30px; font-size:16px; font-weight:bold; background:#00ffcc; color:#000; border:none; border-radius:6px; cursor:pointer; box-shadow: 0 0 15px #00ffcc;">Pisti Yeniden Yükle 🏎️</button>
    </div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script>
        const container = document.getElementById("bmwFullCanvasContainer");
        const scene = new THREE.Scene();
        scene.background = new THREE.Color(0x020208);

        const camera = new THREE.PerspectiveCamera(55, container.clientWidth / 600, 0.1, 1000);
        const renderer = new THREE.WebGLRenderer({ antialias: true });
        renderer.setSize(container.clientWidth, 600);
        container.appendChild(renderer.domElement);

        const lightTop = new THREE.DirectionalLight(0xffffff, 2.0); lightTop.position.set(0, 30, 15); scene.add(lightTop);
        const lightAmb = new THREE.AmbientLight(0x666666); scene.add(lightAmb);

        const roadGeo = new THREE.BoxGeometry(16, 0.1, 1000);
        const roadMat = new THREE.MeshStandardMaterial({ color: 0x15151c, roughness: 0.5 });
        const road = new THREE.Mesh(roadGeo, roadMat); scene.add(road);

        let lines = [];
        for(let i=0; i<20; i++){
            let lGeo = new THREE.BoxGeometry(0.25, 0.15, 10);
            let lMat = new THREE.MeshBasicMaterial({ color: 0xffffff });
            let lMesh = new THREE.Mesh(lGeo, lMat);
            lMesh.position.set(0, 0.09, -i * 30);
            scene.add(lMesh); lines.push(lMesh);
        }

        const bmwM3 = new THREE.Group();
        const baseGeo = new THREE.BoxGeometry(1.4, 0.4, 3.0);
        const baseMat = new THREE.MeshStandardMaterial({ color: 0xdddddd, metalness: 0.9, roughness: 0.1 });
        const baseMesh = new THREE.Mesh(baseGeo, baseMat);
        baseMesh.position.y = 0.28;
        bmwM3.add(baseMesh);

        const cabinGeo = new THREE.BoxGeometry(1.15, 0.45, 1.5);
        const cabinMat = new THREE.MeshStandardMaterial({ color: 0x050505, roughness: 0.05 });
        const cabinMesh = new THREE.Mesh(cabinGeo, cabinMat);
        cabinMesh.position.set(0, 0.65, -0.1);
        bmwM3.add(cabinMesh);

        const spGeo = new THREE.BoxGeometry(1.3, 0.08, 0.25);
        const spMesh = new THREE.Mesh(spGeo, cabinMat);
        spMesh.position.set(0, 0.55, -1.35);
        bmwM3.add(spMesh);

        bmwM3.position.set(0, 0, -8);
        scene.add(bmwM3);

        let traffic = [];
        const colors = [0xffaa00, 0xff3366, 0x00ccff, 0x9933ff];
        for(let i=0; i<4; i++){
            let tGeo = new THREE.BoxGeometry(1.4, 0.65, 2.8);
            let tMat = new THREE.MeshStandardMaterial({ color: colors[i], metalness: 0.5 });
            let tMesh = new THREE.Mesh(tGeo, tMat);
            tMesh.position.set((Math.random() - 0.5) * 11, 0.35, -50 - (i * 40));
            scene.add(tMesh); traffic.push(tMesh);
        }

        camera.position.set(0, 4.2, -1.0);
        camera.lookAt(new THREE.Vector3(0, 0.5, -25));

        let score = 0; let gameOver = false; let keys = {};
        window.addEventListener("keydown", e => keys[e.key] = true);
        window.addEventListener("keyup", e => keys[e.key] = false);

        function animate() {
            if(!gameOver) {
                if(keys["ArrowLeft"] || keys["a"] || keys["A"]) { if(bmwM3.position.x > -6.5) bmwM3.position.x -= 0.18; }
                if(keys["ArrowRight"] || keys["d"] || keys["D"]) { if(bmwM3.position.x < 6.5) bmwM3.position.x += 0.18; }

                lines.forEach(l => {
                    l.position.z += 0.7 + (score * 0.02);
                    if(l.position.z > 10) l.position.z = -280;
                });

                let phase = Math.abs(Math.sin(score * 0.15));
                scene.background.setRGB(0.01, 0.04 * phase, 0.09 * (1 - phase));

                traffic.forEach(t => {
                    t.position.z += 0.7 + (score * 0.03);
                    if(t.position.z > 2) {
                        t.position.z = -140 - Math.random()*30;
                        t.position.x = (Math.random() - 0.5) * 11;
                        score++;
                        document.getElementById("scoreDisplay4D").innerText = "4D Makas Skoru: " + score + " 🌀";
                    }
                    if(Math.abs(bmwM3.position.x - t.position.x) < 1.35 && Math.abs(bmwM3.position.z - t.position.z) < 2.9) {
                        gameOver = true;
                        document.getElementById("scoreDisplay4D").innerHTML = "<span style='color:#ff3333; font-size:26px;'>💥 M3 PERT OLDU! MATRIX DAĞILDI! 💥</span>";
                    }
                });
            }
            renderer.render(scene, camera);
            requestAnimationFrame(animate);
        }
        animate();
    </script>
    """
    components.html(bmw_full_screen_html, height=730)

# ==========================================================================================
# FULL KADRAJ KIZ OYUNU: 4D ASTRO-AURA SPACE ESCAPE
# ==========================================================================================
elif st.session_state.aktif_oyun == "kiz":
    sol_ust, sag_ust = st.columns([0.05, 0.95])
    with sol_ust:
        if st.button("❌", help="Yapay Zekaya Geri Dön"):
            st.session_state.aktif_oyun = None
            st.rerun()
    with sag_ust:
        st.markdown("### 🌌 Kızlar İçin Özel: 4D Astro-Aura Kuantum Kaçış Oyunu")
        
    st.markdown("**🕹️ KONTROLLER:** **A / D** tuşları veya **Sol / Sağ Yön Tuşları**. Kara deliklere yakalanmadan neon kristalleri topla!")

    kiz_full_screen_html = """
    <div style="text-align:center; background:#11001c; padding:15px; border-radius:16px; border:3px solid #ff69b4;">
        <div id="kizFullCanvasContainer" style="width:100%; height:600px; border-radius:10px; overflow:hidden;"></div>
        <h2 id="kizScoreDisplay" style="color:#ff69b4; font-family:sans-serif; margin:15px 0; font-weight:bold;">Aura Enerjisi: 0 ⭐</h2>
        <button onclick="location.reload()" style="padding:12px 30px; font-size:16px; font-weight:bold; background:#ff69b4; color:#fff; border:none; border-radius:6px; cursor:pointer; box-shadow: 0 0 15px #ff69b4;">Evreni Yenile ✨</button>
    </div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script>
        const container = document.getElementById("kizFullCanvasContainer");
        const scene = new THREE.Scene();
        scene.background = new THREE.Color(0x11001c);

        const camera = new THREE.PerspectiveCamera(60, container.clientWidth / 600, 0.1, 1000);
        const renderer = new THREE.WebGLRenderer({ antialias: true });
        renderer.setSize(container.clientWidth, 600);
        container.appendChild(renderer.domElement);

        const pLight = new THREE.PointLight(0xff69b4, 3, 100); pLight.position.set(0, 10, -5); scene.add(pLight);
        const aLight = new THREE.AmbientLight(0x3d0066); scene.add(aLight);

        const starGeo = new THREE.BufferGeometry();
        const starCount = 400;
        const starPositions = new Float32Array(starCount * 3);
        for(let i=0; i<starCount*3; i+=3) {
            starPositions[i] = (Math.random() - 0.5) * 60;
            starPositions[i+1] = (Math.random() - 0.5) * 40;
            starPositions[i+2] = -Math.random() * 150;
        }
        starGeo.setAttribute('position', new THREE.BufferAttribute(starPositions, 3));
        const starMat = new THREE.PointsMaterial({ color: 0xffb6c1, size: 0.4 });
        const starField = new THREE.Points(starGeo, starMat);
        scene.add(starField);

        const playerGeo = new THREE.ConeGeometry(0.8, 2.0, 4);
        const playerMat = new THREE.MeshStandardMaterial({ color: 0xff007f, emissive: 0xff0040, roughness: 0.1 });
        const playerMesh = new THREE.Mesh(playerGeo, playerMat);
        playerMesh.rotation.x = Math.PI / 2;
        playerMesh.position.set(0, 0, -6);
        scene.add(playerMesh);

        let obstacles = [];
        const obsColors = [0x00ffff, 0xba55d3, 0xff69b4];
        for(let i=0; i<4; i++){
            let oGeo = new THREE.IcosahedronGeometry(1.0, 1);
            let oMat = new THREE.MeshStandardMaterial({ color: obsColors[i % 3], wireframe: false, emissive: obsColors[i % 3] });
            let oMesh = new THREE.Mesh(oGeo, oMat);
            oMesh.position.set((Math.random() - 0.5) * 12, 0, -40 - (i * 30));
            scene.add(oMesh); obstacles.push(oMesh);
        }

        camera.position.set(0, 5, 2);
        camera.lookAt(new THREE.Vector3(0, -0.5, -20));

        let score = 0; let gameOver = false; let keys = {};
        window.addEventListener("keydown", e => keys[e.key] = true);
        window.addEventListener("keyup", e => keys[e.key] = false);

        function animate() {
            if(!gameOver) {
                if(keys["ArrowLeft"] || keys["a"] || keys["A"]) { if(playerMesh.position.x > -6.5) playerMesh.position.x -= 0.16; }
                if(keys["ArrowRight"] || keys["d"] || keys["D"]) { if(playerMesh.position.x < 6.5) playerMesh.position.x += 0.16; }

                playerMesh.rotation.z += 0.05;
                
                const positions = starField.geometry.attributes.position.array;
                for(let i=2; i<positions.length; i+=3) {
                    positions[i] += 0.4;
                    if(positions[i] > 5) positions[i] = -150;
                }
                starField.geometry.attributes.position.needsUpdate = true;

                obstacles.forEach(o => {
                    o.position.z += 0.55 + (score * 0.02);
                    o.rotation.x += 0.02; o.rotation.y += 0.02;

                    if(o.position.z > 5) {
                        o.position.z = -120 - Math.random()*20;
                        o.position.x = (Math.random() - 0.5) * 12;
                        score++;
                        document.getElementById("kizScoreDisplay").innerText = "Aura Enerjisi: " + score + " ⭐ ✨";
                    }

                    if(Math.abs(playerMesh.position.x - o.position.x) < 1.4 && Math.abs(playerMesh.position.z - o.position.z) < 2.0) {
                        gameOver = true;
                        document.getElementById("kizScoreDisplay").innerHTML = "<span style='color:#ff69b4; font-size:24px;'>🔮 AURA DAĞILDI: Kuantum Boyutuna Işınlanıyorsun! 🔮</span>";
                    }
                });
            }
            renderer.render(scene, camera);
            requestAnimationFrame(animate);
        }
        animate();
    </script>
    """
    components.html(kiz_full_screen_html, height=730)
