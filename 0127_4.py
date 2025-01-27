def skaiciuoti_sumos_tipa(x, y, tik_teigiama=False):
    return max(x + y, 0) if tik_teigiama else x + y
print(skaiciuoti_sumos_tipa(8, -9, tik_teigiama=True))
print(skaiciuoti_sumos_tipa(8, 9))

print(" - " * 60)

def apskaiciuok_vidurki(skaiciai):
    """Apskaičiuoja sąrašo vidurkį."""
    return sum(skaiciai) / len(skaiciai) if skaiciai else 0
print(apskaiciuok_vidurki([2, 4, 6]))

print(" - " * 60)

def prideti_zodi(tekstas: str, zodis: str) -> str:
    return f"{tekstas} {zodis}"
print(prideti_zodi("Ar šiandien saulėtas oras ?", "Nuostabus !"))

print(" - " * 60)

def apskaiciuok_vidurki(skaiciai: list[int]) -> int:
    """Apskaičiuoja sąrašo sveikųjų skaičių vidurkį ir grąžina kaip sveikąjį skaičių."""
    return round(sum(skaiciai) / len(skaiciai)) if skaiciai else 0
print(apskaiciuok_vidurki([2, 4, 6, 8]))
print(apskaiciuok_vidurki([1, 2, 3, 4, 9]))

print(" - " * 60)

