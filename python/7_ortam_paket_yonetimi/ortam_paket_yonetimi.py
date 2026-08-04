"""
Environment (Ortam)
    - proje için gerekli olan python araçlarının, kütüphanelerin, paketlerin bulunduğu izloe bir çalışma alanıdır.
Neden kullanılır: farklı projelerde farklı sürümlerinin kullanılabilmesi için.

Virtual Environment (Sanal ortam)
    - kurulum: python -m venv venv
    - aktif hale getirmek: 
        - windows: .\venv\Scripts\activate
        - mac, linux: source venv/bin/activate

Paket Yöneticisi (pip)
    - kütüphane = paket
        - numpy: sayısal işlemler
        - pandas: veri analizi
        - matploblit: görselleştirme
    - python paketleri yönetmek için kullanılan araç = pip
        - paket kurabilir
        - silebilir 
        - listeleyebilir (pip list)

Paket kurma:
    - numpy: pip install numpy
    - pandas, matplotlib: pip install pandas matplotlib

requirements.txt
    - bir projenin ihtiyaç duyduğu tüm paketlerin listelendiği dosya
    - pip freeze > requirements.txt

    - Kurulum:
        - pip install -r .\requirements.txt (requirements.txt dosyasındaki paketleri kurar)
"""