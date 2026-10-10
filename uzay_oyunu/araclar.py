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
    
    # Gezegenleri önce bağlantı sayısına (çoktan aza - eksi işareti ile), 
    # sonra alfabetik olarak sıralayan lambda
    sirali = sorted(gezegenler, key=lambda g: (-len(baglantilar.get(g, [])), g))
    return sirali

# Çalıştığını görmek için test bloğu
if __name__ == "__main__":
    print("--- Hamle Sayacı Testi ---")
    sayici = hamle_sayaci()
    print("Adım:", sayici())
    print("Adım:", sayici())
    
    print("\n--- En Bağlı Gezegenler Testi ---")
    # Test için Görev 3'teki harita verimizi simüle ediyoruz
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
    print("Sıralama:", en_bagli_gezegenler(g))