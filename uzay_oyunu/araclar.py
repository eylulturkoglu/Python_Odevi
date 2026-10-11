import time

# 1. Fonksiyon: Closure ve nonlocal ile hamle sayacı
def hamle_sayaci():
    sayac = 0
    def artir():
        nonlocal sayac
        sayac += 1
        return sayac
    return artir

# 2. Fonksiyon: Lambda ile gezegen sıralama
def en_bagli_gezegenler(galaksi):
    gezegenler = galaksi["gezegenler"]
    baglantilar = galaksi["baglantilar"]
    
    # Gezegenleri önce bağlantı sayısına, sonra alfabetik olarak sıralayan lambda
    sirali = sorted(gezegenler, key=lambda g: (-len(baglantilar.get(g, [])), g))
    return sirali

# BONUS (+10 Puan): Çalışma süresini ölçen fonksiyon
def sure_olc(fonksiyon):
    def sarmalayici(*args, **kwargs):
        baslangic = time.time()
        sonuc = fonksiyon(*args, **kwargs)
        bitis = time.time()
        print(f"[{fonksiyon.__name__}] Çalışma süresi: {bitis - baslangic:.6f} saniye")
        return sonuc
    return sarmalayici

# Test Bloğu
if __name__ == "__main__":
    print("--- Hamle Sayacı Testi ---")
    sayici = hamle_sayaci()
    print("Adım:", sayici())
    print("Adım:", sayici())
    
    print("\n--- En Bağlı Gezegenler & Bonus Testi ---")
    g = {
        "gezegenler": ["dünya", "mars", "sirius", "centauri", "orion", "kara_delik"],
        "baglantilar": {
            "dünya": ["mars", "sirius"],
            "mars": ["dünya", "centauri"],
            "sirius": ["dünya", "orion", "kara_delik", "centauri"],
            "centauri": ["mars", "orion", "sirius"],
            "orion": ["sirius", "centauri"],
            "kara_delik": ["sirius"]
        }
    }
    
    # Bonus kullanımı:
    en_bagli_gezegenler = sure_olc(en_bagli_gezegenler)
    print("Sıralama:", en_bagli_gezegenler(g))