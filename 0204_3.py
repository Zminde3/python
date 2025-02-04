from datetime import date

class Book:
    publisher = "Alma Littera"

    def __init__(self, title, author, year):
        if year > date.today().year:
            raise ValueError("❌ Leidimo metai negali būti ateityje!")
        self.title, self.author, self.year = title, author, year

    def get_book_age(self):
        return date.today().year - self.year

    def __str__(self):
        return f"📖 \"{self.title}\" – {self.author} ({self.year})"

books = [
    Book("Altorių šešėly", "Vincas Mykolaitis-Putinas", 1933),
    Book("Balta drobulė", "Antanas Škėma", 1958),
    Book("Tadas Blinda", "Rimantas Šavelis", 1987)
]

for book in books:
    print(book)  # Automatiškai kviečia __str__()
    print(f"📚 Knyga \"{book.title}\" yra {book.get_book_age()} metų amžiaus.\n")
