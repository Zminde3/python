def spausdinti_zinutes(kartai, *args, pabaiga="!"):
    print(*(z * kartai + pabaiga for z in args), sep="\n")
def dauginti_skaicius(n, *args):
    return [x * n for x in args]
spausdinti_zinutes(2, "Labas", "Python", pabaiga="!!!")
print(dauginti_skaicius(3, 1, 2, 3, 4))
