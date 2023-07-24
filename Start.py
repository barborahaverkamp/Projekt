from Evidencni_system import EvidencniSystem

"""
Tato funkce je hlavním vstupním bodem programu.
Spouští nekonečnou smyčku, která vypisuje menu
a umožňuje uživateli provádět akce.
"""
def start():
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

start()
