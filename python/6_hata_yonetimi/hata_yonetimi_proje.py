"""
Bozuk veri temizleme
    - dosyayı oku, sayıya çevrilemeyen satırları atla, geçerli notları topla, ortalama hesapla
"""

notlar = [] 
hata = 0 # hata sayisi

with open("6_hata_yonetimi/notlar.txt", "r", encoding="utf-8") as dosya:

    for satir in dosya:

        try: 
            notlar.append(int(satir.strip())) # geçerli notları listeye eklenir hata varsa except bloğu çalışır ve hata sayısı bir artırılır
        except ValueError:
            print(f"Hatalı veri bulundu: {satir.strip()}")
            hata += 1 # dosyada hatalı satir sayısı

print(f"notlar: {notlar}") # [70, 85, 90, 50, 60]
print(f"hata: {hata}") #  2

print(f"ortalama: {sum(notlar) / len(notlar)}")