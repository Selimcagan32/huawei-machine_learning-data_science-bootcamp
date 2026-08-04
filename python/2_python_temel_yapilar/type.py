# veri tipi kontrolü
x = 10
print(type(x)) # <class 'int'>

x = "10"
print(type(x)) # <class 'str'>

# print("25" + 5) # TypeError: str (not "int") to str

# tip dönüşümleri (casting)
x = "25" # str
print(type(int(x))) # <class 'int'>
print(type(float(x))) # <class 'float'>

x = 35
print(type(str(x))) # <class 'str'>

sayi = int(input("Bir sayı girin: ")) # input fonksiyonu çıktısı str tipindedir. int() ile int tipine çevrilir.
print(sayi) 
print(type(sayi)) # <class 'int'>

print(int("abc")) # ValueError: invalid literal for int() with base 10: 'abc'