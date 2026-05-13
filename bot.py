import requests
import asyncio
import edge_tts

def hava_durumu_al():
    url = "https://api.open-meteo.com/v1/forecast?latitude=41.00&longitude=28.97&current_weather=true"
    yanit = requests.get(url).json()
    derece = yanit['current_weather']['temperature']
    return f"Gezeryolu bilgi merkezi sunar. Su an bolgemizde hava sicakligi {derece} derece. Keyifli dinlemeler."

async def ses_yap():
    metin = hava_durumu_al()
    iletisim = edge_tts.Communicate(metin, "tr-TR-AhmetNeural")
    await iletisim.save("haberler.mp3")

if __name__ == "__main__":
    asyncio.run(ses_yap())
