import datetime

class Book:
    def __init__(self, title, author, year, available=True):
        self.title = title
        self.author = author
        self.year = year
        self.available = available
        self.due_date = None

    def __str__(self):
        status = "Prieinama" if self.available else f"Išduota iki {self.due_date}"
        return f"{self.title} - {self.author} ({self.year}) | {status}"

    def is_classic(self):
        return datetime.datetime.now().year - self.year > 50

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        for book in self.books:
            print(book)

    def borrow_book(self, title):
        try:
            book = next(b for b in self.books if b.title.lower() == title.lower() and b.available)
            book.available = False
            book.due_date = datetime.datetime.now() + datetime.timedelta(days=14)
            print(f"Pasiskolinote knygą: {book.title}, grąžinti iki {book.due_date.date()}")
        except StopIteration:
            print("Knyga nerasta arba jau išduota.")

    def return_book(self, title):
        try:
            book = next(b for b in self.books if b.title.lower() == title.lower() and not b.available)
            book.available = True
            book.due_date = None
            print(f"Grąžinote knygą: {book.title}")
        except StopIteration:
            print("Knyga nebuvo išduota arba nerasta.")

    def filter_books(self, *args, **kwargs):
        results = self.books
        for key, value in kwargs.items():
            results = [b for b in results if getattr(b, key, None) == value]
        for book in results:
            print(book)

library = Library()
while True:
    action = input("Pasirinkite veiksmą (1-Pridėti, 2-Peržiūrėti, 3-Skolinti, 4-Grąžinti, 5-Filtruoti, 6-Išeiti): ")
    if action == "1":
        try:
            title = input("Įveskite pavadinimą: ")
            author = input("Įveskite autorių: ")
            year = int(input("Įveskite metus: "))
            library.add_book(Book(title, author, year))
        except ValueError:
            print("Netinkami duomenys.")
    elif action == "2":
        library.display_books()
    elif action == "3":
        title = input("Knygos pavadinimas: ")
        library.borrow_book(title)
    elif action == "4":
        title = input("Knygos pavadinimas: ")
        library.return_book(title)
    elif action == "5":
        key = input("Filtruoti pagal (title, author, year): ")
        value = input("Reikšmė: ")
        library.filter_books(**{key: value})
    elif action == "6":
        break
    else:
        print("Netinkamas pasirinkimas.")
