import pytest
from uzay_oyunu.komutlar import KOMUTLAR, komut
from uzay_oyunu.oyun import travel

def test_komut_dekoratoru_ve_kayit():
    # Aynı adla ikinci kez tanımlandığında ValueError fırlatıp fırlatmadığını test edelim
    @komut("test_komut_ornek", "açıklama")
    def ornek_fonk(durum):
        return "test"

    assert "test_komut_ornek" in KOMUTLAR
    
    # Çift kayıt hatası testi
    with pytest.raises(ValueError):
        @komut("test_komut_ornek", "ikinci açıklama")
        def ikinci_fonk(durum):
            return "ikinci"

def test_yardim_komutu():
    assert "yardim" in KOMUTLAR
    func, aciklama = KOMUTLAR["yardim"]
    durum = {}
    # Hata almadan çalışıp çalışmadığını test ediyoruz
    yardim_cikti = func(durum)
    assert aciklama == "komutları listeler"

def test_envanter_komutu():
    assert "envanter" in KOMUTLAR
    func, aciklama = KOMUTLAR["envanter"]
    durum = {"credits": 150, "engines": ["hizli"], "copilot": "Ali"}
    # Fonksiyonun düzgün çalışıp çalışmadığını kontrol ediyoruz
    func(durum)
    assert aciklama == "eşyalarını gösterir"

def test_harita_komutu():
    assert "harita" in KOMUTLAR
    func, aciklama = KOMUTLAR["harita"]
    durum = {
        "konum": "dunya",
        "baglantilar": {"dunya": ["orion", "mars"]}
    }
    func(durum)
    assert aciklama == "gidebileceğin gezegenleri gösterir"