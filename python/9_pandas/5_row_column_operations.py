import pandas as pd

"""
Sütun ve satır işlemleri
"""

# dataframe oluştur
veri = {
    "isim": ["selim", "tuğba", "rana"],
    "yas": [28, 30, 28],
    "maas": [90000, 70000, 60000]
}

df = pd.DataFrame(veri)
print(df)

# yeni bir sütun ekleme
df["sehir"] = ["Ankara", "İstanbul", "Antalya"]
print(df)

# hesaplama ile sütun oluşturma
df["yillik_maas"] = df["maas"] * 12 
print(df)

# sütun silme
df = df.drop("maas", axis = 1)
print(df)

# sütun isim değiştirme
df = df.rename(columns={"yillik_maas": "yillikMaas"})
print(df)

# yeni satır eklemek
df.loc[3] = ["beyza", 26, "Ankara", 960000]
print(df)

# satır silme
df = df.drop(1)
print(df)

# index değerlerini yeniden düzenleme
df = df.reset_index(drop = True)
print(df)