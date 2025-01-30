pakelti_kvadratu = lambda x: x**2
darbuotojai = [("Jonas", 2500), ("Asta", 3200), ("Mantas", 2100)]
rikiuoti = sorted(darbuotojai, key=lambda x: x[1])
skaiciai = [5, 10, 15, 20, 25, 30]
filtruoti = list(filter(lambda x: x % 10 == 0, skaiciai))
print(pakelti_kvadratu(4))
print(rikiuoti)
print(filtruoti)
