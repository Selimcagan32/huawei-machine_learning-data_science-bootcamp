import matplotlib.pyplot as plt
"""
dağılım grafiği (scatter plot)
"""

calisma_saatleri = [1, 2, 3, 4, 5, 6]
notlar = [50, 55, 65, 70, 80, 90]


# (x = calisma_saatleri, y = notlar)
plt.scatter(calisma_saatleri, notlar, color = "red", s = 100)
# s = nokta boyutunu değiştirme


plt.title("Çalışma Süresi ve Sınav Notu") # grafik başlığı
plt.xlabel("Çalışma Saatleri") # x ekseni başlık
plt.ylabel("Notlar") # y ekseni başlık


plt.show()



# birden fazla veri grubu çizdirme

# fen sonuçları
x1 = [1, 2, 3, 4]
y1 = [50, 60, 70, 80]

# mat sonuçları
x2 = [1, 2, 3, 4]
y2 = [55, 65, 75, 85]

plt.scatter(x1, y1, color ="blue", label = "fen")
plt.scatter(x2, y2, color = "red", label = "mat")
plt.legend()
plt.show()
