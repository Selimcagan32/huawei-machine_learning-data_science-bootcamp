import pandas as pd

"""
temel pandas fonksiyonları
"""

# örnek dataframe oluşturalım
veri = {
    "isim": ["selim", "gözde", "merve", "ece", "leyla"],
    "yas": [25, 30, 28, 35, 22],
    "sehir": ["Ankara", "İstanbul", "Ankara", "Isparta", "İstanbul"],
    "maas": [8000, 9000, 6000, 8000, 4500]
}

df = pd.DataFrame(veri)
print(df)
"""
     isim  yas     sehir  maas
0   selim   25    Ankara  8000
1   gözde   30  İstanbul  9000
2   merve   28    Ankara  6000
3   ece     35   Isparta  8000
4   leyla   22  İstanbul  4500
"""
# head fonksiyonu ile ilk 5 satırı görelim
print(df.head())

# tail ile son 3 satırı görme
print(df.tail(3))

# info()
print(df.info())
"""
<class 'pandas.DataFrame'>
RangeIndex: 5 entries, 0 to 4
Data columns (total 4 columns):
 #   Column  Non-Null Count  Dtype
---  ------  --------------  -----
 0   isim    5 non-null      str
 1   yas     5 non-null      int64
 2   sehir   5 non-null      str
 3   maas    5 non-null      int64
dtypes: int64(2), str(2)
memory usage: 292.0 bytes
"""

# sayısal sütunların temel istatistiklerini görmek için describe()
print(df.describe())
"""
             yas         maas
count   5.000000     5.000000
mean   28.000000  7100.000000
std     4.949747  1816.590212
min    22.000000  4500.000000
25%    25.000000  6000.000000
50%    28.000000  8000.000000
75%    30.000000  8000.000000
max    35.000000  9000.000000
"""

# bir sütunda ki değerlerin kaç kez tekrar ettiğini görmek için value_counts()
print(df["sehir"].value_counts())
"""
sehir
Ankara      2
İstanbul    2
Isparta     1
Name: count, dtype: int64
"""

# bir sütunda ki benzersiz değerleri görmek için unique fonksiyonunu kullanırız
print(df["sehir"].unique()) # ['Ankara', 'İstanbul', 'Isparta']

# bir sütunda kaç farklı değer olduğunu görmek için nunique
print(df["sehir"].nunique()) # 3