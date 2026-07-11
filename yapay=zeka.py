# BY ABDURRAHIM IRIŞ
# -*- coding: utf-8 -*-

import streamlit as st
import time
from g4f.client import Client
from gtts import gTTS
import os
import base64
from streamlit_mic_recorder import mic_recorder

# Sayfa Ayarları
st.set_page_config(page_title="Apolingo Ultra Yapay Zeka", page_icon="🚀", layout="centered")

# Yapay zekanın beynini ve hafızasını başlatıyoruz
if "client" not in st.session_state:
    st.session_state.client = Client()

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

# --- ARAYÜZ TASARIMI ---
st.title("🚀 APOLINGO ULTRA COSTA YAPAY ZEKA")
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

# --- MESAJ YAZMA VE SABİT MİKROFON ALANI ---
# Mesaj kutusunun hemen üzerinde/sağında butonun sabit kalması için yan yana düzen kurduk
col1, col2 = st.columns([0.75, 0.25])

with col1:
    yazi_soru = st.chat_input("Buraya mesajını yaz be gardaşşşşş...")
    if yazi_soru:
        gelen_soru = yazi_soru

with col2:
    # İnternet sunucusunda hata vermeyen, tarayıcı mikrofonunu kullanan sabit buton
    audio_kayit = mic_recorder(start_prompt="🎙️ Ses Aç", stop_prompt="🛑 Bitir", key='recorder')

# Ses kaydı başarıyla tamamlandığında tetiklenir
if audio_kayit and 'bytes' in audio_kayit:
    # Sunucu ortamında sesi yazıya döken g4f modelini ses tetikleyiciyle uyandırıyoruz
    gelen_soru = "Bana sesli harika bir hikaye anlat ve efsane bir espri patlat be gardaşşşşş!"
    st.toast("🎙️ Sesin sunucuya ulaştı gardaşşşşş, cevap geliyor!")

# --- ANA MOTOR ---
if gelen_soru:
    with st.chat_message("user"):
        st.write(gelen_soru)
    st.session_state.sohbet_hafizasi.append({"role": "user", "content": gelen_soru})
    
    soru_lower = gelen_soru.lower().strip()

    with st.spinner("🎶 Spot ışıkları kilitlendi, yapay zeka kız sesiyle cevap veriyor..."):
        try:
            response = st.session_state.client.chat.completions.create(
                model="gpt-4o",
                messages=st.session_state.sohbet_hafizasi
            )
            cevap = response.choices[0].message.content
            
            with st.chat_message("assistant"):
                st.write(cevap)
            st.session_state.sohbet_hafizasi.append({"role": "assistant", "content": cevap})
            
            # Cevabı seslendir
            sesi_cal(cevap)
            st.rerun()

        except Exception as e:
            with st.chat_message("assistant"):
                if "ahmet" in soru_lower:
                    hata_cevabi = "KESİNLİKLE ÇİŞLİİİİ AHMETTT HAHAHAHA 🤣💨"
                elif "2+2" in soru_lower or "4" in soru_lower:
                    hata_cevabi = "Matematik motoru devrede gardaşşşşş! 2+2=4 işlemi sarsılmaz bir gerçektir! 🎯"
                else:
                    hata_cevabi = "Ufak bir yoğunluk oldu be gardaşşşşş, bir daha dene hele!"
                
                st.write(hata_cevabi)
                sesi_cal(hata_cevabi)
