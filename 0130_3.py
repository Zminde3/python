while True:
    try:
        sk = int(input("Įveskite skaičių: "))
    except ValueError:
        print("❌ Klaida: įveskite tik skaičių!")
    else:
        print(f"✅ Konversija sėkminga: {sk}")
        break
    finally:
        print("🔹 Programa baigė darbą.")
