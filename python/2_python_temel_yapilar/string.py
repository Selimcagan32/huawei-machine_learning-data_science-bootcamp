# string
isim = "selim" # çift tırnak örneği
sirket = 'baykar' # tek tırnak örneği
bilgi = "selimin çalıştığı şirketinin ismi baykar teknoloji"
print(bilgi)

# string birleştirme (concatenation)
isim = "selim"
sirket = 'baykar'
bilgi2 = isim + "in çalıştığı şirketinin ismi " + sirket + " " + "teknoloji"
print(bilgi2)

# string ve sayı birleştirme
yas = 23 # int
int_to_str = str(yas) # 23 -> "23"
isim = "selim" # string
sonuc = isim + " in yaşı: " + int_to_str # selim in yaşı: 23
print(sonuc)

kurulus_tarihi = 1986
print("baykar teknoloji " + str(kurulus_tarihi) +  " yılında kurulmuştur.")

print(f"baykar teknoloji {kurulus_tarihi} yılında kurulmuştur.") # f string
accuracy = 97
print(f"Karar ağacı accuracy: {accuracy} %")

# string indexleme
kelime = "türkiye" 
print(kelime[0])
print(kelime[3])

# string metotları
metin = "TürkiE"
metin_kucuk_harf = metin.lower()
print(metin_kucuk_harf)

# uzunluk bulma
metin = "türkiye"
metin_uzunlugu = len(metin)
print(metin_uzunlugu)

# yer değiştirme
metin = "türkiye"
print(metin.replace("ü", "Ü")) # küçük harf ü yerine büyük harf Ü ile değiştirme