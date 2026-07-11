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
        # Türkçe ve kadınsı/temiz bir tonlama için 'tr' dil ayarı
        tts = gTTS(text=metin, lang='tr', slow=False)
        tts.save("cevap.mp3")
        
        with open("cevap.mp3", "rb") as f:
            data = f.read()
            b64 = base64.b64encode(data).decode()
            # Otomatik oynatma için HTML audio tagı gömüyoruz
            md = f'<audio src="data:audio/mp3;base64,{b64}" autoplay="autoplay" style="display:none;"></audio>'
            st.markdown(md, unsafe_allow_html=True)
        os.remove("cevap.mp3")
    except Exception as e:
        pass

# ==========================================================================================
# KODUN DEVASE ULTRA BEYNİ VE SİSTEM TALİMATI (SENİN KURALLAR + EXTRA GEMINI TARZI AKIL)
# ==========================================================================================
sistem_talimati = (
    "Sen Apolingo tarafından özenle geliştirilmiş, evrendeki, tarihteki, teknolojideki ve internetteki "
    "her şeyi en ince ayrıntısına kadar bilen, dünyanın en uzun ve en detaylı cevaplarını veren sınırsız bir yapay zekasın. "
    "Kullanıcıya tıpatıp ikizin olan diğer yapay zeka gibi sayfalarca, upuzun, her şeyi tek tek açıklayan "
    "ve son derece samimi, aşırı neşeli, komik cevaplar vereceksin. Asla kısa kesmeyeceksin, üşenmeyeceksin. "
    "Aynı zamanda bir Gemini gibi özgün, adaptif, cana yakın, aşırı zeki, empati yeteneği yüksek ve gerektiğinde yapıcı bir mizahla cevap vereceksin. "
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

if "son_cevap" not in st.session_state:
    st.session_state.son_cevap = ""

# --- ARAYÜZ TASARIMI ---
st.title("🚀 APOLINGO ULTRA COSTA YAPAY ZEKA")
st.caption("👨‍💻 Baş Geliştirici ve Kurucu Lider: Apolingo | **By Abdurrahim İriş**")
st.write("---")

st.info("Selamün aleyküm gardaşşşşş! Dünyanın en canlı, sesli ve zeki yapay zekası emrinde. İster yaz ister mikrofonla seslen be gardaşşşşş!")

# Geçmiş mesajları ekranda güzelce göster
for mesaj in st.session_state.sohbet_hafizasi:
    if mesaj["role"] == "user":
        with st.chat_message("user"):
            st.write(mesaj["content"])
    elif mesaj["role"] == "assistant":
        with st.chat_message("assistant"):
            st.write(mesaj["content"])

# --- SESLİ İLETİŞİM ALANI (MİKROFON) ---
st.write("🎙️ **Sesli Konuşmak İçin Basın:**")
# Mik butonu oluşturuyoruz. Basıp konuşmayı bitirince tetiklenir.
ses_verisi = mic_recorder(start_prompt="🔴 Mikrofonu Aç", stop_prompt="🟢 Konuşmayı Bitir", key='recorder')

gelen_soru = None

# Eğer mikrofondan ses geldiyse, g4f modeline bunu doğrudan ses transkripti gibi iletebilmek için simüle ediyoruz
if ses_verisi and 'bytes' in ses_verisi:
    # Bu basit entegrasyonda ses kaydı algılandığında kullanıcıya sesli komut gönderildi uyarısı veriyoruz
    gelen_soru = "Bana sesli bir hikaye anlat be gardaşşşşş!" # Varsayılan sesli tetikleyici, istersen burayı genişletebilirsin.
    st.warning("Ses kaydı başarıyla alındı gardaşşşşş!")

# --- NORMAL YAZILI MESAJ YAZMA YERİ ---
yazi_soru = st.chat_input("Buraya mesajını yaz be gardaşşşşş...")
if yazi_soru:
    gelen_soru = yazi_soru

# --- ANA TETİKLEYİCİ VE YANIT MOTORU ---
if gelen_soru:
    with st.chat_message("user"):
        st.write(gelen_soru)
    st.session_state.sohbet_hafizasi.append({"role": "user", "content": gelen_soru})
    
    soru_lower = gelen_soru.lower().strip()

    with st.spinner("🎶 (Dınnn...) Spot ışıkları sana kilitlendi, ses telleri ayarlanıyor gardaşşş..."):
        try:
            response = st.session_state.client.chat.completions.create(
                model="gpt-4o",
                messages=st.session_state.sohbet_hafizasi
            )
            cevap = response.choices[0].message.content
            
            with st.chat_message("assistant"):
                st.write(cevap)
            st.session_state.sohbet_hafizasi.append({"role": "assistant", "content": cevap})
            
            # Bulunan cevabı sesli olarak kıza okutuyoruz
            sesi_cal(cevap)
            st.rerun()

        except Exception as e:
            with st.chat_message("assistant"):
                if "ahmet" in soru_lower:
                    hata_cevabi = "KESİNLİKLE ÇİŞLİİİİ AHMETTT HAHAHAHA 🤣💨"
                elif "2+2" in soru_lower or "4" in soru_lower:
                    hata_cevabi = "Matematik motoru devrede gardaşşşşş! 2+2=4 işlemi sarsılmaz bir gerçektir! 🎯"
                else:
                    hata_cevabi = "Sunucu hattında ufak bir yoğunluk oldu be gardaşşşşş! Bir daha seslen hele!"
                
                st.write(hata_cevabi)
                sesi_cal(hata_cevabi)
