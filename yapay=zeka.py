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
st.set_page_config(page_title="Apolingo Ultra Costa AI & Game Suite", page_icon="🚀", layout="wide")

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
sol_taraf, sag_taraf = st.columns([0.52, 0.48])

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
    c1, c2, c3 = st.columns([0.65, 0.13, 0.22])
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
# SAĞ PANEL - STABİL, NET GÖRÜNÜR VE KATMANLI OYUN MERKEZİ (ÇORAP DESTEKLİ)
# ==========================================================================================
with sag_taraf:
    st.subheader("🎮 APOLINGO OYUN MERKEZİ")
    st.write("---")
    
    if st.session_state.oyun_panel_acik:
        oyun_secimi = st.radio(
            "Gardaşşşşş ne oynamak istersin? Seçimini yap oyunun yüklensin:",
            ["Henüz Seçmedim ⏳", "🏎️ BMW M3 Otoban Makas", "👗 Barbie & Çorap Gardırobu"],
            index=0
        )
        st.write("---")

        if oyun_secimi == "🏎️ BMW M3 Otoban Makas":
            st.markdown("**🕹️ KONTROLLER:** Klavyeden **A/D** veya **Sol/Sağ Ok** tuşları ile gümüş BMW M3'ü sağa sola kaçır, makası patlat!")
            
            # Tamamen Görünür ve Stabil Perspektifli Yarış Motoru
            yaris_html = """
            <div style="text-align:center; background:#1e1e1e; padding:15px; border-radius:12px; border:3px solid #333;">
                <canvas id="raceCanvas" width="360" height="420" style="background:#252525; border:3px solid #ff4500; border-radius:8px;"></canvas>
                <h3 id="scoreText" style="color:#fff; font-family:sans-serif; margin:10px 0;">Makas Skoru: 0</h3>
                <button onclick="restartRace()" style="padding:10px 20px; font-weight:bold; background:#ff4500; color:white; border:none; border-radius:6px; cursor:pointer;">Gazı Kökle (Yeniden Başlat) 🏎️</button>
            </div>
            <script>
                const canvas = document.getElementById("raceCanvas"); const ctx = canvas.getContext("2d");
                let score = 0; let gameOver = false;
                let player = { x: 160, y: 340, w: 40, h: 65, color: '#c0c0c0' }; // Net Gümüş Gri M3
                let enemies = [
                    { x: 60, y: -80, w: 38, h: 60, speed: 4, color: '#ffcc00' },
                    { x: 240, y: -280, w: 38, h: 60, speed: 5, color: '#00ccff' }
                ];
                let keys = {}; window.addEventListener("keydown", e => keys[e.key] = true); window.addEventListener("keyup", e => keys[e.key] = false);
                function restartRace() { score = 0; gameOver = false; player.x = 160; enemies[0].y = -80; enemies[1].y = -280; }
                function run() {
                    if(!gameOver){
                        if(keys["ArrowLeft"] || keys["a"] || keys["A"]) { if(player.x > 45) player.x -= 5; }
                        if(keys["ArrowRight"] || keys["d"] || keys["D"]) { if(player.x < 275) player.x += 5; }
                        // Asfaltı çiz
                        ctx.fillStyle = "#333"; ctx.fillRect(0,0,canvas.width,canvas.height);
                        // Emniyet Şeritleri
                        ctx.fillStyle = "#fff"; ctx.fillRect(35,0,6,canvas.height); ctx.fillRect(320,0,6,canvas.height);
                        // Hareketli Yol Çizgileri
                        ctx.fillStyle = "#fffa"; for(let i=0; i<canvas.height; i+=50) { ctx.fillRect(130, (i + (score*6)) % canvas.height, 5, 25); ctx.fillRect(225, (i + (score*6)) % canvas.height, 5, 25); }
                        // Kendi Arabamız (BMW M3) - Net ve Görünür Çizim
                        ctx.fillStyle = player.color; ctx.fillRect(player.x, player.y, player.w, player.h);
                        ctx.fillStyle = "#111"; ctx.fillRect(player.x+5, player.y+12, player.w-10, 18); // Cam
                        ctx.fillStyle = "#ff0"; ctx.fillRect(player.x+2, player.y, 8, 5); ctx.fillRect(player.x+player.w-10, player.y, 8, 5); // Farlar
                        // Rakip Arabaların Çizimi
                        enemies.forEach(en => {
                            en.y += en.speed; if(en.y > canvas.height) { en.y = -80; en.x = 50 + Math.random()*210; score++; document.getElementById("scoreText").innerText = "Makas Skoru: " + score; }
                            ctx.fillStyle = en.color; ctx.fillRect(en.x, en.y, en.w, en.h);
                            ctx.fillStyle = "#111"; ctx.fillRect(en.x+5, en.y+30, en.w-10, 15); // Cam
                            if(player.x < en.x + en.w && player.x + player.w > en.x && player.y < en.y + en.h && player.y + player.h > en.y) { gameOver = true; }
                        });
                    } else {
                        ctx.fillStyle = "rgba(0,0,0,0.85)"; ctx.fillRect(0,0,canvas.width,canvas.height);
                        ctx.fillStyle = "red"; ctx.font = "bold 24px sans-serif"; ctx.fillText("BMW M3 PERT OLDU!", 60, 200);
                    }
                    requestAnimationFrame(run);
                }
                run();
            </script>
            """
            components.html(yaris_html, height=520)

        elif oyun_secimi == "👗 Barbie & Çorap Gardırobu":
            st.markdown("**✨ Katmanlı Tasarım Stüdyosu:** Kıyafetler ve çoraplar asla birbirine karışmaz, tam istediğin parçalar sırayla Barbie'nin üzerine oturur!")
            
            # Katmanları Ayrılmış, Asla Çökmeyen ve Çorap Eklenmiş Barbie Simülasyonu
            barbie_katman_html = """
            <div style="text-align:center; background:#fff0f5; padding:15px; border-radius:15px; border:4px solid #ff69b4; display:flex; justify-content:space-between; align-items:flex-start; font-family:sans-serif; max-width:550px; margin:0 auto;">
                
                <!-- GERÇEK BARBIE MANKEN SİLÜETİ VE KATMANLARI -->
                <div style="width:160px; height:340px; background:#ffd1dc; border-radius:40px; position:relative; border:2px solid #ffb6c1; overflow:hidden; box-shadow: 0px 4px 10px rgba(0,0,0,0.15);">
                    <!-- Altın Sarısı Saçlar -->
                    <div style="position:absolute; top:10px; left:35px; width:90px; height:75px; background:#ffd700; border-radius:45px 45px 15px 15px; z-index:1;"></div>
                    <!-- Yüz -->
                    <div style="position:absolute; top:25px; left:55px; width:50px; height:50px; background:#ffdab9; border-radius:50%; z-index:2; text-align:center; font-size:18px; line-height:48px;">🏼‍♀️</div>
                    <!-- Vücut Tabanı -->
                    <div style="position:absolute; top:80px; left:45px; width:70px; height:180px; background:#ffdab9; border-radius:15px; z-index:1;"></div>
                    <!-- Bacaklar -->
                    <div style="position:absolute; top:240px; left:53px; width:20px; height:90px; background:#ffdab9; z-index:1; border-right:2px solid #eab699;"></div>
                    <div style="position:absolute; top:240px; left:87px; width:20px; height:90px; background:#ffdab9; z-index:1;"></div>

                    <!-- KATLANMAYI ENGELLEYEN BAĞIMSIZ GİYSİ KATMANLARI -->
                    <div id="katmanUst" style="position:absolute; top:80px; left:43px; width:74px; height:65px; z-index:4; border-radius:5px; transition:0.2s;"></div>
                    <div id="katmanAlt" style="position:absolute; top:142px; left:45px; width:70px; height:95px; z-index:3; border-radius:0 0 10px 10px; transition:0.2s;"></div>
                    
                    <!-- ÇORAP KATMANLARI (SOL VE SAĞ BACAK İÇİN ÖZEL BAĞIMSIZ ALAN) -->
                    <div id="katmanCorapSol" style="position:absolute; top:245px; left:53px; width:20px; height:80px; z-index:2; transition:0.2s;"></div>
                    <div id="katmanCorapSag" style="position:absolute; top:245px; left:87px; width:20px; height:80px; z-index:2; transition:0.2s;"></div>
                </div>
                
                <!-- MAĞAZA VE KOMBİN MENÜSÜ -->
                <div style="text-align:left; width:250px; padding-left:10px;">
                    <h5 style="color:#ff1493; margin:0 0 4px 0; border-bottom:1px solid #ff69b4;">👚 Üst Seçimi</h5>
                    <button onclick="secUst('#ff1493')" style="width:100%; padding:5px; background:#ff1493; color:white; border:none; margin-bottom:3px; border-radius:4px; font-weight:bold; cursor:pointer;">💖 Pembe Crop</button>
                    <button onclick="secUst('#8a2be2')" style="width:100%; padding:5px; background:#8a2be2; color:white; border:none; margin-bottom:6px; border-radius:4px; font-weight:bold; cursor:pointer;">🔮 Mor Bluz</button>
                    
                    <h5 style="color:#ff1493; margin:4px 0 4px 0; border-bottom:1px solid #ff69b4;">👖 Alt Seçimi</h5>
                    <button onclick="secAlt('#4682b4')" style="width:100%; padding:5px; background:#4682b4; color:white; border:none; margin-bottom:3px; border-radius:4px; font-weight:bold; cursor:pointer;">💙 Kot Etek</button>
                    <button onclick="secAlt('#fff')" style="width:100%; padding:5px; background:#fff; color:#333; border:1px solid #ccc; margin-bottom:6px; border-radius:4px; font-weight:bold; cursor:pointer;">⚪ Beyaz Şort</button>
                    
                    <h5 style="color:#ff1493; margin:4px 0 4px 0; border-bottom:1px solid #ff69b4;">🧦 Çorap Seçimi (Yeni!)</h5>
                    <button onclick="secCorap('mesh')" style="width:100%; padding:6px; background:#333; color:white; border:none; margin-bottom:3px; border-radius:4px; font-weight:bold; cursor:pointer;">🖤 Siyah Fileli Çorap</button>
                    <button onclick="secCorap('pink')" style="width:100%; padding:6px; background:#ffb6c1; color:black; border:none; margin-bottom:3px; border-radius:4px; font-weight:bold; cursor:pointer;">🌸 Uzun Pembe Çorap</button>
                    <button onclick="secCorap('clear')" style="width:100%; padding:6px; background:#e0e0e0; color:black; border:none; border-radius:4px; font-weight:bold; cursor:pointer;">❌ Çorapları Çıkar</button>
                    
                    <p id="bilgiKutusu" style="color:#ff1493; font-weight:bold; font-size:12px; margin-top:10px; text-align:center; background:#fff; padding:5px; border-radius:5px;">Kombin Yapılıyor...</p>
                </div>
            </div>
            
            <script>
                function secUst(color) {
                    document.getElementById("katmanUst").style.background = color;
                    document.getElementById("katmanUst").style.boxShadow = "0 2px 5px rgba(0,0,0,0.2)";
                    document.getElementById("bilgiKutusu").innerText = "Üst Giyim Güncellendi! ✨";
                }
                function secAlt(color) {
                    document.getElementById("katmanAlt").style.background = color;
                    document.getElementById("katmanAlt").style.boxShadow = "0 2px 5px rgba(0,0,0,0.2)";
                    document.getElementById("bilgiKutusu").innerText = "Alt Giyim Güncellendi! 👗";
                }
                function secCorap(stil) {
                    const l = document.getElementById("katmanCorapSol");
                    const r = document.getElementById("katmanCorapSag");
                    if(stil === 'mesh') {
                        // Fileli görünüm için çizgili arka plan efekti
                        l.style.background = "repeating-linear-gradient(45deg, #222, #222 2px, transparent 2px, transparent 4px)";
                        r.style.background = "repeating-linear-gradient(45deg, #222, #222 2px, transparent 2px, transparent 4px)";
                    } else if(stil === 'pink') {
                        l.style.background = "#ffb6c1";
                        r.style.background = "#ffb6c1";
                    } else {
                        l.style.background = "none";
                        r.style.background = "none";
                    }
                    document.getElementById("bilgiKutusu").innerText = "Çorap Seçimi Güncellendi! 🧦";
                }
            </script>
            """
            components.html(barbie_katman_html, height=410)
            
        else:
            st.info("🎯 Panel açıldı be gardaşşşşş! Şimdi üstteki menüden oyununu seç, her şey eksiksiz buraya gelsin!")
    else:
        st.warning("🕹️ Oyun alanı kilitli. Sol tarafta mikrofonun yanındaki '🎮 Oyun Modu' butonuna basarak eğlenceyi başlatabilirsin!")
