from functools import reduce, partial

# Yolculuk fonksiyonu (partial uygulaması için)
def yolculuk(mesafe, hiz):
    return mesafe / hiz

# 1. Yol: map, filter ve reduce ile çözümler
def buyuk_harf_map(gezegenler):
    return list(map(str.upper, gezegenler))

def en_az_iki_baglanti_filter(baglantilar):
    return list(filter(lambda g: len(baglantilar[g]) >= 2, baglantilar))

def toplam_baglanti_reduce(baglantilar):
    return reduce(lambda toplam, g: toplam + len(baglantilar[g]), baglantilar, 0)


# 2. Yol: Liste üreteci (list comprehension) ve sum ile çözümler (Alternatif yazım)
def buyuk_harf_liste_ureteci(gezegenler):
    return [g.upper() for g in gezegenler]

def en_az_iki_baglanti_liste_ureteci(baglantilar):
    return [g for g in baglantilar if len(baglantilar[g]) >= 2]

def toplam_baglanti_sum(baglantilar):
    return sum(len(baglantilar[g]) for g in baglantilar)


# Görev 5 - Partial (Kısmi uygulama) ve Okunabilirlik Yorumu:
# Okunabilirlik Yorumu: Liste üreteci (list comprehension) ve sum yapısı, 
# map/filter/reduce fonksiyonlarına kıyasla lambda ifadeleri gerektirmediği için 
# Python diline daha uygundur ve okunması çok daha kolaydır.
hizli_yolculuk = partial(yolculuk, hiz=3)
