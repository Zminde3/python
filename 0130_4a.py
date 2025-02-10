from PIL import Image
import sys


def tikrinti_amziu(amzius):
    if amzius < 0:
        raise ValueError("❌ Amžius negali būti neigiamas!")
    return "✅ Vartotojas pilnametis." if amzius >= 18 else "🔹 Vartotojas nepilnametis."


def rodyti_paveiksleli(kelias):
    try:
        with Image.open(kelias) as img:
            img.show()
    except FileNotFoundError:
        print(f"⚠ Paveikslėlis nerastas: {kelias}")


for a in (96, 15, 21):
    try:
        rezultatas = tikrinti_amziu(a)
        print(rezultatas)

        if a < 0:
            rodyti_paveiksleli("error.png")
        elif a < 18:
            rodyti_paveiksleli("nepilnametis.png")
        else:
            rodyti_paveiksleli("pilnametis.png")

    except ValueError as e:
        print(e)
