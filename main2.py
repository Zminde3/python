#skaicius = float(input("Įveskite skaičių: "))
#print("Teigiamas" if skaicius > 0 else "Neigiamas")


#eilute = input("Įveskite tekstą: ")
#print("Didžioji raidė" if eilute[0].isupper() else "Mažoji raidė")

# print("Didžioji raidė" if input("Įveskite tekstą: ")[0].isupper() else "Mažoji raidė")


#zodis = input("Įveskite žodį: ").strip()
#print("Žodis prasideda didžiąja raide:", zodis[0].isupper() if zodis else False)
#print("Visi žodžio simboliai yra mažosios raidės:", zodis.islower())

#sakiniu_skaicius = int(input(" Kiek sakinių norite patikrinti? "))
#for _ in range(sakiniu_skaicius):
#sakinys = input("Įveskite sakinį: ")
#print("Sakinys prasideda 'A':", sakinys.startswith("A"))
#print("Sakinys parašytas tik didžiosiomis raidėmis:", sakinys.isupper())

#print("Sakinys prasideda 'A'" if (sakinys := input("Įveskite sakinį: ")).startswith("A") else "Sakinys neprasideda 'A'", "ir visas didžiosiomis raidėmis" if sakinys.isupper() else "ir nėra visas didžiosiomis raidėmis")

#print(f"{'Prasideda A' if (s := input('Įveskite sakinį: ')).startswith('A') else 'Neprasideda A'}, {'Didžiosiomis' if s.isupper() else 'Ne didžiosiomis'}")

#vardas, amzius = input("Įveskite savo vardą: "), int(input("Įveskite savo amžių: "))
#print(f"Sveikas, {vardas}! Tau {amzius} metai.", f"Vardo ilgis: {len(vardas)} raidės.", "Pilnametis" if amzius > 18 else "Nepilnametis")

#vardas = input("Įveskite savo vardą: ")
#amzius = input("Įveskite savo amžių: ")
#if amzius.isdigit():
 #   amzius = int(amzius)
  #  print(f"Sveikas, {vardas}! Tau {amzius} metai.", f"Vardo ilgis: {len(vardas)} raidės.", "Pilnametis" if amzius > 18 else "Nepilnametis")
#else:
 #   print("Amžius turi būti skaičiumi!")

#for skaicius in range(2, 21, 2):
 #   print(skaicius, end=" ")
#print()

#suma = 0
#for skaicius in range(2, 21, 2):
 #   suma += skaicius**2
#print("Kvadratų suma:", suma)

#for skaicius in range(10, 0, -1):
 #   print(skaicius, end=" ")
#print()

#import random
#print("Sveiki atvykę į 'Atspėk skaičių' žaidimą!")
#teisingas_skaicius = random.randint(1, 100)
#bandymai = 0
#while True:
 #   bandymai += 1
  #  spejimas = int(input("Atspėkite skaičių (nuo 1 iki 100): "))
   # if spejimas < teisingas_skaicius:
    #    print("Per mažas skaičius! Bandykite dar kartą.")
    #elif spejimas > teisingas_skaicius:
     #   print("Per didelis skaičius! Bandykite dar kartą.")
    #else:
     #   print(f"Teisingai! Atspėjote skaičių {teisingas_skaicius} per {bandymai} bandymų!")
      #  break
#print("Ačiū, kad žaidėte!")

# 5.1 uzduotis
#zodziai = ['Obuolys', 'Kriaušė', 'Bananas', 'Vyšnia']
#print(" | ".join(zodziai))
#print(", ".join(f"{i+1}) {zodis}" for i, zodis in enumerate(zodziai)))
#print("Tai yra pirma dalis", end=", ")
#print("o čia – kita dalis.")



#duomenys = [1234, 'Labas', True, 45.6, None]

# 5.2 uzduotis
#for elementas in duomenys:
 #   if isinstance(elementas, bool):
  #      print("True arba False aptikta")
   # elif isinstance(elementas, int):
    #    print(elementas * 10)
    #elif isinstance(elementas, str):
     #   print(elementas.upper())
    #elif isinstance(elementas, float):
     #   print(round(elementas, 2))
    #else:
     #   print(" Nenustatytas:", elementas)


#mokykla = {
 #   "pavadinimas": "Vųdūno gimnazija",
  #  "mokytojai": [
   #     {"vardas": "Jonas", "pavarde": "Petrauskas", "mokomas_dalykas": "Matematika"},
    #    {"vardas": "Asta", "pavarde": "Kazlauskienė", "mokomas_dalykas": "Lietuvių kalba"}
    #],
    #"mokiniu_sk": 520
#}
#pirmas_mokytojas = mokykla["mokytojai"][0]
#print(f"Pirmas mokytojas: {pirmas_mokytojas['vardas']}, Mokomas dalykas: {pirmas_mokytojas['mokomas_dalykas']}")
#if mokykla["mokiniu_sk"] > 500:
 #   print("Mokykloje yra daugiau nei 500 mokinių.")
#else:
 #   print("Mokykloje yra mažiau nei 500 mokinių.")

#company = {
#   "name": "MPG CAPITAL",
 # "employees": [
  #      {"name": "Aldas", "role": "General manager", "salary": 4000},
   #     {"name": "Mindaugas", "role": "Chief Accountant", "salary": 3000},
    #    {"name": "Sandra", "role": "bookkeeper", "salary": 2500}
   # ],
    #"location": "Klaipėda",
    #"industry": "IT"
#}
#print("Darbuotojai:")
#for employee in company["employees"]:
 #   print(f"Vardas: {employee['name']}, Pareigos: {employee['role']}")
#salaries = [employee["salary"] for employee in company["employees"]]
#vidurkis = sum(salaries) / len(salaries)
#print(f"Vidutinis atlyginimas: {vidurkis:.2f}")
#if "location" in company:
 #print(f"Įmonės vieta: {company['location']}")
#else:
 #   print("Raktas 'location' neegzistuoja.")

library = {
    "books": [
        {"title": "1984", "author": "George Orwell", "copies": 3},
        {"title": "To Kill a Mockingbird", "author": "Harper Lee", "copies": 5},
        {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "copies": 2}
    ],
    "location": "Šilutė",
    "open_hours": {"start": "8:00", "end": "20:00"}
}
print(f"Biblioteka yra: {library['location']}")
print(f"Darbo valandos: nuo {library['open_hours']['start']} iki {library['open_hours']['end']}")
print("Knygos bibliotekoje:")
for book in library["books"]:
    print(f"Pavadinimas: {book['title']}, Autorius: {book['author']}")
maziausiai_kopiju = min(library["books"], key=lambda book: book["copies"])
print(f"Knyga su mažiausiai kopijų: {maziausiai_kopiju['title']}")

library = {
    "books": [
        {"title": "1984", "author": "George Orwell", "copies": 3},
        {"title": "To Kill a Mockingbird", "author": "Harper Lee", "copies": 5},
        {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "copies": 2}
    ],
    "location": "Šilutė",
    "open_hours": {"start": "8:00", "end": "20:00"}
}
print(f"Biblioteka yra: {library['location']}")
print(f"Darbo valandos: nuo {library['open_hours']['start']} iki {library['open_hours']['end']}")

print("Knygos bibliotekoje:")
[print(f"Pavadinimas: {b['title']}, Autorius: {b['author']}") for b in library["books"]]
fewest_copies_book = min(library["books"], key=lambda b: b["copies"])
print(f"Knyga su mažiausiai kopijų: {fewest_copies_book['title']}")

library = {
    "books": [
        {"title": "1984", "author": "George Orwell", "copies": 3},
        {"title": "To Kill a Mockingbird", "author": "Harper Lee", "copies": 5},
        {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "copies": 2}
    ],
    "location": "Šilutė",
    "open_hours": {"start": "8:00", "end": "20:00"}
}
print(f"Biblioteka yra: {library['location']}")
print(f"Darbo valandos: nuo {library['open_hours']['start']} iki {library['open_hours']['end']}")

print("\nKnygos bibliotekoje:")
print("\n".join(f"Pavadinimas: {b['title']}, Autorius: {b['author']}" for b in library["books"]))

fewest_copies_book = min(library["books"], key=lambda b: b["copies"])
print(f"\nKnyga su mažiausiai kopijų: {fewest_copies_book['title']}")


















