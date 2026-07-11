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

# Sayfa Ayarları (Geniş ekran düzeni)
st.set_page_config(page_title="Apolingo 4D Quantum AI & Game Suit", page_icon="🚀", layout="wide")

# Yapay zekanın beynini ve hafızasını başlatıyoruz
if "client" not in st.session_state:
    st.session_state.client = Client()

# Spam engellemek için ses takip hafızası
if "son_islenen_ses_adi" not in st.session_state:
    st.session_state.son_islenen_ses_adi = None

# Oyun panelinin açık/kapalı olma durumu
if "oyun_panel_acik" not in st.session_state:
    st.session_state.oyun_panel_acik = False

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
# KODUN DEVASE ULTRA BEYNİ VE SİSTEM TALİMATI (SENİN TÜM MADDELERİN AYNEN İÇİNDE!)
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

# --- SOL VE SAĞ PANEL DÜZENİ ---
sol_taraf, sag_taraf = st.columns([0.50, 0.50])

with sol_taraf:
    st.title("🚀 APOLINGO ULTRA COSTA AI")
    st.caption("👨‍💻 Baş Geliştirici ve Kurucu Lider: Apolingo | **By Abdurrahim İriş**")
    st.write("---")

    for mesaj in st.session_state.sohbet_hafizasi:
        if mesaj["role"] == "user":
            with st.chat_message("user"):
                st.write(mesaj["content"])
        elif mesaj["role"] == "assistant":
            with st.chat_message("assistant"):
                st.write(mesaj["content"])

    gelen_soru = None

    c1, c2, c3 = st.columns([0.63, 0.13, 0.24])
    with c1:
        yazi_soru = st.chat_input("Buraya mesajını yaz be gardaşşşşş...")
        if yazi_soru:
            gelen_soru = yazi_soru
    with c2:
        ses_dosyasi = st.audio_input("🎙️")
    with c3:
        if not st.session_state.oyun_panel_acik:
            if st.button("🎮 Oyun Modu", use_container_width=True):
                st.session_state.oyun_panel_acik = True
                st.rerun()
        else:
            if st.button("🛑 Kapat", use_container_width=True):
                st.session_state.oyun_panel_acik = False
                st.rerun()

    if ses_dosyasi is not None:
        if st.session_state.son_islenen_ses_adi != ses_dosyasi.name:
            r = sr.Recognizer()
            try:
                with sr.AudioFile(ses_dosyasi) as source:
                    audio_data = r.record(source)
                    soylenen_soz = r.recognize_google(audio_data, language="tr-TR")
                    if soylenen_soz:
                        gelen_soru = soylenen_soz
                        st.session_state.son_islenen_ses_adi = ses_dosyasi.name
            except Exception as e:
                pass

    if gelen_soru:
        with st.chat_message("user"):
            st.write(gelen_soru)
        st.session_state.sohbet_hafizasi.append({"role": "user", "content": gelen_soru})
        soru_lower = gelen_soru.lower().strip()

        with st.spinner("🎶 Kız sesiyle okunuyor..."):
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
# SAĞ PANEL - FULLEDEN GÖRÜNEN 4D BMW M3 VE SİHİRLİ 4D ASTRO-AURA KIZ ODASI
# ==========================================================================================
with sag_taraf:
    st.subheader("🎮 APOLINGO QUANTUM REALM OYUN ALANI")
    st.write("---")
    
    if st.session_state.oyun_panel_acik:
        oyun_secimi = st.radio(
            "Gardaşşşşş boyutlar arası kodlama şovuna hoş geldin! Birini seç:",
            ["Henüz Seçmedim ⏳", "🏎️ FULLEDEN GÖRÜNEN 3D/4D BMW M3", "🌌 4D Sihirli Astro-Aura Kız Tasarım Odası"],
            index=0
        )
        st.write("---")

        if oyun_secimi == "🏎️ FULLEDEN GÖRÜNEN 3D/4D BMW M3":
            st.markdown("**🕹️ ULTRA KONTROL:** **A/D** veya **Yön Tuşları**. Kamera mükemmel açıda, gümüş canavar BMW M3 tüm ihtişamıyla tam gövde gözünün önünde!")
            
            bmw_full_3d_html = """
            <div style="text-align:center; background:#0d0d0d; padding:10px; border-radius:12px; border:2px solid #00ffff;">
                <div id="fullBmwContainer" style="width:100%; height:420px; border-radius:8px; overflow:hidden;"></div>
                <h3 id="scoreText4D" style="color:#00ffff; font-family:sans-serif; margin:10px 0;">4D Makas Skoru: 0</h3>
                <button onclick="location.reload()" style="padding:10px 20px; font-weight:bold; background:#00ffff; color:#000; border:none; border-radius:6px; cursor:pointer;">4. Boyuttan Yeniden Başla 🏎️</button>
            </div>
            <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
            <script>
                const container = document.getElementById("fullBmwContainer");
                const scene = new THREE.Scene();
                scene.background = new THREE.Color(0x0a0a16);

                // Kamerayı geriye ve hafif yukarı çekerek arabayı FULLEDEN gösteriyoruz
                const camera = new THREE.PerspectiveCamera(55, container.clientWidth / 420, 0.1, 1000);
                const renderer = new THREE.WebGLRenderer({ antialias: true });
                renderer.setSize(container.clientWidth, 420);
                container.appendChild(renderer.domElement);

                // Işıklar
                const light1 = new THREE.DirectionalLight(0xffffff, 1.8); light1.position.set(0, 30, 10); scene.add(light1);
                const light2 = new THREE.AmbientLight(0x444444); scene.add(light2);

                // Otoyol Pisti
                const roadGeo = new THREE.BoxGeometry(16, 0.1, 1000);
                const roadMat = new THREE.MeshStandardMaterial({ color: 0x1f1f1f, roughness: 0.5 });
                const road = new THREE.Mesh(roadGeo, roadMat); scene.add(road);

                // Yol şeritleri
                let lines = [];
                for(let i=0; i<20; i++){
                    let lGeo = new THREE.BoxGeometry(0.3, 0.15, 10);
                    let lMat = new THREE.MeshBasicMaterial({ color: 0xffffff });
                    let lMesh = new THREE.Mesh(lGeo, lMat);
                    lMesh.position.set(0, 0.1, -i * 40);
                    scene.add(lMesh); lines.push(lMesh);
                }

                # FULLEDEN GÖZÜKEN GERÇEKÇİ 3D BMW M3 GÖVDESİ
                const bmwM3 = new THREE.Group();
                
                // Alt Kasa ve Tekerlek Boşlukları
                const baseGeo = new THREE.BoxGeometry(1.8, 0.4, 4);
                const baseMat = new THREE.MeshStandardMaterial({ color: 0xcccccc, metalness: 0.9, roughness: 0.1 });
                const baseMesh = new THREE.Mesh(baseGeo, baseMat);
                baseMesh.position.y = 0.3;
                bmwM3.add(baseMesh);

                // Üst Tavan ve Cam Alanı
                const cabinGeo = new THREE.BoxGeometry(1.5, 0.5, 1.8);
                const cabinMat = new THREE.MeshStandardMaterial({ color: 0x222222, roughness: 0.0 });
                const cabinMesh = new THREE.Mesh(cabinGeo, cabinMat);
                cabinMesh.position.set(0, 0.75, -0.2);
                bmwM3.add(cabinMesh);

                // Arka Spoiler (Kanat)
                const spGeo = new THREE.BoxGeometry(1.7, 0.1, 0.3);
                const spMesh = new THREE.Mesh(spGeo, cabinMat);
                spMesh.position.set(0, 0.6, -1.8);
                bmwM3.add(spMesh);

                bmwM3.position.set(0, 0, -8);
                scene.add(bmwM3);

                // Trafikteki Diğer Araçlar
                let traffic = [];
                const colors = [0xffaa00, 0xff3333, 0x00aaff];
                for(let i=0; i<3; i++){
                    let tGeo = new THREE.BoxGeometry(1.8, 0.8, 3.8);
                    let tMat = new THREE.MeshLambertMaterial({ color: colors[i] });
                    let tMesh = new THREE.Mesh(tGeo, tMat);
                    tMesh.position.set((Math.random() - 0.5) * 11, 0.4, -70 - (i*40));
                    scene.add(tMesh); traffic.push(tMesh);
                }

                // Kamera Tam Arkada ve Muazzam Perspektifte (Arabayı Fullden Gösteriyor)
                camera.position.set(0, 4.2, -2);
                camera.lookAt(new THREE.Vector3(0, 0.5, -25));

                let score = 0; let gameOver = false; let keys = {};
                window.addEventListener("keydown", e => keys[e.key] = true);
                window.addEventListener("keyup", e => keys[e.key] = false);

                function loop() {
                    if(!gameOver) {
                        if(keys["ArrowLeft"] || keys["a"] || keys["A"]) { if(bmwM3.position.x > -6) bmwM3.position.x -= 0.18; }
                        if(keys["ArrowRight"] || keys["d"] || keys["D"]) { if(bmwM3.position.x < 6) bmwM3.position.x += 0.18; }

                        // Sonsuz Yol Akış Efekti
                        lines.forEach(l => {
                            l.position.z += 0.6 + (score * 0.02);
                            if(l.position.z > 10) l.position.z = -300;
                        });

                        // 4D Uzay Zaman Döngüsü (Skor arttıkça atmosfer pavyon gibi bükülür)
                        let pulse = Math.abs(Math.sin(score * 0.15));
                        scene.background.setRGB(0.02, 0.02 * pulse, 0.1 * (1 - pulse));

                        traffic.forEach(t => {
                            t.position.z += 0.6 + (score * 0.03);
                            if(t.position.z > -1) {
                                t.position.z = -140 - Math.random()*20;
                                t.position.x = (Math.random() - 0.5) * 11;
                                score++;
                                document.getElementById("scoreText4D").innerText = "4D Makas Skoru: " + score + " 🌀";
                            }
                            // Gelişmiş 3D Kutu Çarpışma Algoritması
                            if(Math.abs(bmwM3.position.x - t.position.x) < 1.6 && Math.abs(bmwM3.position.z - t.position.z) < 3.8) {
                                gameOver = true;
                                document.getElementById("scoreText4D").innerHTML = "<span style='color:red;'>💥 4D BOYUT YIRTILDI! BMW M3 PERT OLMUŞTUR! 💥</span>";
                            }
                        });
                    }
                    renderer.render(scene, camera);
                    requestAnimationFrame(loop);
                }
                loop();
            </script>
            """
            components.html(bmw_full_3d_html, height=540)

        elif oyun_secimi == "██ 4D Sihirli Astro-Aura Kız Tasarım Odası":
            st.markdown("**🌌 4D KOZMİK SİMÜLATÖR:** Kızlar için özel astrolojik aura odası! Alt taraftaki Zaman Akış butonuyla odayı **4. Boyutta (Gündüz, Gün Batımı, Gece, Siber Kuantum)** canlandır!")
            
            # Kızlar İçin 4D Zaman Akışlı Astro-Aura Tasarım Odası
            astro_4d_html = """
            <div style="text-align:center; background:#fff2fa; padding:15px; border-radius:15px; border:4px solid #da70d6; font-family:sans-serif; max-width:550px; margin:0 auto;">
                
                <div id="roomBox" style="width:100%; height:260px; background:linear-gradient(135deg, #ffedfa, #ffd3f0); border-radius:20px; position:relative; border:3px solid #ee82ee; transition:1s ease; overflow:hidden; box-shadow:0 6px 15px rgba(0,0,0,0.1);">
                    
                    <div id="roomWindow" style="position:absolute; top:20px; right:30px; width:90px; height:80px; background:#87ceeb; border:4px solid #fff; border-radius:10px; transition:1s; text-align:center; font-size:24px; line-height:70px;">☀️</div>
                    
                    <div style="position:absolute; bottom:20px; left:40px; width:120px; height:15px; background:#8b4513; border-radius:3px; z-index:2;"></div>
                    <div id="rgbMonitor" style="position:absolute; bottom:35px; left:65px; width:70px; height:45px; background:#111; border:3px solid #ff69b4; border-radius:5px; box-shadow: 0 0 15px #ff69b4; transition:0.5s; z-index:2; text-align:center; color:#fff; font-size:10px; line-height:40px; font-weight:bold;">Aura Active</div>
                    
                    <div style="position:absolute; top:0; left:50%; width:4px; height:30px; background:#333;"></div>
                    <div id="roomChandelier" style="position:absolute; top:30px; left:calc(50% - 15px); width:30px; height:30px; background:#ffff00; border-radius:50%; box-shadow: 0 0 20px #ffff00; transition:1s;"></div>
                    
                    <div style="position:absolute; bottom:20px; right:50px; font-size:32px; z-index:2;">🐱</div>
                </div>

                <div style="margin-top:15px; text-align:left; display:grid; grid-template-columns: 1fr 1fr; gap:10px;">
                    <div>
                        <h5 style="color:#ba55d3; margin:0 0 5px 0; border-bottom:2px solid #da70d6;">🔮 Neon Işık Rengi</h5>
                        <button onclick="changeNeon('#ff007f', 'Sıcak Pembe')" style="width:100%; padding:8px; background:#ff007f; color:white; border:none; margin-bottom:5px; border-radius:5px; cursor:pointer; font-weight:bold;">Sıcak Pembe Neon</button>
                        <button onclick="changeNeon('#00ffff', 'Galaksi Mavisi')" style="width:100%; padding:8px; background:#00ffff; color:black; border:none; border-radius:5px; cursor:pointer; font-weight:bold;">Galaksi Mavisi Neon</button>
                    </div>
                    <div>
                        <h5 style="color:#ba55d3; margin:0 0 5px 0; border-bottom:2px solid #da70d6;">🌀 4. BOYUT (ZAMAN AKIŞI)</h5>
                        <button onclick="shiftDimension('sunset')" style="width:100%; padding:8px; background:#ff8c00; color:white; border:none; margin-bottom:5px; border-radius:5px; cursor:pointer; font-weight:bold;">🌅 Gün Batımı Boyutu</button>
                        <button onclick="shiftDimension('cyber')" style="width:100%; padding:8px; background:#4b0082; color:white; border:none; border-radius:5px; cursor:pointer; font-weight:bold;">🌌 Siber Kuantum Gece</button>
                    </div>
                </div>
                
                <p id="auraStatus" style="background:#fff; color:#da70d6; font-weight:bold; padding:8px; margin-top:15px; border-radius:8px; border:1px solid #da70d6;">4D Oda Enerjisi: Dengeli Standart Zaman Modu ☀️</p>
            </div>

            <script>
                function changeNeon(hex, name) {
                    document.getElementById("rgbMonitor").style.borderColor = hex;
                    document.getElementById("rgbMonitor").style.boxShadow = "0 0 20px " + hex;
                    document.getElementById("auraStatus").innerText = "Neon Işık Değişti: " + name + " Aura Aktif! ⚡";
                }

                // 4D Zaman Mekan Bükülme Fonksiyonu
                function shiftDimension(mode) {
                    const room = document.getElementById("roomBox");
                    const win = document.getElementById("roomWindow");
                    const chan = document.getElementById("roomChandelier");
                    const status = document.getElementById("auraStatus");

                    if(mode === 'sunset') {
                        room.style.background = "linear-gradient(135deg, #ff7f50, #ff4500)";
                        win.style.background = "#ffaa00"; win.innerText = "🌇";
                        chan.style.background = "#ffda89"; chan.style.boxShadow = "0 0 25px #ffaa00";
                        status.innerText = "4D Zaman Büküldü: Büyülü Gün Batımı Modu! 🌅";
                    } else if(mode === 'cyber') {
                        room.style.background = "linear-gradient(135deg, #0f051d, #290b54)";
                        win.style.background = "#050014"; win.innerText = "🔮";
                        chan.style.background = "#00ffff"; chan.style.boxShadow = "0 0 30px #00ffff";
                        status.innerText = "4D Boyut Yırtılması: Siber Kuantum Gece Boyutu! 🌌🛸";
                    }
                }
            </script>
            """
            components.html(astro_4d_html, height=440)
            
        else:
            st.info("🎯 Panel açıldı be gardaşşşşş! Şimdi üstteki menüden 4D Full BMW veya 4D Astro-Aura Kız odasını seç!")
    else:
        st.warning("🕹️ Oyun alanı kilitli. Sol tarafta mikrofonun yanındaki '🎮 Oyun Modu' butonuna basarak eğlenceyi başlatabilirsin!")
