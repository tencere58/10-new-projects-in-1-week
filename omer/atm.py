bakiye = 1000
kredi = 2000



while True:
    islem = int(input("Para Çek (0) \n Para Yatır (1) \n Bakiye Göster (2) \n Kredi Limiti Göster (3) \n Hesabımdan Çıkış Yap (4) \n İşlem Seçiniz: "))
    if islem == 0:
        miktar = int(input("Çekmek istediğiniz para miktarını giriniz: "))
        if miktar <= bakiye:
            bakiye -= miktar
            print(f"Güncel Bakiyeniz: {bakiye} TL")
        elif miktar < bakiye+kredi:
            kalan = miktar - bakiye
            kredi = kredi - kalan
            bakiye = bakiye - miktar
            print(f"Güncel Kredi Limitiniz: {kredi} TL")
            print(f"Güncel Bakiyeniz: {bakiye} TL")
        elif miktar > bakiye+kredi:
            print("Malesef yetersiz kredi limiti sebebiyle isteğinizi yerine getiremiyoruz.")
    elif islem == 1:
        miktar = int(input("Yatırmak istediğiniz para miktarını giriniz: "))
        bakiye += miktar
        print(f"Güncel Bakiyeniz: {bakiye} TL")
    elif islem == 2:
        print(f"Güncel Bakiyeniz: {bakiye} TL")
    elif islem == 3:
        print(f"Güncel Kredi Limitiniz: {kredi} TL")
    elif islem == 4:
        break

