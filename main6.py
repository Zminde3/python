ivedimai = []
while (skaicius := int(input("Įveskite skaičių nuo 1 iki 10: "))) != 5:
    if 1 <= skaicius <= 10:
        ivedimai.append(skaicius)
    else:
        print("Skaičius turi būti nuo 1 iki 10. Bandykite dar kartą.")
print(f"Ivestų skaičių suma (be '5'): {sum(ivedimai)}")
