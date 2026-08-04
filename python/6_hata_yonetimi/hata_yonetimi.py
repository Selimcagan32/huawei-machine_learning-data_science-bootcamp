"""
try - except
    - program hata verdiğinde durmasını istemeyiz
    - hata olursa yakalyıp kontrollü şekilde yönetmesi lazım
"""
# belirli bir hata yakalama yöntemi
try:
    sayi = int(input("Sayı girin: "))
    print(10/sayi)
except ValueError:
    print("Lütfen bir sayı girin")
except ZeroDivisionError:
    print("Sıfıra bölme yapılamaz")

# else: hata yoksa çalışır
try:
    sayi = int(input("Sayı girin: "))
    sonuc = 10/sayi
except (ValueError, ZeroDivisionError):
    print("Hatalı giriş.")
else: # hata yoksa
    print(f"Sonuç: {sonuc}")

# finally: her durumda çalışır
try: 
    dosya = open("veri.txt", "r", encoding="utf-8")
    icerik = dosya.read()
    print(icerik)
except FileNotFoundError:
    print("Dosya bulunamadı")
finally:
    try:
        dosya.close()
    except:
        pass

# kendi hatamızı üretmek istersek ne yapalım
yas = int(input("Yaş: "))

if yas < 0:
    raise ValueError("Yaş negatif olamaz.") # ValueError: Yaş negatif olamaz. kendimiz hata mesajı ürettik

# genel hata ayıklama mantığı
try:
    sayi = int(input("bir sayı girin: "))
    print(10/sayi)
except Exception as e:
    print(f"Hata: {str(e)}")