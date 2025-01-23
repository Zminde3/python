skaiciai = [-10, -5, 0, 5, 10, 15, 20]
teigiami, neigiami = sum(s for s in skaiciai if s > 0), sum(s for s in skaiciai if s < 0)
didziausias, maziausias = max(skaiciai), min(skaiciai)
print(f"Teigiami: {teigiami}, Neigiami: {neigiami}")
print(f"Didžiausias: {didziausias}, Mažiausias: {maziausias}")
#----------------------------------------------------------------------------------------------

skaiciai = [-10, -5, 0, 5, 10, 15, 20]
didziausias = skaiciai[0]
maziausias = skaiciai[0]
for s in skaiciai:
    if s > didziausias:
        didziausias = s
    if s < maziausias:
        maziausias = s
teigiami = sum(s for s in skaiciai if s > 0)
neigiami = sum(s for s in skaiciai if s < 0)
print(f"Teigiami: {teigiami}, Neigiami: {neigiami}")
print(f"Didžiausias: {didziausias}, Mažiausias: {maziausias}")
#-------------------------------------------------------------------------------------------------
skaiciai = [-10, -5, 0, 5, 10, 15, 20]
teigiami, neigiami, didziausias, maziausias = 0, 0, skaiciai[0], skaiciai[0]
for s in skaiciai:
    teigiami += s if s > 0 else 0
    neigiami += s if s < 0 else 0
    didziausias = s if s > didziausias else didziausias
    maziausias = s if s < maziausias else maziausias
print(f"Teigiami: {teigiami}, Neigiami: {neigiami}")
print(f"Didžiausias: {didziausias}, Mažiausias: {maziausias}")





