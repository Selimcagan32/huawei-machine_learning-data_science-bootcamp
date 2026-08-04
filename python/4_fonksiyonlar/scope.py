"""
Scope bir değişkenin nerede erişilebilir olduğunu ifade eder
"""

# local değişken: fonksiyon içerisinde tanımlanan değişken

def test():
    x = 10
    print(f"Fonksiyon içi: {x}")

test()

# global değişken: fonksiyon dışında tanımlanan değişken

x = 15
def test():
    print(f"Fonksiyon içi: {x}")

test()

# aynı isimli değişkenler

x = 11
def test():
    x = 5
    print(f"Fonksiyon içi: {x}") #local değişken olarak x = 5'i alır

test()
print(f"Fonksiyon dışı: {x}") #global değişken olarak x = 11'i alır

# global anahtar kelimesi

x = 9
def test():
    global x # global değişken üzerinde değişiklik yapmak için global anahtar kelimesi kullanılır
    x = 5 # lokal -> global 

test()
print(x)