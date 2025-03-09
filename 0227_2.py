from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from tabulate import tabulate
from datetime import datetime, timedelta
import sys
import pandas as pd

engine = create_engine("sqlite:///library.db", echo=False)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, unique=True, nullable=False)
    author = Column(String, nullable=False)
    year_published = Column(Integer, nullable=False)
    available = Column(Boolean, default=True)

class Reader(Base):
    __tablename__ = "readers"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)


class BorrowedBook(Base):
    __tablename__ = "borrowed_books"
    id = Column(Integer, primary_key=True, autoincrement=True)
    book_id = Column(Integer, ForeignKey("books.id"), nullable=False)
    reader_id = Column(Integer, ForeignKey("readers.id"), nullable=False)
    borrowed_at = Column(DateTime, default=datetime.utcnow)
    return_due_date = Column(DateTime, default=lambda: datetime.utcnow() + timedelta(days=14))

    book = relationship("Book")
    reader = relationship("Reader")


Base.metadata.create_all(engine)


def add_book(title, author, year_published):
    book = Book(title=title, author=author, year_published=year_published, available=True)
    session.add(book)
    session.commit()
    print("Knyga pridėta sėkmingai!")


def add_reader(name, email):
    reader = Reader(name=name, email=email)
    session.add(reader)
    session.commit()
    print("Skaitytojas pridėtas sėkmingai!")


def borrow_book(book_title, reader_email):
    book = session.query(Book).filter_by(title=book_title, available=True).first()
    reader = session.query(Reader).filter_by(email=reader_email).first()
    if book and reader:
        borrowed_book = BorrowedBook(book_id=book.id, reader_id=reader.id)
        book.available = False
        session.add(borrowed_book)
        session.commit()
        print("Knyga paskolinta sėkmingai!")
    else:
        print("Knyga neprieinama arba skaitytojas nerastas!")


def update_book(old_title, new_title, new_author, new_year):
    book = session.query(Book).filter_by(title=old_title).first()
    if book:
        book.title = new_title
        book.author = new_author
        book.year_published = new_year
        session.commit()
        print("Knygos informacija atnaujinta!")
    else:
        print("Knyga nerasta!")


def delete_book(title):
    book = session.query(Book).filter_by(title=title).first()
    if book:
        session.delete(book)
        session.commit()
        print("Knyga pašalinta!")
    else:
        print("Knyga nerasta!")


def list_books():
    books = session.query(Book).all()
    data = [[b.id, b.title, b.author, b.year_published, "Taip" if b.available else "Ne"] for b in books]
    print(
        tabulate(data, headers=["ID", "Pavadinimas", "Autorius", "Leidimo metai", "Galima skolinti"], tablefmt="grid"))


def list_borrowed_books():
    borrowed_books = session.query(BorrowedBook).all()
    data = [
        [b.id, b.book.title, b.reader.name, b.borrowed_at.strftime("%Y-%m-%d"), b.return_due_date.strftime("%Y-%m-%d")]
        for b in borrowed_books]
    print(tabulate(data, headers=["ID", "Knyga", "Skaitytojas", "Paėmimo data", "Grąžinimo terminas"], tablefmt="grid"))


def import_books_from_excel(file_path):
    df = pd.read_excel(file_path, skiprows=1, usecols=["A", "B", "C", "D"],
                       names=["id", "title", "author", "year_published"])
    for _, row in df.iterrows():
        book = Book(title=row["title"], author=row["author"], year_published=int(row["year_published"]))
        session.add(book)
    session.commit()
    print("Knygų sąrašas importuotas sėkmingai!")


def main():
    while True:
        print("\n1. Pridėti knygą")
        print("2. Pridėti skaitytoją")
        print("3. Paskolinti knygą")
        print("4. Atnaujinti knygos informaciją")
        print("5. Pašalinti knygą")
        print("6. Rodyti visas knygas")
        print("7. Rodyti paskolintas knygas")
        print("8. Importuoti knygas iš Excel")
        print("9. Išeiti")

        choice = input("Pasirinkite veiksmą: ")

        if choice == "1":
            add_book(input("Pavadinimas: "), input("Autorius: "), int(input("Leidimo metai: ")))
        elif choice == "2":
            add_reader(input("Vardas: "), input("El. paštas: "))
        elif choice == "3":
            borrow_book(input("Knygos pavadinimas: "), input("Skaitytojo el. paštas: "))
        elif choice == "4":
            update_book(input("Senasis pavadinimas: "), input("Naujas pavadinimas: "), input("Naujas autorius: "),
                        int(input("Nauji leidimo metai: ")))
        elif choice == "5":
            delete_book(input("Knygos pavadinimas: "))
        elif choice == "6":
            list_books()
        elif choice == "7":
            list_borrowed_books()
        elif choice == "8":
            import_books_from_excel(input("Įveskite Excel failo kelią: "))
        elif choice == "9":
            print("Programa baigta.")
            sys.exit()
        else:
            print("Neteisingas pasirinkimas!")


if __name__ == "__main__":
    main()
