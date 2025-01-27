# import pandas as pd
#
# # Įkelti iš Excel failo
# df = pd.read_excel("duomenys.xlsx")
# print("Duomenys iš failo:\n", df.head())
# vidurkis = round(df["Amžius"].mean(), 2)
# print(f"\nVidutinis amžius: {vidurkis}")

import pandas as pd

# Įkelti Excel failą
df = pd.read_excel("duomenys.xlsx")
pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)

print("Visi duomenys iš failo:\n", df)
vidurkis_metais = round(df["Amžius"].mean(), 2)
metai = int(vidurkis_metais)  # Pilni metai
likutis_metu = vidurkis_metais - metai
menesiai = int(likutis_metu * 12)  # Mėnesiai
dienos = int((likutis_metu * 12 - menesiai) * 30.44)
print(f"\nVidutinis amžius: {vidurkis_metais} metai ({metai} metai, {menesiai} mėnesiai ir {dienos} dienos)")

