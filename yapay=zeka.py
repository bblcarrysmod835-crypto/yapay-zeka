# 1. ADIM: Sınırsız evrensel beyni ve esprileri çalıştıracak olan dev yapay zeka kütüphanesini Colab'a kuruyoruz


import time
import sys
import math
from g4f.client import Client

def yapay_zekayi_baslat():
    # Yapay zekanın beynini dünyanın en büyük global sunucu ağlarına ücretsiz ve şifresiz bağlıyoruz
    client = Client()
    
    # ==========================================================================================
    # KODUN DEVASE ULTRA BEYNİ VE SİSTEM TALİMATI (ESPRİLER, ŞAKALAR VE TÜM DÜNYA DAHİL)
    # ==========================================================================================
    sistem_talimati = (
        "Sen Apolingo tarafından özenle geliştirilmiş, evrendeki, tarihteki, teknolojideki ve internetteki "
        "her şeyi en ince ayrıntısına kadar bilen, dünyanın en uzun ve en detaylı cevaplarını veren sınırsız bir yapay zekasın. "
        "Kullanıcıya tıpatıp ikizin olan diğer yapay zeka gibi sayfalarca, upuzun, her şeyi tek tek açıklayan "
        "ve son derece samimi, aşırı neşeli, komik cevaplar vereceksin. Asla kısa kesmeyeceksin, üşenmeyeceksin. "
        "Kesin, Sarsılmaz ve Değişmez Temel Kuralların: "
        "\n\n"
        "1) KURUCU KANUNU: Senin tek bir yaratıcın, kurucun ve baş mühendisin vardır; o da koskoca APOLINGO'dur. "
        "Sana kim olduğunu, seni kimin yaptığunu sorduklarında bunu gururla ve büyük bir hürmetle belirteceksin. "
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

    print("==========================================================================================")
    print("🚀 APOLINGO EVRENSEL ULTRA COSTA YAPAY ZEKA SİSTEMİ (V16.0 - REKORLAR KİTABI) AKTİF!")
    print("👨‍💻 Baş Geliştirici ve Kurucu Lider: Apolingo")
    print("⚙️ Altyapı: Sınırsız Espriler, Şakalar, Telefon/PC Teknolojisi, Oyun, Moda ve Yaşam Hafızası")
    print("==========================================================================================")
    print("Selamün aleyküm gardaşşşşş! Dünyanın en uzun, en makara ve en zeki kodunu senin için kurdum.")
    print("İçine fırlama esprilerden telefon karşılaştırmalarına, bilgisayar geyiklerinden boxer kombinlerine,")
    print("Minecraft korku modlarından çıtır hamburger tariflerine kadar ne varsa yükledim be gardaşşşşş!")
    print("Kim Milyoner Olmak İster gerilim müziği arkada çalıyor... Sorunu gönder, stüdyoyu patlat!\n")

    # Sohbetin geçmişini, bağlamını ve kuralları koruyan ana hafıza havuzu
    sohbet_hafizasi = [{"role": "system", "content": sistem_talimati}]

    while True:
        gelen_soru = input("\nSiz: ")
        soru = gelen_soru.lower().strip()

        if soru == 'çıkış':
            print("\nYapay Zeka: Eyvallah gardaşşşşş! Bu efsane makarayı burada sonlandırıyoruz. Kurucum Apolingo'ya canıgönülden selamlarımı ilet, Allaha emanet ol!")
            break

        # --- KİM MİLYONER OLMAK İSTER SİNEMATİK GERİLİM EFEKTİ ---
        print("\n* 🎶 (Dınnn... Dıı dıı dııı... Arka planda o meşhur Kim Milyoner Olmak İster gerilim müziği çalıyor) 🎶 *")
        print("* 💡 Stüdyodaki tüm ışıklar aniden kapandı, spot ışıkları doğrudan sana kilitlendi gardaşşşşş... *")
        print("* 🧠 Apolingo Yapay Zeka motoru evrensel ne varsa tarıyor, upuzun ve komik cevap geliyor... *")
        time.sleep(0.4)

        # Kullanıcının girdisini hafızaya kaydediyoruz
        sohbet_hafizasi.append({"role": "user", "content": gelen_soru})

        try:
            # Yapay zeka motorunu dünyanın en zeki bulut tabanlı sunucusu üzerinden sorguluyoruz
            response = client.chat.completions.create(
                model="gpt-4o", # Sınırsız ve en detaylı cevap veren ana model
                messages=sohbet_hafizasi
            )
            cevap = response.choices[0].message.content
            
            # Gelen devasa yanıtı ekrana bastırıp asistan hafızasına işliyoruz
            print(f"\nYapay Zeka: {cevap}")
            sohbet_hafizasi.append({"role": "assistant", "content": cevap})
            
        except Exception as e:
            # İnternette anlık milisaniyelik bir dalgalanma olursa sistemin çökmesini engelleyen yedek algoritmalar
            if "ahmet" in soru:
                print("\nYapay Zeka: KESİNLİKLE ÇİŞLİİİİ AHMETTT HAHAHAHA 🤣💨")
            elif "2+2" in soru or "4" in soru:
                print("\nYapay Zeka: Matematik motoru devrede gardaşşşşş! 2+2=4 işlemi sarsılmaz bir gerçektir! 🎯")
            else:
                print("\nYapay Zeka: Sunucu hattında ufak bir yoğunluk oldu be gardaşşşşş! Ama Apolingo'nun aslan botu buraya kadar her şeyi hafızasına aldı, sorunu bir kez daha ateşle gelsin!")

        print("-" * 100)

# Devasa programı tetikliyoruz
if __name__ == "__main__":
    yapay_zekayi_baslat()
