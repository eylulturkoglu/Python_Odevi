# Hatanın None kalıbıyla düzeltilmiş hali
def yakit_ekle(miktar, depo=None):
    if depo is None:
        depo = []
    depo.append(miktar)
    return depo

def test_yakit_ekle_tuzagi():
    # 1. Gemiye 10 birim yakıt ekliyoruz
    gemi1 = yakit_ekle(10)
    assert gemi1 == [10]
    
    # 2. Gemiye 20 birim yakıt ekliyoruz (Artık sıfırdan başlayacak)
    gemi2 = yakit_ekle(20)
    assert gemi2 == [20]