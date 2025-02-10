from datetime import date, timedelta
import difflib


# --------------------------------------------------
# --------------------------------------------------
class Book:
    publisher = "Alma Littera"

    def __init__(self, title, author, year, quantity=2):
        if year > date.today().year:
            raise ValueError("❌ Leidimo metai negali būti ateityje!")
        self.title, self.author, self.year, self.quantity = title.strip(), author.strip(), year, quantity

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
        self.books = {}

    def add_book(self, title, author, year, quantity=2):
        key = (title.lower(), author.lower(), year)
        if key in self.books:
            self.books[key].quantity += quantity
            print(f"✅ Likutis atnaujintas: {self.books[key]}")
        else:
            new_book = Book(title, author, year, quantity)
            self.books[key] = new_book
            print(f"✅ Pridėta nauja knyga: {new_book}")

    def display_books(self):
        print("\n📚 Atnaujintas bibliotekos sąrašas:\n" + "-" * 50)
        for book in self.books.values():
            print(book)
        print("-" * 50)

    def suggest_book(self, title):
        matches = difflib.get_close_matches(title, [b.title for b in self.books.values()], n=3, cutoff=0.4)
        return matches if matches else None

    def borrow_book(self, title):
        matches = self.suggest_book(title)
        if matches:
            print(f"🔍 Galimi pasirinkimai: {', '.join(matches)}")
            title = input("📖 Patikslinkite knygos pavadinimą: ").strip()

        for book in self.books.values():
            if book.title.lower() == title.lower():
                if book.borrow():
                    print(f"📖 \"{book.title}\" – {book.author} ({book.year}) pasiskolinta! Liko: {book.quantity} vnt.")
                    self.display_books()
                else:
                    print(f"❌ \"{book.title}\" nebegalima skolintis! Liko: {book.quantity} vnt.")
                return
        print(f"❌ Knyga \"{title}\" nerasta.")

    def return_book(self, title):
        matches = self.suggest_book(title)
        if matches:
            print(f"🔍 Galimi pasirinkimai: {', '.join(matches)}")
            title = input("📖 Patikslinkite knygos pavadinimą: ").strip()

        for book in self.books.values():
            if book.title.lower() == title.lower():
                book.return_book()
                print(f"✅ \"{book.title}\" – {book.author} ({book.year}) grąžinta! Dabar yra {book.quantity} vnt.")
                self.display_books()
                return
        print(f"❌ Knyga \"{title}\" nerasta.")


# --------------------------------------------------
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
    library.add_book(*book, quantity=2)

# --------------------------------------------------
# --------------------------------------------------
while True:
    print("\n📌 Pasirinkite veiksmą:\n" + "-" * 50)
    print("[1] Pridėti knygą  [2] Peržiūrėti knygas  [3] Skolintis  [4] Grąžinti  [0] Išeiti")
    print("-" * 50)

    veiksmas = input("➡️ Jūsų pasirinkimas: ").strip()

    if veiksmas == "1":
        title = input("📖 Knygos pavadinimas: ").strip()
        author = input("✍️ Autorius: ").strip()
        year = int(input("📆 Leidimo metai: ").strip())
        library.add_book(title, author, year, quantity=2)
        library.display_books()

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
