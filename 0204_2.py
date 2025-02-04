class Car: manufacturer = "Toyota"
class Bike: manufacturer = "Yamaha"

class Book:
    publisher = "Alma Littera"
    def __init__(self, title, author, year): self.title, self.author, self.year = title, author, year

books = [
    Book("Altorių šešėly", "Vincas Mykolaitis-Putinas", 1933),
    Book("Balta drobulė", "Antanas Škėma", 1958),
    Book("Tadas Blinda", "Rimantas Šavelis", 1987)
]

print(f"🚗 Car manufacturer: {Car.manufacturer}\n🏍️ Bike manufacturer: {Bike.manufacturer}")
print(f"📚 Leidykla: {Book.publisher}")
for b in books: print(f"📖 \"{b.title}\" – {b.author} ({b.year})")
