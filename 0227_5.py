from flask import Flask, request, jsonify, render_template
from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from datetime import datetime, timedelta
import pandas as pd
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Duomenų bazė
engine = create_engine("sqlite:///library.db", echo=False)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

# Lentelės modeliai
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

# API Endpointai
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/books', methods=['GET', 'POST'])
def books():
    if request.method == 'POST':
        data = request.json
        new_book = Book(title=data['title'], author=data['author'], year_published=data['year_published'], available=True)
        session.add(new_book)
        session.commit()
        return jsonify({"message": "Knyga pridėta sėkmingai!"})
    books = session.query(Book).all()
    return jsonify([{ "id": b.id, "title": b.title, "author": b.author, "year_published": b.year_published, "available": b.available } for b in books])

@app.route('/readers', methods=['GET', 'POST'])
def readers():
    if request.method == 'POST':
        data = request.json
        new_reader = Reader(name=data['name'], email=data['email'])
        session.add(new_reader)
        session.commit()
        return jsonify({"message": "Skaitytojas pridėtas sėkmingai!"})
    readers = session.query(Reader).all()
    return jsonify([{ "id": r.id, "name": r.name, "email": r.email } for r in readers])

@app.route('/borrow', methods=['POST'])
def borrow_book():
    data = request.json
    book = session.query(Book).filter_by(title=data['title'], available=True).first()
    reader = session.query(Reader).filter_by(email=data['email']).first()
    if book and reader:
        borrowed_book = BorrowedBook(book_id=book.id, reader_id=reader.id)
        book.available = False
        session.add(borrowed_book)
        session.commit()
        return jsonify({"message": "Knyga paskolinta sėkmingai!"})
    return jsonify({"error": "Knyga neprieinama arba skaitytojas nerastas!"})

@app.route('/import-books', methods=['POST'])
def import_books():
    if 'file' not in request.files:
        return jsonify({"error": "Nėra failo!"})
    file = request.files['file']
    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)
    df = pd.read_excel(file_path, skiprows=1, usecols=["A", "B", "C", "D"], names=["id", "title", "author", "year_published"])
    for _, row in df.iterrows():
        book = Book(title=row["title"], author=row["author"], year_published=int(row["year_published"]))
        session.add(book)
    session.commit()
    return jsonify({"message": "Knygos importuotos sėkmingai!"})

if __name__ == '__main__':
    app.run(debug=True)
