class SkaiciuSekosIteratorius:
    def __init__(self, pradinis, galinis=20):
        self.pradinis = pradinis
        self.galinis = galinis
        self.dabartinis = pradinis - 2

    def __iter__(self):
        return self

    def __next__(self):
        self.dabartinis += 2
        if self.dabartinis > self.galinis:
            raise StopIteration
        return self.dabartinis

    def atgaline_seka(self):
        return reversed(range(self.pradinis, self.galinis + 1, 2))

    def suma(self):
        return sum(range(self.pradinis, self.galinis + 1, 2))

    def vidurkis(self):
        skaiciai = list(range(self.pradinis, self.galinis + 1, 2))
        return sum(skaiciai) / len(skaiciai) if skaiciai else 0

iteratorius = SkaiciuSekosIteratorius(1, 20)
print("Eilės tvarka:", list(iteratorius))
print("Atgaline tvarka:", list(iteratorius.atgaline_seka()))
print("Suma:", iteratorius.suma())
print("Vidurkis:", iteratorius.vidurkis())
