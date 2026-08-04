# listeler
# liste tanımlaması köşeli parantez ile gerçekleşir
sayilar = [1, 2, 3, 4, 5, 6] # integer listesi
isimler = ["selim", "cagan", "baykar", "staj"] # string listesi
karisik = ["selim", 1, "cagan", "baykar", 32, 42.5] # farklı veri tiplerini aynı anda tutabilir.

print(karisik) # ['selim', 1, 'cagan', 'baykar', 32, 42.5]

#listelerde indeks 0 dan başlar
meyveler = ["karpuz", "erik", "muz"]

print(meyveler[0]) # karpuz
print(meyveler[2]) # muz
print(meyveler[-1]) # muz

# liste uzunluğu
print(len(meyveler)) # 3

# listelerde slicing
sayilar = [10, 20, 30, 40, 50, 60]
print(sayilar[1:4]) # 20, 30, 40   [a:b] a dahil, b dahil değil
print(sayilar[0:3]) # ilk 3 eleman 10, 20, 30
print(sayilar[:3]) # ilk 3 eleman 10, 20, 30
print(sayilar[2:]) # 30dan sonrası [30, 40, 50, 60]

# listeye eleman eklemek
sayilar = [1, 2, 3]
sayilar.append(4)
print(sayilar) # [1, 2, 3, 4]

sayilar.insert(1, 100)
print(sayilar) # [1, 100, 2, 3, 4]

sayilar.remove(100) # eleman silme
print(sayilar) # [1, 2, 3, 4]

sayilar.pop() # en son indekste bulunan değer çıkartılır
print(sayilar) # [1, 2, 3]

sayilar.pop(0) # belirli bir indeks silme
print(sayilar) # [2, 3]

sayilar[0] = 999 # belirli bir indeksde ki değeri bşka bir değer ile değiştir
print(sayilar) # [999, 3]