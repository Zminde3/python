import pdfplumber
import pandas as pd

pdf_path = "Tarpusavio_įsiskolinimai.pdf"

# Atidarome PDF dokumentą
with pdfplumber.open(pdf_path) as pdf:
    tekstas = ""
    lentele = []

    for page in pdf.pages:
        # Ištraukiame tekstą iš PDF
        tekstas += page.extract_text() + "\n"

        # Ištraukiame lentelę (jei yra)
        tables = page.extract_tables()
        for table in tables:
            lentele.extend(table)

# Spausdiname visą tekstą (jei reikia)
print("🔹 Pilnas išgautas tekstas:\n", tekstas)

# Jei lentelė egzistuoja, perkeliame į pandas DataFrame
if lentele:
    df = pd.DataFrame(lentele[1:], columns=lentele[0])  # Pirmoji eilutė kaip antraštė
    print("\n🔹 Struktūrizuota lentelė iš PDF:\n")
    print(df)
