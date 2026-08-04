sayi = -3

if sayi > 0:
    print("pozitif")
else:
    print("pozitif değil")

ogrenci_not = 72
if ogrenci_not > 85:
    print("A")
elif ogrenci_not > 70:
    print("B")
elif ogrenci_not > 50:
    print("C")
else:
    print("F")

# mantıksal operatörler: birden fazla koşulun birleşmesi
yas = 20
ogrenci = True # boolean

# yaşı 25 den küçükse ve öğrenci ise 
if yas < 25 and ogrenci == True:
    print("Öğrenci indirimi uygula")

# yaşı 25 ten küçükse veya öğrenci ise 
if yas < 25 or ogrenci == True: 
    print("Öğrenci indirimi uygula")


# if ve liste kullanımı
meyveler = ["elma", "portakal", "muz"]

if "elma" in meyveler:
    print("elma listede var")
else:
    print("elma listede yok")


# stok kontrol örneği
meyveler = ["elma", "portakal", "muz"]

urun = input("Bir meyve girin: ")
if urun in meyveler:
    print("Stokta var")
else:
    print("Stokta yok")