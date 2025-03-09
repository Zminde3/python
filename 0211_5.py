import numpy as np
import pandas as pd
import statsmodels.api as sm

# Sugeneruojame duomenų rinkinį
np.random.seed(42)
education = np.random.randint(10, 20, 30)  # Išsilavinimo metai
experience = np.random.randint(1, 30, 30)  # Darbo patirtis metais
wage = 2000 + 500 * education + 300 * experience + np.random.normal(0, 1000, 30)  # Darbo užmokestis

# Sukuriame DataFrame
data = pd.DataFrame({"Išsilavinimas": education, "Patirtis": experience, "Atlyginimas": wage})

# Pridedame konstantą regresijos modeliui
X = sm.add_constant(data[["Išsilavinimas", "Patirtis"]])
Y = data["Atlyginimas"]

# Vykdome regresiją
model = sm.OLS(Y, X).fit()

# Spausdiname rezultatus lietuviškai
print("Regresijos modelio rezultatai:")
print(f"Konstanta: {model.params['const']:.2f}")
print(f"Išsilavinimo įtaka: {model.params['Išsilavinimas']:.2f}")
print(f"Patirties įtaka: {model.params['Patirtis']:.2f}")
print(f"R^2 reikšmė: {model.rsquared:.3f}")
print("---")
print("Hipotezės tikrinimas:")
print(f"Išsilavinimo p-reikšmė: {model.pvalues['Išsilavinimas']:.5f}")
print(f"Patirties p-reikšmė: {model.pvalues['Patirtis']:.5f}")
print("Jei p-reikšmė mažesnė nei 0.05, kintamasis yra statistiškai reikšmingas.")
