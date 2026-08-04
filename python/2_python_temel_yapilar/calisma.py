# ============================================================
# değişkenlerin tiplerini type() ile yazdırma.
# ============================================================

ad = "Selim"
yas = 23
ortalama = 3.45

print("ad = Selim, yas = 23, ortalama = 3.45")
print(type(ad))
print(type(yas))
print(type(ortalama))
print("-" * 50)

# ============================================================
# yaş bilgisini input() ile alama.
# yaşın tipini ekrana yazdır ve 5 yıl ekleyip sonucu yazdır.
# input() her zaman string döndürür, int çevir.
# ============================================================

yas = input("yaşınızı girin: ")
print("veri tipi:", type(yas))

yas_int = int(yas)
print("5 yıl sonra yaş:", yas_int + 5)
print("-" * 50)


# ============================================================
# ürün fiyatı float al. %18 KDV hesapla
# virgül sonrası 3 basamak olacak şekilde yazdır
# ============================================================

fiyat = float(input("Ürün fiyatını girin: "))
kdv = fiyat * 0.18
toplam = fiyat + kdv
print("KDV:", round(kdv, 3))
print("Toplam:", round(toplam, 3))
print("-" * 50)

# ============================================================
sayilar = [10, 20, 30, 40, 50]
# - İlk elemanı yazdır
# - Son elemanı yazdır
# - 2. indexten sona kadar olan parçayı yazdır
# - Listeye 60 ekle
# - Listedeki 20 değerini sil
# ============================================================

print("İlk eleman:", sayilar[0])
print("Son eleman:", sayilar[-1])
print("2. indexten sonrası:", sayilar[2:])

sayilar.append(60)
print("60 eklendi:", sayilar)

sayilar.remove(20)
print("20 silindi:", sayilar)
print("-" * 50)


# ============================================================
koordinat = (12, 34)
# - Tuple içindeki değerleri unpacking ile x ve y değişkenlerine al
# - x ve y'yi yazdır
# - Tuple'ın değiştirilemediğini göster
# ============================================================

koordinat = (12, 34)
x, y = koordinat
print("x:", x)
print("y:", y)
# koordinat[0] = 99  # Bu satır hata verir çünkü tuple immutable (değiştirilemez)
print("-" * 50)

# ============================================================
ogrenci = {"isim": "Ayşe", "yas": 22, "bolum": "Yazılım"}
# - Öğrencinin ismini yazdır
# - "not" anahtarı ile 90 ekle
# - "yas" değerini 23 yaparak güncelle
# - anahtarları ve değerleri yazdır
# ============================================================

print("İsim:", ogrenci["isim"])

ogrenci["not"] = 90
ogrenci["yas"] = 23

print("Güncel sözlük:", ogrenci)
print("Anahtarlar:", list(ogrenci.keys()))
print("Değerler:", list(ogrenci.values()))
print("-" * 50)

# ============================================================
# Set oluştur ve tekrar edenleri temizle
liste = ["Ali", "Ayşe", "Ali", "Mehmet", "Ayşe"]
# - listeyi set'e çevirip benzersiz isimleri yazdır
# - benzersiz isim sayısını yazdır
# ============================================================
benzersiz_isimler = set(liste)
print("Benzersiz isimler:", benzersiz_isimler)
print("Benzersiz isim sayısı:", len(benzersiz_isimler))
print("-" * 50) 