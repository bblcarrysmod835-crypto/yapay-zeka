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
st.set_page_config(page_title="Apolingo Ultra Costa AI & Game", page_icon="🚀", layout="wide")

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
# SAĞ PANEL - SEÇİMLİ VE GİZLENEBİLİR OYUN SAHASI (GERÇEK BARBIE TASARIMLI)
# ==========================================================================================
with sag_taraf:
    st.subheader("🎮 APOLINGO OYUN MERKEZİ")
    st.write("---")
    
    if st.session_state.oyun_panel_acik:
        oyun_secimi = st.radio(
            "Gardaşşşşş ne oynamak istersin? Seçimini yap oyunun açılsın:",
            ["Henüz Seçmedim ⏳", "🏎️ BMW M3 Otoban Makas", "👗 Barbie Kıyafet Tasarımı"],
            index=0
        )
        st.write("---")

        if oyun_secimi == "🏎️ BMW M3 Otoban Makas":
            st.markdown("**🕹️ YÖNLER:** **A/D** veya **Sol/Sağ Ok Tuşları** ile BMW M3'ü kontrol et, makasları diz!")
            
            bmw_oyun_html = """
            <div style="text-align:center;">
                <canvas id="roadCanvas" width="340" height="440" style="border:4px solid #1a1a1a; background:#222; border-radius:10px;"></canvas>
                <h3 id="scoreBoard" style="color:white; font-family:sans-serif; margin-top:5px;">Makas Skoru: 0</h3>
                <button onclick="resetGame()" style="padding:8px 15px; font-weight:bold; background:#e60000; color:white; border:none; border-radius:5px; cursor:pointer;">Yeniden Gazla! 🏎️</button>
            </div>
            <script>
                const canvas = document.getElementById("roadCanvas"); const ctx = canvas.getContext("2d");
                let score = 0; let gameOver = false;
                let player = { x: 150, y: 350, w: 35, h: 65, speed: 6 };
                let enemies = [{ x: 60, y: -100, w: 35, h: 60, speed: 4, color: '#ffcc00' }, { x: 160, y: -300, w: 35, h: 60, speed: 5, color: '#00ccff' }];
                let keys = {}; window.addEventListener("keydown", e => { keys[e.key] = true; }); window.addEventListener("keyup", e => { keys[e.key] = false; });
                function resetGame() { score = 0; gameOver = false; player.x = 150; enemies[0].y = -100; enemies[1].y = -300; }
                function loop() {
                    if(!gameOver) {
                        if(keys["ArrowLeft"] || keys["a"] || keys["A"]) { if(player.x > 40) player.x -= player.speed; }
                        if(keys["ArrowRight"] || keys["d"] || keys["D"]) { if(player.x < 265) player.x += player.speed; }
                        ctx.fillStyle = "#333"; ctx.fillRect(0, 0, canvas.width, canvas.height);
                        ctx.fillStyle = "#fff"; ctx.fillRect(35, 0, 5, canvas.height); ctx.fillRect(300, 0, 5, canvas.height);
                        ctx.fillStyle = "#fffa"; for(let i=0; i<canvas.height; i+=40) { ctx.fillRect(120, (i + (score*4)) % canvas.height, 4, 20); ctx.fillRect(210, (i + (score*4)) % canvas.height, 4, 20); }
                        ctx.fillStyle = "#a6b4c9"; ctx.fillRect(player.x, player.y, player.w, player.h);
                        ctx.fillStyle = "#0066cc"; ctx.fillRect(player.x+5, player.y, 4, player.h); ctx.fillStyle = "#111"; ctx.fillRect(player.x+4, player.y+15, player.w-8, 15);
                        enemies.forEach(enemy => {
                            enemy.y += enemy.speed; if(enemy.y > canvas.height) { enemy.y = -70; enemy.x = 45 + Math.random() * 210; score++; document.getElementById("scoreBoard").innerText = "Makas Skoru: " + score; }
                            ctx.fillStyle = enemy.color; ctx.fillRect(enemy.x, enemy.y, enemy.w, enemy.h); ctx.fillStyle = "#111"; ctx.fillRect(enemy.x+4, enemy.y+25, enemy.w-8, 12);
                            if(player.x < enemy.x + enemy.w && player.x + player.w > enemy.x && player.y < enemy.y + enemy.h && player.y + player.h > enemy.y) { gameOver = true; }
                        });
                    } else { ctx.fillStyle = "rgba(0,0,0,0.8)"; ctx.fillRect(0,0,canvas.width,canvas.height); ctx.fillStyle = "red"; ctx.font = "bold 24px sans-serif"; ctx.fillText("BMW M3 PERT OLDU!", 50, 200); }
                    requestAnimationFrame(loop);
                }
                loop();
            </script>
            """
            components.html(bmw_oyun_html, height=530)

        elif oyun_secimi == "👗 Barbie Kıyafet Tasarımı":
            st.markdown("**✨ Barbie Manken Gardırobu:** Kıyafetlerin üzerine tıkla, gerçek elbiseler Barbie'nin üzerinde anında canlansın!")
            
            # Tamamen Geliştirilmiş, Görsel Giydirmeli Barbie Oyunu
            barbie_gorsel_html = """
            <div style="text-align:center; background:#fff0f5; padding:20px; border-radius:15px; border:4px solid #ff69b4; font-family:sans-serif; max-width:440px; margin:0 auto;">
                <div style="display:flex; justify-content: space-between; align-items:flex-start;">
                    
                    <!-- GERÇEK BARBIE MANKEN SİLÜETİ -->
                    <div style="width:160px; height:320px; background:#ffe4e1; border-radius:50px 50px 20px 20px; position:relative; border:2px solid #ffb6c1; overflow:hidden; box-shadow: 0px 4px 10px rgba(0,0,0,0.1);">
                        <!-- Barbie Altın Sarısı Saçları -->
                        <div style="position:absolute; top:12px; left:40px; width:80px; height:65px; background:#ffd700; border-radius:40px 40px 10px 10px; z-index:1;"></div>
                        <!-- Barbie Kafası ve Yüzü -->
                        <div style="position:absolute; top:25px; left:57px; width:46px; height:46px; background:#ffdab9; border-radius:50%; z-index:2; border:1px solid #ffb6c1; text-align:center; font-size:16px; line-height:44px;">👩🏼</div>
                        <!-- Barbie Boynu -->
                        <div style="position:absolute; top:68px; left:73px; width:14px; height:15px; background:#ffdab9; z-index:1;"></div>
                        <!-- Barbie Vücut / Gövde Yapısı -->
                        <div style="position:absolute; top:80px; left:45px; width:70px; height:180px; background:#ffdab9; border-radius:20px; z-index:1;"></div>
                        
                        <!-- ÜSTÜNE GELECEK DİNAMİK KIYAFET KATMANLARI (BOŞ BAŞLAR, SEÇİLİNCE ÇİZİLİR) -->
                        <div id="layerTop" style="position:absolute; top:80px; left:42px; width:76px; height:65px; z-index:3; transition: 0.2s; border-radius:5px;"></div>
                        <div id="layerBottom" style="position:absolute; top:140px; left:45px; width:70px; height:100px; z-index:3; transition: 0.2s; border-radius:0 0 15px 15px;"></div>
                    </div>
                    
                    <!-- EFSANE KIYAFET DOLABI BUTONLARI -->
                    <div style="text-align:left; width:220px; padding-left:15px;">
                        <h4 style="color:#ff1493; margin:0 0 8px 0; border-bottom:2px solid #ff69b4; padding-bottom:3px;">👚 Üst Kıyafetler</h4>
                        <button onclick="wearTop('pinkDress')" style="width:100%; padding:8px; background:#ff69b4; color:white; border:none; margin-bottom:5px; border-radius:6px; font-weight:bold; cursor:pointer; box-shadow:0 2px 4px rgba(0,0,0,0.1);">💖 Pembe Şık Elbise</button>
                        <button onclick="wearTop('purpleTop')" style="width:100%; padding:8px; background:#8a2be2; color:white; border:none; margin-bottom:5px; border-radius:6px; font-weight:bold; cursor:pointer; box-shadow:0 2px 4px rgba(0,0,0,0.1);">🔮 Mor Gece Bluzu</button>
                        <button onclick="wearTop('blackCrop')" style="width:100%; padding:8px; background:#222; color:white; border:none; margin-bottom:12px; border-radius:6px; font-weight:bold; cursor:pointer; box-shadow:0 2px 4px rgba(0,0,0,0.1);">🖤 Tarz Siyah Crop</button>
                        
                        <h4 style="color:#ff1493; margin:0 0 8px 0; border-bottom:2px solid #ff69b4; padding-bottom:3px;">👖 Alt Kıyafetler</h4>
                        <button onclick="wearBottom('jeanSkirt')" style="width:100%; padding:8px; background:#4682b4; color:white; border:none; margin-bottom:5px; border-radius:6px; font-weight:bold; cursor:pointer; box-shadow:0 2px 4px rgba(0,0,0,0.1);">💙 Havalı Kot Etek</button>
                        <button onclick="wearBottom('tutuPink')" style="width:100%; padding:8px; background:#ffb6c1; color:black; border:none; margin-bottom:5px; border-radius:6px; font-weight:bold; cursor:pointer; box-shadow:0 2px 4px rgba(0,0,0,0.1);">🌸 Kabarık Tütü Etek</button>
                        <button onclick="wearBottom('whitePants')" style="width:100%; padding:8px; background:#fff; color:#333; border:1px solid #ccc; margin-bottom:5px; border-radius:6px; font-weight:bold; cursor:pointer; box-shadow:0 2px 4px rgba(0,0,0,0.1);">⚪ Klasik Beyaz Şort</button>
                    </div>
                </div>
                
                <h3 id="statusText" style="color:#db7093; margin-top:15px; font-size:16px; background:#fff; padding:8px; border-radius:8px;">👗 Barbie'yi Giydir Be Gardaşşşşş!</h3>
            </div>
            
            <script>
                function wearTop(type) {
                    const topLayer = document.getElementById("layerTop");
                    if(type === 'pinkDress') {
                        topLayer.style.background = "linear-gradient(to bottom, #ff69b4, #ff1493)";
                        topLayer.style.border = "2px solid #fff";
                    } else if(type === 'purpleTop') {
                        topLayer.style.background = "linear-gradient(to bottom, #9370db, #8a2be2)";
                        topLayer.style.border = "2px solid #fff";
                    } else if(type === 'blackCrop') {
                        topLayer.style.background = "#222222";
                        topLayer.style.border = "1px solid #444";
                    }
                    checkStyleStatus();
                }
                
                function wearBottom(type) {
                    const btmLayer = document.getElementById("layerBottom");
                    if(type === 'jeanSkirt') {
                        btmLayer.style.background = "linear-gradient(to bottom, #4682b4, #1e90ff)";
                        btmLayer.style.border = "2px solid #fff";
                    } else if(type === 'tutuPink') {
                        btmLayer.style.background = "linear-gradient(to bottom, #ffb6c1, #ff69b4)";
                        btmLayer.style.border = "2px solid #fff";
                    } else if(type === 'whitePants') {
                        btmLayer.style.background = "#f8f9fa";
                        btmLayer.style.border = "1px solid #ddd";
                    }
                    checkStyleStatus();
                }
                
                function checkStyleStatus() {
                    document.getElementById("statusText").innerHTML = "✨ <b>Muazzam Kombin!</b> Barbie Resmen Podyumu Sallıyor! 💅💖";
                }
            </script>
            """
            components.html(barbie_gorsel_html, height=420)
            
        else:
            st.info("🎯 Panel açıldı be gardaşşşşş! Şimdi üstteki butonlardan oyununu seç, anında buraya gelsin!")
    else:
        st.warning("🕹️ Oyun alanı kilitli. Sol tarafta mikrofonun yanındaki '🎮 Oyun Modu' butonuna basarak eğlenceyi başlatabilirsin!")
