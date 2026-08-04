i = 0 
while i < 5: # i küçüktür 5 ten koşulu doğru olduğu sürece
    print(i)
    i = i + 1

print(f"i: {i}")

# sayaç mantığı
sayac = 1
while sayac <= 3:
    print("merhaba")
    sayac += 1

# while + if kullanımı
i = 0
while i < 10:
    if i % 2 == 0:
        print(f"çift: {i}")   
    i += 1

# kullanıcı kontrollü while
giris = ""
while giris != "q": 
    giris = input("Çıkmak için q yazın: ")
    print(f"Kullanıcı mesajı: {giris}")

# chatbot örneği
giris = ""
while giris != "q": 

    giris = input("Çıkmak için q yazın: ")
    print(f"Kullanıcı mesajı: {giris}")
    # chatbot bize cevabı return eder
    # chatbotun cevabını ekrana yazdırıyoruz
    print("chatbot: merhaba")