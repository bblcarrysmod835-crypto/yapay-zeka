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
st.set_page_config(page_title="Apolingo Ultra Costa AI & 3D Game", page_icon="🚀", layout="wide")

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
    "ve işlemcibadge'lerinden, RAM yetersizliğinden ve bilgisayara virüs bulaşma hikayelerinden mizahi ve aşırı detaylı bahsedeceksin. "
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
sol_taraf, sag_taraf = st.columns([0.55, 0.45])

with sol_taraf:
    st.title("🚀 APOLINGO ULTRA COSTA AI")
    st.caption("👨‍💻 Baş Geliştirici ve Kurucu Lider: Apolingo | **By Abdurrahim İriş**")
    st.write("---")

    # Eski mesajları listele
    for mesaj in st.session_state.sohbet_hafizasi:
        if mesaj["role"] == "user":
            with st.chat_message("user"):
                st.write(mesaj["content"])
        elif mesaj["role"] == "assistant":
            with st.chat_message("assistant"):
                st.write(mesaj["content"])

    gelen_soru = None

    # MİKROFONUN YANINA BUTON YERLEŞTİRME ALANI
    c1, c2, c3 = st.columns([0.65, 0.15, 0.20])
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

    # Ses Tanımlama Motoru
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

    # AI Cevap İşleme Motoru
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
# SAĞ PANEL - DEVRİM NİTELİĞİNDE 3D WEBGL OYUN MERKEZİ (THREE.JS ENTEGRELİ)
# ==========================================================================================
with sag_taraf:
    st.subheader("🎮 APOLINGO 3D GAME MATRIX")
    st.write("---")
    
    if st.session_state.oyun_panel_acik:
        oyun_secimi = st.radio(
            "Gardaşşşşş ne oynamak istersin? Seçimini yap 3D motor ateşlensin:",
            ["Henüz Seçmedim ⏳", "🏎️ 3D BMW M3 Otoban Makas", "👗 3D Barbie Kıyafet Tasarımı"],
            index=0
        )
        st.write("---")

        if oyun_secimi == "🏎️ 3D BMW M3 Otoban Makas":
            st.markdown("**🕹️ 3D KONTROLLER:** Klavyeden **A / D** veya **Sol / Sağ Ok Tuşları** ile gümüş renkli 3D BMW M3'ü sağa sola kır, diğer arabalara makas at!")
            
            # THREE.JS ile 3D Araba Makas Atma Oyunu
            bmw_3d_html = """
            <div style="text-align:center; background:#111; padding:10px; border-radius:10px;">
                <div id="game3dContainer" style="width:100%; height:400px; border-radius:8px; overflow:hidden;"></div>
                <h3 id="score3dBoard" style="color:white; font-family:sans-serif; margin:10px 0;">3D Makas Skoru: 0</h3>
                <button onclick="location.reload()" style="padding:10px 20px; font-weight:bold; background:#e60000; color:white; border:none; border-radius:5px; cursor:pointer;">Kazadan Sonra Yeniden Gazla! 🏎️</button>
            </div>
            
            <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
            <script>
                const container = document.getElementById("game3dContainer");
                const scene = new THREE.Scene();
                scene.background = new THREE.Color(0x1a1a1a);
                scene.fog = new THREE.FogExp2(0x1a1a1a, 0.015);

                const camera = new THREE.PerspectiveCamera(60, container.clientWidth / 400, 0.1, 1000);
                const renderer = new THREE.WebGLRenderer({ antialias: true });
                renderer.setSize(container.clientWidth, 400);
                container.appendChild(renderer.domElement);

                // Işıklandırma
                const light = new THREE.DirectionalLight(0xffffff, 1.2);
                light.position.set(0, 20, 10).normalize();
                scene.add(light);
                scene.add(new THREE.AmbientLight(0x404040));

                // 3D Sonsuz Otoban Pisti
                const roadGeo = new THREE.PlaneGeometry(20, 1000);
                const roadMat = new THREE.MeshLambertMaterial({ color: 0x333333 });
                const road = new THREE.Mesh(roadGeo, roadMat);
                road.rotation.x = -Math.PI / 2;
                scene.add(road);

                // Bizim Efsanevi 3D BMW M3 (Gümüş Gri Kutu Gövde Üzerine Detaylar)
                const bmwGeo = new THREE.BoxGeometry(1.6, 1, 3);
                const bmwMat = new THREE.MeshLambertMaterial({ color: 0xc0c0c0 }); // Metalik gümüş
                const playerBMW = new THREE.Mesh(bmwGeo, bmwMat);
                playerBMW.position.set(0, 0.5, -5);
                scene.add(playerBMW);

                // Trafikteki 3D Arabalar
                let enemies = [];
                const colors = [0xffcc00, 0x00ccff, 0xff3333];
                for(let i=0; i<3; i++) {
                    let enGeo = new THREE.BoxGeometry(1.6, 1, 3);
                    let enMat = new THREE.MeshLambertMaterial({ color: colors[i] });
                    let enMesh = new THREE.Mesh(enGeo, enMat);
                    enMesh.position.set((Math.random() - 0.5) * 12, 0.5, -50 - (i * 30));
                    scene.add(enMesh);
                    enemies.push(enMesh);
                }

                // Kamera yerleşimi (Araba arkası kokpit/takip açısı)
                camera.position.set(0, 4, 3);
                camera.lookAt(new THREE.Vector3(0, 1, -15));

                let score = 0;
                let gameOver = false;
                let keys = {};

                window.addEventListener("keydown", e => keys[e.key] = true);
                window.addEventListener("keyup", e => keys[e.key] = false);

                function animate() {
                    if (!gameOver) {
                        // BMW Kontrol mekanizması
                        if (keys["ArrowLeft"] || keys["a"] || keys["A"]) { if(playerBMW.position.x > -5) playerBMW.position.x -= 0.15; }
                        if (keys["ArrowRight"] || keys["d"] || keys["D"]) { if(playerBMW.position.x < 5) playerBMW.position.x += 0.15; }

                        // Trafik akış motoru
                        enemies.forEach(en => {
                            en.position.z += 0.4 + (score * 0.02); // Skor arttıkça hızlanır!
                            if (en.position.z > 5) {
                                en.position.z = -100 - Math.random()*20;
                                en.position.x = (Math.random() - 0.5) * 10;
                                score++;
                                document.getElementById("score3dBoard").innerText = "3D Makas Skoru: " + score;
                            }

                            // 3D Çarpışma Kutusu Algılaması (AABB)
                            if (Math.abs(playerBMW.position.x - en.position.x) < 1.5 && Math.abs(playerBMW.position.z - en.position.z) < 3) {
                                gameOver = true;
                                document.getElementById("score3dBoard").innerHTML = "<span style='color:red;'>💥 BMW M3 PERT OLDU! 💥</span>";
                            }
                        });
                    }
                    renderer.render(scene, camera);
                    requestAnimationFrame(animate);
                }
                animate();
            </script>
            """
            components.html(bmw_3d_html, height=520)

        elif oyun_secimi == "👗 3D Barbie Kıyafet Tasarımı":
            st.markdown("**✨ 3D Barbie Tasarım Podyumu:** Gardıroptan butonlara basarak Barbie'ye elbiseler giydir, 3D model podyumda anlık olarak değişsin!")
            
            # THREE.JS ile 3D Dönen Barbie Modeli Kıyafet Giydirme Simülatörü
            barbie_3d_html = """
            <div style="text-align:center; background:#fff0f5; padding:15px; border-radius:15px; border:4px solid #ff69b4; display:flex; justify-content:space-between; align-items:center;">
                
                <!-- 3D PODYUM ALANI -->
                <div id="barbie3dCanvas" style="width:200px; height:340px; background:#ffe4e1; border-radius:20px; overflow:hidden;"></div>
                
                <!-- DİNAMİK GARDIROP BUTONLARI -->
                <div style="text-align:left; width:200px;">
                    <h4 style="color:#ff1493; margin:0 0 10px 0; border-bottom:2px solid #ff69b4;">👗 3D Elbise Seçimi</h4>
                    <button onclick="change3DStyle(0xff69b4, '💖 Pembe Kokteyl Elbisesi')" style="width:100%; padding:10px; background:#ff69b4; color:white; border:none; margin-bottom:6px; border-radius:6px; font-weight:bold; cursor:pointer;">💖 Pembe Elbise</button>
                    <button onclick="change3DStyle(0x8a2be2, '🔮 Mor Parti Elbisesi')" style="width:100%; padding:10px; background:#8a2be2; color:white; border:none; margin-bottom:6px; border-radius:6px; font-weight:bold; cursor:pointer;">🔮 Mor Elbise</button>
                    <button onclick="change3DStyle(0x222222, '🖤 Asil Siyah Gece Kıyafeti')" style="width:100%; padding:10px; background:#222; color:white; border:none; margin-bottom:6px; border-radius:6px; font-weight:bold; cursor:pointer;">🖤 Siyah Elbise</button>
                    <button onclick="change3DStyle(0x4682b4, '💙 Günlük Denim Tarzı')" style="width:100%; padding:10px; background:#4682b4; color:white; border:none; margin-bottom:6px; border-radius:6px; font-weight:bold; cursor:pointer;">💙 Denim Kombin</button>
                    
                    <p id="barbieLabel" style="color:#ff1493; font-weight:bold; font-size:12px; margin-top:10px; text-align:center;">Kombin Seçimi Bekleniyor...</p>
                </div>
            </div>
            
            <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
            <script>
                const bContainer = document.getElementById("barbie3dCanvas");
                const bScene = new THREE.Scene();
                bScene.background = new THREE.Color(0xffe4e1);

                const bCamera = new THREE.PerspectiveCamera(50, 200 / 340, 0.1, 100);
                const bRenderer = new THREE.WebGLRenderer({ antialias: true });
                bRenderer.setSize(200, 340);
                bContainer.appendChild(bRenderer.domElement);

                // Aydınlatma Şovları
                const bLight = new THREE.DirectionalLight(0xffffff, 1.5);
                bLight.position.set(5, 10, 5).normalize();
                bScene.add(bLight);
                bScene.add(new THREE.AmbientLight(0x555555));

                // 3D Barbie Silüeti Tasarımı (Kafa, Saç ve Elbise Katmanları)
                const group = new THREE.Group();

                // Barbie Kafası
                const headGeo = new THREE.SphereGeometry(0.5, 32, 32);
                const headMat = new THREE.MeshLambertMaterial({ color: 0xffdab9 });
                const head = new THREE.Mesh(headGeo, headMat);
                head.position.y = 1.6;
                group.add(head);

                // Barbie'nin Efsanevi 3D Altın Sarısı Saçları
                const hairGeo = new THREE.SphereGeometry(0.54, 32, 32, 0, Math.PI*2, 0, Math.PI/2);
                const hairMat = new THREE.MeshLambertMaterial({ color: 0xffd700 });
                const hair = new THREE.Mesh(hairGeo, hairMat);
                hair.position.y = 1.7;
                group.add(hair);

                // Barbie'nin Giydirilebilir 3D Gövde/Elbise Silindiri
                const dressGeo = new THREE.CylinderGeometry(0.4, 0.7, 2, 32);
                const dressMat = new THREE.MeshLambertMaterial({ color: 0xffffff }); // İlk başta beyaz mayo
                const dressMesh = new THREE.Mesh(dressGeo, dressMat);
                dressMesh.position.y = 0.4;
                group.add(dressMesh);

                bScene.add(group);
                bCamera.position.set(0, 1, 4);
                bCamera.lookAt(0, 1, 0);

                // İnteraktif Kıyafet Değiştirme Fonksiyonu
                function change3DStyle(colorHex, name) {
                    dressMat.color.setHex(colorHex);
                    document.getElementById("barbieLabel").innerText = name + " Giydirildi! ✨";
                }

                // Podyumda Sürekli Dönen 3D Barbie Efekti
                function bAnimate() {
                    group.rotation.y += 0.015; // Kendi etrafında zarifçe döner
                    bRenderer.render(bScene, bCamera);
                    requestAnimationFrame(bAnimate);
                }
                bAnimate();
            </script>
            """
            components.html(barbie_3d_html, height=390)
            
        else:
            st.info("🎯 Panel açıldı be gardaşşşşş! Şimdi üstteki butonlardan oyununu seç, 3D motor anında yüklensin!")
    else:
        st.warning("🕹️ Oyun alanı kilitli. Sol tarafta mikrofonun yanındaki '🎮 Oyun Modu' butonuna basarak eğlenceyi başlatabilirsin!")
