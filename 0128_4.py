import matematika as m

print(m.sudetis(10, 20), m.daugyba(5, 4))
print(m.sudetis(8, 3), m.daugyba(8, 3))
print(m.sudetis(12, 18), m.daugyba(7, 6))

duomenys = [(10, 20), (5, 4), (8, 3), (8, 3), (12, 18), (7, 6)]
for a, b in zip(duomenys[::2], duomenys[1::2]):
     print(m.sudetis(*a), m.daugyba(*b))