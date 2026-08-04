# dosya açma ve okuma
# test.txt: dosya
# "r" read okumna modu
dosya = open("test.txt", "r", encoding="utf-8")
icerik = dosya.read() # tüm dosyayı okur
print(icerik)
dosya.close() # dosyayı kapatır  

# satır satır okuma
dosya = open("test.txt", "r", encoding="utf-8")
for satir in dosya:
    print(satir.strip()) #strip() ile satır başı ve sonundaki boşlukları temizleriz

dosya.close()

# dosya içeriğinin işlenmesi
# okuduğumuz veri üzerinde işlem 

dosya = open("test.txt", "r", encoding="utf-8")
icerik = dosya.read()
dosya.close()
print(icerik)
yeni_icerik = icerik.upper() # tüm içeriği büyük harfe çevirir
print(f"yeni_icerik: \n{yeni_icerik}")

# satır sayısını bulma
dosya = open("test.txt", "r", encoding="utf-8")
satirlar = dosya.readlines() #tüm satırları liste olarak döndürür
dosya.close()
print(f"Toplam satır: {len(satirlar)}") # satırlar listesi üzerinden uzunluğu alarak satır sayısını buluruz

# dosyaya yazma
dosya = open("yeni_dosya.txt", "w", encoding="utf-8") #okuma modu "r" yerine yazma modu "w" kullanılır
dosya.write("Merhaba Dünya\n")
dosya.write("Python öğreniyoruz")
dosya.close()

# oku -> işle -> kaydet
dosya = open("test.txt", "r", encoding="utf-8")
icerik = dosya.read()
dosya.close()

yeni_icerik = icerik.upper()

dosya = open("islenmis_test.txt", "w", encoding="utf-8")
dosya.write(yeni_icerik)
dosya.close()

# with yapısı: dosya otomatik kapanır hata olsa bile kapanır
with open("test.txt", "r", encoding="utf-8") as dosya:
    icerik = dosya.read()
    print("with yapısı:")
    print(icerik)
    # otomatik bir şekilde kendi kendine kapanıyor

# with ile yazma
with open("with_dosya_yazma.txt", "w", encoding="utf-8") as dosya:
    dosya.write("with ile yazma işlemi gerçekleştirildi.")