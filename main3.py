import random
print("Sveiki atvykę į 'Atspėk skaičių su analize' žaidimą!")
print("Kompiuteris sugeneravo skaičių nuo 1 iki 100.")

teisingas_skaicius = random.randint(1, 100)
spejimai = []

while True:
    try:

        spejimas = int(input("Įveskite savo spėjimą (arba -1 baigti žaidimą): "))
        if spejimas == -1:
            print("Žaidimas baigtas! Ačiū už žaidimą.")
            break


        spejimai.append(spejimas)


        if spejimas < teisingas_skaicius:
            print("Per mažas skaičius! Bandykite dar kartą.")
        elif spejimas > teisingas_skaicius:
            print("Per didelis skaičius! Bandykite dar kartą.")
        else:
            print(f"Teisingai! Atspėjote skaičių {teisingas_skaicius} per {len(spejimai)} bandymus!")
            break
    except ValueError:
        print("Prašome įvesti tik skaičių!")

if spejimai:
    print("\nŽaidimo analizė:")
    print(f"Bendras spėjimų skaičius: {len(spejimai)}")
    print(f"Mažiausias spėjimas: {min(spejimai)}")
    print(f"Didžiausias spėjimas: {max(spejimai)}")
    print(f"Vidutinis spėjimas: {sum(spejimai) / len(spejimai):.2f}")
    print(f"Visi jūsų spėjimai: {', '.join(map(str, spejimai))}")
