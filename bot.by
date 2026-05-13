import requests
import asyncio
import edge_tts

# Bu fonksiyon havadan internetten çekilir (Tamamen yasal yolla)
def hava_durumu_al():
    # İstanbul koordinatları: örnektir
    url = "https://api.open-meteo.com/v1/forecast?latitude=41.00&longitude=28.97&current_weather=true"
    yanit = requests.get(url).json()
    derece = yanit['current_weather']['temperature']
    return f"Gezeryolu bilgi merkezi sunar. Şu an bölgemizde hava sıcaklığı {derece} derece. Keyifli dinlemeler."

# Bu fonksiyon metni ses dosyasına (MP3) çevirir
async def ses_yap():
    metin = hava_durumu_al()
    # Microsoft Ahmet sesini kullanıyoruz
    iletisim = edge_tts.Communicate(metin, "tr-TR-AhmetNeural")
    await iletisim.save("haberler.mp3")

if __name__ == "__main__":
    asyncio.run(ses_yap())
