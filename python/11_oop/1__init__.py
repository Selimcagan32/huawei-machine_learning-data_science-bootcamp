#  __init__ : metodu nesne oluşturulduğunda otomatik olarak çalışan özel bir metottur. (kurucu metod)
class Ogrenci:

    def __init__(self, isim, yas): # self = oluşturulan nesneyi temsil eder, isim ve yaş başlangıç parametrelerimiz
        print(f"Yeni bir öğrenci oluşturuluyor: isim: {isim}, yaş: {yas}")

# nesne (object) oluşturma
ogrenci1 = Ogrenci("Selim", 23)