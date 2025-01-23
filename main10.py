skaiciai = [[x, x**2, x**3, x % 2 == 0] for x in [1, 2, 3, 4, 5]]
print(skaiciai)

skaiciai = [5, 8, 12, 18, 25, 30, 35, 40]
didesni_nei_20 = [x for x in skaiciai if x > 20]
dalyjasi_is_5 = [x for x in skaiciai if x % 5 == 0]
lyg_nelyg = ["Lyginis" if x % 2 == 0 else "Nelyginis" for x in skaiciai]
print(didesni_nei_20)
print(dalyjasi_is_5)
print(lyg_nelyg)
