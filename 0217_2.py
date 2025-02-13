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
    format=f"{Fore.BLUE}%(asctime)s - %(levelname)s - %(message)s{Style.RESET_ALL}",
    force=True
)

def prideti_irasa(modelio_klase, **duomenys):
    with session.begin():
        naujas_irasas = modelio_klase(**duomenys)
        session.add(naujas_irasas)
        logging.info(f"Pridėtas naujas įrašas: {duomenys}")

if __name__ == "__main__":
    prideti_irasa(Mokinys, vardas="Mindaugas", pavarde="Bernotas", klase=8)
    prideti_irasa(Mokytojas, vardas="Dariuš", pavarde="Daškevičius", dalykas="Matematika")
