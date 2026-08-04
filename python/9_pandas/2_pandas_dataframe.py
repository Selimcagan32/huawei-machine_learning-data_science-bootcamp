import pandas as pd

"""
dataframe
"""

# dataframe oluşturma
veri = {
    "isim":  ["ali", "ayse", "mehmet"],
    "yas":   [25, 30, 28],
    "sehir": ["Ankara", "İstanbul", "İzmir"] 
}

df = pd.DataFrame(veri)
print(df)
"""
sütunlar: veri kategorileri
satırlar: her bir kayıt
     isim  yas     sehir
0     ali   25    Ankara
1    ayse   30  İstanbul
2  mehmet   28     İzmir
"""

# sütun isimleri
print(df.columns) # Index(['isim', 'yas', 'sehir'], dtype='str')

# dataframe satır sayısı öğrenme
print(df.shape) # (3, 3)

# sütunlara erişim
print(df["isim"])

# birden fazla sütun seçme
print(df[["isim", "yas"]])

# yeni sütun ekleme
df["maas"] = [5000, 7000, 6000]
print(df)
"""
     isim  yas     sehir  maas
0     ali   25    Ankara  5000
1    ayse   30  İstanbul  7000
2  mehmet   28     İzmir  6000
"""

# sütun silme
df = df.drop("sehir", axis = 1) # sütun oldu için axis = 1
print(df)
"""
     isim  yas  maas
0     ali   25  5000
1    ayse   30  7000
2  mehmet   28  6000
"""

# ilk satırları görüntülemek
print(df.head()) # ilk 5 satır

# son satırları görüntüleme
print(df.tail()) # son 5 satır

# dataframe hakkında bilgi alma
print(df.info())
"""
<class 'pandas.DataFrame'>
RangeIndex: 3 entries, 0 to 2
Data columns (total 3 columns):
 #   Column  Non-Null Count  Dtype
---  ------  --------------  -----
 0   isim    3 non-null      str
 1   yas     3 non-null      int64
 2   maas    3 non-null      int64
dtypes: int64(2), str(1)
memory usage: 204.0 bytes
"""