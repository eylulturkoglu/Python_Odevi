# KOMUTLAR sözlüğü: komut_adi -> (fonksiyon, aciklama)
KOMUTLAR = {}

def komut(ad, aciklama=""):
    """
    Fonksiyonu değiştirmeden (fonksiyon, aciklama) olarak KOMUTLAR sözlüğüne kaydeden dekoratör.
    Aynı ad iki kez kullanılırsa tanım anında ValueError fırlatır.
    """
    def decorator(func):
        if ad in KOMUTLAR:
            raise ValueError(f"'{ad}' komutu zaten tanımlı!")
        KOMUTLAR[ad] = (func, aciklama)
        return func
    return decorator


@komut("yardim", "komutları listeler")
def yardim(durum):
    for cmd, (_, aciklama) in KOMUTLAR.items():
        print(f"{cmd:10} {aciklama}")

@komut("envanter", "eşyalarını gösterir")
def envanter(durum):
    # Eğer durum içinde envanter/engines/copilot gibi bilgiler varsa yazdırılır
    print(f"Credits: {durum.get('credits', 0)}, Engines: {durum.get('engines', [])}, Copilot: {durum.get('copilot', 'Yok')}")

@komut("harita", "gidebileceğin gezegenleri gösterir")
def harita(durum):
    konum = durum.get("konum")
    baglantilar = durum.get("baglantilar", {})
    komsu_gezegenler = baglantilar.get(konum, [])
    print(", ".join(komsu_gezegenler))