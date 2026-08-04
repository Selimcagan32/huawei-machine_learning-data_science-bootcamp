"""
Kullanıcıdan vize notu ve final notu al orta hesapla ve harf notunu belirle
"""

# not hesaplama
def ort_hesap(vize: float, final: float) -> float:
    ortalama = vize * 0.4 + final * 0.6
    return ortalama

def harf_not(ortalama: float) -> str:
    if ortalama >= 85:
        return "A"
    elif ortalama >= 70:
        return "B"
    elif ortalama >= 50:
        return "C"
    else:
        return "F"

def sonuc(isim: str, ortalama: float, harf: str):
    print("----------------------------")
    print(f"Öğrenci: {isim}")
    print(f"Ortalama: {ortalama}")
    print(f"Harf Notu: {harf}")


# program akış
isim = input("öğrenci adı: ")
vize = float(input("Vize not: "))
final = float(input("Final not: "))

ortalama = ort_hesap(vize = vize, final = final)
harf = harf_not(ortalama = ortalama)

sonuc(isim = isim, ortalama = ortalama, harf = harf)