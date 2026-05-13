import asyncio
import edge_tts
import os

# Gezeryolu Radyo Haber Metni
TEXT = "Gezeryolu Radyo haber bülteni hazırlandı. Bugünün tüm gelişmeleri başarıyla seslendirildi."
VOICE = "tr-TR-AhmetNeural"
OUTPUT_FILE = "haberler.mp3"

async def generate_news():
    print("Haberler seslendiriliyor...")
    communicate = edge_tts.Communicate(TEXT, VOICE)
    await communicate.save(OUTPUT_FILE)
    print(f"Başarılı: {OUTPUT_FILE} oluşturuldu.")

if __name__ == "__main__":
    if not os.path.exists(OUTPUT_FILE):
        asyncio.run(generate_news())
    else:
        print("Dosya zaten mevcut, güncelleme gerekmiyor.")
