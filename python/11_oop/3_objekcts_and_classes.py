
# class: şablon -> araba
# object (nesne): şablondan üretilen yapı (mercedes, audi)


class Kitap: # ad, yazar, sayfa

    def __init__(self, ad, yazar, sayfa):
        self.ad = ad
        self.yazar = yazar
        self.sayfa = sayfa

    def bilgi_goster(self):
        print(f"Kitap: {self.ad}")
        print(f"Yazar: {self.yazar}")
        print(f"Sayfa sayısı: {self.sayfa}")

# object oluşturma
kitap1 = Kitap("Python programlama", "Selim", 478)

# attribute değerlerine erişim
print(kitap1.ad)
print(kitap1.yazar)
print(kitap1.sayfa)

# method
kitap1.bilgi_goster()
"""
Kitap: Python programlama
Yazar: Kaan
Sayfa sayısı: 500
"""

# birden fazla obje oluşturma
kitap1 = Kitap("Python programlama", "Selim", 478)
kitap2 = Kitap("Python programlamaya Giriş", "Turgay", 327)
kitap3 = Kitap("Python", "Maruf", 253)

print(kitap2.ad)
kitap3.bilgi_goster()