raides = ['A', 'B', 'C']
skaiciai = [1, 2, 3]

sa1 = [f"{r}{s}" for r in raides for s in skaiciai]
sa2 = [f"{r}{s}" for i, r in enumerate(raides) for s in skaiciai if i + s > 3]
sa3 = [f"{r.lower()}{s}" for r in raides for s in skaiciai if s % 2 == 0]

print(sa1)
print(sa2)
print(sa3)

print("-" * 30)

skaiciai = [1, 2, 3, 2, 1, 4, 5, 5]

aibe = {x for x in skaiciai}
tup = tuple(x + 1 for x in skaiciai)
zodynas = {x: x**2 for x in skaiciai}

print(aibe)
print(tup)
print(zodynas)

