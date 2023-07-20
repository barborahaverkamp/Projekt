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

"""
Slouží k evidenci pojištěných osob.
"""
class EvidencniSystem:

    """
    Prázdný seznam 'pojisteni',
    do kterého budou přidávány instance třídy 'Pojisteny'.
    """
    def __init__(self):
        self.pojisteni = []

    """
    Tato metoda umožňuje uživateli zadat informace o novém pojištěném.
    """
    def vytvor_pojisteneho(self):
        jmeno = input("Zadejte jméno: ")
        prijmeni = input("Zadejte příjmení: ")
        vek = int(input("Zadejte věk: "))
        telefon = input("Zadejte telefonní číslo: ")

        pojisteny = Pojisteny(jmeno, prijmeni, vek, telefon)
        self.pojisteni.append(pojisteny)
        print("Pojištěný byl úspěšně vytvořen.")

    """
    Tato metoda zobrazí seznam všech pojištěných osob.
    """
    def zobraz_seznam(self):
        if len(self.pojisteni) == 0:
            print("Nejsou k dispozici žádní pojištění.")
        else:
            for index, pojisteny in enumerate(self.pojisteni, start=1):
                print("------")
                print(f"{index}. {pojisteny}")

        
    """
    Tato metoda umožňuje vyhledat pojištěného podle jména a příjmení.
    """
    def vyhledej_pojisteneho(self):
        zadat_jmeno = input("Zadejte jméno a příjmení pojištěného (Oddělené mezerou): ")
        jmeno, prijmeni = zadat_jmeno.split()

        nalezen = False
        for pojisteny in self.pojisteni:
            if pojisteny.jmeno.lower() == jmeno.lower() and pojisteny.prijmeni.lower() == prijmeni.lower():
                print(pojisteny)
                nalezen = True
        if not nalezen:
            print("Pojištený nebyl nalezen.")

"""
Tato funkce je hlavním vstupním bodem programu.
Spouští nekonečnou smyčku, která vypisuje menu
a umožňuje uživateli provádět akce.
"""
def main():
    system = EvidencniSystem()
     
    while True:
        print("\n----- Evidenční systém -----")
        print("1. Vytvořit pojištěného")
        print("2. Zobrazit seznam pojištěných")
        print("3. Vyhledat pojištěného")
        print("0. Konec")

        volba = input("Zvolte akci (0-3): ")

        if volba == "1":
            system.vytvor_pojisteneho()
        elif volba == "2":
            system.zobraz_seznam()
        elif volba == "3":
            system.vyhledej_pojisteneho()
        elif volba == "0":
            break
        else:
            print("Neplatná volba.")

main()
