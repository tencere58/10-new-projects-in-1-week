import random

def adam_asmaca():
    
    kelimeler = ["PYTHON", "YAZILIM", "BILGISAYAR", "KLAVYE", "EKRAN", "MOUSE"]
    
    secilen_kelime = random.choice(kelimeler)
    tahmin_edilenler = []
    can = 5
    
    print(f"Toplam can: {'❤️ ' * can} ")
    
    while can > 0:
        gorunen_kelime = ""
        for harf in secilen_kelime:
            if harf in tahmin_edilenler:
                gorunen_kelime += harf + " "
            else:
                gorunen_kelime += "_ "
        
        print(f"Kelime: {gorunen_kelime}")
        print(f"Kalan Can: {'❤️ ' * can}")
        
        if "_" not in gorunen_kelime:
            print(f"\n TEBRİKLER! Kelimeyi bildin: {secilen_kelime} ")
            break
            
        
        tahmin = input("Bir harf tahmin edin: ").upper()
        
        if len(tahmin) != 1:
            print("Lütfen tek bir harf giriniz!\n")
            continue
            
        if tahmin in tahmin_edilenler:
            print("Bu harfi zaten söylediniz.\n")
            continue
            
        tahmin_edilenler.append(tahmin)
        
        if tahmin in secilen_kelime:
            print(f"Süper! '{tahmin}' harfi var.\n")
        else:
            can -= 1
            print(f"Maalesef... '{tahmin}' harfi yok.\n")
            
    if can == 0:
        print(f"\nKAYBETTİNİZ! Kelime şuydu: {secilen_kelime} ")


adam_asmaca()