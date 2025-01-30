try:
    a, b = map(int, input("Įveskite du skaičius: ").split())
    print(f"Rezultatas: {a / b}")
except ValueError:
    print("Klaida: įveskite tik skaičius!")
except ZeroDivisionError:
    print("Klaida: dalyba iš nulio negalima!")
