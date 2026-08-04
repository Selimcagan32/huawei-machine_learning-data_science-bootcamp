import numpy as np
"""
Dizi birleştirme ve bölme
"""

# dizi birleştirme
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

sonuc = np.concatenate((a, b))
print(sonuc) # [1 2 3 4 5 6]

# iki boyutlu dizi birleştirme
a = np.array(
    [
        [1, 2],
        [3, 4]
    ]
)

b = np.array(
    [
        [5, 6], 
        [7, 8]
    ]
)

sonuc = np.concatenate((a, b))
print(sonuc)
"""
varsayılan olarak satır yönünde birleştirdik
[[1 2]
 [3 4]
 [5 6]
 [7 8]]
"""

# axis parametresi
# axis = 0 -> satır yönünde birleştirme
# axis = 1 -> sütun yönünde birleştirme

sonuc = np.concatenate((a, b), axis = 1)
print(sonuc)
"""
[[1 2 5 6]
 [3 4 7 8]]
"""

# vstack (dikey birleştirme): axis = 0 gibi yapar
sonuc = np.vstack((a, b))
print(sonuc)

# hstack (yatay birleştirme): axis = 1 gibi yapar
sonuc = np.hstack((a, b))
print(sonuc)

# diziyi parçalara bölme
dizi = np.array([1,2,3,4,5,6])

sonuc = np.split(dizi, 2) # 2 parçaya böl
print(sonuc) # [array([1, 2, 3]), array([4, 5, 6])]

sonuc = np.split(dizi, 3)
print(sonuc) # [array([1, 2]), array([3, 4]), array([5, 6])]

# 2 boyutlu dizilerde bölme
matris = np.array(
    [
        [1, 2],
        [3, 4],
        [5, 6],
        [7, 8]
    ]
)

sonuc = np.split(matris, 2) # satır bazında 2 ye bölme axis = 0
print(sonuc)
"""
array([[1, 2],
       [3, 4]]), 
       
array([[5, 6],
       [7, 8]])
"""

sonuc = np.split(matris, 2, axis = 1) # sütun bazında ikiye bölme axis = 1
print(sonuc)
"""
array([[1],
       [3],
       [5],
       [7]]), 

array([[2],
       [4],
       [6],
       [8]])
"""