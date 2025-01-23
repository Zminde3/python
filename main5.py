ivedimai = []

while True:
    try:
        skaicius = int(input("Įveskite skaičių nuo 1 iki 10: "))
        if skaicius < 1 or skaicius > 10:
            print("Skaičius turi būti nuo 1 iki 10. Bandykite dar kartą.")
            continue
        if skaicius == 5:
            print("Įvesta '5'. Ciklas nutraukiamas.")
            break
        ivedimai.append(skaicius)
    except ValueError:
        print("Prašome įvesti sveikąjį skaičių.")

suma = sum(ivedimai)
print(f"Ivestų skaičių suma (be '5'): {suma}")
