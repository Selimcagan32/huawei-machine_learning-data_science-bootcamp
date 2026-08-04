# liste ile for döngüsü
sayilar = [10, 20 , 30]

for sayi in sayilar:
    print(sayi + 5) #sayiler listesinde ki her bir sayıya 5 ekleme

# range fonksiyonu ile for döngüsü
for i in range(5): # [0, 1, 2, 3, 4]
    print(i)

for i in range(1, 7):
    print(i)

# for ile toplama işlemi
sayilar = [10, 20, 30]
toplam = 0
for s in sayilar:
    print(s)
    toplam = toplam + s

print(toplam) # 60

# for + if kullanımı
sayilar = [1,2,3,4,5,6]
for sayi in sayilar:
    if sayi % 2 == 0:
        print(f"Çift: {sayi}")

# string üzerinden for döngüsü
kelime = "baykar"

for harf in kelime:
    print(harf)