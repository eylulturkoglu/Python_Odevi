import json
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
if __name__ == "__main__":
    with open("uzay_oyunu/galaksi.json", "r", encoding="utf-8") as dosya:
        veri = json.load(dosya)
        
    g = galaksi_kur(**veri)
    print("Harita başarıyla yüklendi!")
    print("Başlangıç konumu:", g["konum"])
    print("Kalan Yakıt:", g["yakit"])