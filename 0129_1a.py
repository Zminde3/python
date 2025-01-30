import pdfplumber
import pandas as pd
import textwrap

pdf_path = "Tarpusavio_įsiskolinimai.pdf"
excel_path = "Duomenys.xlsx"

tekstas = ""
lenteles = []

# Atidarome PDF ir ištraukiame duomenis
with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages:
        # Ištraukiame visą tekstą
        tekstas += page.extract_text() + "\n\n"

        # Ištraukiame lenteles
        tables = page.extract_tables()
        for table in tables:
            lenteles.append(pd.DataFrame(table))

# **1. Tvarkome tekstą į A4 formatą**
teksto_eilutes = textwrap.wrap(tekstas, width=100)  # Kiekviena eilutė max 100 simbolių
df_tekstas = pd.DataFrame({"Tekstas": teksto_eilutes})  # Perkeliame į pandas

# **2. Išsaugome į Excel su keliais lapais**
with pd.ExcelWriter(excel_path, engine="openpyxl") as writer:
    # Išsaugome lenteles (jei jos yra)
    for i, df in enumerate(lenteles, start=1):
        df.to_excel(writer, sheet_name=f"Lentele_{i}", index=False)

    # Išsaugome tekstą su A4 išdėstymu
    df_tekstas.to_excel(writer, sheet_name="Tekstas", index=False)

print(f"🔹 PDF duomenys sėkmingai eksportuoti į `{excel_path}` su A4 išdėstymu.")
