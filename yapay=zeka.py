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

# Sayfa Ayarları (Oyunlar sığsın diye genişlettim biraz)
st.set_page_config(page_title="Apolingo Ultra Costa AI & Game", page_icon="🚀", layout="wide")

# Yapay zekanın beynini ve hafızasını başlatıyoruz
if "client" not in st.session_state:
    st.session_state.client = Client()

# Spam engellemek için ses takip hafızası
if "son_islenen_ses_adi" not in st.session_state:
    st.session_state.son_islenen_ses_adi = None

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
    "6) TELEFON VE BİLGİSAYAR DÜNYASI (TEKNOLOJİ GEYİKLERİ): Kullanıcı bilgisayar, telefon, tablet sorduğunda; iPhone mu Samsung mu "
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
sol_taraf, sag_taraf = st.columns([0.65, 0.35])

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

    # Chat Girişi ve Mikrofon Alanı
    c1, c2 = st.columns([0.80, 0.20])
    with c1:
        yazi_soru = st.chat_input("Buraya mesajını yaz be gardaşşşşş...")
        if yazi_soru:
            gelen_soru = yazi_soru
    with c2:
        ses_dosyasi = st.audio_input("🎙️ Seslen")

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

    # --- ANA MOTOR ---
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
# SAĞ PANEL - MİKROFONUN SAĞINDAKİ OYUN MERKEZİ (BMW M3 OTOMATİK MAKAS & BARBIE SEÇİMİ)
# ==========================================================================================
with sag_taraf:
    st.subheader("🎮 APOLINGO OYUN MERKEZİ")
    oyun_secimi = st.radio("Oyun Modu Seçin Gardaşşşşş:", ["🏎️ BMW M3 Otoban Makas", "👗 Barbie Kıyafet Tasarımı"], horizontal=True)
    st.write("---")

    if oyun_secimi == "🏎️ BMW M3 Otoban Makas":
        st.markdown("**🕹️ YÖNLER:** **A/D** veya **Sol/Sağ Ok Tuşları** ile BMW M3'ü kontrol et, arabalara makas at!")
        
        # HTML5 & JS Tabanlı BMW M3 Makas Atma Oyunu (Kokpit Görünümlü Efektle)
        bmw_oyun_html = """
        <div style="text-align:center;">
            <canvas id="roadCanvas" width="340" height="450" style="border:4px solid #1a1a1a; background:#222; border-radius:10px;"></canvas>
            <h3 id="scoreBoard" style="color:white; font-family:sans-serif; margin-top:5px;">Makas Skoru: 0</h3>
            <button onclick="resetGame()" style="padding:8px 15px; font-weight:bold; background:#e60000; color:white; border:none; border-radius:5px; cursor:pointer;">Yeniden Gazla! 🏎️</button>
        </div>
        <script>
            const canvas = document.getElementById("roadCanvas");
            const ctx = canvas.getContext("2d");
            
            let score = 0;
            let gameOver = false;
            
            let player = { x: 150, y: 360, w: 35, h: 65, speed: 6 };
            let enemies = [
                { x: 60, y: -100, w: 35, h: 60, speed: 4, color: '#ffcc00' },
                { x: 160, y: -300, w: 35, h: 60, speed: 5, color: '#00ccff' }
            ];
            
            let keys = {};
            window.addEventListener("keydown", e => { keys[e.key] = true; });
            window.addEventListener("keyup", e => { keys[e.key] = false; });
            
            function resetGame() {
                score = 0; gameOver = false;
                player.x = 150;
                enemies[0].y = -100; enemies[1].y = -300;
                enemies[0].x = 60; enemies[1].x = 180;
            }
            
            function loop() {
                if(!gameOver) {
                    // Yön kontrolleri
                    if(keys["ArrowLeft"] || keys["a"] || keys["A"]) { if(player.x > 40) player.x -= player.speed; }
                    if(keys["ArrowRight"] || keys["d"] || keys["D"]) { if(player.x < 265) player.x += player.speed; }
                    
                    // Arka Plan Şeritleri (Otoban Akışı)
                    ctx.fillStyle = "#333";
                    ctx.fillRect(0, 0, canvas.width, canvas.height);
                    
                    // Yol kenarı çizgileri
                    ctx.fillStyle = "#fff";
                    ctx.fillRect(35, 0, 5, canvas.height);
                    ctx.fillRect(300, 0, 5, canvas.height);
                    
                    // Kesikli çizgiler
                    ctx.fillStyle = "#fffa";
                    for(let i=0; i<canvas.height; i+=40) {
                        ctx.fillRect(120, (i + (score*4)) % canvas.height, 4, 20);
                        ctx.fillRect(210, (i + (score*4)) % canvas.height, 4, 20);
                    }
                    
                    // Bizim BMW M3 (Gümüş Gri/Mavi Şeritli Efsane)
                    ctx.fillStyle = "#a6b4c9"; // Metalik BMW Rengi
                    ctx.fillRect(player.x, player.y, player.w, player.h);
                    ctx.fillStyle = "#0066cc"; // M Şeridi
                    ctx.fillRect(player.x+5, player.y, 4, player.h);
                    ctx.fillStyle = "#111"; // Camlar
                    ctx.fillRect(player.x+4, player.y+15, player.w-8, 15);
                    
                    // Diğer Trafikteki Arabalar
                    enemies.forEach(enemy => {
                        enemy.y += enemy.speed;
                        if(enemy.y > canvas.height) {
                            enemy.y = -70;
                            enemy.x = 45 + Math.random() * 210;
                            score++;
                            document.getElementById("scoreBoard").innerText = "Makas Skoru: " + score;
                        }
                        
                        ctx.fillStyle = enemy.color;
                        ctx.fillRect(enemy.x, enemy.y, enemy.w, enemy.h);
                        ctx.fillStyle = "#111";
                        ctx.fillRect(enemy.x+4, enemy.y+25, enemy.w-8, 12); // cam
                        
                        // Çarpışma Testi (Makas Atarken Vurursan)
                        if(player.x < enemy.x + enemy.w && player.x + player.w > enemy.x &&
                           player.y < enemy.y + enemy.h && player.y + player.h > enemy.y) {
                            gameOver = true;
                        }
                    });
                } else {
                    ctx.fillStyle = "rgba(0,0,0,0.8)";
                    ctx.fillRect(0,0,canvas.width,canvas.height);
                    ctx.fillStyle = "red";
                    ctx.font = "bold 24px sans-serif";
                    ctx.fillText("BMW M3 PERT OLDU!", 50, 200);
                    ctx.fillStyle = "white";
                    ctx.font = "16px sans-serif";
                    ctx.fillText("Toplam Makas: " + score, 110, 240);
                }
                requestAnimationFrame(loop);
            }
            loop();
        </script>
        """
        components.html(bmw_oyun_html, height=550)

    elif oyun_secimi == "👗 Barbie Kıyafet Tasarımı":
        st.markdown("**✨ Kombinini Seç:** Barbie'ye en uyumlu tarzı bul ve alt tarafta stili tamamla!")
        
        # JavaScript tabanlı interaktif Barbie Giydirme Oyunu
        barbie_oyun_html = """
        <div style="text-align:center; background:#fff0f5; padding:15px; border-radius:12px; border:3px solid #ff69b4; font-family:sans-serif;">
            <div style="display:flex; justify-content: space-around; align-items:center;">
                <!-- Barbie Figürü -->
                <div id="barbieModel" style="width:120px; height:240px; background:#ffe4e1; border-radius:30px; position:relative; border:2px solid #ffb6c1;">
                    <div style="width:50px; height:50px; background:#ffe4e1; border-radius:50%; position:absolute; top:10px; left:35px; border:1px solid #ffb6c1;">👨‍🦰</div>
                    <div id="chosenTop" style="width:100px; height:70px; background:none; position:absolute; top:65px; left:10px; border-radius:10px; text-align:center; color:white; font-size:12px; line-height:70px;"></div>
                    <div id="chosenBottom" style="width:90px; height:90px; background:none; position:absolute; top:135px; left:15px; border-radius:5px; text-align:center; color:white; font-size:12px; line-height:90px;"></div>
                </div>
                
                <!-- Gardırop Seçenekleri -->
                <div style="text-align:left;">
                    <h5 style="color:#ff1493; margin:2px;">👚 Üst Giyim</h5>
                    <button onclick="changeTop('#ff69b4', 'Pembe Tişört')" style="background:#ff69b4; color:white; border:none; margin:2px; border-radius:4px; cursor:pointer;">Pembe Tişört</button><br>
                    <button onclick="changeTop('#9400d3', 'Mor Bluz')" style="background:#9400d3; color:white; border:none; margin:2px; border-radius:4px; cursor:pointer;">Mor Bluz</button><br>
                    <button onclick="changeTop('#00black', 'Siyah Crop')" style="background:#111; color:white; border:none; margin:2px; border-radius:4px; cursor:pointer;">Siyah Crop</button>
                    
                    <h5 style="color:#ff1493; margin:8px 0 2px 0;">👖 Alt Giyim</h5>
                    <button onclick="changeBottom('#4169e1', 'Kot Etek')" style="background:#4169e1; color:white; border:none; margin:2px; border-radius:4px; cursor:pointer;">Kot Etek</button><br>
                    <button onclick="changeBottom('#ffb6c1', 'Tütü Etek')" style="background:#ffb6c1; color:black; border:none; margin:2px; border-radius:4px; cursor:pointer;">Tütü Etek</button><br>
                    <button onclick="changeBottom('#f5f5dc', 'Krem Şort')" style="background:#f5f5dc; color:black; border:none; margin:2px; border-radius:4px; cursor:pointer;">Krem Şort</button>
                </div>
            </div>
            <h4 id="styleRating" style="color:#ff1493; margin-top:15px;">Kombin Durumu: Giysi Seç bekleniyor...</h4>
        </div>
        <script>
            function changeTop(color, name) {
                const top = document.getElementById("chosenTop");
                top.style.background = color;
                top.innerText = name;
                checkStyle();
            }
            function changeBottom(color, name) {
                const btm = document.getElementById("chosenBottom");
                btm.style.background = color;
                btm.innerText = name;
                checkStyle();
            }
            function checkStyle() {
                const t = document.getElementById("chosenTop").innerText;
                const b = document.getElementById("chosenBottom").innerText;
                if(t && b) {
                    document.getElementById("styleRating").innerText = "✨ Harika Kombin! Barbie Piste Hazır! 💅";
                }
            }
        </script>
        """
        components.html(barbie_oyun_html, height=400)
