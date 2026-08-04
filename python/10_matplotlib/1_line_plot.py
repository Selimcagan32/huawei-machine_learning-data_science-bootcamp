import matplotlib.pyplot as plt 

"""
line plot
"""

# çizgi grafiği oluşturma
gunler = [1, 2, 3, 4, 5]
sicaklik = [22, 24, 23, 25, 27]


#(x = gunler, y = sicaklik)                                 
plt.plot(gunler, sicaklik, color = "red" , linestyle = "--" , marker = "o")
# color = çizgi rengi
# linestyle = çizgi stili
# marker = noktaları gösterme


plt.title("Günlere Göre Sıcaklık") # grafik başlığı
plt.xlabel("Günler") # grafikte x eksenine isim verme
plt.ylabel("Sıcaklık") # grafikte y eksenine isim verme


plt.grid(True) # grafikte grid çizgilerini gösterme

plt.show() # grafiğin ekranda görünmesini sağlar