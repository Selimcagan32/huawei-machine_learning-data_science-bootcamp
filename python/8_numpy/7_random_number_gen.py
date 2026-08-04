import numpy as np

"""
Rastgele sayı üretme
"""

# rastgele [0-1] arasında sayılar üretme
rastgele = np.random.rand(5)
print(rastgele) # [0.01305906 0.49617281 0.8339516  0.34911464 0.63700101]

# rastgele matris oluşturma
rastgele = np.random.rand(3, 3)
print(rastgele)
"""
[[0.2350457  0.99922835 0.25611634]
 [0.27177059 0.13965271 0.72517363]
 [0.56062539 0.14892058 0.04243103]]
"""

# rastgele tam sayı üretme
rastgele = np.random.randint(1, 10, 5) # 1 ile 10 arasında 5 adet 
print(rastgele) # [1 1 4 8 6]

# rastgele tam sayı matrisi üretme
rastgele = np.random.randint(1, 20, (3, 4)) # 1 ile 20 arasında 3 satır 4 sütun dan oluşan 12 tane tam sayı 
print(rastgele)
"""
[[13 12  8  2]
 [ 1  2 13 12]
 [12 18  4  3]]"""

# aynı rastgele sonucu üretmek için (seed)

np.random.seed(32) #ısparta (yörükistan)
rastgele = np.random.rand(5) #seedi 32 giren herkes için aynı rastgele sayılar üretilir
print(rastgele) # [0.85888927 0.37271115 0.55512878 0.95565655 0.7366696 ]

np.random.seed(None) #tekrar rastgele sayı üretmek için seed'i None yapıyoruz

# bir diziden rastgele eleman seçmek
dizi = np.array([10, 20, 30, 40, 50])
secim = np.random.choice(dizi)
print(secim)

# birden fazla eleman seçme 
secim = np.random.choice(dizi, 3)
print(secim)