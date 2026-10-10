# Kapsam (Scope) ve UnboundLocalError İncelemesi

## Örnek 1: Sadece Okuma Yapmak
**Tahminim:** Hata vermez, dışarıdaki değişkeni ekrana yazdırır.
**Gerçek Sonuç:** Sorunsuz çalıştı.
**Neden:** Python, fonksiyon içinde bir değişken bulamazsa hemen bir üst kapsama (global) bakar ve oradaki değeri okur.

## Örnek 2: UnboundLocalError (Tuzak Durumu)
**Tahminim:** Fonksiyon çöker ve hata verir.
**Gerçek Sonuç:** `UnboundLocalError: cannot access local variable where it is not associated with a value` hatası alındı.
**Neden:** Python'da bir fonksiyonun içinde bir değişkene atama (`=`) yaparsanız, Python o değişkeni otomatik olarak "yerel (local)" kabul eder. Ancak biz onu yerel olarak oluşturmadan önce `x = x + 1` gibi bir işlemle okumaya çalışırsak, Python "Daha oluşturmadığın bir yerel değişkeni okumaya çalışıyorsun" diyerek `UnboundLocalError` fırlatır.

## Örnek 3: Global ile Çözüm
**Tahminim:** `global` kelimesi kullanıldığı için hata vermeden dışarıdaki değeri değiştirecek.
**Gerçek Sonuç:** Başarıyla çalıştı ve değer güncellendi.
**Neden:** `global` anahtar kelimesi ile Python'a "İçeride yeni bir yerel değişken yaratma, dışarıdaki mevcut değişkeni kullan" emrini vermiş olduk.