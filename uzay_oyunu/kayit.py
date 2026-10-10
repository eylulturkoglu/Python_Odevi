def gorev_kaydi(baslik, *adimlar, oncelik="normal", **ekler):
    # Çıktı metnini oluşturmaya başlıyoruz
    satirlar = []
    satirlar.append(f"[{oncelik.upper()}] {baslik}")
    
    # Adımları 1, 2, 3 diye numaralandırarak ekliyoruz
    for i in range(len(adimlar)):
        satirlar.append(f"  {i+1}. {adimlar[i]}")
        
    # Ek bilgileri (sorumlu: Ayşe vb.) ekliyoruz
    for anahtar, deger in ekler.items():
        satirlar.append(f"  {anahtar}: {deger}")
        
    # Hepsini alt alta birleştirip döndürüyoruz
    return "\n".join(satirlar)

# "iki çağrı biçimini de main bloğunda gösterin" kuralı:
if __name__ == "__main__":
    # 1. Çağrı Biçimi: Argümanları doğrudan elle vererek
    print("--- 1. NORMAL ÇAĞRI BİÇİMİ ---")
    print(gorev_kaydi("Kara deliğe atla", "Kredi kazan", "Pilot bul", "Hiperdrive al", oncelik="Yüksek", sorumlu="Ayşe"))
    
    print("\n--- 2. YILDIZLI AÇARAK ÇAĞRI BİÇİMİ ---")
    # 2. Çağrı Biçimi: Liste (*) ve Sözlük (**) açarak
    adimlar_listesi = ["Kredi kazan", "Pilot bul", "Hiperdrive al"]
    ekler_sozlugu = {"sorumlu": "Ayşe"}
    print(gorev_kaydi("Kara deliğe atla", *adimlar_listesi, oncelik="Yüksek", **ekler_sozlugu))