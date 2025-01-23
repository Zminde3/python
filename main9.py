skaiciai = [-10, -5, 0, 5, 10, 15, 20]

teigiami, neigiami = sum(s for s in skaiciai if s > 0), sum(s for s in skaiciai if s < 0)
didziausias, maziausias = (lambda d, m: (d, m))(skaiciai[0], skaiciai[0])
for s in skaiciai:
    didziausias, maziausias = (s if s > didziausias else didziausias), (s if s < maziausias else maziausias)
print(f"Teigiami: {teigiami}, Neigiami: {neigiami}")
print(f"Didžiausias: {didziausias}, Mažiausias: {maziausias}")



