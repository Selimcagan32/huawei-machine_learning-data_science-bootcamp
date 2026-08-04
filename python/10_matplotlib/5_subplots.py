import matplotlib.pyplot as plt
"""
subplots
"""

x = [1, 2, 3, 4]
y1 = [10, 20, 30, 40]
y2 = [40, 30, 20, 10]

plt.subplot(1, 2, 1) # (1 satıra ,  2 grafik sütunu,  grafik numarası)
plt.plot(x, y1)
plt.title("Grafik 1")

plt.subplot(1, 2, 2)
plt.plot(x, y2)
plt.title("Grafik 2")

plt.show()

# farklı grafik türleri kullanarak subplot oluşturma
x = [1, 2, 3, 4]
y = [10, 20, 30, 40]

plt.subplot(1, 2, 1)
plt.plot(x, y)
plt.title("Line Plot")

plt.subplot(1, 2, 2)
plt.bar(x, y)
plt.title("Bar Chart")

plt.show()

# 2x2 grafik oluşturma
x = [1, 2, 3, 4]
y = [10, 20, 30, 40]

plt.subplot(2, 2, 1) # 2 satıra 2 grafik sütunu 
plt.plot(x, y)
plt.title("Grafik 1")

plt.subplot(2, 2, 2)
plt.bar(x, y)
plt.title("Grafik 2")

plt.subplot(2, 2, 3)
plt.scatter(x, y)
plt.title("Grafik 3")

plt.subplot(2, 2, 4)
plt.pie(y)
plt.title("Grafik 4")

plt.show()