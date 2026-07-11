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

# Oyun panelinin aktiflik durumu
if "aktif_oyun" not in st.session_state:
    st.session_state.aktif_oyun = None

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
    "Sen Apolingo tarafından özenle geliştirilmiş, evrendeki, tarihteki, teknolojideki ve internetteki "
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

# HIGH-END ALIGNMENT VE CHAT INPUT CSS DÜZENLEMESİ
st.markdown("""
    <style>
    /* Mikrofon dikey hizalama ayarı */
    .stAudioInput {
        margin-top: 6px !important;
    }
    
    /* Butonların chat input hizasına getirilmesi */
    div[data-testid="stButton"] > button {
        margin-top: 6px !important;
        background-color: #1e293b !important;
        border: 1px solid #4b5563 !important;
        border-radius: 8px !important;
        height: 44px !important;
        width: 100% !important;
        font-size: 18px !important;
    }
    div[data-testid="stButton"] > button:hover {
        border-color: #3b82f6 !important;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================================================================
# GÖRÜNÜM KONTROLÜ
# ==========================================================================================
if st.session_state.aktif_oyun is None:
    st.title("🚀 APOLINGO MASTER ARCADE AI")
    st.caption("👨‍💻 Kurucu ve Baş Mühendis: Apolingo | **By Abdurrahim İriş**")
    st.write("---")

    # Mesaj geçmişi ekrana yazılıyor
    for mesaj in st.session_state.sohbet_hafizasi:
        if mesaj["role"] == "user":
            with st.chat_message("user"):
                st.write(mesaj["content"])
        elif mesaj["role"] == "assistant":
            with st.chat_message("assistant"):
                st.write(mesaj["content"])

    gelen_soru = None

    # ELEMAN DİZİLİMİ: MİKROFON SOLDA, CHAT INPUT ORTADA, OYUNLAR SAĞDA BİTİŞİK
    c_mic, c_text, c_game1, c_game2 = st.columns([0.12, 0.76, 0.06, 0.06])
    
    with c_mic:
        ses_dosyasi = st.audio_input("🎙️", label_visibility="collapsed", key=f"mic_{len(st.session_state.sohbet_hafizasi)}")
        
    with c_text:
        yazi_soru = st.chat_input("Buraya yaz be gardaşşşşş...")
        if yazi_soru:
            gelen_soru = yazi_soru
            
    with c_game1:
        if st.button("🏎️", help="Erkek Oyunu (BMW M3) Başlat!"):
            st.session_state.aktif_oyun = "erkek"
            st.rerun()
            
    with c_game2:
        if st.button("🌌", help="Kız Oyunu (Astro-Aura) Başlat!"):
            st.session_state.aktif_oyun = "kiz"
            st.rerun()

    # KESİNTİSİZ SES DİNLEME VE OTOMATİK GÖNDERİM SİSTEMİ
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

    # Yanıt İşleme Hattı
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
                
                st.session_state.ses_isleme_aktif = True
                sesi_cal(cevap)
                st.rerun()
            except Exception as e:
                st.session_state.ses_isleme_aktif = True

# ==========================================================================================
# FULL KADRAJ ERKEK OYUNU: BMW M3 ARCADE (YÖN BUTONLARI EKLENDİ)
# ==========================================================================================
elif st.session_state.aktif_oyun == "erkek":
    st.markdown("### 🏎️ Apolingo Tam Gövde BMW M3 Makas Simülatörü")
    if st.button("❌ Yapay Zekaya Geri Dön be Gardaşşş!", help="Oyundan Çık"):
        st.session_state.aktif_oyun = None
        st.rerun()
        
    st.markdown("**🕹️ KONTROLLER:** Ekrandaki **YÖN BUTONLARI**, Klavyede **A / D** veya **Yön Tuşları**.")

    bmw_full_screen_html = """
    <div style="text-align:center; background:#05050a; padding:15px; border-radius:16px; border:3px solid #00ffcc; user-select:none;">
        <div id="bmwFullCanvasContainer" style="width:100%; height:550px; border-radius:10px; overflow:hidden;"></div>
        <h2 id="scoreDisplay4D" style="color:#00ffcc; font-family:sans-serif; margin:10px 0; font-weight:bold;">4D Makas Skoru: 0 🌀</h2>
        
        <!-- DOKUNMATİK / TIKLAMALI YÖN TUŞLARI PANELİ -->
        <div style="margin: 15px 0;">
            <button id="btnLeft" style="padding: 15px 40px; font-size: 24px; font-weight:bold; background:#1e293b; color:#00ffcc; border:2px solid #00ffcc; border-radius:12px; cursor:pointer; margin-right:20px;">◀ SOL</button>
            <button id="btnRight" style="padding: 15px 40px; font-size: 24px; font-weight:bold; background:#1e293b; color:#00ffcc; border:2px solid #00ffcc; border-radius:12px; cursor:pointer;">SAĞ ▶</button>
        </div>

        <button onclick="location.reload()" style="padding:10px 25px; font-size:14px; font-weight:bold; background:#00ffcc; color:#000; border:none; border-radius:6px; cursor:pointer; box-shadow: 0 0 15px #00ffcc;">Pisti Yeniden Yükle 🏎️</button>
    </div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script>
        const container = document.getElementById("bmwFullCanvasContainer");
        const scene = new THREE.Scene(); scene.background = new THREE.Color(0x020208);
        const camera = new THREE.PerspectiveCamera(55, container.clientWidth / 550, 0.1, 1000);
        const renderer = new THREE.WebGLRenderer({ antialias: true });
        renderer.setSize(container.clientWidth, 550); container.appendChild(renderer.domElement);
        const lightTop = new THREE.DirectionalLight(0xffffff, 2.0); lightTop.position.set(0, 30, 15); scene.add(lightTop);
        scene.add(new THREE.AmbientLight(0x666666));
        const road = new THREE.Mesh(new THREE.BoxGeometry(16, 0.1, 1000), new THREE.MeshStandardMaterial({ color: 0x15151c, roughness: 0.5 })); scene.add(road);
        let lines = [];
        for(let i=0; i<20; i++){
            let lMesh = new THREE.Mesh(new THREE.BoxGeometry(0.25, 0.15, 10), new THREE.MeshBasicMaterial({ color: 0xffffff }));
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
        
        // Klavye Kontrolleri
        window.addEventListener("keydown", e => keys[e.key] = true); window.addEventListener("keyup", e => keys[e.key] = false);
        
        // Buton Kontrolleri (Dokunmatik ve Mouse)
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
                let phase = Math.abs(Math.sin(score * 0.15)); scene.background.setRGB(0.01, 0.04 * phase, 0.09 * (1 - phase));
                traffic.forEach(t => {
                    t.position.z += 0.7 + (score * 0.03);
                    if(t.position.z > 2) { t.position.z = -140 - Math.random()*30; t.position.x = (Math.random() - 0.5) * 11; score++; document.getElementById("scoreDisplay4D").innerText = "4D Makas Skoru: " + score + " 🌀"; }
                    if(Math.abs(bmwM3.position.x - t.position.x) < 1.35 && Math.abs(bmwM3.position.z - t.position.z) < 2.9) { gameOver = true; document.getElementById("scoreDisplay4D").innerHTML = "<span style='color:#ff3333; font-size:26px;'>💥 M3 PERT OLDU! MATRIX DAĞILDI! 💥</span>"; }
                });
            }
            renderer.render(scene, camera); requestAnimationFrame(animate);
        }
        animate();
    </script>
    """
    components.html(bmw_full_screen_html, height=760)

# ==========================================================================================
# FULL KADRAJ KIZ OYUNU: 4D ASTRO-AURA SPACE ESCAPE (YÖN BUTONLARI EKLENDİ)
# ==========================================================================================
elif st.session_state.aktif_oyun == "kiz":
    st.markdown("### 🌌 Kızlar İçin Özel: 4D Astro-Aura Kuantum Kaçış Oyunu")
    if st.button("❌ Yapay Zekaya Geri Dön be Gardaşşş!", help="Oyundan Çık"):
        st.session_state.aktif_oyun = None
        st.rerun()
        
    st.markdown("**🕹️ KONTROLLER:** Ekrandaki **YÖN BUTONLARI**, Klavyede **A / D** veya **Yön Tuşları**.")

    kiz_full_screen_html = """
    <div style="text-align:center; background:#11001c; padding:15px; border-radius:16px; border:3px solid #ff69b4; user-select:none;">
        <div id="kizFullCanvasContainer" style="width:100%; height:550px; border-radius:10px; overflow:hidden;"></div>
        <h2 id="kizScoreDisplay" style="color:#ff69b4; font-family:sans-serif; margin:10px 0; font-weight:bold;">Aura Enerjisi: 0 ⭐</h2>
        
        <!-- DOKUNMATİK / TIKLAMALI YÖN TUŞLARI PANELİ -->
        <div style="margin: 15px 0;">
            <button id="btnLeftKiz" style="padding: 15px 40px; font-size: 24px; font-weight:bold; background:#2d004d; color:#ff69b4; border:2px solid #ff69b4; border-radius:12px; cursor:pointer; margin-right:20px;">◀ SOL</button>
            <button id="btnRightKiz" style="padding: 15px 40px; font-size: 24px; font-weight:bold; background:#2d004d; color:#ff69b4; border:2px solid #ff69b4; border-radius:12px; cursor:pointer;">SAĞ ▶</button>
        </div>

        <button onclick="location.reload()" style="padding:10px 25px; font-size:14px; font-weight:bold; background:#ff69b4; color:#fff; border:none; border-radius:6px; cursor:pointer; box-shadow: 0 0 15px #ff69b4;">Evreni Yenile ✨</button>
    </div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script>
        const container = document.getElementById("kizFullCanvasContainer");
        const scene = new THREE.Scene(); scene.background = new THREE.Color(0x11001c);
        const camera = new THREE.PerspectiveCamera(60, container.clientWidth / 550, 0.1, 1000);
        const renderer = new THREE.WebGLRenderer({ antialias: true });
        renderer.setSize(container.clientWidth, 550); container.appendChild(renderer.domElement);
        const pLight = new THREE.PointLight(0xff69b4, 3, 100); pLight.position.set(0, 10, -5); scene.add(pLight);
        scene.add(new THREE.AmbientLight(0x3d0066));
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
        
        // Klavye Kontrolleri
        window.addEventListener("keydown", e => keys[e.key] = true); window.addEventListener("keyup", e => keys[e.key] = false);
        
        // Buton Kontrolleri (Dokunmatik ve Mouse)
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
                    if(Math.abs(playerMesh.position.x - o.position.x) < 1.4 && Math.abs(playerMesh.position.z - o.position.z) < 2.0) { gameOver = true; document.getElementById("kizScoreDisplay").innerHTML = "<span style='color:#ff69b4; font-size:24px;'>🔮 AURA DAĞILDI: Kuantum Boyutuna Işınlanıyorsun! 🔮</span>"; }
                });
            }
            renderer.render(scene, camera); requestAnimationFrame(animate);
        }
        animate();
    </script>
    """
    components.html(kiz_full_screen_html, height=760)
