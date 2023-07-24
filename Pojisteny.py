"""
Slouží k reprezentaci pojištěné osoby.
"""
class Pojisteny:

    def __init__(self, jmeno, prijmeni, vek, telefon):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.telefon = telefon

    """
    Vrátí řetězcovou reprezentaci pojištěné osoby.
    """
    def __str__(self):
        return f"Jméno: {self.jmeno}\nPříjmení: {self.prijmeni}\nVěk: {self.vek}\nTelefonní číslo: {self.telefon}"

