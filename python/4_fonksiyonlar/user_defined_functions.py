"""
def fonksiyon_adi():
    kod_blok
"""

# merhaba fonksiyonunu
def selam_ver():
    print("Merhaba")
selam_ver() # fonksiyon tanımlandıktan sonra bu şekilde çağrılır

# parametre kullanımı
def selam_ver(isim): # isim input parametresi alır
    print(f"Merhaba ben {isim} akıllı asistanıyım")

selam_ver("İletişim Başkanlığı") # fonksiyon çağrılırken input parametresi verilir

# birden fazla parametre
def selam_ver(isim, selamlama_cumlesi):
    print(isim +  " " + selamlama_cumlesi)

selam_ver("İletişim Başkanlığı", "akıllı asistanı size merhaba diyor.")

# return kullanımı
def topla(a, b):
    sonuc = a + b
    print(f"sonuc: {sonuc}")
    return sonuc #return olmadan sonuc fonksiyon dışına çıkmaz

toplama_islemi_sonucu = topla(3, 8)
print(f"toplama_islemi_sonucu: {toplama_islemi_sonucu}")

# birden fazla değer döndürme
def hesapla(x, y):
    toplam = x + y
    carpim = x * y
    return toplam, carpim

hesapla_toplam, hesapla_carpim = hesapla(3, 9)
print(f"hesapla_toplam: {hesapla_toplam}")
print(f"hesapla_carpim: {hesapla_carpim}")

# varsayılan parametre
def selam(isim, mesaj = "merhaba"):
    print(f"{isim} {mesaj}")

selam("arkadaşlar")
selam("selim", "nasılsın")

# keyword argüman
def selam(isim, yas, meslek, c, lr, epoch):
    """
    Docstring
    Description: bu fonksiyon selamlama yapar.
    Input: 
        isim (str): kullanıcının ismi
        yas (int): kullanıcının yaşı
        meslek, 
        c, 
        lr, 
        epoch
    Output: None
    """
    print(isim, yas, meslek, c, lr, epoch)

selam(isim = "selim", yas = "23", meslek = "mühendis", c = "0.4", lr = "0.001", epoch="1000")


# type hint modern python
def topla(a: int, b: int) -> int:
    return a + b

print(topla(3, 4))

# fonksiyon içinde fonksiyon kullanımı
def kare(x):
    kare = x**2 
    return kare

def yazdir(x):
    print(kare(x))

yazdir(5)