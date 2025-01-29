def rodyti_duomenis(**d): print(*[f"{k}: {v}" for k, v in d.items()], sep="\n")

def registruoti_naudotoja(v, e, **d): print(f"Vardas: {v}, El. paštas: {e}", *[f"{k}: {v}" for k, v in d.items()], sep="\n")

def atspausdinti_lista(l, **d): print(*l, **d)

rodyti_duomenis(vardas="Mindaugas", amzius=30, miestas="Šilutė")
registruoti_naudotoja("Mindaugas", "zminde3@gmail.com", amzius=47, miestas="Klaipėda")
atspausdinti_lista(["vysnia", "abrikosas", "litis"], sep=" | ")
