import functools

def sekimo_dekoratorius(funkcija):
    @functools.wraps(funkcija)
    def vidine(*args, **kwargs):
        print(f"Vykdoma funkcija: {funkcija.__name__}")
        rezultatas = funkcija(*args, **kwargs)
        print("Funkcija baigta!")
        return rezultatas
    return vidine

@sekimo_dekoratorius
def dauginti(a, b):
    return a * b

@sekimo_dekoratorius
def dalinti(a, b):
    return a / b if b else "Klaida: dalyba iš nulio"

print(dauginti(6, 7))
print(dalinti(10, 2))
print(dalinti(10, 0))
