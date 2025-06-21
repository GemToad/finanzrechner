from rechner import Rechner
from datetime import datetime
import json

rechner = Rechner()

print("Willkommen beim Finanzrechner")
while True:
    print("Gib eine Zahl ein:")
    print("1. Einnahmen hinzufügen \n2. Ausgaben hinzufügen \n3. Kontostand einsehen \n4. Beenden")
    userInput = input("Bitte Zahl eingeben: ")

    if userInput == "1":
        datum = input("Datum eingeben: ")
        bezeichnung = input("Bezeichnung eingeben: ")
        einnahme = float(input("Einnahme eingeben: "))
        rechner.add_einnahme(einnahme, bezeichnung, datum)
        if einnahme == 0:
            print()
            break
    if userInput == "2":
        datum = input("Datum eingeben: ")
        bezeichnung = input("Bezeichnung eingeben: ")
        ausgabe = float(input("Ausgabe eingeben: "))
        rechner.add_ausgabe(ausgabe, bezeichnung, datum)
        if ausgabe == 0:
            print()
            break
    if userInput == "3":
        print(f"Dein aktueller Kontostand beträgt: {rechner.berechne_kontostand()} €\n")
    if userInput == "4":
        print("Programm wird beendet")
        break

