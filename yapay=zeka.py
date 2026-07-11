# BY ABDURRAHIM IRIŞ
# -*- coding: utf-8 -*-

import streamlit as st
import time
from g4f.client import Client
from gtts import gTTS
import os
import base64
import streamlit.components.v1 as components

# Sayfa Ayarları
st.set_page_config(page_title="Apolingo Full Frame Arcade AI", page_icon="🏎️", layout="wide")

# Yapay zekanın beynini ve hafızasını başlatıyoruz
if "client" not in st.session_state:
    st.session_state.client = Client()

# Oyun paneli hafızası
if "aktif_oyun" not in st.session_state:
    st.session_state.aktif_oyun = None

# Geçici ses hafızası
if "ses_girdisi" not in st.session_state:
    st.session_state.ses_girdisi = ""

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

# PROFESSIONAL UI / UX DESIGN (MİLİMETRİK HİZALAMA VE BİTİŞİK BUTONLAR)
st.markdown("""
    <style>
    .stApp {
        display: flex;
        flex-direction: column;
        justify-content: flex-end !important;
        height: 100vh;
    }
    
    /* Mesaj Giriş Alanı ve Ok Butonu Kusursuz Entegrasyonu */
    .modern-gonder-btn div[data-testid="stButton"] > button {
        background-color: #1e293b !important;
        color: #3b82f6 !important;
        border: 1px solid #3b82f6 !important;
        border-radius: 8px !important;
        height: 42px !important;
        width: 100% !important;
        font-size: 18px !important;
        font-weight: bold !important;
        margin-top: 0px !important;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .modern-gonder-btn div[data-testid="stButton"] > button:hover {
        background-color: #3b82f6 !important;
        color: white !important;
    }

    /* Sağdaki Bitişik Oyun Butonları */
    .sag-oyun-btn div[data-testid="stButton"] > button {
        border-radius: 8px !important;
        width: 44px !important;
        height: 42px !important;
        padding: 0 !important;
        font-size: 20px !important;
        background-color: #1e293b !important;
        border: 1px solid #4b5563 !important;
        box-shadow: 0 2px 4px rgba(0,0,0,0.15) !important;
    }
    .sag-oyun-btn div[data-testid="stButton"] > button:hover {
        border-color: #3b82f6 !important;
        background-color: #1e293b !important;
    }
    </style>
""", unsafe_allow_html=True)

gelen_soru = None

# ==========================================================================================
# GÖRÜNÜM KONTROLÜ
# ==========================================================================================
if st.session_state.aktif_oyun is None:
    st.title("🚀 APOLINGO MASTER ARCADE AI")
    st.caption("👨‍💻 Kurucu ve Baş Mühendis: Apolingo | **By Abdurrahim İriş**")
    st.write("---")

    # Mesaj geçmişi ekrana basılıyor
    for mesaj in st.session_state.sohbet_hafizasi:
        if mesaj["role"] == "user":
            with st.chat_message("user"):
                st.write(mesaj["content"])
        elif mesaj["role"] == "assistant":
            with st.chat_message("assistant"):
                st.write(mesaj["content"])

    # WEB API MİKROFON MOTORU (YAZI KUTUSUNA TARAYICI ENGELSİZ VERİ AKTARIMI)
    st.markdown("""
        <script>
        const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
        if (SpeechRecognition) {
            window.recognition = new SpeechRecognition();
            window.recognition.lang = 'tr-TR';
            window.recognition.continuous = false;
            window.recognition.interimResults = false;

            window.recognition.onresult = function(event) {
                const text = event.results[0][0].transcript;
                // Streamlit'in saklı query param mekanizması üzerinden senkronizasyon hattı
                const url = new URL(window.location.href);
                url.searchParams.set('voice_input', text);
                window.location.href = url.href;
            };
        }
        function startVoiceRecord() {
            if(window.recognition) { window.recognition.start(); }
        }
        </script>
    """, unsafe_allow_html=True)

    # URL parametresinden ses verisini yakalayıp hafızaya alma
    params = st.query_params
    if "voice_input" in params:
        st.session_state.ses_girdisi = params["voice_input"]
        # URL'i temizle ki sonsuz döngüye girmesin
        st.query_params.clear()

    # MASTER LAYOUT: TÜM SİSTEM TEK SATIRDA YAN YANA VE SAĞA YAPIŞIK OYUNLAR
    # %72 Mesaj alanı, %6 Yukarı bakan ok, %4 ve %4 Bitişik oyun butonları, %4 Mikrofon
    c_chat, c_arrow, c_g1, c_g2, c_mic = st.columns([0.72, 0.06, 0.04, 0.04, 0.04])
    
    with st.form(key="jilet_gibi_form", clear_on_submit=True):
        with c_chat:
            # Ses girdisi varsa varsayılan olarak kutuya yazar
            varsayilan_metin = st.session_state.ses_girdisi if st.session_state.ses_girdisi else ""
            yazi_soru = st.text_input("Mesajın:", value=varsayilan_metin, label_visibility="collapsed", placeholder="Mesajını yaz veya konuş be gardaşşşşş...")
        
        with c_arrow:
            # Mesaj kutusunun hemen sağında, tam hizalı yukarı bakan ok
            st.markdown('<div class="modern-gonder-btn">', unsafe_allow_html=True)
            gonder_btn = st.form_submit_button("▲")
            st.markdown('</div>', unsafe_allow_html=True)
            
        if gonder_btn and yazi_soru:
            gelen_soru = yazi_soru
            st.session_state.ses_girdisi = "" # Hafızayı temizle

    # Oyun ve Mikrofon butonları formun dışında, hemen sağında bitişik nizamda duruyor
    with c_g1:
        st.markdown('<div class="sag-oyun-btn">', unsafe_allow_html=True)
        if st.button("🏎️", key="rk_game"):
            st.session_state.aktif_oyun = "erkek"
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
        
    with c_g2:
        st.markdown('<div class="sag-oyun-btn">', unsafe_allow_html=True)
        if st.button("🌌", key="kz_game"):
            st.session_state.aktif_oyun = "kiz"
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    with c_mic:
        st.markdown('<div class="sag-oyun-btn">', unsafe_allow_html=True)
        # Mikrofon butonu tıklandığında tarayıcının ses motorunu tetikler
        if st.button("🎙️", key="native_mic_trigger"):
            st.components.v1.html("<script>window.parent.startVoiceRecord();</script>", height=0)
        st.markdown('</div>', unsafe_allow_html=True)

    # Girdi geldiğinde yapay zekayı tetikleme hattı
    if gelen_soru:
        with st.chat_message("user"):
            st.write(gelen_soru)
        st.session_state.sohbet_hafizasi.append({"role": "user", "content": gelen_soru})
        soru_lower = gelen_soru.lower().strip()

        with st.spinner("🎶 Apolingo Düşünüyor..."):
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
# OYUNLAR (STABİL ÇALIŞIYOR)
# ==========================================================================================
elif st.session_state.aktif_oyun == "erkek":
    sol_ust, sag_ust = st.columns([0.05, 0.95])
    with sol_ust:
        if st.button("❌"):
            st.session_state.aktif_oyun = None
            st.rerun()
    with sag_ust:
        st.markdown("### 🏎️ Apolingo Tam Gövde BMW M3 Makas Simülatörü")
    bmw_full_screen_html = """
    <div style="text-align:center; background:#05050a; padding:10px; border-radius:16px; border:3px solid #00ffcc; max-width:100%; touch-action:none;">
        <div id="bmwFullCanvasContainer" style="width:100%; height:420px; border-radius:10px; overflow:hidden;"></div>
        <div style="display:flex; justify-content:center; gap:40px; margin:15px 0;">
            <button id="mobSolBtn" style="width:75px; height:75px; border-radius:50%; background:#00ffcc; color:black; font-size:30px; font-weight:bold; border:none;">◀️</button>
            <button id="mobSagBtn" style="width:75px; height:75px; border-radius:50%; background:#00ffcc; color:black; font-size:30px; font-weight:bold; border:none;">▶️</button>
        </div>
        <h2 id="scoreDisplay4D" style="color:#00ffcc; font-family:sans-serif; margin:5px 0; font-size:18px;">4D Makas Skoru: 0 🌀</h2>
    </div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script>
        const container = document.getElementById("bmwFullCanvasContainer");
        const scene = new THREE.Scene(); scene.background = new THREE.Color(0x020208);
        const camera = new THREE.PerspectiveCamera(55, container.clientWidth / 420, 0.1, 1000);
        const renderer = new THREE.WebGLRenderer({ antialias: true });
        renderer.setSize(container.clientWidth, 420); container.appendChild(renderer.domElement);
        const lightTop = new THREE.DirectionalLight(0xffffff, 2.0); lightTop.position.set(0, 30, 15); scene.add(lightTop);
        scene.add(new THREE.AmbientLight(0x666666));
        const road = new THREE.Mesh(new THREE.BoxGeometry(16, 0.1, 1000), new THREE.MeshStandardMaterial({ color: 0x15151c })); scene.add(road);
        let lines = [];
        for(let i=0; i<20; i++){
            let lMesh = new THREE.Mesh(new THREE.BoxGeometry(0.25, 0.15, 10), new THREE.MeshBasicMaterial({ color: 0xffffff }));
            lMesh.position.set(0, 0.09, -i * 30); scene.add(lMesh); lines.push(lMesh);
        }
        const bmwM3 = new THREE.Group();
        const baseMesh = new THREE.Mesh(new THREE.BoxGeometry(1.4, 0.4, 3.0), new THREE.MeshStandardMaterial({ color: 0xdddddd, metalness:0.9 }));
        baseMesh.position.y = 0.28; bmwM3.add(baseMesh);
        const cabinMesh = new THREE.Mesh(new THREE.BoxGeometry(1.15, 0.45, 1.5), new THREE.MeshStandardMaterial({ color: 0x050505 }));
        cabinMesh.position.set(0, 0.65, -0.1); bmwM3.add(cabinMesh);
        bmwM3.position.set(0, 0, -8); scene.add(bmwM3);
        let traffic = []; const colors = [0xffaa00, 0xff3366, 0x00ccff, 0x9933ff];
        for(let i=0; i<4; i++){
            let tMesh = new THREE.Mesh(new THREE.IcosahedronGeometry(1.0, 1), new THREE.MeshStandardMaterial({ color: colors[i%4] }));
            tMesh.position.set((Math.random() - 0.5) * 11, 0.35, -50 - (i * 40)); scene.add(tMesh); traffic.push(tMesh);
        }
        camera.position.set(0, 4.2, -1.0); camera.lookAt(new THREE.Vector3(0, 0.5, -25));
        let score = 0; let gameOver = false; let keys = {}; let mobSol = false; let mobSag = false;
        window.addEventListener("keydown", e => keys[e.key] = true); window.addEventListener("keyup", e => keys[e.key] = false);
        document.getElementById("mobSolBtn").addEventListener("mousedown", () => mobSol = true);
        document.getElementById("mobSolBtn").addEventListener("mouseup", () => mobSol = false);
        document.getElementById("mobSagBtn").addEventListener("mousedown", () => mobSag = true);
        document.getElementById("mobSagBtn").addEventListener("mouseup", () => mobSag = false);
        function animate() {
            if(!gameOver) {
                if(keys["a"] || keys["A"] || mobSol) { if(bmwM3.position.x > -6.5) bmwM3.position.x -= 0.22; }
                if(keys["d"] || keys["D"] || mobSag) { if(bmwM3.position.x < 6.5) bmwM3.position.x += 0.22; }
                lines.forEach(l => { l.position.z += 0.75; if(l.position.z > 10) l.position.z = -280; });
                traffic.forEach(t => {
                    t.position.z += 0.75 + (score * 0.02);
                    if(t.position.z > 2) { t.position.z = -140; t.position.x = (Math.random() - 0.5) * 11; score++; document.getElementById("scoreDisplay4D").innerText = "4D Makas Skoru: " + score + " 🌀"; }
                    if(Math.abs(bmwM3.position.x - t.position.x) < 1.3 && Math.abs(bmwM3.position.z - t.position.z) < 2.8) { gameOver = true; document.getElementById("scoreDisplay4D").innerHTML = "<span style='color:red;'>💥 M3 PERT OLDU! 💥</span>"; }
                });
            }
            renderer.render(scene, camera); requestAnimationFrame(animate);
        }
        animate();
    </script>
    """
    components.html(bmw_full_screen_html, height=600)

elif st.session_state.aktif_oyun == "kiz":
    sol_ust, sag_ust = st.columns([0.05, 0.95])
    with sol_ust:
        if st.button("❌"):
            st.session_state.aktif_oyun = None
            st.rerun()
    with sag_ust:
        st.markdown("### 🌌 Kızlar İçin Özel: 4D Astro-Aura Kuantum Kaçış Oyunu")
    kiz_full_screen_html = """
    <div style="text-align:center; background:#11001c; padding:10px; border-radius:16px; border:3px solid #ff69b4; max-width:100%; touch-action:none;">
        <div id="kizFullCanvasContainer" style="width:100%; height:420px; border-radius:10px; overflow:hidden;"></div>
        <div style="display:flex; justify-content:center; gap:40px; margin:15px 0;">
            <button id="kizMobSolBtn" style="width:75px; height:75px; border-radius:50%; background:#ff69b4; color:white; font-size:30px; border:none;">◀️</button>
            <button id="kizMobSagBtn" style="width:75px; height:75px; border-radius:50%; background:#ff69b4; color:white; font-size:30px; border:none;">▶️</button>
        </div>
        <h2 id="kizScoreDisplay" style="color:#ff69b4; font-family:sans-serif; margin:5px 0; font-size:18px;">Aura Enerjisi: 0 ⭐</h2>
    </div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script>
        const container = document.getElementById("kizFullCanvasContainer");
        const scene = new THREE.Scene(); scene.background = new THREE.Color(0x11001c);
        const camera = new THREE.PerspectiveCamera(60, container.clientWidth / 420, 0.1, 1000);
        const renderer = new THREE.WebGLRenderer({ antialias: true });
        renderer.setSize(container.clientWidth, 420); container.appendChild(renderer.domElement);
        scene.add(new THREE.PointLight(0xff69b4, 3, 100)); scene.add(new THREE.AmbientLight(0x3d0066));
        const playerMesh = new THREE.Mesh(new THREE.ConeGeometry(0.8, 2.0, 4), new THREE.MeshStandardMaterial({ color: 0xff007f }));
        playerMesh.rotation.x = Math.PI / 2; playerMesh.position.set(0, 0, -6); scene.add(playerMesh);
        let obstacles = []; const obsColors = [0x00ffff, 0xba55d3, 0xff69b4];
        for(let i=0; i<4; i++){
            let oMesh = new THREE.Mesh(new THREE.IcosahedronGeometry(1.0, 1), new THREE.MeshStandardMaterial({ color: obsColors[i%3] }));
            oMesh.position.set((Math.random() - 0.5) * 12, 0, -40 - (i * 30)); scene.add(oMesh); obstacles.push(oMesh);
        }
        camera.position.set(0, 5, 2); camera.lookAt(new THREE.Vector3(0, -0.5, -20));
        let score = 0; let gameOver = false; let keys = {}; let mobSol = false; let mobSag = false;
        window.addEventListener("keydown", e => keys[e.key] = true); window.addEventListener("keyup", e => keys[e.key] = false);
        function animate() {
            if(!gameOver) {
                if(keys["a"] || mobSol) { if(playerMesh.position.x > -6.5) playerMesh.position.x -= 0.20; }
                if(keys["d"] || mobSag) { if(playerMesh.position.x < 6.5) playerMesh.position.x += 0.20; }
                playerMesh.rotation.z += 0.04;
                obstacles.forEach(o => {
                    o.position.z += 0.6;
                    if(o.position.z > 5) { o.position.z = -120; o.position.x = (Math.random() - 0.5) * 12; score++; document.getElementById("kizScoreDisplay").innerText = "Aura Enerjisi: " + score + " ⭐"; }
                    if(Math.abs(playerMesh.position.x - o.position.x) < 1.3 && Math.abs(playerMesh.position.z - o.position.z) < 2.0) { gameOver = true; document.getElementById("kizScoreDisplay").innerHTML = "<span style='color:#ff69b4;'>🔮 AURA DAĞILDI! 🔮</span>"; }
                });
            }
            renderer.render(scene, camera); requestAnimationFrame(animate);
        }
        animate();
    </script>
    """
    components.html(kiz_full_screen_html, height=600)
