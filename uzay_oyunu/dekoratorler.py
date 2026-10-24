import time
from functools import wraps


def sure_olc(func):
  """Fonksiyonun calisma suresini olcup ekrana yazdiran dekorator."""

  @wraps(func)
  def wrapper(*args, **kwargs):
    baslangic = time.perf_counter()
    sonuc = func(*args, **kwargs)
    bitis = time.perf_counter()
    sure = bitis - baslangic
    print(f"{func.__name__}: {sure:.6f} sn")
    return sonuc

  return wrapper

def say(func):
  """Fonksiyonun kac kez cagrildigini sayan dekorator."""
  cagri_sayisi = 0

  @wraps(func)
  def wrapper(*args, **kwargs):
    nonlocal cagri_sayisi
    cagri_sayisi += 1
    return func(*args, **kwargs)

  wrapper.cagri = lambda: cagri_sayisi
  return wrapper