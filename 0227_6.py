from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from tabulate import tabulate
from datetime import datetime, timedelta
import sys
import pandas as pd
import tkinter as tk
from tkinter import filedialog

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
    print("✅ Knyga pridėta sėkmingai!")

def add_reader(name, email):
    existing_reader = session.query(Reader).filter_by(email=email).first()
    if existing_reader:
        print("⚠️ Klaida: skaitytojas su tokiu el. paštu jau egzistuoja!")
        return
    new_reader = Reader(name=name, email=email)
    session.add(new_reader)
    session.commit()
    print(f"✅ Skaitytojas '{name}' sėkmingai pridėtas!")

def delete_book(title):
    book = session.query(Book).filter_by(title=title).first()
    if book:
        session.delete(book)
        session.commit()
        print("✅ Knyga pašalinta sėkmingai!")
    else:
        print("⚠️ Knyga nerasta!")

def delete_reader(email):
    reader = session.query(Reader).filter_by(email=email).first()
    if reader:
        session.delete(reader)
        session.commit()
        print("✅ Skaitytojas pašalintas sėkmingai!")
    else:
        print("⚠️ Skaitytojas nerastas!")

def borrow_book(book_title, reader_email):
    book = session.query(Book).filter_by(title=book_title, available=True).first()
    reader = session.query(Reader).filter_by(email=reader_email).first()
    if book and reader:
        borrowed_book = BorrowedBook(book_id=book.id, reader_id=reader.id)
        book.available = False
        session.add(borrowed_book)
        session.commit()
        print("✅ Knyga paskolinta sėkmingai!")
    else:
        print("⚠️ Knyga neprieinama arba skaitytojas nerastas!")

def return_book(book_title):
    borrowed_entry = session.query(BorrowedBook).join(Book).filter(Book.title == book_title).first()
    if not borrowed_entry:
        print("⚠️ Klaida: ši knyga nėra paskolinta!")
        return
    session.delete(borrowed_entry)
    book = session.query(Book).filter(Book.id == borrowed_entry.book_id).first()
    if book:
        book.available = True
    session.commit()
    print(f"✅ Knyga '{book_title}' sėkmingai grąžinta!")

def list_books():
    books = session.query(Book).all()
    data = [[b.id, b.title, b.author, b.year_published, "Taip" if b.available else "Ne"] for b in books]
    print(tabulate(data, headers=["ID", "Pavadinimas", "Autorius", "Leidimo metai", "Galima skolinti"], tablefmt="grid"))

def list_readers():
    readers = session.query(Reader).all()
    data = [[r.id, r.name, r.email] for r in readers]
    print(tabulate(data, headers=["ID", "Vardas", "El. paštas"], tablefmt="grid"))

def list_borrowed_books():
    borrowed_books = session.query(BorrowedBook).all()
    data = [[b.id, b.book.title, b.reader.name, b.borrowed_at.strftime("%Y-%m-%d"), b.return_due_date.strftime("%Y-%m-%d")] for b in borrowed_books]
    print(tabulate(data, headers=["ID", "Knyga", "Skaitytojas", "Paėmimo data", "Grąžinimo terminas"], tablefmt="grid"))

def import_books_from_excel():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(title="Pasirinkite Excel failą", filetypes=[("Excel Files", "*.xlsx;*.xls")])
    if not file_path:
        print("⚠️ Failas nepasirinktas.")
        return

    df = pd.read_excel(file_path, skiprows=1, usecols=[0, 1, 2, 3], names=["id", "title", "author", "year_published"])
    for _, row in df.iterrows():
        book = Book(title=row["title"], author=row["author"], year_published=int(row["year_published"]))
        session.add(book)
    session.commit()
    print("✅ Knygų sąrašas importuotas sėkmingai!")

def main():
    while True:
        print("\n📚 Bibliotekos sistema 📚")
        print("1️⃣ Pridėti naują knygą")
        print("2️⃣ Pridėti naują skaitytoją")
        print("3️⃣ Paskolinti knygą skaitytojui")
        print("4️⃣ Atnaujinti knygos informaciją")
        print("5️⃣ Pašalinti skaitytoją")
        print("6️⃣ Pašalinti knygą")
        print("7️⃣ Rodyti visas knygas")
        print("8️⃣ Rodyti visus skaitytojus")
        print("9️⃣ Rodyti visas paskolintas knygas")
        print("🔟 Importuoti knygas iš Excel")
        print("1️⃣1️⃣ Grąžinti knygą")
        print("0️⃣ Išeiti")

        pasirinkimas = input("👉 Įveskite pasirinkimą: ")

        if pasirinkimas == "1":
            add_book(input("📖 Pavadinimas: "), input("✍️ Autorius: "), int(input("📅 Leidimo metai: ")))
        elif pasirinkimas == "2":
            add_reader(input("👤 Vardas: "), input("📧 El. paštas: "))
        elif pasirinkimas == "3":
            borrow_book(input("📖 Knygos pavadinimas: "), input("📧 Skaitytojo el. paštas: "))
        elif pasirinkimas == "4":
            print("🔧 Ši funkcija dar neįgyvendinta.")
        elif pasirinkimas == "5":
            delete_reader(input("📧 Skaitytojo el. paštas: "))
        elif pasirinkimas == "6":
            delete_book(input("📖 Knygos pavadinimas: "))
        elif pasirinkimas == "7":
            list_books()
        elif pasirinkimas == "8":
            list_readers()
        elif pasirinkimas == "9":
            list_borrowed_books()
        elif pasirinkimas == "10":
            import_books_from_excel()
        elif pasirinkimas == "11":
            return_book(input("📖 Įveskite grąžinamos knygos pavadinimą: "))
        elif pasirinkimas == "0":
            print("👋 Programa baigta.")
            sys.exit()
        else:
            print("⚠️ Neteisingas pasirinkimas!")

if __name__ == "__main__":
    main()
