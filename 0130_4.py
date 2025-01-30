def tikrinti_amziu(amzius):
    if amzius < 0:
        raise ValueError("❌ Amžius negali būti neigiamas!")
    return "✅ Vartotojas pilnametis." if amzius >= 18 else "🔹 Vartotojas nepilnametis."

for a in (-5, 15, 21):
    try:
        print(tikrinti_amziu(a))
    except ValueError as e:
        print(e)
