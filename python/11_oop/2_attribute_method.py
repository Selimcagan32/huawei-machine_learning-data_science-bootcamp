
# Attribute bir class a veya nesneye ait özellikleri temsil eden değişkenlerdir.
# isim, yaş ve bölüm: bunlar öğrencinin attribute larıdır.


class Ogrenci:

    def __init__(self, isim, yas):
        self.isim = isim  # isim attribute
        self.yas = yas    # yas attribute



# attribute kullanımı
ogrenci1 = Ogrenci("Selim", 23) 

# ogrenci1 nesnesinin attribute larına nasıl ulaşabiliriz?
print(ogrenci1.isim) # Selim
print(ogrenci1.yas)  # 23

#----------------------------------------------------------------------------------------

# Metot (method): bir class içerisinde tanımlanan fonksiyonlardır


class Ogrenci:

    def __init__ (self, isim, yas):
        self.isim = isim
        self.yas = yas

    def tanit(self):
        print(f"Merhaba benim adım: {self.isim}")

ogrenci1 = Ogrenci("Selim", 23)
ogrenci2 = Ogrenci("Selçuk", 25)

ogrenci1.tanit()
ogrenci2.tanit()