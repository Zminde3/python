from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from appy import Book  # arba iš to failo, kur aprašyta duomenų bazė

engine = create_engine('sqlite:///library.db')
Session = sessionmaker(bind=engine)
session = Session()

# surask ir ištrink knygą
book = session.query(Book).filter(Book.title == 'Netinkamai įvesta knyga').first()

if book:
    session.delete(book)
    session.commit()
    print('Knyga pašalinta sėkmingai!')
else:
    print('Knyga nerasta.')
