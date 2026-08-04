import matplotlib.pyplot as plt

# ÖRNEK VERİ

aylar = ["Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran"]
satislar = [120, 150, 170, 160, 200, 220]
karlar = [20, 35, 40, 30, 50, 60]
reklam = [5, 8, 10, 7, 12, 15]


# Aylar ve satışlar verisini kullanarak basit bir çizgi grafiği oluşturun.

plt.plot(aylar,satislar)
plt.show()


# Aylar ve kârlar verisini kullanarak çizgi grafiği oluşturun.
# Çizgi rengi kırmızı olsun.

plt.plot(aylar, karlar, color = "red")
plt.show()


# Aylar ve satışlar verisini kullanarak marker'lı bir çizgi grafiği oluşturun.

plt.plot(aylar, satislar, marker = "o")
plt.show()


# Aylar ve satışlar verisini kullanarak sütun grafiği oluşturun.

plt.bar(aylar, satislar)
plt.show()


# Aylar ve reklam verisini kullanarak yeşil renkli bir sütun grafiği oluşturun.

plt.bar(aylar, reklam, color = "green")
plt.show()


# Satışlar verisini kullanarak pasta grafiği oluşturun.
# Ay isimlerini etiket olarak gösterin ve yüzdeleri ekrana yazdırın.

plt.pie(satislar, labels=aylar, autopct="%1.1f%%")
plt.show()


# Reklam ve satışlar verisini kullanarak scatter plot oluşturun.

plt.scatter(reklam, satislar)
plt.show()


# Reklam ve kâr verisini kullanarak kırmızı renkli ve büyük noktalı scatter plot oluşturun.

plt.scatter(reklam, karlar, color="red", s=150)
plt.show()


# Aynı figür içinde 1 satır 2 sütun olacak şekilde iki grafik oluşturun.
# Solda satışlar için line plot, sağda kârlar için bar chart gösterin.
 
plt.subplot(1, 2, 1)
plt.plot(aylar, satislar)

plt.subplot(1, 2, 2)
plt.bar(aylar, karlar)

plt.show()


# 2 satır 2 sütun olacak şekilde 4 farklı grafik oluşturun.
# 1. grafik: satışlar line plot
# 2. grafik: kârlar bar chart
# 3. grafik: reklam-satış scatter plot
# 4. grafik: satışlar pie chart

plt.subplot(2, 2, 1)
plt.plot(aylar, satislar, marker="o")
plt.title("garfik 1")


plt.subplot(2, 2, 2)
plt.bar(aylar, karlar, color="orange")
plt.title("garfik 2")

plt.subplot(2, 2, 3)
plt.scatter(reklam, satislar, color="green", s=100)
plt.title("garfik 3")

plt.subplot(2, 2, 4)
plt.pie(satislar, labels=aylar, autopct="%1.1f%%")
plt.title("garfik 4")

plt.show()