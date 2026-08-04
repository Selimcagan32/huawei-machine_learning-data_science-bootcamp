import pandas as pd

"""
Dosya okuma ve yazma
"""

# csv (comma separated values) dosyası okuma
df = pd.read_csv("veri.csv")
print(df)
"""
     isim   yas   not
0    kaan    35    90
1     can    25    95
2  yılmaz    30    85
"""

# excel okuma
df = pd.read_excel("veri_excel.xlsx")
print(df)
"""
     isim  yas  not
0    kaan   35   95
1     can   25   90
2  yılmaz   30   85
"""

# csv ve excel dosyası yazma
veri = {
    "isim": ["ali", "ayse", "mehmet"],
    "yas": [25, 30, 35]
}

# csv dosyası yazma
df = pd.DataFrame(veri)
df.to_csv("veri_output.csv", index=False) # index=False parametresi ile index sütunu yazdırılmaz

# excel dosyası yazma
df.to_excel("veri_output.xlsx", index=False) 