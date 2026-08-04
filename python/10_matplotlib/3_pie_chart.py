import matplotlib.pyplot as plt

"""
pie chart
"""

etiketler = ["python", "java", "c++", "javascript"]
degerler = [40, 25, 20, 15]


ayrim = [0, 0, 0, 0.1] # dilimi ayrımak için
renkler = ["blue", "yellow", "green", "orange"]

plt.pie(degerler, labels = etiketler, explode = ayrim, autopct="%1.1f%%", colors = renkler)
# labels = her dilimin etiketi
# autopct %1.1f%% = yüzdeyi 1 basamaklı ondalık ile gösterir


plt.title("Programlama Dili Kullanımı") # grafik başlığı

plt.show()