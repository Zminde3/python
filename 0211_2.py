def prideti_zenkliuka(tekstas):
    return tekstas + "*"

def apversti_teksta(tekstas):
    return tekstas[::-1]

def apdoroti_teksta(tekstas, funkcija=None):
    return funkcija(tekstas) if funkcija else tekstas.lower()

def keli_apdorojimai(tekstas, *funkcijos):
    for funkcija in funkcijos:
        tekstas = funkcija(tekstas)
    return tekstas

print(prideti_zenkliuka("Labas"))
print(apversti_teksta("Python"))
print(apdoroti_teksta("Šiandien guvo LABAI GERAS oras"))
print(apdoroti_teksta("Labas", prideti_zenkliuka))
print(keli_apdorojimai("Mindaugas", prideti_zenkliuka, apversti_teksta))
