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

def log_cagri(func):
    """Fonksiyon cagri bilgilerini ve donus degerini loglayan dekorator."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        
        print(f"-> {func.__name__}({signature})")
        result = func(*args, **kwargs)
        print(f"<- {func.__name__} = {result!r}")
        return result
    return wrapper

def sinirla(alt, ust):
    """Fonksiyonun ilk argümanının [alt, ust] aralığında olup olmadığını kontrol eden dekoratör."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if args:
                ilk_arg = args[0]
                if not (alt <= ilk_arg <= ust):
                    raise ValueError(f"{func.__name__}: {ilk_arg} değeri {alt}-{ust} aralığında değil")
            return func(*args, **kwargs)
        return wrapper
    return decorator