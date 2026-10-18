from typing import Iterator
from typing import Iterator, Iterable, Tuple
from functools import lru_cache
def fibonacci() -> Iterator[int]:
    """
    Sonsuz bir Fibonacci dizisi üreten üreteç (generator) fonksiyonu.
    Her çağrıldığında dizinin bir sonraki elemanını üretir.
    """
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def yakit_gostergesi(yakit: int, tuketim: int) -> Iterator[int]:
    """
    Her adımda (next çağrıldığında) yakıtı tüketim kadar azaltan üreteç.
    Yakıt bitince (0 veya altına düşünce) 0 değerini verip durur.
    """
    while yakit > 0:
        yakit -= tuketim
        if yakit < 0:
            yakit = 0
        yield yakit

# --- GÖREV 3 KODLARI ---

def satirlari_oku(yol: str) -> Iterator[str]:
    """
    Belirtilen dosyadaki metni satır satır okur.
    Boş satırları ve '#' karakteri ile başlayan yorum satırlarını atlar.
    """
    with open(yol, "r", encoding="utf-8") as dosya:
        for satir in dosya:
            temiz_satir = satir.strip()
            if temiz_satir and not temiz_satir.startswith("#"):
                yield temiz_satir

def ayristir(satirlar: Iterable[str]) -> Iterator[Tuple[str, str, int]]:
    """
    Okunan metin satırlarını boşluklardan bölerek ayrıştırır.
    Her satır için (kaynak, hedef, yakıt) formatında bir demet (tuple) üretir.
    """
    for satir in satirlar:
        parcalar = satir.split() 
        kaynak = parcalar[0]
        hedef = parcalar[2]
        yakit = int(parcalar[3])
        yield (kaynak, hedef, yakit)

def uzun_yolculuklar(kayitlar: Iterable[Tuple[str, str, int]], esik: int) -> Iterator[Tuple[str, str, int]]:
    """
    Verilen uçuş kayıtları arasından, harcanan yakıt miktarı 
    belirtilen 'esik' değerinden kesinlikle büyük olanları süzer.
    """
    for kaynak, hedef, yakit in kayitlar:
        if yakit > esik:
            yield (kaynak, hedef, yakit)

def rota_sayaci(baglantilar):
    """Verilen bağlantılara göre lru_cache ile optimize edilmiş rota sayacı döndürür."""
    @lru_cache(maxsize=None)
    def rota_sayisi(gezegen, adim):
        if adim == 0:
            return 1
        if gezegen not in baglantilar:
            return 0
        return sum(rota_sayisi(komsu, adim - 1) for komsu in baglantilar[gezegen])
    
    return rota_sayisi