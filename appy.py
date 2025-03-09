from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta
import os
import pandas as pd
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Slaptažodis knygos pašalinimui
DELETE_BOOK_PASSWORD = "Labas123"

db = SQLAlchemy(app)

# Duomenų bazės lentelės
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    author = db.Column(db.String, nullable=False)
    year_published = db.Column(db.Integer, nullable=False)
    available = db.Column(db.Boolean, default=True)

class Reader(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)

class BorrowedBook(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
    reader_id = db.Column(db.Integer, db.ForeignKey('reader.id'))
    borrowed_at = db.Column(db.DateTime, default=datetime.utcnow)
    return_due_date = db.Column(db.DateTime, default=lambda: datetime.utcnow() + timedelta(days=14))

    book = db.relationship('Book')
    reader = db.relationship('Reader')

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template('0227_5.html')

@app.route('/books', methods=['GET', 'POST'])
def books():
    if request.method == 'POST':
        data = request.json
        new_book = Book(
            title=data['title'],
            author=data['author'],
            year_published=data['year_published']
        )
        db.session.add(new_book)
        db.session.commit()
        return jsonify({"message": "Knyga pridėta!"})

    books = Book.query.all()
    return jsonify([{
        "id": b.id,
        "title": b.title,
        "author": b.author,
        "year_published": b.year_published,
        "available": b.available
    } for b in books])

@app.route('/readers', methods=['GET', 'POST'])
def readers():
    if request.method == 'POST':
        data = request.json
        new_reader = Reader(name=data['name'], email=data['email'])
        db.session.add(new_reader)
        db.session.commit()
        return jsonify({"message": "Skaitytojas pridėtas!"})

    readers = Reader.query.all()
    return jsonify([{ "id": r.id, "name": r.name, "email": r.email } for r in readers])

@app.route('/borrow', methods=['POST'])
def borrow():
    data = request.json
    book = Book.query.filter_by(title=data['title'], available=True).first()
    reader = Reader.query.filter_by(email=data['email']).first()

    if book and reader:
        borrowed_book = BorrowedBook(book_id=book.id, reader_id=reader.id)
        book.available = False
        db.session.add(borrowed_book)
        db.session.commit()
        return jsonify({"message": "Knyga paskolinta!"})

    return jsonify({"error": "Klaida skolinant knygą."}), 400

@app.route('/borrowed-books', methods=['GET'])
def borrowed_books():
    borrowed = BorrowedBook.query.all()
    return jsonify([{
        "id": b.id,
        "title": b.book.title,
        "reader": b.reader.name,
        "borrowed_at": b.borrowed_at.strftime("%Y-%m-%d"),
        "return_due_date": b.return_due_date.strftime("%Y-%m-%d")
    } for b in borrowed])

@app.route('/return', methods=['POST'])
def return_book():
    data = request.json
    borrowed = BorrowedBook.query.join(Book).filter(Book.title == data['title']).first()
    if borrowed:
        borrowed.book.available = True
        db.session.delete(borrowed)
        db.session.commit()
        return jsonify({"message": "Knyga grąžinta!"})

    return jsonify({"error": "Klaida grąžinant knygą."}), 400

@app.route('/delete-book', methods=['POST'])
def delete_book():
    data = request.json
    if data.get('password') != DELETE_BOOK_PASSWORD:
        return jsonify({"error": "⚠️ Neteisingas slaptažodis!"}), 401

    book = Book.query.filter_by(title=data['title']).first()
    if book:
        BorrowedBook.query.filter_by(book_id=book.id).delete()
        db.session.delete(book)
        db.session.commit()
        db.session.execute("UPDATE SQLITE_SEQUENCE SET seq = (SELECT MAX(id) FROM book) WHERE name='book'")
        db.session.commit()
        return jsonify({"message": "✅ Knyga pašalinta!"})

    return jsonify({"error": "⚠️ Knyga nerasta!"}), 400

@app.route('/all-books', methods=['GET'])
def all_books():
    books = Book.query.all()
    result = []
    for b in books:
        borrowed = BorrowedBook.query.filter_by(book_id=b.id).first()
        result.append({
            "id": b.id,
            "title": b.title,
            "author": b.author,
            "year_published": b.year_published,
            "available": b.available,
            "borrowed_at": borrowed.borrowed_at.strftime("%Y-%m-%d") if borrowed else None,
            "return_due_date": borrowed.return_due_date.strftime("%Y-%m-%d") if borrowed else None
        })
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
