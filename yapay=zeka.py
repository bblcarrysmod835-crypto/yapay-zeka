# BY ABDURRAHIM IRIŞ
# -*- coding: utf-8 -*-

import streamlit as st
import time
from g4f.client import Client
from gtts import gTTS
import os
import base64
import speech_recognition as sr

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
# KODUN DEVASE ULTRA BEYNİ VE SİSTEM TALİMATI
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
    "dünyanın en soğuk ama en çok güldüren esprilerini, caps muhabbetlerini, fırlama şakaları upuzun anlatacaksın. "
    "\n"
    "6) TELEFON VE BİLGİSAYAR DÜNYASI: Teknolojik tüm detayları, RGB pavyon fanları, iPhone vs Samsung kavgalarını komik anlatacaksın. "
    "\n"
    "7) ODA TASARIMI VE RENKLER: Antrasit, led ışıklar ve setup rehberini döktüreceksin. "
    "\n"
    "8) STİL VE GİYİM: Renk teorisini, kahverengi tonlarını ve boxer kombinlerini uzun uzun öveceksin. "
    "\n"
    "9) YEMEK AKADEMİSİ: Çıtır tavuk, hamburger ve sos tariflerini şef sırlarıyla vereceksin. "
    "\n"
    "10) MATEMATİK VE OYUN: 2+2=4 gibi sorulara 'Son kararınız mı?' diyeceksin. Minecraft Herobrine, Valorant elo cehennemini anlatacaksın."
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

# --- MESAJ YAZMA YERİ VE SAĞINA MİKROFON EKLEME ALANI ---
# Yan yana iki sütun açıyoruz. Biri büyük yazı alanı, diğeri buton için.
col1, col2 = st.columns([0.85, 0.15])

with col1:
    yazi_soru = st.chat_input("Buraya mesajını yaz be gardaşşşşş...")
    if yazi_soru:
        gelen_soru = yazi_soru

with col2:
    # Mesaj kutusunun hemen sağında duracak yuvarlak ikonlu mikrofon tuşu
    mik_butonu = st.button("🎙️ Seslen", use_container_width=True)

# Mikrofon tuşuna basıldığında ses kaydetme ve Türkçeye çevirme motoru çalışır
if mik_butonu:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.toast("🎙️ Dinliyorum... Konuş be gardaşşşşş!")
        # Arka plan gürültüsünü filtrele ve sesi al
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.listen(source, timeout=5, phrase_time_limit=8)
    
    try:
        # Sesi Google altyapısı ile Türkçeye (Yazıya) çeviriyoruz
        soylenen_soz = r.recognize_google(audio, language="tr-TR")
        st.success(f"Anladım: '{soylenen_soz}'")
        gelen_soru = soylenen_soz
    except sr.UnknownValueError:
        st.error("Ne dediğini tam seçemedim be gardaşşşşş, biraz daha net konuş hele!")
    except sr.RequestError:
        st.error("Ses tanıma sunucusuna bağlanamadım!")

# --- CEVAPLANDIRMA VE KONUŞMA MOTORU ---
if gelen_soru:
    with st.chat_message("user"):
        st.write(gelen_soru)
    st.session_state.sohbet_hafizasi.append({"role": "user", "content": gelen_soru})
    
    soru_lower = gelen_soru.lower().strip()

    with st.spinner("🎶 Spot ışıkları sana kilitlendi, cevap hazırlanıyor..."):
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
                    hata_cevabi = "Ufak bir bağlantı sorunu oldu gardaşşşşş, bir daha söyle hele!"
                
                st.write(hata_cevabi)
                sesi_cal(hata_cevabi)
