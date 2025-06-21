from rechner import Rechner
import tkinter as tk
from datetime import datetime
import json

rechner = Rechner()


print("Willkommen beim Finanzrechner")
while True:
    print("\nGib eine Zahl ein:")
    print("1. Einnahmen hinzufügen \n2. Ausgaben hinzufügen \n3. Kontostand einsehen \n4. Monatsübersicht\n5. Beenden")
    userInput = input("Bitte Zahl eingeben: ")

    if userInput == "1":
        print("Einnahmen")
        einnahme = float(input("Betrag eingeben: "))
        bezeichnung = input("Bezeichnung eingeben: ")
        datum = input("Datum eingeben: ")

        rechner.add_einnahme(einnahme, bezeichnung, datum)
        if einnahme == 0:
            print()
            break

    elif userInput == "2":
        print("Ausgaben")
        ausgabe = float(input("Betrag eingeben: "))
        bezeichnung = input("Bezeichnung eingeben: ")
        datum = input("Datum eingeben: ")
        rechner.add_ausgabe(ausgabe, bezeichnung, datum)
        if ausgabe == 0:
            print()
            break

    elif userInput == "3":
        print(f"Dein aktueller Kontostand beträgt: {rechner.berechne_kontostand()} €\n")

    elif userInput == "4":
        month = int(input("Für welchen Monat möchtest du die Übersicht? "))
        print(rechner.get_monthly_summary(2025, month))
    elif userInput == "5":
        print("Programm wird beendet")
        break
    else:
        print("Ungültige Eingabe, bitte 1-4 wählen.")

