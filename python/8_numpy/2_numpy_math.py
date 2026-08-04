import numpy as np
"""
matematiksel işlemler
"""

# toplama
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
sonuc = a + b
print(sonuc) # [5 7 9]

# çıkarma
sonuc = a - b
print(sonuc) # [-3 -3 -3]

# çarpma
sonuc = a * b
print(sonuc) # [ 4 10 18]

# bölme
sonuc = a / b
print(sonuc) # [0.25 0.4  0.5 ]

# dizi ile sayı arasında işlem
a = np.array([1, 2, 3])
sonuc = a * 2 
print(sonuc) # [2 4 6]

# dizinin karesi
a = np.array([1, 2, 3, 4])
sonuc = a ** 2
print(sonuc) # [ 1  4  9 16]

# karekökü
a = np.array([1, 4, 9, 16])
sonuc = np.sqrt(a)
print(sonuc) # [1. 2. 3. 4.]

# dizinin toplamını bulma
a = np.array([1, 2, 3, 4])
print(np.sum(a)) # 10

# ortalama
print(np.mean(a)) # 2.5

# min max
print(np.max(a)) # 4
print(np.min(a)) # 1

# standart sapma
print(np.std(a)) # 1.1