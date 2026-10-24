# Dekoratör Sıralaması ve Özyinelemeli Fibonacci Deneyi

Bu çalışmada, Fibonacci(20) hesaplaması için `@say` ve `@lru_cache` dekoratörlerinin farklı sıralama kombinasyonları test edilmiş ve çağrı sayıları incelenmiştir.

## Test Sonuçları ve Açıklamalar

1. **Yalnızca `@say`**: **21891 çağrı**
   - **Neden**: Önbellekleme (`lru_cache`) kullanılmadığı için saf özyinelemeli (recursive) Fibonacci her alt adımda tekrar tekrar hesaplama yapar. Üstel bir büyüme gerçekleştiği için fonksiyon binlerce kez kendini çağırır ve `@say` bunların hepsini tek tek kaydeder.

2. **`@say` üstte, `@lru_cache` altta (`@say` -> `@lru_cache`)**: **39 çağrı**
   - **Neden**: Alttaki `@lru_cache` fonksiyonu sarmaladığı için daha önce hesaplanan değerler cache'ten (önbellekten) çekilir. Üstteki `@say` ise cache mekanizmasının dışında kaldığı için yalnızca cache'e takılmayan (önbellekten dönmeyen) ilk çağrıları sayar.

3. **`@lru_cache` üstte, `@say` altta (`@lru_cache` -> `@say`)**: **21 çağrı**
   - **Neden**: Altta `@say` olduğu için dekoratör doğrudan fonksiyonun kendisine yapışıktır. Üstteki `@lru_cache` devreye girip daha önceki sonuçları doğrudan cache'ten döndürdüğü için, fonksiyonun orijinal gövdesi her $n$ değeri için tam olarak **1 kez** gerçek hesaplamaya girer ($0$'dan $20$'ye kadar toplam 21 değer olduğu için sonuç 21 çıkar).
   - *Not*: Bu durumda sayaç verisine dışarıdan erişmek için `fib.__wrapped__.cagri()` yöntemi kullanılır.