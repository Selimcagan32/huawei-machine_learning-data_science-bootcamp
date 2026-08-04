# sözlük (dictionary)
ogrenci = { # isim = anahtar, selim = key değeri -> {anahtar: değer}
    "isim": "selim", 
    "yas": 21,
    "bolum": "bilgisayar"
}

print(ogrenci)

# dictionary ye erişim
print(ogrenci["isim"]) # selim
print(ogrenci["yas"]) # 21

# dictionary yeni değer ekleme
ogrenci["not"] = 85
print(ogrenci) # {'isim': 'selim', 'yas': 21, 'bolum': 'bilgisayar', 'not': 85}

# dictionary değer güncelleme
ogrenci["yas"] = 23
print(ogrenci) # {'isim': 'selim', 'yas': 23, 'bolum': 'bilgisayar', 'not': 85}

# dictionary eleman silme
del ogrenci["bolum"]
print(ogrenci) # {'isim': 'selim', 'yas': 23, 'not': 85}

# anahtarları ve değerleri al
print(ogrenci.keys()) # anahtarlar dict_keys(['isim', 'yas', 'not'])
print(ogrenci.values()) # değerler dict_values(['selim', 23, 85])
print(ogrenci.items()) # anahtar - değer dict_items([('isim', 'selim'), ('yas', 23), ('not', 85)])

