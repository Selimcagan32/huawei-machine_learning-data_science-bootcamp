import pandas as pd
"""
Series
"""
# series oluşturma
veri = pd.Series([10, 20, 30, 40])
print(veri)
"""
index   value
0       10     
1       20     
2       30     
3       40 

key-value (dict)
index- value (pandas series)
0: 10
1: 20
2: 30
3: 40
"""

# series içinde ki verilere erişme
veri = pd.Series([10, 20, 30, 40])
print(veri[0]) # 10
print(veri[2]) # 30

# series için özel indeks 
veri = pd.Series([10, 20, 30], index = ["a", "b", "c"])
print(veri)
"""
a    10     
b    20     
c    30 
"""
print(veri["b"]) # 20

# dictionary ile series oluşturma
veri = { # anahtar-value
    "ali": 80,
    "ayse": 90,
    "mehmet": 75
}

seri = pd.Series(veri)
print(seri)
"""
index   value
ali       80
ayse      90
mehmet    75
"""

# series özellikleri
print(seri.index) # index Index(['ali', 'ayse', 'mehmet'], dtype='str')
print(seri.values) # değerleri [80 90 75]
print(seri.dtype) # int64

# series ile matematiksel işlemler
veri = pd.Series([10, 20, 30, 40])
sonuc = veri * 2
print(sonuc)

# series filtreleme
yas = pd.Series([10, 20, 30, 40, 50])
filtre = yas > 25 # boolean filtre
print(filtre)
"""
0    False
1    False
2     True
3     True
4     True
"""
sonuc = yas[filtre]
print(sonuc)