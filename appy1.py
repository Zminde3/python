from flask import Flask, request, jsonify, render_templaterom flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta
import pandas as pd
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
db = SQLAlchemy(app)

# Lentelės modeliai
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

# Sukuriame DB lenteles
db.create_all()

# Pagrindinis puslapis
@app.route('/')
def home():
    return render_template('index.html')

# API endpointai
@app.route('/books', methods=['GET', 'POST'])
def books():
    if request.method == 'POST':
        data = request.json
        book = Book(title=data['title'], author=data['author'], year_published=data['year_published'])
        db.session.add(book)
        db.session.commit()
        return jsonify({"message": "Knyga pridėta!"})

    books = Book.query.all()
    return jsonify([{"id": b.id, "title": b.title, "author": b.author, "year_published": b.year_published, "available": b.available} for b in books])

@app.route('/readers', methods=['GET', 'POST'])
def readers():
    if request.method == 'POST':
        data = request.json
        reader = Reader(name=data['name'], email=data['email'])
        db.session.add(reader)
        db.session.commit()
        return jsonify({"message": "Skaitytojas pridėtas!"})

    readers = Reader.query.all()
    return jsonify([{"id": r.id, "name": r.name, "email": r.email} for r in readers])

@app.route('/borrow', methods=['POST'])
def borrow():
    data = request.json
    book = Book.query.filter_by(title=data['title'], available=True).first()
    reader = Reader.query.filter_by(email=data['email']).first()
    if book and reader:
        borrowed = BorrowedBook(book_id=book.id, reader_id=reader.id)
        book.available = False
        db.session.add(borrowed)
        db.session.commit()
        return jsonify({"message": "Knyga paskolinta!"})
    return jsonify({"message": "Klaida skolinant knygą."})

@app.route('/return', methods=['POST'])
def return_book():
    data = request.json
    borrowed = BorrowedBook.query.join(Book).filter(Book.title == data['title']).first()
    if borrowed:
        book = borrowed.book
        book.available = True
        db.session.delete(borrowed)
        db.session.commit()
        return jsonify({"message": "Knyga grąžinta!"})
    return jsonify({"message": "Klaida grąžinant knygą."})

if __name__ == '__main__':
    app.run(debug=True)
