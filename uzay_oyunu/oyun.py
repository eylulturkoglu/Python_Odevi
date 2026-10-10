def envanter_metni(credits: bool, engines: bool, copilot: bool) -> str:
    """
    Oyuncunun elindeki özelliklere göre envanter durumunu metin olarak döndürür.
    Eğer hiçbir eşya yoksa boş metin döndürür.
    """
    esyalar = []
    if credits:
        esyalar.append("bol kredi")
    if engines:
        esyalar.append("güçlü motorlar") 
    if copilot:
        esyalar.append("yetenekli bir pilot")
        
    if len(esyalar) == 0:
        return ""
        
    return "Sende: " + ", ".join(esyalar)

def hedef_menusu(hedefler: list[str]) -> str:
    satirlar = ["Nereye gitmek istersin?"]
    for i in range(len(hedefler)):
        satirlar.append(f"[{i+1}] {hedefler[i]}")
        
    return "\n".join(satirlar)