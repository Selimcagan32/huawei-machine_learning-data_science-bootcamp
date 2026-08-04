import numpy as np
# SORU 1
# 1) NumPy kullanarak 1’den 20’ye kadar sayılardan oluşan bir dizi oluşturun.
# 2) Dizinin kaç eleman içerdiğini ekrana yazdırın.

dizi= np.arange(1, 21)
print(dizi)
print("Dizi eleman sayısı:", len(dizi))

# SORU 2
# 1) [5, 10, 15, 20, 25] değerlerinden oluşan bir NumPy dizisi oluşturun.
# 2) Dizideki tüm elemanları 3 ile çarpın.
# 3) Sonucu ekrana yazdırın.

dizi2 = np.array([5, 10, 15, 20, 25])
print("Dizi2:", dizi2)
dizi2_carpim = dizi2 * 3
print("Dizi2'nin 3 ile çarpımı:", dizi2_carpim)

# SORU 3
# 1) 0’dan 30’a kadar sayılar içeren bir dizi oluşturun.
# 2) Bu diziden sadece 10 ile 20 arasındaki elemanları slicing kullanarak seçin.

dizi3 = np.arange(0, 31)
print("Dizi3:", dizi3)
dizi3_secim = dizi3[10:21]
print("Dizi3'ten 10 ile 20 arasındaki elemanlar:", dizi3_secim)


# SORU 4
# 1) [1,2,3] ve [4,5,6] dizilerini oluşturun.
# 2) Bu iki diziyi NumPy kullanarak birleştirin.

dizi_a = np.array([1, 2, 3])
dizi_b = np.array([4, 5, 6])
print("Dizi A:", dizi_a)
print("Dizi B:", dizi_b)
dizi_birlestirilmis = np.concatenate((dizi_a, dizi_b))
print("Birleştirilmiş dizi:", dizi_birlestirilmis)

# SORU 5
# 1) 1’den 12’ye kadar sayılar içeren bir dizi oluşturun.
# 2) Bu diziyi reshape kullanarak 3x4 boyutunda bir matrise dönüştürün.
# 3) Matrisin shape değerini yazdırın.

dizi4 = np.arange(1, 13)
print("Dizi4:", dizi4)
matris = dizi4.reshape(3, 4)
print("Matris:\n", matris)
print("Matrisin shape değeri:", matris.shape)


# SORU 6
# 1) Aşağıdaki matrisi oluşturun
# [[1,2,3],
#  [4,5,6],
#  [7,8,9]]
# 2) İkinci satırı ekrana yazdırın.
# 3) İkinci sütunu ekrana yazdırın.

matris2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Matris2:\n", matris2)
ikinci_satir = matris2[1, :]
print("İkinci satır:", ikinci_satir)
ikinci_sutun = matris2[:, 1]
print("İkinci sütun:", ikinci_sutun)

# SORU 7
# 1) 3x3 boyutunda rastgele sayılardan oluşan bir matris oluşturun.
# 2) Matrisin ortalamasını hesaplayın.
# 3) Matrisin maksimum değerini yazdırın.

matris3 = np.random.rand(3, 3)
print("Rastgele matris:\n", matris3)
print("Matrisin ortalaması:", np.mean(matris3))
print("Matrisin maksimum değeri:", np.max(matris3))

# SORU 8
# 1) [2,4,6,8] ve [1,3,5,7] dizilerini oluşturun.
# 2) Dizileri eleman bazlı çarpın.
# 3) Sonucu ekrana yazdırın.

dizix = np.array([2, 4, 6, 8])
diziy = np.array([1, 3, 5, 7])
dizi_carpimi = dizix * diziy
print("Dizilerin eleman bazlı çarpımı:", dizi_carpimi)

# SORU 9
# 1) 1’den 9’a kadar sayılar içeren bir dizi oluşturun.
# 2) Bu diziyi 3x3 matrise dönüştürün.
# 3) Matrisin transpose’unu hesaplayın.

dizi5 = np.arange(1, 10)
print("Dizi5:", dizi5)
matris4 = dizi5.reshape(3, 3)
print("Matris4:\n", matris4)
print("Matris4'ün transpose'u:\n", matris4.T)

# SORU 10
# 1) 1 ile 50 arasında rastgele 10 tam sayı üretin.
# 2) Bu sayılardan oluşan dizinin toplamını hesaplayın.
# 3) Dizinin ortalamasını yazdırın.

dizi5 = np.random.randint(1, 51, 10)
print("Rastgele tam sayılar:", dizi5)
print("Dizinin toplamı:", np.sum(dizi5))
print("Dizinin ortalaması:", np.mean(dizi5))