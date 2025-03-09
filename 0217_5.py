import logging
import sys
import time
import random
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
from colorama import Fore, Style, init
from pyfiglet import figlet_format

init(autoreset=True)

Base = declarative_base()

COLORS = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]

def spalvotas_tekstas(tekstas):
    zodziai = tekstas.split()
    spalvoti_zodziai = [random.choice(COLORS) + zodis + Style.RESET_ALL for zodis in zodziai]
    return " ".join(spalvoti_zodziai)

def typewriter(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def show_banner():
    print(Fore.CYAN + figlet_format("Mokyklos DB", font="slant"))

def show_joke():
    jokes = [
        "😂 Kodėl programuotojai neina į lauką? Nes ten per daug klaidų!",
        "🖥️ Kas yra Python? Tai kalba, kurioje rašai klaidas greičiau nei bet kada anksčiau!",
        "🤓 Kodėl programa nesisuka? Nes užsuko per daug ciklų!"
    ]
    joke = random.choice(jokes)
    typewriter(spalvotas_tekstas(f"🎭 Juokelis: {joke}"))


def progress_bar(iteration, total, length=30):
    percent = ("{0:.1f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = "█" * filled_length + "-" * (length - filled_length)
    sys.stdout.write(f"\r|{bar}| {percent}%")
    sys.stdout.flush()
    if iteration == total:
        print()

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
    if session.query(Mokinys).count() == 0:
        naujas_mokinys = Mokinys(vardas=vardas, pavarde=pavarde, klase=klase)
        session.add(naujas_mokinys)
        session.commit()
        typewriter(spalvotas_tekstas(f"Pridėtas pirmasis mokinys: {vardas} {pavarde}, klasė: {klase}"))
    elif not session.query(Mokinys).filter_by(vardas=vardas, pavarde=pavarde).first():
        naujas_mokinys = Mokinys(vardas=vardas, pavarde=pavarde, klase=klase)
        session.add(naujas_mokinys)
        session.commit()
        typewriter(spalvotas_tekstas(f"Pridėtas naujas mokinys: {vardas} {pavarde}, klasė: {klase}"))
    else:
        typewriter(spalvotas_tekstas(f"Mokinys {vardas} {pavarde} jau yra duomenų bazėje, neįtrauktas."))

def prideti_mokytoja(vardas, pavarde, dalykas):
    naujas_mokytojas = Mokytojas(vardas=vardas, pavarde=pavarde, dalykas=dalykas)
    session.add(naujas_mokytojas)
    session.commit()
    typewriter(spalvotas_tekstas(f"Pridėtas mokytojas: {vardas} {pavarde}, dalykas: {dalykas}"))

def rodyti_mokinius():
    mokiniai = session.query(Mokinys).all()
    if not mokiniai:
        typewriter(spalvotas_tekstas("📭 Duomenų bazėje nėra mokinių."))
    else:
        for mokinys in mokiniai:
            typewriter(spalvotas_tekstas(f"🆔 {mokinys.id} | {mokinys.vardas} {mokinys.pavarde} | Klasė: {mokinys.klase}"))

def rodyti_mokytojus():
    mokytojai = session.query(Mokytojas).all()
    if not mokytojai:
        typewriter(spalvotas_tekstas("📭 Duomenų bazėje nėra mokytojų."))
    else:
        for mokytojas in mokytojai:
            typewriter(spalvotas_tekstas(f"🆔 {mokytojas.id} | {mokytojas.vardas} {mokytojas.pavarde} | Dėsto: {mokytojas.dalykas}"))

if __name__ == "__main__":
    show_banner()
    typewriter("🔹 Kuriama mokinių duomenų bazė... ")
    for i in range(1, 11):
        progress_bar(i, 10)
        time.sleep(0.1)
    typewriter("✅ Duomenys sėkmingai įrašyti!")
    show_joke()
    prideti_mokini("Mindaugas", "Bernotas", 8)
    prideti_mokini("Tomas", "Matukas", 9)
    prideti_mokini("Gabija", "Barauskaitė", 7)
    prideti_mokytoja("Darius", "Daškevičius", "Matematika")
    prideti_mokytoja("Ligita", "Dobrovienė", "Lietuvių kalba")
    rodyti_mokinius()
    rodyti_mokytojus()
