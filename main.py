number1 = 53
number2 = 80
print (number1 + number2)
print (number1 - number2)
print(15 + 27)  # 1
print(50 - 23)  # 2
print(12 * 8)   # 3
print(144 / 12) # 4
print(100 % 9)  # 5
print(3 ** 2)    # 1
print(2 ** 5)    # 2
print(10 ** 0)   # 3 (Rezultatas bus 1)
print(3 * 15)      # 1
print(40 // 15)    # 2
print(40 % 15)     # 3
print(45 % 7 > 6)           # 1
print(10 + 5 > 15 // 2)     # 2
print(20 / 5 == 4)          # 3
result = (20 + 15) * 2 - (30 // 3) + (50 % 6)
print(result)
print(45 / 9)    # 1
print(15 % 3 == 0) # 2
print(100 // 7)  # 3
x = 10 + 20 - (15 % 4) * 2
print(x)
print(50 > 5 ** 2)           # 1
print(15 // 4 == 20 % 4)     # 2
print(10 + 5 - 3 < 15 ** 0)  # 3
print(2 ** 10)   # 1
print(3 ** 3)    # 2
for i in range(1, 6):  # 3
    print(i ** 2)
numbers = [56, 23, 8]
total = sum(numbers)
print(total)           # 1
print(total % 9)       # 2
print(56 // 8)         # 3
print(100 % 9 == 10 ** 1)    # 1
print(15 + 10 - 5 == 20)     # 2
print((5 + 5) ** 2 > 50)     # 3
result = (25 // 3 + 10 % 4) * (3 ** 2 - 10) + 50
print(result)
days = 1000
years = days // 365  # 1
remaining_days = days % 365  # 2
months = days // (365 // 12)  # 3
print(years, remaining_days, months)
students = 53
groups = students // 5  # 1
remaining_students = students % 5  # 2
missing_for_full_group = 5 - remaining_students if remaining_students > 0 else 0  # 3
print(groups, remaining_students, missing_for_full_group)
result = (100 - 25) % 7 + (50 // 3) ** 2
print(result)

# Duomenys
data = [
    {"vardas": "Jonas", "svoris": 65, "ugis": 1.75},
    {"vardas": "Ona", "svoris": 50, "ugis": 1.60},
    {"vardas": "Tomas", "svoris": 85, "ugis": 1.80},
    {"vardas": "Rasa", "svoris": 95, "ugis": 1.68},
]

# F. BMI zonai nustatyti
def nustatyti_bmi_zona(bmi):
    if bmi < 18.5:
        return "Nepakankamas svoris"
    elif 18.5 <= bmi <= 24.9:
        return "Normalus svoris"
    elif 25 <= bmi <= 29.9:
        return "Antsvoris"
    else:
        return "Nutukimas"

# BMI skaičiavimas
for zmogus in data:
    svoris = zmogus["svoris"]
    ugis = zmogus["ugis"]
    bmi = svoris / (ugis ** 2)
    zona = nustatyti_bmi_zona(bmi)
    print(f"{zmogus['vardas']}: BMI = {bmi:.2f}, zona = {zona}")

# Duomenys
automobiliai = [
    {"modelis": "Toyota", "atstumas": 200, "sanaudos": 6.5},
    {"modelis": "BMW", "atstumas": 350, "sanaudos": 8.0},
    {"modelis": "Honda", "atstumas": 120, "sanaudos": 5.0},
    {"modelis": "Audi", "atstumas": 500, "sanaudos": 7.2},
]

# Kuro l. kaina
kuro_kaina = 1.50

# Kuro sąnaudų ir išlaidų skaičiavimas
for auto in automobiliai:
    atstumas = auto["atstumas"]
    sanaudos = auto["sanaudos"]

    # Apskaičiuojame kuro sunaudojimą litr.
    kuro_sunaudojimas = (atstumas * sanaudos) / 100

    # Apskaičiuojame kuro kainą
    kaina = kuro_sunaudojimas * kuro_kaina

    # Išvedame rezultatus
    print(f"{auto['modelis']}:")
    print(f"  Kuro sunaudojimas: {kuro_sunaudojimas:.2f} L")
    print(f"  Kaina: {kaina:.2f} €\n")

    # Automobilių duomenys
    automobiliai = [
        ("Toyota", 200, 6.5),
        ("BMW", 350, 8.0),
        ("Honda", 120, 5.0),
        ("Audi", 500, 7.2),
    ]

    # Kuro litro kaina
    kuro_kaina = 1.50

    # Apskaičiuojame ir išvedame rezultatus
    for modelis, atstumas, sanaudos in automobiliai:
        kuro_sunaudojimas = (atstumas * sanaudos) / 100
        kaina = kuro_sunaudojimas * kuro_kaina
        print(f"{modelis}: Kuro sunaudojimas = {kuro_sunaudojimas:.2f} L, Kaina = {kaina:.2f} €")

        # Task slice "Hello World"

    print("Hello")

    text = "Hello World"
    print(text[:5])

    print(text[-5:])

    print(text[:7])

    print(text[1:7])

    print(text[1:10])

    print(text[5])

    text = "Hello World"
    print(len(text))  # 11
    text = "12345"
    print(text.isdigit())  # True

# BMI skaičiavimas 2
bmi2 = [
    {"vardas": "Jonas", "svoris": 70, "ugis": 1.75},
    {"vardas": "Petras", "svoris": 85, "ugis": 1.80},
    {"vardas": "Ona", "svoris": 50, "ugis": 1.60}
]

for zmogus in bmi2:
    print(f"{zmogus['vardas']}: BMI = {(bmi := zmogus['svoris'] / zmogus['ugis'] ** 2):.2f}, zona = {'Nepakankamas svoris' if bmi < 18.5 else 'Normalus svoris' if 18.5 <= bmi <= 24.9 else 'Antsvoris' if 25 <= bmi <= 29.9 else 'Nutukimas'}")

# 1. Kas yra sąrašas?
sarasas = []
print(f"Tuščias sąrašas: {sarasas}, jo tipas: {type(sarasas)}")

sarasas.append("sausis")
print(f"Po pridėjimo: {sarasas}")

sarasas.append("vasaris")
print(f"Po pridėjimo: {sarasas}")

sarasas.append(2024)
print(f"Po pridėjimo: {sarasas}")

# 2. Sąrašų metodai
gyvunai = ["šuo", "katė", "zuikis"]
print(f"Pradinis sąrašas: {gyvunai}")

gyvunai.append("dramblys")
print(f"Po pridėjimo į pabaigą: {gyvunai}")

gyvunai.insert(1, "žirafa")
print(f"Po įterpimo į antrąją poziciją: {gyvunai}")

gyvunai.remove("katė")
print(f"Po 'katė' pašalinimo: {gyvunai}")

paskutinis = gyvunai.pop()
print(f"Paskutinis elementas: {paskutinis}")
print(f"Po 'pop()': {gyvunai}")

gyvunai[0] = "tigrai"
print(f"Po pirmojo elemento pakeitimo: {gyvunai}")


# Mėnesių sąrašas ir iteracija
menesiai = ["sausis", "vasaris", "kovas", "balandis"]
for menuo in menesiai:
    print(menuo + " mėnuo")

print("---------------")

# Skaičių sąrašo sumos skaičiavimas
skaiciai = [5, 10, 15, 20]
suma = 0
for skaicius in skaiciai:
    suma += skaicius

print(f"Visų skaičių suma: {suma}")

print("---------------")

# Skaičių dauginimas iš 2
for skaicius in skaiciai:
    print(f"{skaicius} padauginus iš 2 yra {skaicius * 2}")

    # Numbers
    numbers = [3, 8, 12, 5, 10]

    #  len()
    num_elements = len(numbers)
    print(f"Number of elements in the list: {num_elements}")

    # b. sum()
    total_sum = sum(numbers)
    print(f"Total sum of the elements: {total_sum}")

    # c. Use max() and min()
    largest_number = max(numbers)
    smallest_number = min(numbers)
    print(f"Largest number: {largest_number}")
    print(f"Smallest number: {smallest_number}")

# Create a list
countries = ["Lietuva", "Latvija", "Estija", "Lenkija"]

# Print the first and last elements
print(f"First element: {countries[0]}")
print(f"Last element: {countries[-1]}")

# Use slicing to get the middle elements
middle_elements = countries[1:-1]
print(f"Middle elements: {middle_elements}")

# Print the list in reverse order
reversed_list = countries[::-1]
print(f"Reversed list: {reversed_list}")

# Create a tuple
days = ("pirmadienis", "antradienis", "trečiadienis", "ketvirtadienis")

# Print the second element
print(f"Second element: {days[1]}")

# Use .count() to find how many times "pirmadienis" appears
count_pirmadienis = days.count("pirmadienis")
print(f"'pirmadienis' appears {count_pirmadienis} time(s).")

# Use .index() to find the index of "pirmadienis"
index_pirmadienis = days.index("pirmadienis")
print(f"The index of 'pirmadienis' is {index_pirmadienis}.")

# a. Paversti eilutę į sąrašą naudojant .split()
eilute = "obuolys bananai kriaušės"
sarasas = eilute.split()  # Pagal numatytuosius nustatymus skiria pagal tarpus
print("Sąrašas:", sarasas)

# b. Sujungti sąrašo elementus į vieną eilutę su skiriamąja linija "---"
nauja_eilute = "---".join(sarasas)
print("Nauja eilutė:", nauja_eilute)

# 1. Patikriname, kuris skaičius yra didesnis
skaicius1 = 10  # Pirmas skaičius
skaicius2 = 7   # Antras skaičius

if skaicius1 > skaicius2:
    print(f"Pirmas skaičius ({skaicius1}) yra didesnis.")
elif skaicius1 < skaicius2:
    print(f"Antras skaičius ({skaicius2}) yra didesnis.")
else:
    print("Abu skaičiai yra lygūs.")

# 2. Patikriname, ar skaičius yra lyginis ar nelyginis
skaicius = 15  # Pasirinktas skaičius

if skaicius % 2 == 0:
    print(f"Skaičius {skaicius} yra lyginis.")
else:
    print(f"Skaičius {skaicius} yra nelyginis.")

# 3. Patikriname, ar žodis yra sąraše
sarasas = ["obuolys", "bananai", "kriaušės", "apelsinas", "braškės"]
zodis = "kriaušės"  # Parinktas žodis

if zodis in sarasas:
    print(f"Žodis '{zodis}' yra sąraše.")
else:
    print(f"Žodis '{zodis}' nėra sąraše.")

    # Tikriname  amžių
    amzius = int(input("Įveskite savo amžių: "))

    #if amzius < 18:
     #   print("Nepilnametis")
    #else:
     #   print("Pilnametis")

        # Tikriname  temperatūrą
      #  temperatura = float(input("Įveskite temperatūrą: "))

       # if temperatura < 0:
        #    print("Šalta")
        #elif 0 <= temperatura <= 20:
         #   print("Vidutiniška")
        #else:
         #   print("Šilta")

            # 1. Patikrinti  įvestą balą
#            balas = int(input("Įveskite balą (0-10): "))

 #           if 0 <= balas <= 4:
  #              print("Nepatenkinamas")
   #         elif 5 <= balas <= 7:
    #            print("Vidutinis")
     #       elif 8 <= balas <= 10:
      #          print("Puikus")
       #     else:
        #        print("Klaida: balas turi būti tarp 0 ir 10.")






