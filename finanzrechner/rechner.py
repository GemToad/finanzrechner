class Rechner:

    def __init__(self):
        self.einnahmen_gesamt = 0.00
        self.ausgaben_gesamt = 0.00

    def add_einnahme(self, betrag):
        self.einnahmen_gesamt += betrag

    def add_ausgabe(self, betrag):
        self.ausgaben_gesamt += betrag

    def berechne_kontostand(self):
        return self.einnahmen_gesamt - self.ausgaben_gesamt


