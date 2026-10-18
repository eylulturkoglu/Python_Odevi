from typing import Iterator

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