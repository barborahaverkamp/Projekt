from Pojisteny import Pojisteny

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
