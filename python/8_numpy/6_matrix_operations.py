import numpy as np

"""
Matris işlemleri
"""

# matris oluşturma
a = np.array([
    [1, 2],
    [3, 4]
])

b = np.array([
    [5, 6],
    [7, 8]
])

print(a)
print(b)

print(a + b) # toplama eleman bazında olarak yapılır
print(a - b) # çıkarma 
print(a * b) # çarpma 

# gerçek matris çarpımı satır x sütun olarak yapılır
sonuc = np.dot(a, b)
print(sonuc)
"""
[1, 2],
[3, 4]
*
[5, 6],
[7, 8]
=
[[19 22]
 [43 50]]
"""

# matris transpose (matrisin ters çevrilmesi) satırlar sütun olur
print(a.T)

"""
[1, 2],
[3, 4]

[[1 3]
 [2 4]]
"""

# matris determinantı
det = np.linalg.det(a)
print(det) # -2.0000000000000004

# matrisin tersi
ters = np.linalg.inv(a)
print(ters)
"""
[[-2.   1. ]
 [ 1.5 -0.5]]
"""