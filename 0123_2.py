kainos_eurais = [10, 15, 20, 25, 30]
kainos_doleriais = [k * 1.1 for k in kainos_eurais]
pranesimai = [f"Kaina: {k} EUR" for k in kainos_eurais]
print(kainos_doleriais)
print(pranesimai)

print(" - " * 30)

kainos_eurais = [10, 15, 20, 25, 30]
kainos_doleriais = [round(k * 1.1, 2) for k in kainos_eurais]
pranesimai = [f"Kaina: {k} EUR" for k in kainos_eurais]
print(kainos_doleriais)
print(pranesimai)

