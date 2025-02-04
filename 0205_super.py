from datetime import date, timedelta


# --------------------------------------------------
# 📚 Klasės apibrėžimai
# --------------------------------------------------
class Book:
    publisher = "Alma Littera"

    def __init__(self, title, author, year, quantity=2):
        if year > date.today().year:
            raise ValueError("❌ Leidimo metai negali būti ateityje!")
        self.title, self.author, self.year, self.quantity = title, author, year, quantity

    def borrow(self):
        if self.quantity > 0:
            self.quantity -= 1
            return True
        return False

    def return_book(self):
        self.quantity += 1

    def __str__(self):
        return f'📖 "{self.title}" – {self.author} ({self.year}) | Likutis: {self.quantity} vnt.'


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"✅ Pridėta: {book.title} ({book.quantity} vnt.)")

    def display_books(self):
        print("\n📚 Bibliotekos knygos:\n" + "-" * 50)
        for book in self.books:
            print(book)
        print("-" * 50)

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.borrow():
                    print(f"📖 \"{book.title}\" pasiskolinta! Liko: {book.quantity} vnt.")
                else:
                    print(f"❌ \"{book.title}\" nebegalima skolintis! Liko: {book.quantity} vnt.")
                return
        print(f"❌ Knyga \"{title}\" nerasta.")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                book.return_book()
                print(f"✅ \"{book.title}\" grąžinta! Dabar yra {book.quantity} vnt.")
                return
        print(f"❌ Knyga \"{title}\" nerasta.")


# --------------------------------------------------
# 📚 Sukuriame biblioteką ir pridedame 10 knygų su po 2 vnt.
# --------------------------------------------------
library = Library()
books_list = [
    ("Altorių šešėly", "Vincas Mykolaitis-Putinas", 1933),
    ("Balta drobulė", "Antanas Škėma", 1958),
    ("Tadas Blinda", "Rimantas Šavelis", 1987),
    ("Dievų miškas", "Balys Sruoga", 1957),
    ("Dėdės ir dėdienės", "Jonas Biliūnas", 1914),
    ("Sodybų tuštėjimo metas", "Juozas Aputis", 1970),
    ("Šešėliai ir žmonės", "Kazys Saja", 1990),
    ("Pragiedruliai", "Juozas Tumas-Vaižgantas", 1918),
    ("Baltaragio malūnas", "Kazys Boruta", 1945),
    ("Sename dvare", "Šatrijos Ragana", 1922)
]

for book in books_list:
    library.add_book(Book(*book, quantity=2))

# --------------------------------------------------
# 📚 Sąveika su vartotoju
# --------------------------------------------------
while True:
    print("\n📌 Pasirinkite veiksmą:\n" + "-" * 50)
    print("[1] Pridėti knygą  [2] Peržiūrėti knygas  [3] Skolintis  [4] Grąžinti  [0] Išeiti")
    print("-" * 50)

    veiksmas = input("➡️ Jūsų pasirinkimas: ").strip()

    if veiksmas == "1":
        try:
            title = input("📖 Knygos pavadinimas: ").strip()
            author = input("✍️ Autorius: ").strip()
            year = int(input("📆 Leidimo metai: "))
            library.add_book(Book(title, author, year, quantity=2))
        except ValueError:
            print("❌ Netinkami duomenys. Leidimo metai turi būti teisingi!")

    elif veiksmas == "2":
        library.display_books()

    elif veiksmas == "3":
        title = input("📖 Įveskite knygos pavadinimą, kurią norite skolintis: ").strip()
        library.borrow_book(title)

    elif veiksmas == "4":
        title = input("📖 Įveskite knygos pavadinimą, kurią norite grąžinti: ").strip()
        library.return_book(title)

    elif veiksmas == "0":
        print("👋 Programa baigta.")
        break

    else:
        print("❌ Netinkamas pasirinkimas. Bandykite dar kartą.")
