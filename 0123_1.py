skaiciai = [1, 3, 5, 7, 8, 10, 11]

for sk in skaiciai:
    if sk % 2 == 0:
        print(f"Pirmas lyginis skaičius: {sk}")
        break
else:
    print("Lyginių skaičių nėra")
