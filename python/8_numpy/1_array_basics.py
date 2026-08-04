import numpy as np

"""
Diziler (array)
    - ndarray: n-dimensional array
"""

# liste ile numpy dizisi farkları

sayilar = [1, 2, 3, 4, 5] # liste
print(sayilar)

# np.array() -> listeyi numpy dizisine çevirir
dizi = np.array(sayilar) # numpy dizisi
print(dizi)

# numpy dizisi tipi
print(type(dizi)) # <class 'numpy.ndarray'>

# numpy dizisi boyutu öğrenme
print(dizi.shape) # (5,) -> 5 elemanlı tek boyutlu bir dizi

# numpy dizisinin veri tipi
print(dizi.dtype) # int64 -> integer

# numpy ile dizi oluşturma
dizi = np.zeros(5) # [0. 0. 0. 0. 0.]  
print(dizi)

dizi = np.ones(5) # [1. 1. 1. 1. 1.]
print(dizi)

# belirli bir aralıkta sayı dizisi oluşturma
dizi = np.arange(0, 10)
print(dizi) # [0 1 2 3 4 5 6 7 8 9]

# belirli aralıklarla sayı üretme 
dizi = np.arange(0, 10, 2)
print(dizi) # [0 2 4 6 8]

# belirli bir aralığa eşit bölünmüş diziler
dizi = np.linspace(0, 10, 5) # 0 ile 10 arasında 5 sayı
print(dizi) # [ 0.   2.5  5.   7.5 10. ]
