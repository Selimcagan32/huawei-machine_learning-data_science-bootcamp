import numpy as np

"""
Çok boyutlu diziler
"""
# 2 boyutlu dizi oluşturma
matris = np.array(
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
)
print(matris)

print(matris.shape) # (3, 3)  dizinin boyutunu 

print(matris.ndim) # 2  dizinin kaç boyutlu olduğu

print(matris.size) # 9  dizideki eleman sayısı

# 3 boyutlu dizi 
"""
görsel -> (height, width) -> (yükseklik ve genişlik) -> (1920, 1080), (1920, 1080), (1920, 1080), ... (1920, 1080) -> (N, 1920, 1080)
"""
dizi3 = np.array(
    [
        [
            [1,2],
            [3,4]
        ],
        [   
            [5,6],
            [7,8]
        ]
    ]
)
print(dizi3)

"""
(2 adet matris, her matriste 2 satır, her matriste 2 sütun) iki matriste aynı boyutlarda olması gerekiyor
"""
print(dizi3.shape) # (2, 2, 2)

# numpy ile çok boyutlu dizi oluşturma (reshape)
dizi = np.arange(1,13)
print(dizi) # [ 1  2  3  4  5  6  7  8  9 10 11 12]

# matrise dönüştürma
matris = dizi.reshape(3, 4)
print(matris)
"""
3 satır, 4 sütun
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]]
"""

# matris = dizi.reshape(3, 5) # ValueError: cannot reshape array of size 12 into shape (3,5)
