# ============================================================
# Kullanıcıdan bir sayı al
# Pozitifse, negatifse, sıfırsa yazdır
# ============================================================
sayi = int(input("Bir sayı girin: "))

if sayi > 0:
    print("Pozitif")
elif sayi < 0:
    print("Negatif")
else:
    print("Sıfır")

print("-" * 50)

# ============================================================
# 1'den 10'a kadar 10 dahil sayıları yazdır
# sayıların toplamını hesapla
# ============================================================
toplam = 0

for i in range(1, 11):
    print(i)
    toplam += i

print("Toplam:", toplam)
print("-" * 50)

# ============================================================
# "q" yazana kadar sürekli giriş al
# her giriş yaptığında "Girdiniz: ..." yazdır
# "q" yazarsa döngüyü bitir "Çıkış yapıldı" yaz
# ============================================================
giris = "..."

while giris != "q":
    giris = input("Giriş yapın (çıkmak için q): ")
    if giris != "q":
        print(f"Girdiniz: {giris}")

print("Çıkış yapıldı")
print("-" * 50)

# ============================================================
# 1'den 20'ye kadar sayıları dolaş
# çiftse "Çift", tekse "Tek" yazdır
# sayı 10'dan büyükse "Büyük", değilse "Küçük/Eşit" yazdır
# ============================================================
for i in range(1, 21):
    #çift tek kontrolü
    if i % 2 == 0:
        tur = "Çift"
    else:
        tur = "Tek"

    # 10'dan büyük mü kontrolü
    if i > 10:
        boyut = "Büyük"
    else:
        boyut = "Küçük/Eşit"

    print(f"{i} -> {tur} - {boyut}")

print("-" * 50)