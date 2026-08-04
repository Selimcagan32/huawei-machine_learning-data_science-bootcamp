import matplotlib.pyplot as plt

"""
sütun grafikleri (bar charts)
"""

# sütun grafiği oluştur
isimler = ["Selim", "Fatih", "Merve", "Zeynep"]
notlar = [90, 70, 85, 95]

renkler = ["yellow", "blue", "green", "orange"] # her bir sütun için renkler

# (x = isimler, y = notlar) 
plt.bar(isimler, notlar, color = renkler)

plt.title("Öğrenci Notları") # grafik başlığı
plt.xlabel("Öğrenciler") # x ekseni başlığı
plt.ylabel("Notlar") # y ekseni başlığı

plt.show()

# yatay sütun grafiği
plt.barh(isimler, notlar) # bar ın yanına h (horizontal) ekleyerek yatay sütun grafiği oluşturulur
plt.show()
