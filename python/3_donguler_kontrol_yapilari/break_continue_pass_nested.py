"""
Break 
    - döngüyü tamamen durdur
    - koşul sağlandığında döngüden çıkar
"""

for i in range(10):
    if i == 5: # eğer i değeri 5 e eşitse döngüden çıksın, yani döngü devam etmesin
        break
    print(i)

"""
Continue 
    - o anki turun atlanır ama döngü devam eder
"""

for i in range(10):
    if i == 5:
        continue
    print(i)

"""
Pass 
    - henüz kod yazmadığımız yerlerde hata vermemesi için kullanılır
"""

for i in range(3):
    if i == 1:
        pass
        # todo: eğer 1 ise buraya bir şeyler yap
    print(i)

"""
nested yapılar:
    - yapıların birbirinin içinde olması
"""

# for-if 
for i in range(8):
    if i % 2 == 0:
        print(i)

# if-if
yas = 19
ogrenci = True

if yas < 24:
    if ogrenci:
        print("indirim var")

# for-for
for i in range(2):
    for j in range(2):
        print(f"i: {i}, j: {j}")