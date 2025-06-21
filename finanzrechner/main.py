from rechner import Rechner

rechner = Rechner()

print("Willkommen beim Finanzrechner")
while True:
    print("Gib eine Zahl ein:")
    print("1. Einnahmen hinzufügen ")
    print("2. Ausgaben hinzufügen ")
    print("3. Kontostand einsehen ")
    userInput = int(input())

    while userInput == 1:
        einnahme = float(input("Einnahme eingeben: "))
        rechner.add_einnahme(einnahme)
        if einnahme == 0:
            print()
            break
    while userInput == 2:
        ausgabe = float(input("Ausgabe eingeben: "))
        rechner.add_ausgabe(ausgabe)
        if ausgabe == 0:
            print()
            break
    if userInput == 3:
        print(f"Dein aktueller Kontostand beträgt: {rechner.berechne_kontostand()} €\n")


