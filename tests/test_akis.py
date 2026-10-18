import itertools
from uzay_oyunu.akis import fibonacci, yakit_gostergesi

def test_fibonacci_yontemleri():
    # 1. Yöntem: next() ile ilk üç değeri alma
    g = fibonacci()
    assert (next(g), next(g), next(g)) == (0, 1, 1)

    # 2. Yöntem: islice ile ilk 12 değeri alma
    assert list(itertools.islice(fibonacci(), 12)) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

    # 3. Yöntem: takewhile ile 100'den küçük değerleri alma
    assert list(itertools.takewhile(lambda x: x < 100, fibonacci())) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

def test_fibonacci_tek_kullanimlik():
    # Üretecin tek kullanımlık olduğunu gösterme
    g = fibonacci()
    
    ilk_cagri = list(itertools.islice(g, 5)) # İlk 5'i alır: [0, 1, 1, 2, 3]
    ikinci_cagri = list(itertools.islice(g, 5)) # Kaldığı yerden 5 tane alır: [5, 8, 13, 21, 34]
    
    # İkinci çağrının baştan başlamadığını (farklı sonuç verdiğini) doğruluyoruz
    assert ilk_cagri != ikinci_cagri
    assert ikinci_cagri == [5, 8, 13, 21, 34]

def test_yakit_gostergesi():
    # Örneğin birebir testi
    assert list(yakit_gostergesi(100, 30)) == [70, 40, 10, 0]
    
    # Tam bitme durumu testi
    assert list(yakit_gostergesi(50, 25)) == [25, 0]

# --- GÖREV 3 TESTLERİ ---
def test_seyir_defteri_toplam_yakit():
    # Toplam yakıtın 88 çıkıp çıkmadığını test ediyoruz
    from uzay_oyunu.akis import satirlari_oku, ayristir
    toplam_yakit = sum(y for _, _, y in ayristir(satirlari_oku("uzay_oyunu/veri/seyir.txt")))
    assert toplam_yakit == 88

def test_uzun_yolculuklar():
    # Yakıtı 10'dan büyük olan rotaları test ediyoruz
    from uzay_oyunu.akis import satirlari_oku, ayristir, uzun_yolculuklar
    kayitlar = ayristir(satirlari_oku("uzay_oyunu/veri/seyir.txt"))
    hedefler = [h for _, h, _ in uzun_yolculuklar(kayitlar, 10)]
    assert hedefler == ['sirius', 'centauri', 'orion', 'kara_delik']