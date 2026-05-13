import requests
import os

# Gezeryolu Haber Botu
def haber_cek():
    print("Haberler çekiliyor...")
    # Buraya haber çekme mantığını ekleyebilirsin
    return "Gezeryolu Radyo: Günün gelişmeleri hazır."

def seslendir(metin):
    print(f"Seslendiriliyor: {metin}")
    # edge-tts veya ilgili kütüphane komutları buraya gelecek
    os.system(f'edge-tts --text "{metin}" --write-media haberler.mp3')

if __name__ == "__main__":
    bulten = haber_cek()
    seslendir(bulten)
    print("İşlem başarıyla tamamlandı.")
