import pytest
from uzay_oyunu.akis import yakit_harca
from uzay_oyunu.dekoratorler import sure_olc


def test_sure_olc_ozellikler_ve_sonuc():
  # 1. __name__ ve __doc__ korunuyor mu testi
  @sure_olc
  def ornek_fonksiyon(x, y=1):
    """Bu bir docstringdir."""
    return x + y

  assert ornek_fonksiyon.__name__ == "ornek_fonksiyon"
  assert ornek_fonksiyon.__doc__ == "Bu bir docstringdir."

  # 2. Sonuc degismeden donuyor mu ve pozitif/adli argumanlarla calisiyor mu testi
  sonuc_pozisyonel = ornek_fonksiyon(3, 4)
  assert sonuc_pozisyonel == 7

  sonuc_adli = ornek_fonksiyon(x=10, y=5)
  assert sonuc_adli == 15




def test_sinirla_dekoratoru():
    # Sınır içi değerler sorunsuz çalışmalı
    assert yakit_harca(30) == 30
    assert yakit_harca(0) == 0
    assert yakit_harca(100) == 100

    # Sınır dışı değerler ValueError fırlatmalı
    with pytest.raises(ValueError):
        yakit_harca(150)
        
    with pytest.raises(ValueError):
        yakit_harca(-10)