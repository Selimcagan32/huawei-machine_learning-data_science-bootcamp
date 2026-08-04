# set -> {}
sayilar = {1, 2, 3, 4}
print(sayilar) # {1, 2, 3, 4}

# set tekrar eden elemanları kabul etmez
sayilar = {1, 2, 2, 3, 3, 4}
print(sayilar) # {1, 2, 3, 4}

#setler sırasızdır yani indeksi yoktur              
# print(sayilar[2]) # TypeError: 'set' object is not subscriptable hatası verir çünkü set sırasızdır ve indekslenemez

# listeyi set e çevirme
liste = [1, 2, 2, 3, 4, 4]
benzersiz = set(liste)
print(benzersiz) # {1, 2, 3, 4}

# set eleman ekleme
sayilar.add(5)
print(sayilar) # {1, 2, 3, 4, 5}

# set eleman silme
sayilar.remove(2)
print(sayilar) # {1, 3, 4, 5}

# set işlemleri
a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b)) # birleşim {1, 2, 3, 4, 5}
print(a.intersection(b)) # kesişim {3}
print(a.difference(b)) # fark {1, 2}
print(b.difference(a)) # fark {4, 5}
print(a.symmetric_difference(b)) # simetrik fark {1, 2, 4, 5}