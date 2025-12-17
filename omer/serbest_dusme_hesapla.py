import math

def serbest_dusme_hesapla():
    print("Cismin bırakıldığı yüksekliği girin, süreyi ve hızı bulalım.")
    
    try:
        
        g = 9.81
        h = float(input("Yükseklik (metre cinsinden): "))
        
        if h < 0:
            print("Yükseklik negatif olamaz!")
            return

        t = math.sqrt(2 * h / g)
        
        v = g * t
        
        print(f"Yükseklik: {h} metre iken")
        print(f"Düşme Süresi: {t:.2f} saniye")
        print(f"Yere Çarpma Hızı: {v:.2f} m/s")
        
    except ValueError:
        print("Lütfen geçerli bir sayı giriniz!")

serbest_dusme_hesapla()