# try:
#     a, b = map(int, input("Įveskite du skaičius: ").split())
#     print(f"Rezultatas: {a / b}")
# except ValueError:
#     print("Klaida: įveskite tik skaičius!")
# except ZeroDivisionError:
#     print("Klaida: dalyba iš nulio negalima!")
while True:
    try:
        duomenys = input("Įveskite du skaičius atskirtus tarpu: ").split()
        if len(duomenys) != 2:
            raise ValueError("❌ Klaida: Turite įvesti **DU** skaičius!")

        a, b = map(int, duomenys)

        if b == 0:
            raise ZeroDivisionError("❌ Klaida: Dalyba iš nulio negalima!")

        print(f"✅ Rezultatas: {a / b}")
        break

    except ValueError as e:
        print(e if "DU" in str(e) else "❌ Klaida: Įveskite tik sveikus skaičius!")
    except ZeroDivisionError as e:
        print(e)
print("\u2705 tai pavyko")
