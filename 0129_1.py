def sudeti(*s): return sum(s)
def sveikinti(*v): return [f"Labas, {x}!" for x in v]
def pakelti(n, *s): return [x**n for x in s]

print(sudeti(5, 10, 15), sudeti(100, 200, 300, 400))
print(*sveikinti("Jonas", "Asta", "Mantas"), sep="\n")
print(pakelti(2, 3, 4, 5), pakelti(3, 2, 3, 4))
