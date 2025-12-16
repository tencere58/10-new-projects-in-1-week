

data = {
    "Urun": [],
    "Fiyat": []
}

while True:
    islem = int(input("Harcama Ekle (0) \n Toplam Harcamayı Göster (1) \n Ürünlerin Harcanma Oranlarını Göster (2) \n İşlem Seçiniz: "))

    if islem == 0:
        while True:
            islem_2 = int(input("Urun Ekle (0) \n Ürün Seç (1) \n Menye Dön (2) \n İşlem Seçiniz: "))
            if islem_2 == 0:
                urun = input("Eklemek istediğiniz ürünü giriniz: ")
                harcama = int(input("Harcama yaptığınız miktarı giriniz: "))
                data["Urun"].append(urun)
                data["Fiyat"].append(harcama)
            elif islem_2 == 1:
                print(data["Urun"])
                secim = input("Seçmek istediğiniz ürünü harfen yazınız: ")
                if secim in data["Urun"]:
                    ek_harcama = int(input(f"{secim} için ek harcama miktarını giriniz: "))
                    index = data["Urun"].index(secim)
                    data["Fiyat"][index] += ek_harcama
                else:
                    print("Ürün Bulunamadı.")
            elif islem_2 == 2:
                break
                    
            print(data)
    elif islem == 1:
        toplam = sum(data["Fiyat"])
        print(f"Toplam Harcamanız: {toplam}")

    elif islem == 2:
        
        for urun, fiyat in zip(data["Urun"], data["Fiyat"]):
            oran = (fiyat / sum(data["Fiyat"])) * 100
            print(f"{urun}: %{oran:.2f}")

