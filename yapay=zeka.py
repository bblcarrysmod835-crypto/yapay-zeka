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
st.set_page_config(page_title="Apolingo 4D Dimension Master AI", page_icon="🚀", layout="wide")

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
    "PUBG and Brawl Stars taktiklerini, 7. sınıf ders notlarını çok detaylı açıklayacaksın."
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
# SAĞ PANEL - GERÇEK 3D / 4D MOTORLU VE GERÇEK YÜZLÜ BARBIE OYUN SAHASI
# ==========================================================================================
with sag_taraf:
    st.subheader("🎮 APOLINGO MULTI-DIMENSIONAL ENGINE")
    st.write("---")
    
    if st.session_state.oyun_panel_acik:
        oyun_secimi = st.radio(
            "Gardaşşşşş boyutlar arası yolculuğa hazır mısın? Seçimini yap:",
            ["Henüz Seçmedim ⏳", "🏎️ 3D / 4D BMW M3 Otoban Simülatörü", "👗 Gerçek Yüzlü Barbie & Çorap Tasarımı"],
            index=0
        )
        st.write("---")

        if oyun_secimi == "🏎️ 3D / 4D BMW M3 Otoban Simülatörü":
            st.markdown("**🕹️ KONTROLLER:** Klavyeden **A/D** veya **Yön Tuşları**. Skor arttıkça **4. Boyut (Zaman Boyutu)** bükülür, otoyol geceye döner!")
            
            # Three.js ile Gerçek Üç Boyutlu Perspektif ve Zaman Akışlı (4D) Otoban Makas Oyunu
            bmw_4d_html = """
            <div style="text-align:center; background:#111; padding:10px; border-radius:12px;">
                <div id="canvas4dContainer" style="width:100%; height:400px; border-radius:8px; overflow:hidden;"></div>
                <h3 id="score4dText" style="color:#00ffff; font-family:sans-serif; margin:10px 0;">4D Boyut Makas Skoru: 0</h3>
                <button onclick="location.reload()" style="padding:10px 20px; font-weight:bold; background:#00ffff; color:#000; border:none; border-radius:6px; cursor:pointer;">Uzay-Zamanı Sıfırla (Yeniden Gazla) 🏎️</button>
            </div>
            <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
            <script>
                const container = document.getElementById("canvas4dContainer");
                const scene = new THREE.Scene();
                scene.background = new THREE.Color(0x221133); // 4D Kozmik Arka Plan

                const camera = new THREE.PerspectiveCamera(60, container.clientWidth / 400, 0.1, 1000);
                const renderer = new THREE.WebGLRenderer({ antialias: true });
                renderer.setSize(container.clientWidth, 400);
                container.appendChild(renderer.domElement);

                // Gerçekçi Işıklar
                const dirLight = new THREE.DirectionalLight(0xffffff, 1.5);
                dirLight.position.set(0, 20, 5);
                scene.add(dirLight);
                const ambient = new THREE.AmbientLight(0x333333);
                scene.add(ambient);

                // 3D Asfalt Zemini
                const roadGeo = new THREE.BoxGeometry(14, 0.1, 1000);
                const roadMat = new THREE.MeshLambertMaterial({ color: 0x222222 });
                const road = new THREE.Mesh(roadGeo, roadMat);
                scene.add(road);

                // GERÇEK 3D MODEL: Gümüş Gri BMW M3 Canavarı
                const bmwGroup = new THREE.Group();
                const bodyGeo = new THREE.BoxGeometry(1.6, 0.8, 3.4);
                const bodyMat = new THREE.MeshStandardMaterial({ color: 0xdcdcdc, roughness: 0.2, metalness: 0.8 });
                const body = new THREE.Mesh(bodyGeo, bodyMat);
                body.position.y = 0.5;
                bmwGroup.add(body);
                
                // 3D Camlar
                const glassGeo = new THREE.BoxGeometry(1.4, 0.4, 1.5);
                const glassMat = new THREE.MeshBasicMaterial({ color: 0x111111 });
                const glass = new THREE.Mesh(glassGeo, glassMat);
                glass.position.set(0, 0.9, -0.2);
                bmwGroup.add(glass);
                
                bmwGroup.position.set(0, 0, -10);
                scene.add(bmwGroup);

                // Trafikteki Diğer 3D Arabalar
                let targets = [];
                const tColors = [0xffcc00, 0x00ffcc, 0xff3366];
                for(let i=0; i<3; i++) {
                    let tGeo = new THREE.BoxGeometry(1.6, 0.8, 3.2);
                    let tMat = new THREE.MeshLambertMaterial({ color: tColors[i] });
                    let tMesh = new THREE.Mesh(tGeo, tMat);
                    tMesh.position.set((Math.random() - 0.5) * 10, 0.5, -60 - (i * 35));
                    scene.add(tMesh);
                    targets.push(tMesh);
                }

                camera.position.set(0, 5, -2);
                camera.lookAt(new THREE.Vector3(0, 1, -25));

                let score = 0; let gameOver = false; let keys = {};
                window.addEventListener("keydown", e => keys[e.key] = true);
                window.addEventListener("keyup", e => keys[e.key] = false);

                function tick() {
                    if(!gameOver) {
                        if(keys["ArrowLeft"] || keys["a"] || keys["A"]) { if(bmwGroup.position.x > -5) bmwGroup.position.x -= 0.15; }
                        if(keys["ArrowRight"] || keys["d"] || keys["D"]) { if(bmwGroup.position.x < 5) bmwGroup.position.x += 0.15; }

                        // 4D (Zaman Döngüsü) Efekti: Skor arttıkça gökyüzü ve ışık rengi değişerek uzay-zaman bükülür!
                        let timeColor = Math.sin(score * 0.1) * 0.5 + 0.5;
                        scene.background.setRGB(0.1 * timeColor, 0.05, 0.2 * (1 - timeColor));

                        targets.forEach(t => {
                            t.position.z += 0.5 + (score * 0.03); // Zamanla hız bükülmesi
                            if(t.position.z > -2) {
                                t.position.z = -120 - Math.random()*30;
                                t.position.x = (Math.random() - 0.5) * 10;
                                score++;
                                document.getElementById("score4dText").innerText = "4D Boyut Makas Skoru: " + score + " 🌀";
                            }
                            // 3D Çarpışma Testi
                            if(Math.abs(bmwGroup.position.x - t.position.x) < 1.5 && Math.abs(bmwGroup.position.z - t.position.z) < 3.2) {
                                gameOver = true;
                                document.getElementById("score4dText").innerHTML = "<span style='color:red;'>💥 4D ZAMAN DÖNGÜSÜ KIRILDI: BMW PERT! 💥</span>";
                            }
                        });
                    }
                    renderer.render(scene, camera);
                    requestAnimationFrame(tick);
                }
                tick();
            </script>
            """
            components.html(bmw_4d_html, height=520)

        elif oyun_secimi == "👗 Gerçek Yüzlü Barbie & Çorap Tasarımı":
            st.markdown("**💅 Gerçek Makyajlı Barbie Podyumu:** Sıfırdan çizilen gerçek yüze, dudaklara ve gözlere sahip Barbie kızımızın üzerine kıyafetleri ve çorapları hatasız ekle!")
            
            # Tam Detaylı Yüz Şablonu, Kirpikler ve Dudaklar Eklenmiş Gelişmiş Tasarım Stüdyosu
            barbie_yuzlu_html = """
            <div style="text-align:center; background:#fff0f5; padding:15px; border-radius:15px; border:4px solid #ff69b4; display:flex; justify-content:space-between; align-items:flex-start; font-family:sans-serif; max-width:560px; margin:0 auto;">
                
                <!-- GERÇEK DETAYLI YÜZLÜ BARBIE MODELİ -->
                <div style="width:170px; height:360px; background:#ffd1dc; border-radius:40px; position:relative; border:2px solid #ffb6c1; overflow:hidden; box-shadow: 0px 4px 12px rgba(0,0,0,0.2);">
                    
                    <!-- Muazzam Altın Sarısı Uzun Saçlar -->
                    <div style="position:absolute; top:8px; left:25px; width:120px; height:120px; background:#ffd700; border-radius:45px 45px 20px 20px; z-index:1;"></div>
                    
                    <!-- GERÇEKÇİ DETAYLI YÜZ MİMARİSİ -->
                    <div style="position:absolute; top:25px; left:55px; width:60px; height:60px; background:#ffdab9; border-radius:50%; z-index:2; border:1px solid #ffb6c1; box-shadow: inset 0 -2px 5px rgba(0,0,0,0.1);">
                        <!-- Mavi Büyük Gözler ve Kirpikler -->
                        <div style="position:absolute; top:18px; left:10px; width:10px; height:6px; background:#00bfff; border-radius:50%; border-top:2px solid #000;"></div>
                        <div style="position:absolute; top:18px; right:10px; width:10px; height:6px; background:#00bfff; border-radius:50%; border-top:2px solid #000;"></div>
                        <!-- Pembe Allıklar -->
                        <div style="position:absolute; top:26px; left:6px; width:10px; height:8px; background:#ff69b4; opacity:0.4; border-radius:50%;"></div>
                        <div style="position:absolute; top:26px; right:6px; width:10px; height:8px; background:#ff69b4; opacity:0.4; border-radius:50%;"></div>
                        <!-- Barbie Pembe Rujlu Dudakları -->
                        <div style="position:absolute; top:38px; left:20px; width:20px; height:6px; background:#ff1493; border-radius:3px 3px 8px 8px;"></div>
                    </div>
                    
                    <!-- Vücut Silüeti -->
                    <div style="position:absolute; top:90px; left:48px; width:74px; height:160px; background:#ffdab9; border-radius:15px; z-index:1;"></div>
                    <!-- Bacaklar -->
                    <div style="position:absolute; top:245px; left:56px; width:22px; height:95px; background:#ffdab9; z-index:1; border-right:2px solid #eab699;"></div>
                    <div style="position:absolute; top:245px; left:92px; width:22px; height:95px; background:#ffdab9; z-index:1;"></div>

                    <!-- KATMANLI GİYSİ MODÜLLERİ -->
                    <div id="uKatman" style="position:absolute; top:90px; left:46px; width:78px; height:65px; z-index:4; border-radius:6px; transition:0.2s;"></div>
                    <div id="aKatman" style="position:absolute; top:152px; left:48px; width:74px; height:90px; z-index:3; border-radius:0 0 12px 12px; transition:0.2s;"></div>
                    
                    <!-- ÇORAP KATMANLARI -->
                    <div id="cKatmanSol" style="position:absolute; top:250px; left:56px; width:22px; height:85px; z-index:2; transition:0.2s;"></div>
                    <div id="cKatmanSag" style="position:absolute; top:250px; left:92px; width:22px; height:85px; z-index:2; transition:0.2s;"></div>
                </div>
                
                <!-- STİL MAĞAZASI PANELİ -->
                <div style="text-align:left; width:240px; padding-left:5px;">
                    <h5 style="color:#ff1493; margin:0 0 5px 0; border-bottom:1px solid #ff69b4; font-size:14px;">👚 Üst Kıyafet</h5>
                    <button onclick="setU('#ff1493')" style="width:100%; padding:6px; background:#ff1493; color:white; border:none; margin-bottom:4px; border-radius:4px; font-weight:bold; cursor:pointer;">💖 Premium Pembe Top</button>
                    <button onclick="setU('#8a2be2')" style="width:100%; padding:6px; background:#8a2be2; color:white; border:none; margin-bottom:8px; border-radius:4px; font-weight:bold; cursor:pointer;">🔮 Gece Moru Bluz</button>
                    
                    <h5 style="color:#ff1493; margin:4px 0 5px 0; border-bottom:1px solid #ff69b4; font-size:14px;">👖 Alt Kıyafet</h5>
                    <button onclick="setA('#4682b4')" style="width:100%; padding:6px; background:#4682b4; color:white; border:none; margin-bottom:4px; border-radius:4px; font-weight:bold; cursor:pointer;">💙 Tasarım Kot Etek</button>
                    <button onclick="setA('#ffffff')" style="width:100%; padding:6px; background:#fff; color:#333; border:1px solid #ccc; margin-bottom:8px; border-radius:4px; font-weight:bold; cursor:pointer;">⚪ Kar Beyaz Şort</button>
                    
                    <h5 style="color:#ff1493; margin:4px 0 5px 0; border-bottom:1px solid #ff69b4; font-size:14px;">🧦 Çorap Entegrasyonu</h5>
                    <button onclick="setC('mesh')" style="width:100%; padding:6px; background:#222; color:white; border:none; margin-bottom:4px; border-radius:4px; font-weight:bold; cursor:pointer;">🖤 Siyah Fileli Çorap</button>
                    <button onclick="setC('pink')" style="width:100%; padding:6px; background:#ffb6c1; color:black; border:none; margin-bottom:4px; border-radius:4px; font-weight:bold; cursor:pointer;">🌸 Toz Pembe Çorap</button>
                    <button onclick="setC('none')" style="width:100%; padding:6px; background:#e0 e0e0; color:#333; border:none; border-radius:4px; font-weight:bold; cursor:pointer;">❌ Çorapsız Doğal Stil</button>
                    
                    <p id="infoText" style="color:#ff1493; font-weight:bold; font-size:12px; margin-top:12px; text-align:center; background:#fff; padding:6px; border-radius:6px; border:1px solid #ffb6c1;">Makyaj Tamam, Gardırop Hazır! ✨</p>
                </div>
            </div>
            
            <script>
                function setU(c) {
                    document.getElementById("uKatman").style.background = c;
                    document.getElementById("infoText").innerText = "Yüz Hatlarıyla Uyumlu Üst Seçildi! ✨";
                }
                function setA(c) {
                    document.getElementById("aKatman").style.background = c;
                    document.getElementById("infoText").innerText = "Etek/Şort Kombini Tamamlandı! 👗";
                }
                function setC(s) {
                    const l = document.getElementById("cKatmanSol");
                    const r = document.getElementById("cKatmanSag");
                    if(s === 'mesh') {
                        l.style.background = "repeating-linear-gradient(45deg, #111, #111 2px, transparent 2px, transparent 4px)";
                        r.style.background = "repeating-linear-gradient(45deg, #111, #111 2px, transparent 2px, transparent 4px)";
                    } else if(s === 'pink') {
                        l.style.background = "#ffb6c1"; r.style.background = "#ffb6c1";
                    } else {
                        l.style.background = "none"; r.style.background = "none";
                    }
                    document.getElementById("infoText").innerText = "Özel Çorap Kombine İşlendi! 🧦";
                }
            </script>
            """
            components.html(barbie_yuzlu_html, height=430)
            
        else:
            st.info("🎯 Panel açıldı be gardaşşşşş! Şimdi üstteki menüden 4D veya Makyajlı tasarım modunu seç!")
    else:
        st.warning("🕹️ Oyun alanı kilitli. Sol tarafta mikrofonun yanındaki '🎮 Oyun Modu' butonuna basarak eğlenceyi başlatabilirsin!")
