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