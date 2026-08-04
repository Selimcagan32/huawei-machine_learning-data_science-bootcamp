import numpy as np

"""
indeksleme (indexing) - dilimleme (slicing)
"""
# dizilerde indeksleme
dizi = np.array([10, 20, 30, 40, 50])
print(dizi[0]) # 10

# negatif indeksleme
print(dizi[-1]) # 50

# slicing (dilimleme)
# genel kullanım: dizi[başlangıç:bitiş]
print(dizi[1:4]) # 20, 30, 40 # 1. indeksten başlar 4 dahil değildir.

# baştan dilimleme
print(dizi[:3]) # 10, 20, 30

# sondan dilimleme
print(dizi[2:]) # 30, 40, 50

# adım (step) kullanımı
print(dizi[::2]) # diziden ikişer adım ile eleman seçmek [10 30 50]

# 2 boyutlu dizilerde indeksleme
matris = np.array(
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
)
print(matris)

print(matris[0, 0]) # 1 

# belirli bir satırı seçmek
print(matris[1, :]) # [4 5 6] tümünü seçmek için : kullanılır.

# belirli bir sutunu seçmek
print(matris[:, 2]) # [3 6 9]

# matris dilimleme
print(matris[0:2, 0:2])
