kainos_eur = [10, 15, 20, 25, 30]
kainos_usd = [k * 1.1 for k in kainos_eur]
pranesimai = [f"Kaina: {k} EUR" for k in kainos_eur]
print(kainos_usd)
print(pranesimai)

print(" - " * 30)

kainos_eur = [10, 15, 20, 25, 30]
kainos_usd = [round(k * 1.1, 2) for k in kainos_eur]
pranesimai = [f"Kaina: {k} EUR" for k in kainos_eur]
print(kainos_usd)
print(pranesimai)

print(" - " * 30)

#kainos_usd = [f"{k * 1.1:.2f}" for k in kainos_eur]
