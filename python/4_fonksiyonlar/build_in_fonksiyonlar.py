"""
1) build in functions: pythonda tanımlı fonksiyonlar
2) user defined functions: developer tanımlar
"""
liste = [1,2,3,4,5]
print(len(liste)) #len python'da tanımlı bir fonksiyondur
x = 3.14
print(type(x)) #type python'da tanımlı bir fonksiyondur 

# sum(), max(), min()
sayilar = [ 1, 2, 3, 5]
print(sum(sayilar)) # 11
print(max(sayilar)) # 5
print(min(sayilar)) # 1

# abs() verilen sayının mutlak değerini döndürür
x = -8
print(abs(x))

# round() verilen sayıyı yuvarlar
x = 3.56546546546
print(round(x, 3)) # 3.565

# sorted() verilen listeyi sıralar ve yeni bir liste döndürür
sayilar = [5,3,7,1,9,2]
print(sorted(sayilar)) # [1, 2, 3, 5, 7, 9]

# machine learning -> sınıflandırma -> sklearn fit()

# derin öğrenme -> tahmin -> tensorflow predict()