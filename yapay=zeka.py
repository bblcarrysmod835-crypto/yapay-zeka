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
st.set_page_config(page_title="Apolingo Full Frame Arcade AI", page_icon="🏎️", layout="wide")

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

# --- SOL VE SAĞ PANEL YERLEŞİMİ ---
sol_taraf, sag_taraf = st.columns([0.50, 0.50])

with sol_taraf:
    st.title("🚀 APOLINGO MASTER ARCADE")
    st.caption("👨‍💻 Kurucu ve Baş Mühendis: Apolingo | **By Abdurrahim İriş**")
    st.write("---")

    # Mesaj geçmişini yazdırma
    for mesaj in st.session_state.sohbet_hafizasi:
        if mesaj["role"] == "user":
            with st.chat_message("user"):
                st.write(mesaj["content"])
        elif mesaj["role"] == "assistant":
            with st.chat_message("assistant"):
                st.write(mesaj["content"])

    gelen_soru = None

    # MİKROFONUN YANINA YUVARLAK VE GÖRSEL BUTON YERLEŞİMİ (EKRANI KAPLAMAZ)
    c1, c2, c3 = st.columns([0.76, 0.12, 0.12])
    with c1:
        yazi_soru = st.chat_input("Buraya yaz be gardaşşşşş...")
        if yazi_soru:
            gelen_soru = yazi_soru
    with c2:
        ses_dosyasi = st.audio_input("🎙️")
    with c3:
        # Yuvarlak, şık, ikonik buton tasarımı (CSS ile özelleştirilmiş buton taklidi)
        if not st.session_state.oyun_panel_acik:
            if st.button("🎮", help="Oyun Modunu Başlat be Gardaşşş!", use_container_width=True):
                st.session_state.oyun_panel_acik = True
                st.rerun()
        else:
            if st.button("🟢", help="Oyun Modu Açık", use_container_width=True):
                pass

    # Sesli girdi işleme
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

        with st.spinner("🎶 Seslendiriliyor..."):
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
# SAĞ PANEL - FULL SCREEN ARCADE LOBİSİ (SOL ÜSTTEKİ ÇARPI İŞARETİYLE YAPAY ZEKAYA DÖNÜŞ)
# ==========================================================================================
with sag_taraf:
    if st.session_state.oyun_panel_acik:
        # SOL ÜST KÖŞEYE GERİ DÖNÜŞ SAĞLAYAN ÇARPI BUTONU VE SEÇİM MENÜSÜ
        üst_kutu1, üst_kutu2 = st.columns([0.15, 0.85])
        with üst_kutu1:
            if st.button("❌", help="Yapay Zekaya Geri Dön"):
                st.session_state.oyun_panel_acik = False
                st.rerun()
        with üst_kutu2:
            oyun_secimi = st.radio(
                "Apolingo Oyun Merkezindesin Gardaşşşşş! Seçimini Yap:",
                ["🏎️ Erkek Oyunu: Küçültülmüş Tam Gövde BMW M3", "🌌 Kız Oyunu: 4D Astro-Aura Tasarım Odası"],
                label_visibility="collapsed"
            )
        st.write("---")

        if oyun_secimi == "🏎️ Erkek Oyunu: Küçültülmüş Tam Gövde BMW M3":
            st.markdown("**🕹️ OYNANIŞ:** **A / D** veya **Yön Tuşları**. Araba biraz küçültüldü ve tam kadraj full gövde görünüyor!")
            
            bmw_kucuk_full_html = """
            <div style="text-align:center; background:#0a0a0a; padding:10px; border-radius:12px; border:2px solid #00ffcc;">
                <div id="bmwArcadeContainer" style="width:100%; height:410px; border-radius:8px; overflow:hidden;"></div>
                <h4 id="score4D" style="color:#00ffcc; font-family:sans-serif; margin:10px 0;">4D Makas Skoru: 0</h4>
                <button onclick="location.reload()" style="padding:8px 16px; font-weight:bold; background:#00ffcc; color:#000; border:none; border-radius:4px; cursor:pointer;">Pisti Yenile 🏎️</button>
            </div>
            <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
            <script>
                const container = document.getElementById("bmwArcadeContainer");
                const scene = new THREE.Scene();
                scene.background = new THREE.Color(0x05050f);

                const camera = new THREE.PerspectiveCamera(50, container.clientWidth / 410, 0.1, 1000);
                const renderer = new THREE.WebGLRenderer({ antialias: true });
                renderer.setSize(container.clientWidth, 410);
                container.appendChild(renderer.domElement);

                const light1 = new THREE.DirectionalLight(0xffffff, 1.8); light1.position.set(0, 25, 10); scene.add(light1);
                const light2 = new THREE.AmbientLight(0x555555); scene.add(light2);

                // Pist Genişliği Ayarı
                const roadGeo = new THREE.BoxGeometry(14, 0.1, 1000);
                const roadMat = new THREE.MeshStandardMaterial({ color: 0x1a1a1a, roughness: 0.6 });
                const road = new THREE.Mesh(roadGeo, roadMat); scene.add(road);

                let lines = [];
                for(let i=0; i<15; i++){
                    let lGeo = new THREE.BoxGeometry(0.2, 0.12, 8);
                    let lMat = new THREE.MeshBasicMaterial({ color: 0xffffff });
                    let lMesh = new THREE.Mesh(lGeo, lMat);
                    lMesh.position.set(0, 0.08, -i * 35);
                    scene.add(lMesh); lines.push(lMesh);
                }

                // ARABA BİRAZ KÜÇÜLTÜLDÜ VE FULL GÖRÜNECEK ŞEKİLDE TASARLANDI
                const bmwM3 = new THREE.Group();
                
                // Küçültülmüş Alt Gövde (Ölçek düşürüldü)
                const baseGeo = new THREE.BoxGeometry(1.3, 0.35, 2.9);
                const baseMat = new THREE.MeshStandardMaterial({ color: 0xc0c0c0, metalness: 0.85, roughness: 0.15 });
                const baseMesh = new THREE.Mesh(baseGeo, baseMat);
                baseMesh.position.y = 0.25;
                bmwM3.add(baseMesh);

                // Küçültülmüş Kabin/Tavan
                const cabinGeo = new THREE.BoxGeometry(1.1, 0.4, 1.4);
                const cabinMat = new THREE.MeshStandardMaterial({ color: 0x111111, roughness: 0.1 });
                const cabinMesh = new THREE.Mesh(cabinGeo, cabinMat);
                cabinMesh.position.set(0, 0.6, -0.1);
                bmwM3.add(cabinMesh);

                // Spoiler
                const spGeo = new THREE.BoxGeometry(1.2, 0.08, 0.2);
                const spMesh = new THREE.Mesh(spGeo, cabinMat);
                spMesh.position.set(0, 0.5, -1.3);
                bmwM3.add(spMesh);

                bmwM3.position.set(0, 0, -8);
                scene.add(bmwM3);

                // Küçük Trafik Araçları
                let traffic = [];
                const colors = [0xffbb00, 0xff2255, 0x00bfff];
                for(let i=0; i<3; i++){
                    let tGeo = new THREE.BoxGeometry(1.3, 0.6, 2.7);
                    let tMat = new THREE.MeshLambertMaterial({ color: colors[i] });
                    let tMesh = new THREE.Mesh(tGeo, tMat);
                    tMesh.position.set((Math.random() - 0.5) * 10, 0.3, -60 - (i * 35));
                    scene.add(tMesh); traffic.push(tMesh);
                }

                // Kameranın Kusursuz Full Görüş Konumu (Gövdeyi Net Gösterir)
                camera.position.set(0, 3.8, -1.5);
                camera.lookAt(new THREE.Vector3(0, 0.4, -20));

                let score = 0; let gameOver = false; let keys = {};
                window.addEventListener("keydown", e => keys[e.key] = true);
                window.addEventListener("keyup", e => keys[e.key] = false);

                function animate() {
                    if(!gameOver) {
                        if(keys["ArrowLeft"] || keys["a"] || keys["A"]) { if(bmwM3.position.x > -5) bmwM3.position.x -= 0.15; }
                        if(keys["ArrowRight"] || keys["d"] || keys["D"]) { if(bmwM3.position.x < 5) bmwM3.position.x += 0.15; }

                        lines.forEach(l => {
                            l.position.z += 0.55 + (score * 0.02);
                            if(l.position.z > 8) l.position.z = -250;
                        });

                        // 4D Atmosfer Döngüsü
                        let phase = Math.abs(Math.sin(score * 0.2));
                        scene.background.setRGB(0.01, 0.03 * phase, 0.08 * (1 - phase));

                        traffic.forEach(t => {
                            t.position.z += 0.55 + (score * 0.03);
                            if(t.position.z > 0) {
                                t.position.z = -120 - Math.random()*25;
                                t.position.x = (Math.random() - 0.5) * 10;
                                score++;
                                document.getElementById("score4D").innerText = "4D Makas Skoru: " + score + " 🌀";
                            }
                            // Optimize Çarpışma Kutusu
                            if(Math.abs(bmwM3.position.x - t.position.x) < 1.2 && Math.abs(bmwM3.position.z - t.position.z) < 2.8) {
                                gameOver = true;
                                document.getElementById("score4D").innerHTML = "<span style='color:red;'>💥 4D MATRIX DAĞILDI: M3 PERT! 💥</span>";
                            }
                        });
                    }
                    renderer.render(scene, camera);
                    requestAnimationFrame(animate);
                }
                animate();
            </script>
            """
            components.html(bmw_kucuk_full_html, height=520)

        elif oyun_secimi == "🌌 Kız Oyunu: 4D Astro-Aura Tasarım Odası":
            st.markdown("**🌌 4D AURA SEÇİMİ:** Kızlar için özel tasarlanmış kuantum oda! Zaman Akış butonlarıyla evrenin aurasını değiştir!")
            
            kiz_odasi_html = """
            <div style="text-align:center; background:#fff5fa; padding:15px; border-radius:15px; border:3px solid #ff69b4; font-family:sans-serif; max-width:520px; margin:0 auto;">
                <div id="astroRoom" style="width:100%; height:250px; background:linear-gradient(135deg, #ffeef8, #ffcceb); border-radius:15px; position:relative; border:2px solid #ff69b4; transition:1s ease; overflow:hidden;">
                    <div id="astroWin" style="position:absolute; top:20px; right:30px; width:80px; height:70px; background:#87ceeb; border:3px solid #fff; border-radius:8px; transition:1s; text-align:center; font-size:22px; line-height:60px;">☀️</div>
                    <div style="position:absolute; bottom:20px; left:40px; width:110px; height:12px; background:#8b4513; border-radius:2px;"></div>
                    <div id="neonMon" style="position:absolute; bottom:32px; left:60px; width:65px; height:40px; background:#222; border:2px solid #ff007f; border-radius:4px; box-shadow: 0 0 12px #ff007f; text-align:center; color:#fff; font-size:9px; line-height:36px; font-weight:bold;">Apolingo</div>
                    <div style="position:absolute; bottom:20px; right:40px; font-size:28px;">🐱</div>
                </div>
                <div style="margin-top:15px; display:grid; grid-template-columns: 1fr 1fr; gap:10px; text-align:left;">
                    <div>
                        <h5 style="color:#ff69b4; margin:0 0 5px 0;">🌸 Neon Rengi</h5>
                        <button onclick="setNeon('#ff007f')" style="width:100%; padding:6px; background:#ff007f; color:white; border:none; margin-bottom:4px; border-radius:4px; cursor:pointer;">Pembe Neon</button>
                        <button onclick="setNeon('#00ffff')" style="width:100%; padding:6px; background:#00ffff; color:black; border:none; border-radius:4px; cursor:pointer;">Turkuaz Neon</button>
                    </div>
                    <div>
                        <h5 style="color:#ff69b4; margin:0 0 5px 0;">⏳ 4D Zaman Akışı</h5>
                        <button onclick="setDim('sunset')" style="width:100%; padding:6px; background:#ff8c00; color:white; border:none; margin-bottom:4px; border-radius:4px; cursor:pointer;">🌅 Gün Batımı</button>
                        <button onclick="setDim('cyber')" style="width:100%; padding:6px; background:#4b0082; color:white; border:none; border-radius:4px; cursor:pointer;">🌌 Siber Gece</button>
                    </div>
                </div>
                <p id="auraState" style="background:#fff; color:#ff69b4; font-weight:bold; padding:6px; margin-top:12px; border-radius:6px; font-size:12px; border:1px solid #ff69b4;">Sistem Aktif: 4D Standart Gün Işığı ☀️</p>
            </div>
            <script>
                function setNeon(h) {
                    document.getElementById("neonMon").style.borderColor = h;
                    document.getElementById("neonMon").style.boxShadow = "0 0 15px " + h;
                }
                function setDim(m) {
                    const r = document.getElementById("astroRoom");
                    const w = document.getElementById("astroWin");
                    const s = document.getElementById("auraState");
                    if(m === 'sunset') {
                        r.style.background = "linear-gradient(135deg, #ff7f50, #ff4500)"; w.background = "#ffaa00"; w.innerText = "🌇";
                        s.innerText = "4D Zaman Modu: Romantik Gün Batımı 🌅";
                    } else if(m === 'cyber') {
                        r.style.background = "linear-gradient(135deg, #11052c, #3d0c5a)"; w.background = "#0f001a"; w.innerText = "🔮";
                        s.innerText = "4D Zaman Modu: Kuantum Siber Gece 🌌";
                    }
                }
            </script>
            """
            components.html(kiz_odasi_html, height=420)
            
    else:
        # Oyun kapalıyken lobi alanında duracak tatlı bir bilgilendirme ekranı
        st.info("🎯 Lobi Modu Beklemede be Gardaşşşşş! Sol tarafta, chat girişinin en sağındaki yuvarlak `🎮` butonuna bastığın an oyun odası buraya full kadraj açılacak!")
