import pandas as pd
"""
Veri seçme ve filtreleme
"""

# örnek data frame
veri = {
    "isim": ["beyza", "ayse", "selim", "zeynep", "merve"],
    "yas":  [26, 30, 28, 35, 22],
    "sehir": ["Ankara", "İstanbul", "Ankara", "Antalya", "İstanbul"],
    "maas": [5000, 7000, 9000, 8000, 4500] 
}
df = pd.DataFrame(veri) # df = data frame (verilerin tablo şeklinde tutulduğu yapı)
print(df)

# sütun seçme
print(df["isim"])

# birden fazla sütun seçme
print(df[["isim", "maas"]])

# satır seçme: iloc
print(df.iloc[0])
"""
isim      beyza
yas          26
sehir    Ankara
maas       5000
"""

# birden fazla satır
print(df.iloc[0:3])

# satır seçme: loc
print(df.loc[2])
"""
isim       selim
yas           28
sehir     Ankara
maas        9000
"""

# belirli bir satır ve belirli bir sütun
print(df.loc[:, ["isim", "maas"]]) # : tüm satırları seçmek için kullanılır

print(df.loc[:2, ["isim", "maas"]]) # :2 ile 0,1,2 satırlarını seçer

# koşullu filtreleme
filtre = df["yas"] > 30
print(filtre)
"""
0    False
1    False
2    False
3     True
4    False
"""
sonuc = df[filtre]
print(sonuc)

print(df[df["yas"] > 30])

# birden fazla koşul varsa
# şehir ankara ve maas 6000 den büyük olan insaları getir
sonuc = df[(df["sehir"] == "Ankara") & (df["maas"] > 6000)]
print(sonuc)

# belirli bir değeri içeren satılar
print(df[df["sehir"] == "Ankara"])

# sadece belirli sütunları gösterme
# yaşı 25 den büyük olan verinin sadece isim ve maaşını göster
print(df[df["yas"] > 25][["isim", "maas"]])
