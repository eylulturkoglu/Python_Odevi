import json
from uzay_oyunu.akis import yakit_gostergesi
def envanter_metni(credits: bool, engines: bool, copilot: bool) -> str:
    """
    Oyuncunun elindeki özelliklere göre envanter durumunu metin olarak döndürür.
    Eğer hiçbir eşya yoksa boş metin döndürür.
    """
    esyalar = []
    if credits:
        esyalar.append("bol kredi")
    if engines:
        esyalar.append("güçlü motorlar") 
    if copilot:
        esyalar.append("yetenekli bir pilot")
        
    if len(esyalar) == 0:
        return ""
        
    return "Sende: " + ", ".join(esyalar)

def hedef_menusu(hedefler: list[str]) -> str:
    satirlar = ["Nereye gitmek istersin?"]
    for i in range(len(hedefler)):
        satirlar.append(f"[{i+1}] {hedefler[i]}")
        
    return "\n".join(satirlar)

def galaksi_kur(gezegenler, baglantilar, baslangic, **kwargs):
    if baslangic not in gezegenler:
        raise ValueError("Başlangıç gezegeni listede yok!")
    
    yakit = kwargs.get("yakit", 50)
    
    return {
        "gezegenler": gezegenler,
        "baglantilar": baglantilar,
        "konum": baslangic,
        "yakit": yakit
    }

# Görev 3: Dosyayı json.load ile okuyup galaksi_kur fonksiyonuna verme
def travel(galaksi: dict):
    # Oyuncunun güncel gezegenini alalım
    mevcut_gezegen = galaksi["konum"]
    
    # 1. Adım: Oyun başında göstergeyi oluşturuyoruz (örn. yakıt 100, tüketim 5)
    gosterge = yakit_gostergesi(galaksi["yakit"], 5) 
    
    print("\n--- UZAY MACERASI BAŞLIYOR ---")
    
    while True:
        print(f"\nŞu anki konumunuz: {mevcut_gezegen.upper()}")
        
        # 2. Adım: Hata yakalama bloğu (Yakıt biterse StopIteration hatası verecek)
        try:
            kalan_yakit = next(gosterge) # Her turda yakıtı azalt
            print(f"Kalan Yakıt: {kalan_yakit}")
            
            # Gidilebilecek hedefleri bul
            hedefler = galaksi["baglantilar"].get(mevcut_gezegen, [])
            
            if not hedefler:
                print("Buradan gidebileceğin bir yer yok, çıkmaz sokağa girdin!")
                break
                
            # Hedef menüsünü göster
            print(hedef_menusu(hedefler))
            
            secim = input("Nereye gitmek istersin? (Çıkmak için q): ")
            
            if secim.lower() == 'q':
                print("Oyundan çıkılıyor...")
                break
                
            # Basit bir seçim kontrolü
            if secim.isdigit() and 1 <= int(secim) <= len(hedefler):
                mevcut_gezegen = hedefler[int(secim)-1] # Yeni konumu belirle
            else:
                print("Geçersiz seçim, tekrar dene.")
                
        # 3. Adım: Mesajı burada veriyoruz
        except StopIteration:
            print("Yakıtın bitti, uzayda sürükleniyorsun...")
            break


# Kodun ana çalıştırılma kısmı
if __name__ == "__main__":
    with open("uzay_oyunu/galaksi.json", "r", encoding="utf-8") as dosya:
        veri = json.load(dosya)
        
    g = galaksi_kur(**veri)
    print("Harita başarıyla yüklendi!")
    
    # Seyahat döngüsünü başlatıyoruz
    travel(g)