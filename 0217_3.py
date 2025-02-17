import logging
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
from colorama import Fore, Style, init

init(autoreset=True)

Base = declarative_base()

class Mokinys(Base):
    __tablename__ = 'mokiniai'
    id = Column(Integer, primary_key=True, autoincrement=True)
    vardas = Column(String, nullable=False)
    pavarde = Column(String, nullable=False)
    klase = Column(Integer, nullable=False)

class Mokytojas(Base):
    __tablename__ = 'mokytojai'
    id = Column(Integer, primary_key=True, autoincrement=True)
    vardas = Column(String, nullable=False)
    pavarde = Column(String, nullable=False)
    dalykas = Column(String, nullable=False)

engine = create_engine('sqlite:///mokykla.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

logging.basicConfig(
    level=logging.INFO,
    format=f"{Fore.GREEN}%(asctime)s - %(levelname)s - %(message)s{Style.RESET_ALL}",
    force=True
)

def prideti_mokini(vardas, pavarde, klase):
    if not session.query(Mokinys).filter_by(vardas=vardas, pavarde=pavarde).first():
        naujas_mokinys = Mokinys(vardas=vardas, pavarde=pavarde, klase=klase)
        session.add(naujas_mokinys)
        session.commit()
        logging.info(f"Pridėtas mokinys: {vardas} {pavarde}, klasė: {klase}")

def prideti_mokytoja(vardas, pavarde, dalykas):
    naujas_mokytojas = Mokytojas(vardas=vardas, pavarde=pavarde, dalykas=dalykas)
    session.add(naujas_mokytojas)
    session.commit()
    logging.info(f"Pridėtas mokytojas: {vardas} {pavarde}, dalykas: {dalykas}")

def rodyti_mokinius():
    mokiniai = session.query(Mokinys).all()
    for mokinys in mokiniai:
        print(f"🆔 {mokinys.id} | {mokinys.vardas} {mokinys.pavarde} | Klasė: {mokinys.klase}")

def rodyti_mokytojus():
    mokytojai = session.query(Mokytojas).all()
    for mokytojas in mokytojai:
        print(f"🆔 {mokytojas.id} | {mokytojas.vardas} {mokytojas.pavarde} | Dėsto: {mokytojas.dalykas}")

if __name__ == "__main__":
    prideti_mokini("Mindaugas", "Bernotas", 8)
    prideti_mokini("Tomas", "Matukas", 9)
    prideti_mokini("Gabija", "Barauskaitė", 7)
    prideti_mokytoja("Darius", "Daškevičius", "Matematika")
    prideti_mokytoja("Ligita", "Dobrovienė", "Lietuvių kalba")
    rodyti_mokinius()
    rodyti_mokytojus()
