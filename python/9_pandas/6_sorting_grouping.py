import pandas as pd

"""
Veri sıralama ve gruplama
"""

# örnek data frame oluştur
veri = {
    "isim": ["selim", "ayse", "beyza", "zeynep", "hilal"],
    "sehir": ["Ankara", "İstanbul", "Ankara", "Antalya", "İstanbul"],
    "maas": [9000, 7000, 6000, 8000, 4500]
}

df = pd.DataFrame(veri)
print(df)
"""
     isim     sehir  maas
0   selim    Ankara  9000
1    ayse  İstanbul  7000
2   beyza    Ankara  6000
3  zeynep   Antalya  8000
4   hilal  İstanbul  4500
"""
# veri sıralama
df_sirali = df.sort_values("maas")
print(df_sirali)

"""
     isim     sehir  maas
4   hilal  İstanbul  4500
2   beyza    Ankara  6000
1    ayse  İstanbul  7000
3  zeynep   Antalya  8000
0   selim    Ankara  9000
"""

# azalan sıralama
df_sirali = df.sort_values("maas", ascending=False)
print(df_sirali)
"""
     isim     sehir  maas
0   selim    Ankara  9000
3  zeynep   Antalya  8000
1    ayse  İstanbul  7000
2   beyza    Ankara  6000
4   hilal  İstanbul  4500
"""

# birden fazla sütuna göre sıralama
df_sirali = df.sort_values(["sehir", "maas"])
print(df_sirali)
"""
     isim     sehir  maas
2   beyza    Ankara  6000
0   selim    Ankara  9000
4   hilal  İstanbul  4500
1    ayse  İstanbul  7000
3  zeynep   Antalya  8000
"""

# veri gruplama: groupby
# şehir bazında gruplama
gruplar = df.groupby("sehir")
print(gruplar) # <pandas.api.typing.DataFrameGroupBy object at 0x000001DBF8751160>

# grupların ortalama maaşı
sonuc = df.groupby("sehir")["maas"].mean() # şehir bazında ortalama maaş hesaplama
print(sonuc)
"""
Ankara      7500.0
İstanbul    5750.0
Antalya     8000.0
"""

# grupların toplam maaşı
sonuc = df.groupby("sehir")["maas"].sum()
print(sonuc)
"""
sehir
Ankara      15000
İstanbul    11500
Antalya     8000
"""

# grupların kaç kişi olduğunu bulalım
sonuc = df.groupby("sehir")["isim"].count()
print(sonuc)
"""
sehir
Ankara      2
İstanbul    2
Antalya     1
"""

# birden fazla işlem yapma
sonuc = df.groupby("sehir")["maas"].agg(["mean", "max", "min"])
print(sonuc)
"""
            mean   max   min
sehir
Ankara    7500.0  9000  6000
İstanbul  5750.0  7000  4500
Antalya   8000.0  8000  8000
"""