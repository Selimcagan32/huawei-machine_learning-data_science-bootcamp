# (int)
yas = 35
print(yas)
print(35)

# hesaplama
a = 10 
b = 5 
toplam = a + b
carpma = a * b
cikarma = a - b
bolme = a/b
print(toplam, carpma, cikarma, bolme)

# zam uygulaması
birim_fiyat = 10 
yuzde = int(input("Yüzdeyi yazın: ")) #input str alır, int çevir
print(yuzde)
zamli_fiyat = birim_fiyat + birim_fiyat*yuzde/100
print(zamli_fiyat)

# float
sicaklik = 35.5
print(sicaklik)

# matematiksel işlemler
a = 3.5
b = 2.0 

print(a + b) # toplama
print(a/b) # bolme

# ondalık hassasiyeti
print(0.1 + 0.2) # 0.3 yerine 0.30000000000000004 gelir. 
# Bu durum bilgisayarın ondalık sayıları ikili sistemde temsil etmesinden kaynaklanır.

# yuvarlama (round)
sonuc = 0.1 + 0.2
print(sonuc)
sonuc_yuvarlanmis = round(sonuc, 2)
print(sonuc_yuvarlanmis)

# proje: gelen fiyat üzerinden kdv (%20) hesapla
fiyat = float(input("Fiyat Girin: "))
print(fiyat)
kdvli_fiyat = fiyat + 20*fiyat/100
print(kdvli_fiyat)