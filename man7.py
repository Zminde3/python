skaiciai = [5, 7, 15, 6, 3, 20, 12]
for s in skaiciai:
    if s > 10: break
    if s % 2 == 0 or s % 5 == 0: print(s)

skaiciai = [-10, -5, 0, 5, 10, 15, 20]
teigiami = sum(s for s in skaiciai if s > 0)
neigiami = sum(s for s in skaiciai if s < 0)
print(f"Teigiami: {teigiami}, Neigiami: {neigiami}")
print(f"Didžiausias: {max(skaiciai)}, Mažiausias: {min(skaiciai)}")
