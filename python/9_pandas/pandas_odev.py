import pandas as pd

veri = {
    "isim": ["Selim", "Beyza", "Zeynep", "Fatih", "Yaman", "Mira"],
    "yas": [25, 30, 28, 35, 22, 27],
    "sehir": ["Ankara", "Ankara", "İstanbul", "İstanbul", "Isparta", "Isparta"],
    "maas": [5000, 7000, 6000, 8000, 4500, 6500]
}

df = pd.DataFrame(veri)

print("VERİ SETİ")
print(df)
print("-" * 50)


# DataFrame'in ilk 3 satırını gösterin.

print("-" * 50)
print(df.head(3))
print("-" * 50)


# DataFrame'deki sütun isimlerini ekrana yazdırın.

print("-" * 50)
print(df.columns)
print("-" * 50)


# Sadece "isim" sütununu seçin.

print("-" * 50)
print(df["isim"])
print("-" * 50)


# Sadece "isim" ve "maas" sütunlarını birlikte gösterin.

print("-" * 50)
print(df[["isim", "maas"]])
print("-" * 50)


# Yaşı 28'den büyük olan kişileri filtreleyin.

print("-" * 50)
print(df[df["yas"] > 28])
print("-" * 50)


# Maaşı 6000'den büyük olan kişilerin sadece isim ve maaş bilgilerini gösterin.

print("-" * 50)
print(df[df["maas"] > 6000][["isim", "maas"]])
print("-" * 50)


# Maaşa göre küçükten büyüğe sıralayın.

print(df.sort_values ("maas"))
print("-" * 50)


# Maaşa göre büyükten küçüğe sıralayın.

print("-" * 50)
print(df.sort_values("maas", ascending=False))
print("-" * 50)


# Şehirlere göre gruplama yapın ve her şehir için ortalama maaşı hesaplayın.

print("-" * 50)
print(df.groupby("sehir")["maas"].mean())
print("-" * 50)


# "yillik_maas" adında yeni bir sütun oluşturun.
# Bu sütun maaşın 12 ile çarpılması ile oluşturulacaktır.

df["yillik_maas"] = df["maas"] * 12

print("-" * 50)
print(df)
print("-" * 50)